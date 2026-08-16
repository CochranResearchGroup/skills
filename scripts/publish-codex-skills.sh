#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
manifest="$repo_root/.claude-plugin/plugin.json"
destination="${CODEX_USER_SKILLS_DIR:-$HOME/.agents/skills}"
destination_parent="$(dirname "$destination")"
mode="publish"

if [[ "$destination" != /* || "$destination" == "/" ]]; then
  echo "error: CODEX_USER_SKILLS_DIR must be an absolute, non-root path" >&2
  exit 2
fi

if [[ "${1:-}" == "--check" ]]; then
  mode="check"
elif [[ -n "${1:-}" ]]; then
  echo "usage: $0 [--check]" >&2
  exit 2
fi

mapfile -t skill_paths < <(
  python3 - "$manifest" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as handle:
    for skill_path in json.load(handle)["skills"]:
        print(skill_path)
PY
)

declare -A wanted=()
for skill_path in "${skill_paths[@]}"; do
  source_dir="$repo_root/${skill_path#./}"
  skill_name="$(basename "$source_dir")"
  if [[ "$skill_name" == "implement" ]]; then
    echo "error: implement must not be published by this downstream" >&2
    exit 1
  fi
  if [[ ! -f "$source_dir/SKILL.md" || ! -f "$source_dir/agents/openai.yaml" ]]; then
    echo "error: incomplete promoted skill: $source_dir" >&2
    exit 1
  fi
  if [[ -n "${wanted[$skill_name]:-}" ]]; then
    echo "error: duplicate promoted skill name: $skill_name" >&2
    exit 1
  fi
  wanted["$skill_name"]="$source_dir"
done

if [[ "$mode" == "check" ]]; then
  failures=0
  for skill_path in "${skill_paths[@]}"; do
    skill_name="$(basename "$skill_path")"
    target="$destination/$skill_name"
    expected="${wanted[$skill_name]}"
    if [[ ! -L "$target" || "$(readlink -f "$target")" != "$expected" ]]; then
      echo "mismatch: $skill_name expected $expected" >&2
      failures=1
    fi
  done
  for retired_name in implement to-prd to-issues writing-great-skills; do
    if [[ -e "$destination/$retired_name" || -L "$destination/$retired_name" ]]; then
      echo "retired skill still installed: $retired_name" >&2
      failures=1
    fi
  done
  if [[ "$failures" -ne 0 ]]; then
    exit 1
  fi
  echo "verified ${#wanted[@]} Codex user-scope skills in $destination"
  exit 0
fi

mkdir -p "$destination"
timestamp="$(date -u +%Y%m%dT%H%M%SZ)"
backup_dir="$destination_parent/skill-backups/mapocock/$timestamp"
backup_used=0

move_to_backup() {
  local target="$1"
  local name="$2"
  mkdir -p "$backup_dir"
  mv "$target" "$backup_dir/$name"
  backup_used=1
}

for retired_name in implement to-prd to-issues writing-great-skills; do
  retired_target="$destination/$retired_name"
  if [[ -e "$retired_target" || -L "$retired_target" ]]; then
    move_to_backup "$retired_target" "$retired_name"
    echo "retired $retired_name"
  fi
done

for skill_path in "${skill_paths[@]}"; do
  skill_name="$(basename "$skill_path")"
  source_dir="${wanted[$skill_name]}"
  target="$destination/$skill_name"
  if [[ -L "$target" && "$(readlink -f "$target")" == "$source_dir" ]]; then
    echo "current $skill_name"
    continue
  fi
  if [[ -e "$target" || -L "$target" ]]; then
    move_to_backup "$target" "$skill_name"
  fi
  temporary_link="$destination/.${skill_name}.mapocock-new-$$"
  ln -s "$source_dir" "$temporary_link"
  mv "$temporary_link" "$target"
  echo "published $skill_name -> $source_dir"
done

if [[ "$backup_used" -eq 1 ]]; then
  echo "previous installations preserved in $backup_dir"
fi

"$0" --check
