#!/usr/bin/env python3
import os
import shutil
import argparse

# Default YAML front matter
DEFAULT_YAML = """---
format:
  docx:
    highlight-style: github
    toc: false
  html:
    embed-resources: true
    toc: true
    toc-expand: 2
  pdf:
    colorlinks: true
    toc: false
---
"""

def load_yaml_from_file(yaml_path: str) -> str:
    """Load YAML text from a file and ensure it ends with a newline."""
    with open(yaml_path, "r", encoding="utf-8") as f:
        return f.read().rstrip() + "\n"

def has_target_yaml(content: str) -> bool:
    """
    Return True if the file already starts with a YAML block that includes 'format:'.
    This avoids double-prepending similar front matter.
    """
    if not content.startswith("---"):
        return False
    # Find the closing '---' of the first YAML block
    # Accept both '\n---\n' and file end edge cases.
    start = 3  # after leading '---'
    end_marker = "\n---"
    end = content.find(end_marker, start)
    if end == -1:
        return False
    first_block = content[: end + len(end_marker)]
    return "format:" in first_block

def prepend_yaml_to_md_files(root_dir: str, yaml_text: str) -> None:
    updated = skipped = 0
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if not filename.lower().endswith(".md"):
                continue

            filepath = os.path.join(dirpath, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if has_target_yaml(content):
                print(f"Skipping (already has YAML w/ 'format:'): {filepath}")
                skipped += 1
                continue

            # Backup original file
            backup_path = filepath + ".bak"
            shutil.copy2(filepath, backup_path)

            # Prepend YAML front matter
            new_content = yaml_text + "\n" + content
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"Prepended YAML to: {filepath} (backup saved as {backup_path})")
            updated += 1

    print(f"\nDone. Updated: {updated} | Skipped: {skipped}")

def restore_from_backups(root_dir: str) -> None:
    restored = missing = 0
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if not filename.lower().endswith(".md.bak"):
                continue

            bak_path = os.path.join(dirpath, filename)
            orig_path = bak_path[:-4]  # strip '.bak'

            # Restore by copying back, then remove .bak
            shutil.copy2(bak_path, orig_path)
            os.remove(bak_path)

            print(f"Restored: {orig_path}")
            restored += 1

    if restored == 0:
        print("No .md.bak files found to restore.")
    else:
        print(f"\nDone. Restored: {restored}")

def main():
    parser = argparse.ArgumentParser(
        description="Prepend YAML front matter to Markdown files (with optional restore)."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Root directory to scan (default: current directory)",
    )
    parser.add_argument(
        "--yaml",
        dest="yaml_file",
        help="Path to a YAML file to use as front matter (default: built-in YAML).",
    )
    parser.add_argument(
        "--restore",
        action="store_true",
        help="Restore from .md.bak files (ignores --yaml and does not modify backups).",
    )
    args = parser.parse_args()

    if args.restore:
        restore_from_backups(args.directory)
        return

    yaml_text = load_yaml_from_file(args.yaml_file) if args.yaml_file else DEFAULT_YAML
    prepend_yaml_to_md_files(args.directory, yaml_text)

if __name__ == "__main__":
    main()

