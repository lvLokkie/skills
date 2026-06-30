#!/usr/bin/env python3
"""Validate the personal skills marketplace manifest and skill frontmatter."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "personal-skills"
MANIFEST = PLUGIN / ".claude-plugin" / "plugin.json"
SKILLS_DIR = PLUGIN / "skills"
README = ROOT / "README.md"
BUCKET_README = SKILLS_DIR / "README.md"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: missing opening frontmatter fence")
    end = text.find("\n---", 4)
    if end == -1:
        fail(f"{path.relative_to(ROOT)}: missing closing frontmatter fence")
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)}: unsupported frontmatter line {line!r}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        fail("plugin.json must contain a non-empty skills list")

    seen: set[str] = set()
    for rel in skills:
        skill_dir = (PLUGIN / rel).resolve()
        try:
            skill_dir.relative_to(PLUGIN.resolve())
        except ValueError:
            fail(f"skill path escapes plugin root: {rel}")
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            fail(f"manifest skill missing SKILL.md: {rel}")
        fm = parse_frontmatter(skill_file)
        name = fm.get("name") or skill_dir.name
        if name != skill_dir.name:
            fail(f"{skill_file.relative_to(ROOT)}: frontmatter name must match directory")
        if not fm.get("description"):
            fail(f"{skill_file.relative_to(ROOT)}: description is required")
        seen.add(name)

    actual = {p.parent.name for p in SKILLS_DIR.glob("*/SKILL.md")}
    extra = actual - seen
    if extra:
        fail(f"skill folders not listed in plugin.json: {', '.join(sorted(extra))}")

    for doc in (README, BUCKET_README):
        text = doc.read_text(encoding="utf-8")
        for name in sorted(seen):
            if name not in text:
                fail(f"{doc.relative_to(ROOT)} does not mention promoted skill {name}")

    marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    if not marketplace.get("plugins"):
        fail("marketplace.json must list at least one plugin")

    print(f"OK: {len(seen)} promoted skill(s) validated")


if __name__ == "__main__":
    main()
