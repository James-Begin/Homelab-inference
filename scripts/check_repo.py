#!/usr/bin/env python3
"""Check maintained Markdown links and exported animation metadata."""

import hashlib
import json
from pathlib import Path
import re
import struct
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def main():
    documents = [ROOT / "README.md", ROOT / "RESULTS.md", ROOT / "NOTICE"]
    documents += list((ROOT / "docs").glob("*.md"))
    documents += [ROOT / p for p in ["patches/README.md", "archive/README.md",
                                    "archive/tools/README.md", "animations/README.md",
                                    "benchmarks/native/README.md"]]
    failures = []
    for document in documents:
        if not document.exists():
            failures.append(f"Missing maintained document: {document.relative_to(ROOT)}")
            continue
        text = re.sub(r"```.*?```", "", document.read_text(), flags=re.S)
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.strip().strip("<>")
            link = urlsplit(target)
            if link.scheme or not link.path:
                continue
            file = document.parent / unquote(link.path)
            if not file.exists():
                failures.append(f"{document.relative_to(ROOT)}: missing {target}")

    media = ROOT / "docs/media"
    manifest = json.loads((media / "manifest.json").read_text())
    for clip in manifest["clips"]:
        for extension in ["gif", "png", "mp4", "svg"]:
            if not (media / f"{clip['id']}.{extension}").is_file():
                failures.append(f"Missing {clip['id']}.{extension}")
        file = media / f"{clip['id']}.gif"
        if not file.exists():
            continue
        data = file.read_bytes()
        if data[:6] not in (b"GIF87a", b"GIF89a"):
            failures.append(f"Invalid GIF header: {file.name}")
            continue
        size = struct.unpack("<HH", data[6:10])
        if size != (clip["width"], clip["height"]):
            failures.append(f"GIF dimensions differ from manifest: {file.name}")
        if len(data) != clip["gifBytes"] or hashlib.sha256(data).hexdigest() != clip["gifSha256"]:
            failures.append(f"GIF bytes differ from manifest: {file.name}")

    if failures:
        raise SystemExit("\n".join(failures))
    print(f"Checked {len(documents)} maintained documents and {len(manifest['clips'])} media sets.")


if __name__ == "__main__":
    main()
