#!/usr/bin/env python3
"""Validate deterministic portfolio properties without making disclosure decisions."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


MAX_FILE_SIZE = 5 * 1024 * 1024
FORBIDDEN_SUFFIXES = {".key", ".p12", ".pem", ".pfx"}
MEDIA_SUFFIXES = {
    ".avif",
    ".gif",
    ".jpeg",
    ".jpg",
    ".mov",
    ".mp3",
    ".mp4",
    ".pdf",
    ".png",
    ".svg",
    ".wav",
    ".webm",
    ".webp",
}
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_PATTERN = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
DETAILS_PATTERN = re.compile(r"</?details\b[^>]*>", re.IGNORECASE)
FLOWCHART_DECLARATION = re.compile(r"^(?:flowchart|graph)\s+(TB|TD|BT|RL|LR)\s*$")
EDGE_PATTERN = re.compile(r"(?:-->|---|-.->|==>|--o|--x|<-->)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root; defaults to the parent of scripts/",
    )
    return parser.parse_args()


def tracked_paths(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [Path(value) for value in result.stdout.split("\0") if value]


def repository_markdown(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.relative_to(root).parts and path.is_file()
    )


def is_forbidden_path(path: Path) -> bool:
    name = path.name
    return (
        name == ".DS_Store"
        or name == ".env"
        or name.startswith(".env.")
        or path.suffix.lower() in FORBIDDEN_SUFFIXES
    )


def validate_hygiene(root: Path, tracked: list[Path]) -> list[str]:
    errors: list[str] = []
    for relative in tracked:
        if is_forbidden_path(relative):
            errors.append(f"repository hygiene: tracked forbidden file: {relative}")
    return errors


def validate_file_policy(root: Path, tracked: list[Path]) -> list[str]:
    errors: list[str] = []
    for relative in tracked:
        path = root / relative
        if not path.is_file():
            continue

        size = path.stat().st_size
        if size > MAX_FILE_SIZE:
            errors.append(
                f"file policy: {relative} is {size} bytes; "
                f"the per-file limit is {MAX_FILE_SIZE} bytes"
            )

        if relative.suffix.lower() in MEDIA_SUFFIXES and (
            not relative.parts or relative.parts[0] != "assets"
        ):
            errors.append(f"file policy: media file must be under assets/: {relative}")
    return errors


def link_destination(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        return value[1 : value.index(">")]
    return value.split(maxsplit=1)[0]


def validate_links(root: Path, markdown_files: list[Path]) -> tuple[list[str], int]:
    errors: list[str] = []
    checked = 0

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            destination = link_destination(match.group(1))
            if not destination or destination.startswith("#"):
                continue
            if destination.startswith("//") or re.match(
                r"^[A-Za-z][A-Za-z0-9+.-]*:", destination
            ):
                continue

            local = unquote(destination.split("#", 1)[0].split("?", 1)[0])
            if not local:
                continue

            target = (path.parent / local).resolve()
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(
                    f"local references: {path.relative_to(root)} points outside "
                    f"the repository: {destination}"
                )
                continue

            checked += 1
            if not target.exists():
                errors.append(
                    f"local references: {path.relative_to(root)} has missing target: "
                    f"{destination}"
                )

    return errors, checked


def extract_fenced_blocks(path: Path, root: Path) -> tuple[list[str], list[tuple[str, list[str], int]]]:
    errors: list[str] = []
    blocks: list[tuple[str, list[str], int]] = []
    fence_character = ""
    fence_length = 0
    info = ""
    content: list[str] = []
    opened_at = 0

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not fence_character:
            match = FENCE_PATTERN.match(line)
            if match:
                marker = match.group(1)
                fence_character = marker[0]
                fence_length = len(marker)
                info = match.group(2).strip()
                content = []
                opened_at = line_number
            continue

        if re.match(
            rf"^\s*{re.escape(fence_character)}{{{fence_length},}}\s*$", line
        ):
            blocks.append((info, content, opened_at))
            fence_character = ""
            fence_length = 0
            info = ""
            content = []
            opened_at = 0
        else:
            content.append(line)

    if fence_character:
        errors.append(
            f"Markdown structure: {path.relative_to(root)} has an unclosed "
            f"code fence opened at line {opened_at}"
        )
    return errors, blocks


def validate_details(path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    depth = 0
    for match in DETAILS_PATTERN.finditer(path.read_text(encoding="utf-8")):
        if match.group(0).lower().startswith("</"):
            if depth == 0:
                errors.append(
                    f"Markdown structure: {path.relative_to(root)} has an "
                    "unmatched </details>"
                )
            else:
                depth -= 1
        else:
            depth += 1
    if depth:
        errors.append(
            f"Markdown structure: {path.relative_to(root)} has {depth} "
            "unclosed <details> block(s)"
        )
    return errors


def delimiter_error(lines: list[str]) -> str | None:
    opening = {"[": "]", "(": ")", "{": "}"}
    closing = set(opening.values())
    stack: list[str] = []
    quote = ""

    for line in lines:
        escaped = False
        for character in line:
            if escaped:
                escaped = False
                continue
            if character == "\\":
                escaped = True
                continue
            if quote:
                if character == quote:
                    quote = ""
                continue
            if character in {'"', "'", "`"}:
                quote = character
                continue
            if character in opening:
                stack.append(opening[character])
            elif character in closing:
                if not stack or stack.pop() != character:
                    return f"unexpected closing delimiter {character}"

    if quote:
        return "unclosed quoted string"
    if stack:
        return f"missing closing delimiter {stack[-1]}"
    return None


def validate_mermaid_block(
    path: Path, root: Path, lines: list[str], opened_at: int
) -> list[str]:
    errors: list[str] = []
    meaningful = [line.strip() for line in lines if line.strip() and not line.strip().startswith("%%")]
    location = f"{path.relative_to(root)}:{opened_at}"

    if not meaningful:
        return [f"Mermaid structure: {location} is empty"]
    if not FLOWCHART_DECLARATION.fullmatch(meaningful[0]):
        return [
            f"Mermaid structure: {location} must begin with a supported "
            "flowchart declaration and direction"
        ]

    subgraph_depth = 0
    has_edge = False
    for line in meaningful[1:]:
        if line.startswith("subgraph "):
            subgraph_depth += 1
        elif line == "end":
            if subgraph_depth == 0:
                errors.append(f"Mermaid structure: {location} has an unmatched end")
            else:
                subgraph_depth -= 1
        if EDGE_PATTERN.search(line):
            has_edge = True

    if subgraph_depth:
        errors.append(
            f"Mermaid structure: {location} has {subgraph_depth} unclosed subgraph(s)"
        )
    if not has_edge:
        errors.append(f"Mermaid structure: {location} contains no relationship")

    delimiter_issue = delimiter_error(meaningful[1:])
    if delimiter_issue:
        errors.append(f"Mermaid structure: {location} has {delimiter_issue}")
    return errors


def validate_markdown(
    root: Path, markdown_files: list[Path]
) -> tuple[list[str], int]:
    errors: list[str] = []
    mermaid_count = 0

    for path in markdown_files:
        fence_errors, blocks = extract_fenced_blocks(path, root)
        errors.extend(fence_errors)
        errors.extend(validate_details(path, root))
        for info, lines, opened_at in blocks:
            if info.split(maxsplit=1)[0].lower() == "mermaid":
                mermaid_count += 1
                errors.extend(validate_mermaid_block(path, root, lines, opened_at))

    return errors, mermaid_count


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not (root / ".git").exists():
        print(f"[FAIL] not a Git repository root: {root}", file=sys.stderr)
        return 2

    tracked = tracked_paths(root)
    markdown_files = repository_markdown(root)
    errors: list[str] = []

    errors.extend(validate_hygiene(root, tracked))
    errors.extend(validate_file_policy(root, tracked))
    link_errors, link_count = validate_links(root, markdown_files)
    errors.extend(link_errors)
    markdown_errors, mermaid_count = validate_markdown(root, markdown_files)
    errors.extend(markdown_errors)

    if errors:
        for error in errors:
            print(f"[FAIL] {error}", file=sys.stderr)
        print(f"Portfolio validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print("Portfolio validation passed.")
    print(f"- Tracked paths checked: {len(tracked)}")
    print(f"- Markdown files checked: {len(markdown_files)}")
    print(f"- Local references checked: {link_count}")
    print(f"- Mermaid blocks structurally checked: {mermaid_count}")
    print(f"- Per-file ceiling: {MAX_FILE_SIZE} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
