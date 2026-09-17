from pathlib import Path
import re

path = Path("index.html")
s = path.read_text(encoding="utf-8")

# Keep detail pages visible when a table-of-contents anchor is selected.
s = s.replace(
    ".detail-view:target{\n  visibility:visible;\n  opacity:1;\n  pointer-events:auto;\n  transform:translateY(0);\n}\n",
    ".detail-view:target,\n.detail-view:has(:target){\n  visibility:visible;\n  opacity:1;\n  pointer-events:auto;\n  transform:translateY(0);\n}\n",
)

# Styles for entries that are visible but do not have a finished article yet.
s = s.replace(
    ".read-link{color:var(--blue);font-weight:700;font-size:14px}\n",
    ".read-link{color:var(--blue);font-weight:700;font-size:14px}\n"
    ".read-link.disabled-link{color:var(--muted);cursor:default;opacity:.65}\n",
)

s = s.replace(
    ".notes a{display:grid;grid-template-columns:95px 1fr 18px;gap:16px;align-items:center;padding:12px 2px;border-bottom:1px solid var(--line)}\n"
    ".notes time{color:var(--muted);font-size:12px}.notes span{font-size:14px}.notes b{color:var(--blue)}\n",
    ".notes a,.notes .draft-row{display:grid;grid-template-columns:95px 1fr 42px;gap:16px;align-items:center;padding:12px 2px;border-bottom:1px solid var(--line)}\n"
    ".notes time{color:var(--muted);font-size:12px}.notes span{font-size:14px}.notes b{color:var(--blue)}\n"
    ".notes .draft-row{opacity:.62;cursor:default}.notes .draft-row b{color:var(--muted);font-size:11px;text-align:right}\n",
)

s = s.replace(
    ".article-nav .center{\n  text-align:center;\n}\n",
    ".article-nav .center{\n  text-align:center;\n}\n.article-nav.single{grid-template-columns:1fr}\n",
)

# Project cards without a finished case study should not jump to the top of the page.
s = s.replace(
    '<a class="read-link" href="#">Read case study →</a>',
    '<span class="read-link disabled-link">Case study coming soon</span>',
    2,
)

# There is only one real content page at the moment, so remove fake pagination.
s = re.sub(r'\n\s*<nav class="pagination" aria-label="Projects pagination">.*?</nav>', '', s, flags=re.S)
s = re.sub(r'\n\s*<nav class="pagination" aria-label="Troubleshooting pagination">.*?</nav>', '', s, flags=re.S)
s = re.sub(r'\n\s*<nav class="pagination" aria-label="Technical notes pagination">.*?</nav>', '', s, flags=re.S)

# Keep View all posts on the Notes section instead of jumping to the top.
s = s.replace('<a class="section-link" href="#">View all posts →</a>', '<a class="section-link" href="#blog">View all posts →</a>')

# Notes that do not have a finished article yet are shown as drafts, not broken links.
drafts = {
    '<a href="#"><time>02 Sep 2026</time><span>BGP Local Preference vs Weight</span><b>→</b></a>':
        '<div class="draft-row"><time>02 Sep 2026</time><span>BGP Local Preference vs Weight</span><b>DRAFT</b></div>',
    '<a href="#"><time>28 Aug 2026</time><span>Why an IPsec tunnel can be UP but traffic fails</span><b>→</b></a>':
        '<div class="draft-row"><time>28 Aug 2026</time><span>Why an IPsec tunnel can be UP but traffic fails</span><b>DRAFT</b></div>',
    '<a href="#"><time>20 Aug 2026</time><span>Understanding VRFs without overcomplicating them</span><b>→</b></a>':
        '<div class="draft-row"><time>20 Aug 2026</time><span>Understanding VRFs without overcomplicating them</span><b>DRAFT</b></div>',
    '<a href="#"><time>15 Aug 2026</time><span>DNS troubleshooting from client to authoritative server</span><b>→</b></a>':
        '<div class="draft-row"><time>15 Aug 2026</time><span>DNS troubleshooting from client to authoritative server</span><b>DRAFT</b></div>',
}
for old, new in drafts.items():
    s = s.replace(old, new)

# No credential URL exists yet, so do not show a dead link.
s = s.replace('            <a class="section-link" href="#">View credential profile →</a>\n', '')

# The project and note sections currently have only one finished detail page.
s = s.replace(
    '''            <div class="article-nav">\n              <a href="#">← Previous Project</a>\n              <a class="center" href="#projects">Back to Projects</a>\n              <a href="#">Next Project →</a>\n            </div>''',
    '''            <div class="article-nav single">\n              <a class="center" href="#projects">Back to Projects</a>\n            </div>''',
)

s = s.replace(
    '''            <div class="article-nav">\n              <a href="#">← Previous Note</a>\n              <a class="center" href="#blog">All Notes</a>\n              <a href="#">Next Note →</a>\n            </div>''',
    '''            <div class="article-nav single">\n              <a class="center" href="#blog">All Notes</a>\n            </div>''',
)

path.write_text(s, encoding="utf-8")
