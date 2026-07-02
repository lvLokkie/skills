#!/usr/bin/env python3
"""Validate the skills marketplace manifests, plugin manifests, and skill frontmatter."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, NoReturn

ROOT = Path(__file__).resolve().parents[1]
CLAUDE_MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CODEX_MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
README = ROOT / "README.md"
AGENTS = ROOT / "AGENTS.md"
INVOCATION_DOC = ROOT / "docs" / "invocation.md"
SKILL_AUDIT = ROOT / "plugins" / "skill-management" / "skills" / "skill-audit" / "SKILL.md"
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


def validate_claude_plugin(plugin_entry: object, top_readme: str, marketplace_name: str) -> tuple[str, str, set[str]]:
    if not isinstance(plugin_entry, dict):
        fail("Claude marketplace plugin entry must be an object")
    raw_name = plugin_entry.get("name")
    raw_source = plugin_entry.get("source")
    if not isinstance(raw_name, str) or not raw_name:
        fail("Claude marketplace plugin entry missing name")
    name = raw_name
    if not isinstance(raw_source, str) or not raw_source:
        fail(f"Claude marketplace plugin {name}: missing source")
    source = raw_source

    plugin_root = (ROOT / source).resolve()
    try:
        plugin_root.relative_to(ROOT.resolve())
    except ValueError:
        fail(f"Claude marketplace plugin {name}: source escapes repo root: {source}")
    if not plugin_root.is_dir():
        fail(f"Claude marketplace plugin {name}: source directory missing: {source}")

    manifest_path = plugin_root / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        fail(f"Claude marketplace plugin {name}: missing .claude-plugin/plugin.json")
    manifest = load_json(manifest_path)
    if manifest.get("name") != name:
        fail(f"{manifest_path.relative_to(ROOT)}: manifest name must match marketplace entry {name!r}")
    version = manifest.get("version")
    if not isinstance(version, str) or not version:
        fail(f"{manifest_path.relative_to(ROOT)}: version is required")

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

    return name, version, seen


def validate_codex_plugin(
    plugin_entry: object,
    top_readme: str,
    expected_skills: dict[str, set[str]],
    expected_versions: dict[str, str],
) -> str:
    if not isinstance(plugin_entry, dict):
        fail("Codex marketplace plugin entry must be an object")

    raw_name = plugin_entry.get("name")
    if not isinstance(raw_name, str) or not raw_name:
        fail("Codex marketplace plugin entry missing name")
    name = raw_name

    if name not in expected_skills:
        fail(f"Codex marketplace lists unknown plugin {name!r}")

    raw_source = plugin_entry.get("source")
    if not isinstance(raw_source, dict):
        fail(f"Codex marketplace plugin {name}: source must be an object")
    if raw_source.get("source") != "local":
        fail(f"Codex marketplace plugin {name}: source.source must be 'local'")
    raw_path = raw_source.get("path")
    if not isinstance(raw_path, str) or not raw_path:
        fail(f"Codex marketplace plugin {name}: source.path is required")

    plugin_root = (ROOT / raw_path).resolve()
    try:
        plugin_root.relative_to(ROOT.resolve())
    except ValueError:
        fail(f"Codex marketplace plugin {name}: source path escapes repo root: {raw_path}")
    if not plugin_root.is_dir():
        fail(f"Codex marketplace plugin {name}: source directory missing: {raw_path}")

    policy = plugin_entry.get("policy")
    if not isinstance(policy, dict):
        fail(f"Codex marketplace plugin {name}: policy must be an object")
    if policy.get("installation") not in {"NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"}:
        fail(f"Codex marketplace plugin {name}: invalid policy.installation")
    if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
        fail(f"Codex marketplace plugin {name}: invalid policy.authentication")
    if not isinstance(plugin_entry.get("category"), str) or not plugin_entry.get("category"):
        fail(f"Codex marketplace plugin {name}: category is required")

    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    if not manifest_path.exists():
        fail(f"Codex marketplace plugin {name}: missing .codex-plugin/plugin.json")
    manifest = load_json(manifest_path)
    if manifest.get("name") != name:
        fail(f"{manifest_path.relative_to(ROOT)}: manifest name must match marketplace entry {name!r}")
    if manifest.get("version") != expected_versions[name]:
        fail(f"{manifest_path.relative_to(ROOT)}: version must match Claude manifest {expected_versions[name]!r}")
    if manifest.get("skills") != "./skills/":
        fail(f"{manifest_path.relative_to(ROOT)}: skills must be './skills/'")
    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        fail(f"{manifest_path.relative_to(ROOT)}: interface object is required")
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if not isinstance(interface.get(key), str) or not interface.get(key):
            fail(f"{manifest_path.relative_to(ROOT)}: interface.{key} is required")

    skills_dir = plugin_root / "skills"
    actual = {p.parent.name for p in skills_dir.glob("*/SKILL.md")}
    if actual != expected_skills[name]:
        fail(
            f"{manifest_path.relative_to(ROOT)}: skills directory does not match Claude manifest: "
            f"expected {', '.join(sorted(expected_skills[name]))}; got {', '.join(sorted(actual))}"
        )

    require_text(README, top_readme, "codex plugin marketplace add", "Codex marketplace registration command")
    return name


def validate_codex_marketplace(
    top_readme: str,
    expected_skills: dict[str, set[str]],
    expected_versions: dict[str, str],
    expected_marketplace_name: str,
) -> set[str]:
    marketplace = load_json(CODEX_MARKETPLACE)
    if marketplace.get("name") != expected_marketplace_name:
        fail(f"{CODEX_MARKETPLACE.relative_to(ROOT)}: name must match Claude marketplace {expected_marketplace_name!r}")
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail(f"{CODEX_MARKETPLACE.relative_to(ROOT)} must list at least one plugin")

    names: set[str] = set()
    for plugin_entry in plugins:
        plugin_name = validate_codex_plugin(plugin_entry, top_readme, expected_skills, expected_versions)
        if plugin_name in names:
            fail(f"{CODEX_MARKETPLACE.relative_to(ROOT)} lists duplicate plugin {plugin_name}")
        names.add(plugin_name)

    missing = set(expected_skills) - names
    if missing:
        fail(f"{CODEX_MARKETPLACE.relative_to(ROOT)} missing plugin(s): {', '.join(sorted(missing))}")
    return names


def validate_in_progress(top_readme: str, marketplace_names: set[str]) -> int:
    """Validate the optional draft lifecycle category without publishing it."""
    if not IN_PROGRESS.exists():
        return 0

    if "in-progress" in marketplace_names:
        fail("in-progress is a lifecycle category and must not be listed in marketplace.json")

    manifest_path = IN_PROGRESS / ".claude-plugin" / "plugin.json"
    if manifest_path.exists():
        fail(f"{manifest_path.relative_to(ROOT)}: in-progress must not define a publishable plugin manifest")
    codex_manifest_path = IN_PROGRESS / ".codex-plugin" / "plugin.json"
    if codex_manifest_path.exists():
        fail(f"{codex_manifest_path.relative_to(ROOT)}: in-progress must not define a publishable Codex plugin manifest")

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


def validate_multimodel_policy() -> None:
    agents_text = AGENTS.read_text(encoding="utf-8")
    invocation_text = INVOCATION_DOC.read_text(encoding="utf-8")
    audit_text = SKILL_AUDIT.read_text(encoding="utf-8")

    require_text(AGENTS, agents_text, "Multimodel support is mandatory", "mandatory multimodel rule")
    require_text(AGENTS, agents_text, "shared skill behavior must remain agent-neutral", "agent-neutral source rule")
    require_text(INVOCATION_DOC, invocation_text, "Portability invariant", "invocation portability policy")
    require_text(SKILL_AUDIT, audit_text, "Check multimodel portability", "skill-audit multimodel gate")


def main() -> None:
    marketplace = load_json(CLAUDE_MARKETPLACE)
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail("Claude marketplace.json must list at least one plugin")

    marketplace_name = marketplace.get("name")
    if not isinstance(marketplace_name, str) or not marketplace_name:
        fail("Claude marketplace.json missing name")

    top_readme = README.read_text(encoding="utf-8")
    total_skills = 0
    names: set[str] = set()
    expected_skills: dict[str, set[str]] = {}
    expected_versions: dict[str, str] = {}
    for plugin_entry in plugins:
        plugin_name, version, plugin_skills = validate_claude_plugin(plugin_entry, top_readme, marketplace_name)
        if plugin_name in names:
            fail(f"Claude marketplace.json lists duplicate plugin {plugin_name}")
        names.add(plugin_name)
        expected_skills[plugin_name] = plugin_skills
        expected_versions[plugin_name] = version
        total_skills += len(plugin_skills)

    codex_names = validate_codex_marketplace(top_readme, expected_skills, expected_versions, marketplace_name)
    validate_multimodel_policy()

    draft_count = validate_in_progress(top_readme, names | codex_names)
    suffix = f", {draft_count} draft skill(s) checked" if draft_count else ""
    print(f"OK: {len(names)} Claude/Codex plugin(s), {total_skills} promoted skill(s) validated{suffix}")


if __name__ == "__main__":
    main()
