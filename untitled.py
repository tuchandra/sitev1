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


def rfc_2822_format(date_str: str) -> str:
    """Convert yyyy-mm-dd date string to RFC 2822 format date string."""

    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return d.strftime("%a, %d %b %Y %H:%M:%S +0000")


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

    # Update the dictionary with content and RFC 2822 date.
    content.update({"content": text, "rfc_2822_date": rfc_2822_format(content["date"])})
    return content


def render(template: str, **params) -> str:
    """Replace placeholders in template with values from params."""

    return re.sub(
        r"{{\s*([^}\s]+)\s*}}",
        lambda match: str(params.get(match.group(1), match.group(0))),
        template,
    )


def make_pages(src: Path, template: str, layout: str, **params):
    """Generate pages from page content."""

    items = []

    for src_path in src.iterdir():
        content = read_content(src_path)
        page_params = dict(params, **content)

        # Populate placeholders in content if content-rendering is enabled.
        if page_params.get("render") == "yes":
            rendered_content = render(page_params["content"], **page_params)
            page_params["content"] = rendered_content
            content["content"] = rendered_content

        items.append(content)

        dst_path = render(template, **page_params)
        output = render(layout, **page_params)

        log("Rendering {} => {} ...", src_path, dst_path)
        fwrite(Path(dst_path), output)

    return sorted(items, key=lambda x: x["date"], reverse=True)


def make_list(posts, dst, list_layout, item_layout, **params):
    """Generate list page for a blog."""

    items = []
    for post in posts:
        item_params = dict(params, **post)
        item_params["summary"] = truncate(post["content"])
        item = render(item_layout, **item_params)
        items.append(item)

    params["content"] = "".join(items)
    dst_path = render(dst, **params)
    output = render(list_layout, **params)

    log("Rendering list => {} ...", dst_path)
    fwrite(Path(dst_path), output)


def main():
    # Create a new _site directory from scratch.
    if os.path.isdir("_site"):
        shutil.rmtree("_site")
    shutil.copytree("static", "_site")

    # Default parameters.
    params = {
        "base_path": "",
        "subtitle": "Lorem Ipsum",
        "author": "Admin",
        "site_url": "tusharc.dev",
        "current_year": datetime.datetime.now().year,
    }

    # If params.json exists, load it.
    params_path = Path("params.json")
    if params_path.exists():
        params.update(json.loads(fread(params_path)))

    # Load layouts.
    page_layout = fread(Path("layout/page.html"))
    post_layout = fread(Path("layout/post.html"))
    list_layout = fread(Path("layout/list.html"))
    item_layout = fread(Path("layout/item.html"))

    # Combine layouts to form final layouts.
    post_layout = render(page_layout, content=post_layout)
    list_layout = render(page_layout, content=list_layout)

    # Create site pages.
    make_pages(Path("content/index.html"), "_site/index.html", page_layout, **params)
    make_pages(Path("content/[!_]*.html"), "_site/{{ slug }}/index.html", page_layout, **params)

    # Create blogs.
    blog_posts = make_pages(
        Path("content/blog/*.md"),
        "_site/blog/{{ slug }}/index.html",
        post_layout,
        blog="blog",
        **params
    )

    # Create blog list pages.
    make_list(
        blog_posts,
        "_site/blog/index.html",
        list_layout,
        item_layout,
        blog="blog",
        title="Blog",
        **params
    )

    # Copy contents to root directory
    # dir_util.copy_tree("_site", "./", update=1)


# Test parameter to be set temporarily by unit tests.
_test = None


if __name__ == "__main__":
    main()
