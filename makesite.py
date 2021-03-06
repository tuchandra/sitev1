"""Generate my static website with Python; adapted from https://github.com/sunainapai/makesite"""

import commonmark

from pathlib import Path
from typing import Dict, Generator, Tuple

import shutil
import re
import sys


def fread(filename: Path) -> str:
    """Read file and close the file."""

    with open(filename, "r") as f:
        return f.read()


def fwrite(filename: Path, text: str):
    """Write content to file and close the file."""

    filename.parent.mkdir(exist_ok=True, parents=True)
    with open(filename, "w") as f:
        f.write(text)


def log(msg: str, *args):
    """Log message with specified arguments."""

    sys.stderr.write(msg.format(*args) + "\n")


def read_headers(text: str) -> Generator[Tuple[str, str, int], None, None]:
    """Parse headers in text and yield (key, value, end-index) tuples.

    Content files can include optional parameters in the form of <!-- key: value -->, so we want
    to be able to identify and parse these.
    """

    for match in re.finditer(r"\s*<!--\s*(.+?)\s*:\s*(.+?)\s*-->\s*|.+", text):
        if not match.group(1):
            break
        yield match.group(1), match.group(2), match.end()


def get_title(text: str) -> str:
    """Get the title (first top-level heading line) from a Markdown file"""

    lines = text.splitlines()
    for line in lines:
        if line.startswith("#"):
            return line.replace("#", "").strip()

    return ""


def read_content(filename: Path) -> Dict[str, str]:
    """Read content and metadata from file into a dictionary."""

    text = fread(filename)
    content = {"slug": filename.stem}

    # Read headers from top of file, then separate out the rest of the text
    end = 0
    for key, val, end in read_headers(text):
        content[key] = val
    text = text[end:]

    # Convert Markdown content to HTML: get the title from the original text, then parse the
    # Markdown as HTML, then replace any links to other Markdown files with ones to the generated
    # HTML files (using regex that matches <a href="filename.md">, where filename is anything
    # without whitespace or a colon). The links should all be relative to the directory where the
    # current file is, allowing "..." to go up a level.
    if filename.suffix == ".md":
        if "title" not in content:  # only overwrite if title not already found
            content["title"] = get_title(text)
        text = commonmark.commonmark(text)
        text = re.sub(
            r'<a href="([^:\s]+).md">',
            lambda match: f'<a href="{match.group(1)}.html">',
            text,
        )

    content.update({"content": text})
    return content


def render(template: str, **params) -> str:
    """Replace placeholders in template with values from params."""

    return re.sub(
        r"{{\s*([^}\s]+)\s*}}",
        lambda match: str(params.get(match.group(1), match.group(0))),
        template,
    )


def make_page(src: Path, dst: Path, layout: str, **params):
    """Render one output page

    src: a file, either HTML or Markdown, and notably not a directory.
    dst: the output directory for the page (the filename will be generated automatically)
    """

    # Read content and metadata from source
    content = read_content(src)
    page_params = dict(params, **content)

    rendered_content = render(page_params["content"], **page_params)
    page_params["content"] = rendered_content

    # Render the destination path, then render the output, then write the output to the file
    dst_renderable = Path(dst) / "{{ slug }}.html"
    dst_path = render(dst_renderable.as_posix(), **page_params)
    output = render(layout, **page_params)

    log("Rendering {} => {} ...", src, dst_path)
    fwrite(Path(dst_path), output)


def make_pages(src: Path, dst: Path, layout: str, **params):
    """Recursively generate output pages from given source, destination, and layout

    src: directory of HTML / MD files from which to render pages
    dst: target directory where rendered pages should go
    layout: page layout, stored as renderable string
    """

    if not dst.exists():
        dst.mkdir()

    for src_path in src.iterdir():
        if src_path.is_dir():
            subdir = dst / src_path.stem
            make_pages(src_path, subdir, layout, **params)
        elif src_path.suffix in (".html", ".md"):  # do not render e.g., image files
            make_page(src_path, dst, layout, **params)
        elif src_path.suffix in (".png",):
            shutil.copy(src_path, dst)
            log("Copying image {} into {}", src_path, dst)


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
    make_pages(Path("content/"), Path(params["base_path"]), page_layout, **params)


if __name__ == "__main__":
    main()
