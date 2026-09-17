from pathlib import Path

source = Path("index.html")
preview_dir = Path("preview")
preview_file = preview_dir / "index.html"

html = source.read_text(encoding="utf-8")

robots_meta = '  <meta name="robots" content="noindex,nofollow,noarchive" />\n'
if 'name="robots"' not in html:
    html = html.replace("<head>\n", "<head>\n" + robots_meta, 1)

preview_dir.mkdir(parents=True, exist_ok=True)
preview_file.write_text(html, encoding="utf-8")
