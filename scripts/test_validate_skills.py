#!/usr/bin/env python3
"""Regression tests for the skill structure validator."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


MODULE_PATH = Path(__file__).with_name("validate_skills.py")
SPEC = importlib.util.spec_from_file_location("validate_skills", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class FrontmatterTests(unittest.TestCase):
    def parse(self, text: str) -> dict[str, str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "SKILL.md"
            path.write_text(text, encoding="utf-8")
            return VALIDATOR.read_frontmatter(path)

    def test_single_line_description(self) -> None:
        data = self.parse("---\nname: sample\ndescription: A sample skill.\n---\n")
        self.assertEqual(data, {"name": "sample", "description": "A sample skill."})

    def test_folded_multiline_description(self) -> None:
        data = self.parse(
            "---\nname: sample\ndescription: >-\n  A sample skill.\n  Use for testing.\n---\n"
        )
        self.assertEqual(data["description"], "A sample skill. Use for testing.")

    def test_unexpected_indentation_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "unexpected indented"):
            self.parse("---\nname: sample\n  invalid\ndescription: Test.\n---\n")


if __name__ == "__main__":
    unittest.main()
