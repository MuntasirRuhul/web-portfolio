"""Build the three design-direction pages (tv, playful, editorial).

Each page reuses the header, hero, "Creating Beautiful" work section and
footer from index.html, and adds its own sections from variants/<name>.html.
Run from the repo root:  python3 tools/build_variants.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VARIANTS = {
    "tv": "TV network",
    "playful": "Playful",
    "editorial": "Editorial",
}


def cut(src, start, end):
    a = src.index(start)
    b = src.index(end, a)
    return src[a:b]


def switcher(active):
    links = [("index.html", "Current", "current")] + [
        (f"{key}.html", label, key) for key, label in VARIANTS.items()
    ]
    active_attr = ' class="is-active"'
    items = "".join(
        f'<a href="{href}"{active_attr if key == active else ""}>{label}</a>'
        for href, label, key in links
    )
    return f'    <nav class="version-switch" aria-label="Design versions">{items}</nav>\n'


def main():
    index = (ROOT / "index.html").read_text()
    head = index[: index.index("<body>")]
    header = cut(index, "    <!-- header -->", "    <main")
    hero = cut(index, "        <!-- hero -->", "        <!-- about")
    work = cut(index, "        <!-- work -->", "        <!-- crossing marquees -->")
    footer = cut(index, "    <!-- footer -->", "    <!-- review-only")

    for key, label in VARIANTS.items():
        body = (ROOT / "variants" / f"{key}.html").read_text()
        page_head = head.replace(
            '<link rel="stylesheet" href="style.css">',
            '<link rel="stylesheet" href="style.css">\n'
            f'    <link rel="stylesheet" href="variants/{key}.css">',
        ).replace("<title>ninona", f"<title>ninona ({label})")
        html = (
            page_head
            + f'<body class="v-{key}">\n\n'
            + header
            + '    <main id="top">\n\n'
            + hero
            + work
            + body
            + "    </main>\n\n"
            + footer
            + switcher(key)
            + '    <script src="variants/common.js"></script>\n'
            + f'    <script src="variants/{key}.js"></script>\n'
            + "</body>\n</html>\n"
        )
        (ROOT / f"{key}.html").write_text(html)
        print("built", f"{key}.html")


if __name__ == "__main__":
    main()
