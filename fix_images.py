"""
Ameliorer l'affichage des images dans les modules de index.html :
- phone-frame plus grand et responsive
- grilles d'images centrees et bien espacees
- lightbox au clic pour zoom plein ecran
- img-gallery avec hauteur uniforme et meilleur rendu
"""

IN  = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"
OUT = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"

with open(IN, "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================
# 1. REMPLACER le CSS .phone-frame
# ============================================================
OLD_PHONE_CSS = """.phone-frame {
  width: 120px;
  border-radius: 20px;
  border: 3px solid #222;
  overflow: hidden;
  box-shadow: 0 6px 20px rgba(0,0,0,0.25);
  flex-shrink: 0;
  background: #000;
}
.phone-frame img {
  width: 100%;
  display: block;
  border-radius: 17px;
}"""

NEW_PHONE_CSS = """.phone-frame {
  border-radius: 18px;
  border: 2.5px solid #333;
  overflow: hidden;
  box-shadow: 0 6px 24px rgba(0,0,0,0.22);
  background: #000;
  cursor: zoom-in;
  transition: transform .2s, box-shadow .2s;
}
.phone-frame:hover {
  transform: translateY(-4px) scale(1.03);
  box-shadow: 0 12px 32px rgba(0,0,0,0.32);
}
.phone-frame img {
  width: 100%;
  display: block;
  object-fit: contain;
  border-radius: 15px;
}

/* Grille universelle pour les series de captures */
.phone-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 12px;
  margin: 16px 0;
}
.phone-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin: 16px 0;
}
.phone-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin: 16px 0;
}
@media (max-width: 600px) {
  .phone-grid { grid-template-columns: repeat(2, 1fr); }
  .phone-grid-3 { grid-template-columns: repeat(2, 1fr); }
  .phone-grid-2 { grid-template-columns: 1fr; }
}

/* Lightbox */
#lbox {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.92);
  z-index: 9999;
  align-items: center;
  justify-content: center;
  cursor: zoom-out;
}
#lbox.open { display: flex; }
#lbox img {
  max-width: 92vw;
  max-height: 92vh;
  object-fit: contain;
  border-radius: 16px;
  box-shadow: 0 12px 60px rgba(0,0,0,0.6);
}
#lbox-close {
  position: absolute;
  top: 18px; right: 22px;
  color: white;
  font-size: 2rem;
  font-weight: 700;
  cursor: pointer;
  line-height: 1;
  opacity: .85;
}
#lbox-close:hover { opacity: 1; }"""

assert OLD_PHONE_CSS in html, "phone-frame CSS not found"
html = html.replace(OLD_PHONE_CSS, NEW_PHONE_CSS)
print("phone-frame CSS updated OK")

# ============================================================
# 2. REMPLACER le CSS .img-gallery pour uniformiser la hauteur
# ============================================================
OLD_GALLERY_CSS = """.img-gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px,1fr)); gap: 12px; margin: 16px 0; }
.img-gallery-item { border-radius: 10px; overflow: hidden; border: 1px solid #e2e8f0; }
.img-gallery-item img { width: 100%; height: 160px; object-fit: cover; display: block; }
.img-gallery-item-caption { font-size: 11px; color: #64748b; padding: 6px 10px; background: #f8fafc; text-align: center; }"""

NEW_GALLERY_CSS = """.img-gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px,1fr)); gap: 14px; margin: 16px 0; }
.img-gallery-item { border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; box-shadow: 0 2px 10px rgba(0,0,0,.07); cursor: zoom-in; transition: transform .2s, box-shadow .2s; }
.img-gallery-item:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,.15); }
.img-gallery-item img { width: 100%; height: 180px; object-fit: cover; display: block; }
.img-gallery-item-caption { font-size: 11px; color: #64748b; padding: 7px 10px; background: #f8fafc; text-align: center; font-weight: 500; }"""

html = html.replace(OLD_GALLERY_CSS, NEW_GALLERY_CSS)
print("img-gallery CSS updated OK")

# ============================================================
# 3. REMPLACER les conteneurs inline des phone-frames
# ============================================================
# Pattern A : grilles 3 colonnes avec max-width:340px (sections creation)
html = html.replace(
    'style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;flex-shrink:0;max-width:340px"',
    'class="phone-grid-3"'
)
print("Grid 3col max-width replaced OK")

# Pattern B : flex gap:8px flex-shrink:0 (encaissement, lien, etc.)
html = html.replace(
    'style="display:flex;gap:8px;flex-shrink:0"',
    'class="phone-grid"'
)
print("Flex gap:8px replaced OK")

# ============================================================
# 4. RETIRER les sections flex parent qui contraignent les images
#    (les blocs avec flex:1 + images cote a cote dans l'overlay)
#    On passe de layout flex horizontal a layout vertical avec
#    texte puis images en pleine largeur
# ============================================================

# Section creation OM (client existant) - changer display:flex en display:block
# La structure actuelle :
# <div style="display:flex;gap:12px;align-items:flex-start">
#   <div style="flex:1">  ...texte...  </div>
#   <div class="phone-grid-3">  ...images...  </div>
# </div>

# Remplacer les blocs flex qui contiennent a la fois du texte et des phone-frames
# Identifier le bloc par le texte unique "Client OM existant" et "Client Non-OM"

# Remettre la grille d'images en display block pour qu'elle prenne toute la largeur
# sous le texte - faire un remplacement des wrappers flex specifiques

# Section creation OM client existant
html = html.replace(
    '<div style="display:flex;gap:12px;align-items:flex-start">\n            <div style="flex:1">',
    '<div>\n            <div>'
)
html = html.replace(
    '<div style="display:flex;gap:12px;align-items:flex-start">\n            <div style="flex:1">',
    '<div>\n            <div>'
)

# Section creation Non-OM
html = html.replace(
    '<div style="display:flex;gap:12px;align-items:flex-start">\n              <div style="flex:1">',
    '<div>\n              <div>'
)

# Sections encaissement / lien / transfert : les wrappers flex avec min-width
html = html.replace(
    'style="display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap"',
    'style="display:flex;flex-direction:column;gap:16px"'
)
print("Flex wrappers updated OK")

# ============================================================
# 5. AJOUTER le lightbox HTML + JS avant </body>
# ============================================================
LIGHTBOX_HTML = """
<!-- Lightbox images -->
<div id="lbox" onclick="closeLbox()">
  <span id="lbox-close" onclick="closeLbox()">&#10005;</span>
  <img id="lbox-img" src="" alt="">
</div>
"""

LIGHTBOX_JS = """
// Lightbox
function openLbox(src) {
  var lb = document.getElementById('lbox');
  document.getElementById('lbox-img').src = src;
  lb.classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeLbox() {
  document.getElementById('lbox').classList.remove('open');
  document.getElementById('lbox-img').src = '';
  document.body.style.overflow = '';
}
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') closeLbox();
});
// Auto-bind toutes les phone-frame img et img-gallery-item img
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.phone-frame img, .img-gallery-item img').forEach(function(img) {
    img.style.cursor = 'zoom-in';
    img.addEventListener('click', function(e) {
      e.stopPropagation();
      openLbox(this.src);
    });
  });
});
"""

# Insérer lightbox HTML avant </body>
html = html.replace('</body>', LIGHTBOX_HTML + '</body>')

# Insérer lightbox JS avant </script> final
html = html.replace('</script>\n\n</body>', LIGHTBOX_JS + '\n</script>\n\n</body>')
print("Lightbox added OK")

# ============================================================
# WRITE
# ============================================================
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nindex.html: {len(html):,} chars ({len(html)//1024} KB)")
print("Done!")
