import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RepositoryValidationTests(unittest.TestCase):
    def test_content_inventory(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate.py")],
            cwd=ROOT, capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS:", result.stdout)

    def test_each_lesson_has_mermaid_diagram(self):
        lessons = list((ROOT / "lessons").rglob("*.md"))
        self.assertEqual(len(lessons), 50)
        for path in lessons:
            self.assertIn("```mermaid", path.read_text(encoding="utf-8"), str(path))

if __name__ == "__main__":
    unittest.main()
