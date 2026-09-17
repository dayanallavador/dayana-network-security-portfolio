from pathlib import Path
import re

path = Path("index.html")
s = path.read_text(encoding="utf-8")

# Keep detail pages visible when a table-of-contents anchor is selected.
s = s.replace(
    ".detail-view:target{\n  visibility:visible;\n  opacity:1;\n  pointer-events:auto;\n  transform:translateY(0);\n}\n",
    ".detail-view:target,\n.detail-view:has(:target){\n  visibility:visible;\n  opacity:1;\n  pointer-events:auto;\n  transform:translateY(0);\n}\n",
)

# The public portfolio should show finished work only.
# Hide project cards that do not have a finished case study yet.
for title in (
    "BGP Troubleshooting Lab",
    "IPsec: Tunnel Up, Traffic Down",
):
    pattern = rf'\n\s*<article class="card project-card">(?:(?!</article>).)*?<h3>{re.escape(title)}</h3>.*?</article>'
    s = re.sub(pattern, '', s, count=1, flags=re.S)

# Update the project count and make the single finished project use the available space well.
s = s.replace(
    'FEATURED PROJECTS <span class="list-count">3 projects</span>',
    'FEATURED PROJECTS <span class="list-count">1 project</span>',
)
s = s.replace('<div class="project-grid">', '<div class="project-grid single-project">', 1)
s = s.replace(
    '.project-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}\n',
    '.project-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}\n'
    '.project-grid.single-project{grid-template-columns:minmax(0,1fr);max-width:760px}\n',
    1,
)

# Hide technical notes that are not written yet.
unfinished_notes = [
    '<a href="#"><time>02 Sep 2026</time><span>BGP Local Preference vs Weight</span><b>→</b></a>',
    '<a href="#"><time>28 Aug 2026</time><span>Why an IPsec tunnel can be UP but traffic fails</span><b>→</b></a>',
    '<a href="#"><time>20 Aug 2026</time><span>Understanding VRFs without overcomplicating them</span><b>→</b></a>',
    '<a href="#"><time>15 Aug 2026</time><span>DNS troubleshooting from client to authoritative server</span><b>→</b></a>',
]
for note in unfinished_notes:
    s = s.replace(note, '')

s = s.replace(
    'LATEST TECHNICAL NOTES <span class="list-count">5 notes</span>',
    'LATEST TECHNICAL NOTES <span class="list-count">1 note</span>',
)

# There is only one real content page in Projects/Notes at the moment, so remove fake pagination.
s = re.sub(r'\n\s*<nav class="pagination" aria-label="Projects pagination">.*?</nav>', '', s, flags=re.S)
s = re.sub(r'\n\s*<nav class="pagination" aria-label="Troubleshooting pagination">.*?</nav>', '', s, flags=re.S)
s = re.sub(r'\n\s*<nav class="pagination" aria-label="Technical notes pagination">.*?</nav>', '', s, flags=re.S)

# Keep section links functional instead of jumping to the top.
s = s.replace('<a class="section-link" href="#">View all posts →</a>', '<a class="section-link" href="#blog">View all posts →</a>')

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

# Center the single-item article navigation.
s = s.replace(
    ".article-nav .center{\n  text-align:center;\n}\n",
    ".article-nav .center{\n  text-align:center;\n}\n.article-nav.single{grid-template-columns:1fr}\n",
)

path.write_text(s, encoding="utf-8")
