#!/usr/bin/env python3
"""Validate the skills marketplace manifest, plugin manifests, and skill frontmatter."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, NoReturn

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
README = ROOT / "README.md"
IN_PROGRESS = ROOT / "plugins" / "in-progress"


def fail(message: str) -> NoReturn:
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


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)}: expected JSON object")
    return data


def require_text(path: Path, text: str, needle: str, label: str) -> None:
    if needle not in text:
        fail(f"{path.relative_to(ROOT)} missing {label}: {needle}")


def top_skill_link(plugin_name: str, skill_name: str) -> str:
    return f"[{skill_name}](./plugins/{plugin_name}/skills/{skill_name}/SKILL.md)"


def bucket_skill_link(skill_name: str) -> str:
    return f"[{skill_name}](./{skill_name}/SKILL.md)"


def validate_optional_mcp(plugin_root: Path) -> None:
    mcp_path = plugin_root / ".mcp.json"
    if not mcp_path.exists():
        return

    data = load_json(mcp_path)
    servers = data.get("mcpServers")
    if not isinstance(servers, dict) or not servers:
        fail(f"{mcp_path.relative_to(ROOT)}: must contain non-empty mcpServers object")

    for server_name, server_config in servers.items():
        if not isinstance(server_name, str) or not server_name:
            fail(f"{mcp_path.relative_to(ROOT)}: MCP server names must be non-empty strings")
        if not isinstance(server_config, dict):
            fail(f"{mcp_path.relative_to(ROOT)}: MCP server {server_name!r} must be an object")

        has_url = isinstance(server_config.get("url"), str) and bool(server_config.get("url"))
        has_command = isinstance(server_config.get("command"), str) and bool(server_config.get("command"))
        if not has_url and not has_command:
            fail(f"{mcp_path.relative_to(ROOT)}: MCP server {server_name!r} needs url or command")

        headers = server_config.get("headers", {})
        if headers is not None and not isinstance(headers, dict):
            fail(f"{mcp_path.relative_to(ROOT)}: MCP server {server_name!r} headers must be an object")
        for header_name, header_value in (headers or {}).items():
            if not isinstance(header_name, str) or not isinstance(header_value, str):
                fail(f"{mcp_path.relative_to(ROOT)}: MCP server {server_name!r} headers must be string values")
            if header_name.lower() == "authorization" and "bearer " in header_value.lower() and "${" not in header_value:
                fail(f"{mcp_path.relative_to(ROOT)}: MCP server {server_name!r} Authorization header must use an env placeholder")


def validate_plugin(plugin_entry: object, top_readme: str, marketplace_name: str) -> tuple[str, int]:
    if not isinstance(plugin_entry, dict):
        fail("marketplace plugin entry must be an object")
    raw_name = plugin_entry.get("name")
    raw_source = plugin_entry.get("source")
    if not isinstance(raw_name, str) or not raw_name:
        fail("marketplace plugin entry missing name")
    name = raw_name
    if not isinstance(raw_source, str) or not raw_source:
        fail(f"marketplace plugin {name}: missing source")
    source = raw_source

    plugin_root = (ROOT / source).resolve()
    try:
        plugin_root.relative_to(ROOT.resolve())
    except ValueError:
        fail(f"marketplace plugin {name}: source escapes repo root: {source}")
    if not plugin_root.is_dir():
        fail(f"marketplace plugin {name}: source directory missing: {source}")

    manifest_path = plugin_root / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        fail(f"marketplace plugin {name}: missing .claude-plugin/plugin.json")
    manifest = load_json(manifest_path)
    if manifest.get("name") != name:
        fail(f"{manifest_path.relative_to(ROOT)}: manifest name must match marketplace entry {name!r}")

    validate_optional_mcp(plugin_root)

    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        fail(f"{manifest_path.relative_to(ROOT)} must contain a non-empty skills list")

    skills_dir = plugin_root / "skills"
    bucket_readme = skills_dir / "README.md"
    if not bucket_readme.exists():
        fail(f"{skills_dir.relative_to(ROOT)}: missing README.md")
    bucket_text = bucket_readme.read_text(encoding="utf-8")

    category_heading = f"### `{name}`"
    install_command = f"/plugin install {name}@{marketplace_name}"
    require_text(README, top_readme, category_heading, f"promoted category heading for {name}")
    require_text(README, top_readme, install_command, f"install command for plugin {name}")

    seen: set[str] = set()
    for rel in skills:
        if not isinstance(rel, str):
            fail(f"{manifest_path.relative_to(ROOT)}: skill path must be a string")
        skill_dir = (plugin_root / rel).resolve()
        try:
            skill_dir.relative_to(plugin_root)
        except ValueError:
            fail(f"{manifest_path.relative_to(ROOT)}: skill path escapes plugin root: {rel}")
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            fail(f"manifest skill missing SKILL.md: {rel}")
        fm = parse_frontmatter(skill_file)
        skill_name = fm.get("name") or skill_dir.name
        if skill_name != skill_dir.name:
            fail(f"{skill_file.relative_to(ROOT)}: frontmatter name must match directory")
        if not fm.get("description"):
            fail(f"{skill_file.relative_to(ROOT)}: description is required")
        if skill_name in seen:
            fail(f"{manifest_path.relative_to(ROOT)}: duplicate skill {skill_name}")
        seen.add(skill_name)

    actual = {p.parent.name for p in skills_dir.glob("*/SKILL.md")}
    extra = actual - seen
    if extra:
        fail(f"{skills_dir.relative_to(ROOT)}: skill folders not listed in plugin.json: {', '.join(sorted(extra))}")

    for skill_name in sorted(seen):
        require_text(bucket_readme, bucket_text, bucket_skill_link(skill_name), f"bucket README link for skill {skill_name}")
        require_text(README, top_readme, top_skill_link(name, skill_name), f"top-level README link for skill {name}/{skill_name}")
        require_text(README, top_readme, f"/{name}:{skill_name}", f"run command for skill {name}/{skill_name}")

    return name, len(seen)


def validate_in_progress(top_readme: str, marketplace_names: set[str]) -> int:
    """Validate the optional draft lifecycle category without publishing it."""
    if not IN_PROGRESS.exists():
        return 0

    if "in-progress" in marketplace_names:
        fail("in-progress is a lifecycle category and must not be listed in marketplace.json")

    manifest_path = IN_PROGRESS / ".claude-plugin" / "plugin.json"
    if manifest_path.exists():
        fail(f"{manifest_path.relative_to(ROOT)}: in-progress must not define a publishable plugin manifest")

    skills_dir = IN_PROGRESS / "skills"
    bucket_readme = skills_dir / "README.md"
    if not bucket_readme.exists():
        fail(f"{skills_dir.relative_to(ROOT)}: draft lifecycle category requires README.md")
    bucket_text = bucket_readme.read_text(encoding="utf-8")

    if "/in-progress:" in top_readme:
        fail("README.md must not advertise /in-progress:* public run examples")

    draft_files = sorted(skills_dir.glob("*/SKILL.md"))
    for skill_file in draft_files:
        fm = parse_frontmatter(skill_file)
        skill_name = fm.get("name") or skill_file.parent.name
        if skill_name != skill_file.parent.name:
            fail(f"{skill_file.relative_to(ROOT)}: frontmatter name must match directory")
        if not fm.get("description"):
            fail(f"{skill_file.relative_to(ROOT)}: description is required")
        if skill_name not in bucket_text:
            fail(f"{bucket_readme.relative_to(ROOT)} does not mention draft skill {skill_name}")

    return len(draft_files)


def main() -> None:
    marketplace = load_json(MARKETPLACE)
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail("marketplace.json must list at least one plugin")

    marketplace_name = marketplace.get("name")
    if not isinstance(marketplace_name, str) or not marketplace_name:
        fail("marketplace.json missing name")

    top_readme = README.read_text(encoding="utf-8")
    total_skills = 0
    names: set[str] = set()
    for plugin_entry in plugins:
        plugin_name, skill_count = validate_plugin(plugin_entry, top_readme, marketplace_name)
        if plugin_name in names:
            fail(f"marketplace.json lists duplicate plugin {plugin_name}")
        names.add(plugin_name)
        total_skills += skill_count

    draft_count = validate_in_progress(top_readme, names)
    suffix = f", {draft_count} draft skill(s) checked" if draft_count else ""
    print(f"OK: {len(names)} plugin(s), {total_skills} promoted skill(s) validated{suffix}")


if __name__ == "__main__":
    main()
