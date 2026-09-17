from pathlib import Path

path = Path("index.html")
s = path.read_text(encoding="utf-8")

css = """

/* Make finished project/troubleshooting cards clickable as a whole */
.clickable-card{
  cursor:pointer;
  transition:transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.clickable-card:hover{
  transform:translateY(-2px);
  border-color:#b9c8df;
}
.clickable-card:focus-visible{
  outline:2px solid var(--blue);
  outline-offset:3px;
}
"""

js = """
<script>
(() => {
  const cards = document.querySelectorAll('.project-card, .trouble-card');

  cards.forEach((card) => {
    const link = card.querySelector('a.read-link[href]');
    if (!link) return;

    const href = link.getAttribute('href');
    if (!href || href === '#') return;

    card.classList.add('clickable-card');
    card.setAttribute('role', 'link');
    card.setAttribute('tabindex', '0');

    card.addEventListener('click', (event) => {
      if (event.target.closest('a, button')) return;
      link.click();
    });

    card.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        link.click();
      }
    });
  });
})();
</script>
"""

if "/* Make finished project/troubleshooting cards clickable as a whole */" not in s:
    s = s.replace("</style>", css + "\n</style>", 1)

if "const cards = document.querySelectorAll('.project-card, .trouble-card');" not in s:
    s = s.replace("</body>", js + "\n</body>", 1)

path.write_text(s, encoding="utf-8")
