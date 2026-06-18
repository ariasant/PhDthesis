"""Merge multiple .bib files into a single deduplicated refs.bib."""

import re
from pathlib import Path

SOURCE_FILES = [
    "chapters/refs_intro.bib",
    "Chapter_2_paper_folder/refs.bib",
    "Chapter_3_paper_folder/refs.bib",
    "Chapter_4_paper_folder/refs.bib",
    "Chapter_5_paper_folder/refs.bib",
]
OUTPUT_FILE = "refs.bib"

KEY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)", re.IGNORECASE)


def split_entries(text):
    """Split bib text into a list of entry strings using brace-depth tracking."""
    entries = []
    depth = 0
    start = None
    for i, ch in enumerate(text):
        if ch == "@" and depth == 0:
            start = i
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                entries.append(text[start : i + 1].strip())
                start = None
    return entries


def main():
    seen_keys = {}
    all_entries = []
    total_read = 0

    for path_str in SOURCE_FILES:
        path = Path(path_str)
        if not path.exists():
            print(f"  WARNING: {path_str} not found, skipping.")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        entries = split_entries(text)
        file_dupes = 0
        for entry in entries:
            m = KEY_RE.match(entry)
            if not m:
                continue
            total_read += 1
            key = m.group(1)
            if key in seen_keys:
                file_dupes += 1
            else:
                seen_keys[key] = path_str
                all_entries.append(entry)
        print(f"  {path_str}: {len(entries)} entries, {file_dupes} duplicates dropped")

    output = "\n\n".join(all_entries) + "\n"
    Path(OUTPUT_FILE).write_text(output, encoding="utf-8")

    print(f"\nTotal read : {total_read}")
    print(f"Duplicates : {total_read - len(all_entries)}")
    print(f"Written    : {len(all_entries)} entries -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
