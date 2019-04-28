#!/usr/bin/env python

"""Make static website with Python - updated to use Python 3."""

import commonmark


from pathlib import Path
from typing import Dict, Generator, Tuple

import os
import shutil
import distutils.dir_util as dir_util
import re
import glob
import sys
import json
import datetime


def fread(filename: Path) -> str:
    """Read file and close the file."""

    with open(filename, "r") as f:
        return f.read()


def fwrite(filename: Path, text: str):
    """Write content to file and close the file."""

    filename.parent.mkdir(exist_ok=True)
    with open(filename, "w") as f:
        f.write(text)


def log(msg: str, *args):
    """Log message with specified arguments."""

    sys.stderr.write(msg.format(*args) + "\n")


def truncate(text: str, words: int = 25):
    """Remove tags and truncate text to the specified number of words."""

    return " ".join(re.sub("(?s)<.*?>", " ", text).split()[:words])


def read_headers(text: str) -> Generator[Tuple[str, str, int], None, None]:
    """Parse headers in text and yield (key, value, end-index) tuples.

    Content files can include optional parameters in the form of <!-- key: value -->, so we want
    to be able to identify and parse these.
    """

    for match in re.finditer(r"\s*<!--\s*(.+?)\s*:\s*(.+?)\s*-->\s*|.+", text):
        if not match.group(1):
            break
        yield match.group(1), match.group(2), match.end()


def read_content(filename: Path) -> Dict[str, str]:
    """Read content and metadata from file into a dictionary."""

    text = fread(filename)

    # Read metadata and save it in a dictionary.
    match = re.search(r"^(?:(\d\d\d\d-\d\d-\d\d)-)?(.+)$", filename.stem)
    if not match:
        raise FileNotFoundError
    content = {"date": match.group(1) or "1970-01-01", "slug": match.group(2)}

    # Read headers.
    end = 0
    for key, val, end in read_headers(text):
        content[key] = val

    # Separate content from headers.
    text = text[end:]

    # Convert Markdown content to HTML.
    if filename.suffix in (".md", ".mkd", ".mkdn", ".mdown", ".markdown"):
        text = commonmark.commonmark(text)

    content.update({"content": text})
    return content


def render(template: str, **params) -> str:
    """Replace placeholders in template with values from params."""

    return re.sub(
        r"{{\s*([^}\s]+)\s*}}",
        lambda match: str(params.get(match.group(1), match.group(0))),
        template,
    )


def make_pages(src: str, dst: str, layout: str, **params):
    """Generate pages from page content.
    
    dst: optionally renderable string for destination page, i.e., you can include {{ parameters }} in it.
    """

    items = []

    for src_path in glob.glob(src):
        content = read_content(Path(src_path))
        page_params = dict(params, **content)

        rendered_content = render(page_params["content"], **page_params)
        page_params["content"] = rendered_content
        content["content"] = rendered_content

        items.append(content)

        dst_path = render(dst, **page_params)
        output = render(layout, **page_params)

        log("Rendering {} => {} ...", src_path, dst_path)
        fwrite(Path(dst_path), output)

    return sorted(items, key=lambda x: x["date"], reverse=True)


def main():
    if Path("./site").is_dir():
        shutil.rmtree("site")

    shutil.copytree("static", "site")

    # Default parameters.
    params: Dict[str, str] = {
        "base_path": "site",
        "subtitle": "Tushar Chandra",
        "author": "Tushar Chandra",
        "site_url": "tusharc.dev",
        "current_year": "2019",
    }

    page_layout = fread(Path("layout/page.html"))

    make_pages("content/[!_]*.html", "site/{{ slug }}.html", page_layout, **params)
    make_pages("content/[!_]*.md", "site/{{ slug }}.html", page_layout, **params)
    make_pages("content/spark/*.md", "site/spark/{{ slug }}.html", page_layout, **params)


# Test parameter to be set temporarily by unit tests.
_test = None


if __name__ == "__main__":
    main()