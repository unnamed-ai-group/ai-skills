#!/usr/bin/env python3
"""Validate the portable core structure of repository skills."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter marker")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("missing closing frontmatter marker")
    data: dict[str, str] = {}
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    if not skill_dirs:
        errors.append("No skill folders found under skills/.")
    for folder in skill_dirs:
        if not NAME_RE.fullmatch(folder.name):
            errors.append(f"{folder}: folder name must use lowercase letters, numbers, and hyphens")
        skill_file = folder / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{folder}: missing SKILL.md")
            continue
        try:
            data = read_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(f"{skill_file}: {exc}")
            continue
        if set(data) != {"name", "description"}:
            errors.append(f"{skill_file}: frontmatter must contain only name and description")
        if data.get("name") != folder.name:
            errors.append(f"{skill_file}: name must match folder name")
        if not data.get("description"):
            errors.append(f"{skill_file}: description is required")
        if "TODO" in skill_file.read_text(encoding="utf-8"):
            errors.append(f"{skill_file}: remove TODO placeholders")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Validated {len(skill_dirs)} skill folder(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
