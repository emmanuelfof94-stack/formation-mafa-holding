"""
Corriger l'affichage des captures dans M5 :
- Formation images (portrait ~0.625) : phone-frame avec object-fit contain (pas de recadrage)
- Guide images (paysage 1376x768 16:9) : nouvelle classe app-screenshot-landscape, largeur totale
- Ajouter CSS .app-screenshot-portrait et .app-screenshot-landscape
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

IN  = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"
OUT = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"

with open(IN, "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================
# 1. AJOUTER le CSS des nouvelles classes apres le CSS phone-frame
# ============================================================
CSS_MARKER = "#lbox-close:hover { opacity: 1; }"

NEW_CSS = """#lbox-close:hover { opacity: 1; }

/* ── CAPTURES APPLICATION AGENT ── */
/* Portrait (screenshots telephone) - sans recadrage */
.app-screenshot-portrait {
  border-radius: 16px;
  border: 2px solid #ddd;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
  background: #f0f0f0;
  cursor: zoom-in;
  transition: transform .2s, box-shadow .2s;
}
.app-screenshot-portrait:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 10px 30px rgba(0,0,0,0.22);
}
.app-screenshot-portrait img {
  width: 100%;
  display: block;
  object-fit: contain;
  border-radius: 14px;
}

/* Paysage (captures ecran desktop/tablette 16:9) */
.app-screenshot-landscape {
  border-radius: 12px;
  border: 2px solid #ddd;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
  background: #1a1a2e;
  cursor: zoom-in;
  transition: transform .2s, box-shadow .2s;
  width: 100%;
}
.app-screenshot-landscape:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}
.app-screenshot-landscape img {
  width: 100%;
  display: block;
  object-fit: contain;
}

/* Grille de captures paysage - 2 colonnes */
.landscape-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
  gap: 16px;
  margin: 16px 0;
}
/* Grille de captures portrait - 3 colonnes */
.portrait-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 14px;
  margin: 16px 0;
}
@media (max-width: 700px) {
  .landscape-grid { grid-template-columns: 1fr; }
  .portrait-grid { grid-template-columns: repeat(2, 1fr); }
}"""

assert CSS_MARKER in html, "CSS marker not found"
html = html.replace(CSS_MARKER, NEW_CSS, 1)
print("CSS nouvelles classes OK")

# ============================================================
# 2. REMPLACER les phone-frames des images Formation dans M5
#    par app-screenshot-portrait (preserve l'image entiere)
# ============================================================

# Login (centred single)
html = html.replace(
    '<div class="phone-frame" style="width:260px;margin:0 auto">\n          <img src="img_agent/formation_image5.jpg" alt="Page de connexion" style="width:100%;display:block">',
    '<div class="app-screenshot-portrait" style="width:260px;margin:0 auto">\n          <img src="img_agent/formation_image5.jpg" alt="Page de connexion" style="width:100%;display:block">'
)

# Carte + Apercu (grid-2)
html = html.replace(
    '<div class="phone-grid-2" style="max-width:540px;margin:16px auto">\n        <div class="phone-frame">\n          <img src="img_agent/formation_image6.jpg"',
    '<div class="portrait-grid" style="max-width:560px;margin:16px auto">\n        <div class="app-screenshot-portrait">\n          <img src="img_agent/formation_image6.jpg"'
)
html = html.replace(
    '</div>\n        <div class="phone-frame">\n          <img src="img_agent/formation_image9.jpg" alt="Apercu activite"',
    '</div>\n        <div class="app-screenshot-portrait">\n          <img src="img_agent/formation_image9.jpg" alt="Apercu activite"'
)

# KYC form (centred single)
html = html.replace(
    '<div class="phone-frame" style="width:260px;margin:0 auto">\n          <img src="img_agent/formation_image7.jpg" alt="Formulaire KYC"',
    '<div class="app-screenshot-portrait" style="width:260px;margin:0 auto">\n          <img src="img_agent/formation_image7.jpg" alt="Formulaire KYC"'
)

# KYB form (centred single)
html = html.replace(
    '<div class="phone-frame" style="width:260px;margin:0 auto">\n          <img src="img_agent/formation_image8.jpg" alt="Formulaire KYB et enregistrement"',
    '<div class="app-screenshot-portrait" style="width:260px;margin:0 auto">\n          <img src="img_agent/formation_image8.jpg" alt="Formulaire KYB et enregistrement"'
)

# Etapes 0/1/2 (grid-3)
html = html.replace(
    '<div class="phone-grid-3" style="margin:16px 0">\n        <div class="phone-frame">\n          <img src="img_agent/formation_image10.jpg"',
    '<div class="portrait-grid" style="margin:16px 0">\n        <div class="app-screenshot-portrait">\n          <img src="img_agent/formation_image10.jpg"'
)
html = html.replace(
    '        <div class="phone-frame">\n          <img src="img_agent/formation_image11.jpg"',
    '        <div class="app-screenshot-portrait">\n          <img src="img_agent/formation_image11.jpg"'
)
html = html.replace(
    '        <div class="phone-frame">\n          <img src="img_agent/formation_image13.jpg"',
    '        <div class="app-screenshot-portrait">\n          <img src="img_agent/formation_image13.jpg"'
)

# Synchronisation (grid-2)
html = html.replace(
    '<div class="phone-grid-2" style="max-width:540px;margin:16px auto">\n        <div class="phone-frame">\n          <img src="img_agent/formation_image14.jpg"',
    '<div class="portrait-grid" style="max-width:560px;margin:16px auto">\n        <div class="app-screenshot-portrait">\n          <img src="img_agent/formation_image14.jpg"'
)
html = html.replace(
    '        <div class="phone-frame">\n          <img src="img_agent/formation_image15.jpg"',
    '        <div class="app-screenshot-portrait">\n          <img src="img_agent/formation_image15.jpg"'
)

# Dashboard (centred single)
html = html.replace(
    '<div class="phone-frame" style="width:280px;margin:0 auto">\n          <img src="img_agent/formation_image16.jpg" alt="Tableau de bord agent"',
    '<div class="app-screenshot-portrait" style="width:300px;margin:0 auto">\n          <img src="img_agent/formation_image16.jpg" alt="Tableau de bord agent"'
)

print("Formation images -> app-screenshot-portrait OK")

# ============================================================
# 3. REMPLACER les phone-frames Guide (paysage 16:9)
#    par app-screenshot-landscape dans une landscape-grid
# ============================================================

# Remplacer le bloc entier de la phone-grid guide par une landscape-grid
OLD_GUIDE = """      <div class="phone-grid">
        <div class="phone-frame"><img src="img_agent/guide_image1.png" alt="Guide 01" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image2.png" alt="Guide 02" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image3.png" alt="Guide 03" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image4.png" alt="Guide 04" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image5.png" alt="Guide 05" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image6.png" alt="Guide 06" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image7.png" alt="Guide 07" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image8.png" alt="Guide 08" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image9.png" alt="Guide 09" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image10.png" alt="Guide 10" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image11.png" alt="Guide 11" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image12.png" alt="Guide 12" style="width:100%;display:block"></div>
        <div class="phone-frame"><img src="img_agent/guide_image13.png" alt="Guide 13" style="width:100%;display:block"></div>
      </div>"""

NEW_GUIDE = """      <div class="landscape-grid">
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image1.png" alt="Guide 01 - Accueil" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image2.png" alt="Guide 02" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image3.png" alt="Guide 03" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image4.png" alt="Guide 04" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image5.png" alt="Guide 05" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image6.png" alt="Guide 06" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image7.png" alt="Guide 07" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image8.png" alt="Guide 08" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image9.png" alt="Guide 09" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image10.png" alt="Guide 10" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image11.png" alt="Guide 11" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image12.png" alt="Guide 12" style="width:100%;display:block"></div>
        <div class="app-screenshot-landscape"><img src="img_agent/guide_image13.png" alt="Guide 13" style="width:100%;display:block"></div>
      </div>"""

assert OLD_GUIDE in html, "Guide grid not found"
html = html.replace(OLD_GUIDE, NEW_GUIDE, 1)
print("Guide images -> landscape-grid OK")

# ============================================================
# 4. ETENDRE le lightbox pour inclure app-screenshot img
# ============================================================
OLD_LB_JS = "document.querySelectorAll('.phone-frame img, .img-gallery-item img').forEach(function(img) {"
NEW_LB_JS = "document.querySelectorAll('.phone-frame img, .app-screenshot-portrait img, .app-screenshot-landscape img, .img-gallery-item img').forEach(function(img) {"

html = html.replace(OLD_LB_JS, NEW_LB_JS, 1)
print("Lightbox etendu aux nouvelles classes OK")

# ============================================================
# ECRIRE
# ============================================================
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nindex.html: {len(html):,} chars ({len(html)//1024} KB)")
print("Done!")
