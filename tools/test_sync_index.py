import json
from pathlib import Path
import tempfile
import unittest
from tools.sync_index import sync

class SyncIndexTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.communes = self.root / "communes"
        self.communes.mkdir()
        self.index = self.root / "index.json"
        self.entries = {str(10000 + i): {"name": f"Ville {i}", "count": 1, "written": 0, "updated": "2026-01-01"} for i in range(1100)}
        self.entries["76259"] = {"name": "Fécamp", "count": 16, "written": 15, "updated": "2026-10-10"}
        self.index.write_text(json.dumps({"communes": self.entries, "generated": "conservé"}), encoding="utf-8")
        (self.communes / "76259.json").write_text(json.dumps({
            "id": "76259", "insee": "76259", "name": "Fécamp",
            "anecdotes": [{"category": "politique"}] + [{"category": "histoire"}] * 21
        }), encoding="utf-8")

    def test_in_place_update_does_not_touch_neighbors(self):
        changed = sync(self.index, self.communes, {"76259"}, "2026-10-12T12:00:00Z")
        self.assertEqual(changed, ["76259"])
        data = json.loads(self.index.read_text(encoding="utf-8"))
        self.assertEqual(data["commun es".replace(" ", "")]["76259"]["count"], 22)
        self.assertEqual(data["communes"]["76259"]["written"], 21)
        self.assertEqual(data["communes"]["76259"]["updated"], "2026-10-12T12:00:00Z")
        self.assertEqual(len(data["communes"]["76259"]["revision"]), 64)
        self.assertEqual(data["communes"]["10000"], self.entries["10000"])
        self.assertEqual(data["generated"], "conservé")

    def test_idempotent_and_same_count_text_edit_is_detected(self):
        self.assertEqual(sync(self.index, self.communes, {"76259"}, "2026-10-12T12:00:00Z"), ["76259"])
        first = self.index.read_bytes()
        self.assertEqual(sync(self.index, self.communes, {"76259"}, "2026-10-12T12:01:00Z"), [])
        self.assertEqual(self.index.read_bytes(), first)
        file = self.communes / "76259.json"
        data = json.loads(file.read_text(encoding="utf-8"))
        data["anecdotes"][1]["text"] = "Une histoire modifiée"
        file.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(sync(self.index, self.communes, {"76259"}, "2026-10-12T12:02:00Z"), ["76259"])

    def test_reject_inconsistent_file_without_raising_index_changes(self):
        before = self.index.read_bytes()
        (self.communes / "76259.json").write_text('{"id":"76259","insee":"00000","anecdotes":[]}', encoding="utf-8")
        with self.assertRaises(ValueError):
            sync(self.index, self.communes, {"76259"}, "2026-10-12")
        self.assertEqual(self.index.read_bytes(), before)

if __name__ == "__main__":
    unittest.main()
