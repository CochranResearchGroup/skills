#!/usr/bin/env python3
"""Validate the additive ChatGPT GitHub skills package."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import zipfile


NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_SKILLS = {
    "github-architecture-survey",
    "github-ask-matt",
    "github-code-review",
    "github-codebase-design",
    "github-domain-modeling",
    "github-grill-me",
    "github-grill-with-docs",
    "github-grilling",
    "github-handoff",
    "github-research",
    "github-to-spec",
    "github-to-tickets",
    "github-wayfinder",
    "github-writing-for-agents",
}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"missing YAML frontmatter: {path}")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"unterminated YAML frontmatter: {path}")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip()] = value.strip()
    return fields


def validate_zip(path: Path, required_suffix: str) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if not names or not any(name.endswith(required_suffix) for name in names):
            raise ValueError(f"archive lacks {required_suffix}: {path}")
        if any(name.startswith("/") or ".." in Path(name).parts for name in names):
            raise ValueError(f"unsafe archive member: {path}")


def main() -> int:
    plugin_root = Path(__file__).resolve().parents[1]
    repo_root = plugin_root.parents[1]
    manifest = json.loads((plugin_root / "plugin.json").read_text())
    marketplace = json.loads((repo_root / ".agents/plugins/marketplace.json").read_text())

    if manifest["name"] != "chatgpt-github-engineering":
        raise ValueError("unexpected plugin identity")
    entry = marketplace["plugins"][0]
    if entry["name"] != manifest["name"]:
        raise ValueError("marketplace and plugin names differ")
    source = (repo_root / entry["source"]["path"]).resolve()
    if source != plugin_root:
        raise ValueError("marketplace source does not resolve to plugin root")

    skills_root = plugin_root / "skills"
    actual = {path.name for path in skills_root.iterdir() if path.is_dir()}
    if actual != EXPECTED_SKILLS:
        raise ValueError(f"skill inventory differs: {sorted(actual ^ EXPECTED_SKILLS)}")
    for name in sorted(actual):
        fields = frontmatter(skills_root / name / "SKILL.md")
        if fields.get("name") != name or not NAME.fullmatch(name):
            raise ValueError(f"invalid skill name: {name}")
        if len(fields.get("description", "")) < 40:
            raise ValueError(f"description is not discriminating: {name}")

    dist = plugin_root / "dist"
    for name in sorted(actual):
        validate_zip(dist / f"{name}.zip", "SKILL.md")
    validate_zip(
        dist / f"{manifest['name']}-plugin.zip",
        f"{manifest['name']}/plugin.json",
    )
    print(f"validated plugin, marketplace, and {len(actual)} skill archives")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
