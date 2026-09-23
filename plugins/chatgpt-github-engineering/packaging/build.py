#!/usr/bin/env python3
"""Build reproducible individual-skill and bundled-plugin ZIP archives."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import zipfile


FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def files_below(root: Path, excluded_root: Path | None = None):
    for path in sorted(root.rglob("*")):
        if excluded_root is not None and (path == excluded_root or excluded_root in path.parents):
            continue
        if "__pycache__" in path.parts:
            continue
        if path.is_symlink():
            raise ValueError(f"symlinks are not permitted in packages: {path}")
        if path.is_file():
            yield path


def write_zip(
    source: Path,
    destination: Path,
    archive_root: str,
    excluded_root: Path | None = None,
) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files_below(source, excluded_root):
            relative = path.relative_to(source).as_posix()
            info = zipfile.ZipInfo(f"{archive_root}/{relative}", FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    plugin_root = Path(__file__).resolve().parents[1]
    manifest = json.loads((plugin_root / "plugin.json").read_text())
    skills_root = plugin_root / "skills"
    skills = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skills:
        raise ValueError("plugin contains no skills")

    for skill in skills:
        if not (skill / "SKILL.md").is_file():
            raise ValueError(f"missing SKILL.md: {skill}")
        write_zip(skill, args.output_dir / f"{skill.name}.zip", skill.name)

    plugin_name = manifest["name"]
    output_dir = args.output_dir.resolve()
    excluded_root = output_dir if plugin_root in output_dir.parents else None
    write_zip(
        plugin_root,
        output_dir / f"{plugin_name}-plugin.zip",
        plugin_name,
        excluded_root,
    )
    print(f"built {len(skills)} skill ZIPs and 1 plugin ZIP in {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
