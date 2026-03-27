"""
Fix images v2 - Ameliorer la visibilite des images dans index.html :
- Ajouter aspect-ratio 9/16 sur .phone-frame pour que les images aient toujours une hauteur visible
- Augmenter la taille minimale des grilles (140px -> 200px)
- Supprimer les width inline trop petits (80px, 100px, 130px) sur les phone-frames
- Corriger les flex containers texte+images en layout vertical
- Agrandir le phone-frame solo (130px -> 280px centre)
- Corriger les grids restants avec max-width:280px
- Corriger les display:flex;gap:8px restants avec des phone-frames
"""

IN  = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"
OUT = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"

with open(IN, "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================
# 1. AMELIORER le CSS .phone-frame avec aspect-ratio + min-width
# ============================================================
OLD_PF = """.phone-frame {
  border-radius: 18px;
  border: 2.5px solid #333;
  overflow: hidden;
  box-shadow: 0 6px 24px rgba(0,0,0,0.22);
  background: #000;
  cursor: zoom-in;
  transition: transform .2s, box-shadow .2s;
}"""

NEW_PF = """.phone-frame {
  border-radius: 18px;
  border: 2.5px solid #333;
  overflow: hidden;
  box-shadow: 0 6px 24px rgba(0,0,0,0.22);
  background: #111;
  cursor: zoom-in;
  transition: transform .2s, box-shadow .2s;
  aspect-ratio: 9/16;
  min-width: 140px;
  display: flex;
  align-items: stretch;
}"""

assert OLD_PF in html, "phone-frame CSS not found"
html = html.replace(OLD_PF, NEW_PF)
print("phone-frame aspect-ratio OK")

# ============================================================
# 2. AMELIORER .phone-frame img pour occuper toute la hauteur
# ============================================================
OLD_IMG = """.phone-frame img {
  width: 100%;
  display: block;
  object-fit: contain;
  border-radius: 15px;
}"""

NEW_IMG = """.phone-frame img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  border-radius: 15px;
  flex: 1;
}"""

assert OLD_IMG in html, "phone-frame img CSS not found"
html = html.replace(OLD_IMG, NEW_IMG)
print("phone-frame img CSS OK")

# ============================================================
# 3. AGRANDIR le minmax de .phone-grid (140px -> 200px)
# ============================================================
html = html.replace(
    "grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));",
    "grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));"
)
print("phone-grid minmax OK")

# ============================================================
# 4. AGRANDIR le phone-frame solo (width:130px -> 280px centre)
# ============================================================
html = html.replace(
    '<div class="phone-frame" style="width:130px;margin:0 auto">',
    '<div class="phone-frame" style="width:280px;margin:0 auto">'
)
print("Solo phone-frame size OK")

# ============================================================
# 5. SUPPRIMER les width inline petits sur les phone-frames
#    et remplacer les conteneurs flex par des grilles
# ============================================================

# Classique docs (4 images, width:100px) dans flex -> phone-grid-2
html = html.replace(
    '<div style="display:flex;gap:6px;flex-wrap:wrap">\n            <div class="phone-frame" style="width:100px"><img src="img_m4/s20_classique_doc1.jpg" alt="Doc classique 1" style="width:100%;display:block"></div>\n            <div class="phone-frame" style="width:100px"><img src="img_m4/s20_classique_doc2.jpg" alt="Doc classique 2" style="width:100%;display:block"></div>\n            <div class="phone-frame" style="width:100px"><img src="img_m4/s20_classique_doc3.jpg" alt="Doc classique 3" style="width:100%;display:block"></div>\n            <div class="phone-frame" style="width:100px"><img src="img_m4/s20_classique_doc4.jpg" alt="Doc classique 4" style="width:100%;display:block"></div>\n          </div>',
    '<div class="phone-grid-2">\n            <div class="phone-frame"><img src="img_m4/s20_classique_doc1.jpg" alt="Doc classique 1" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s20_classique_doc2.jpg" alt="Doc classique 2" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s20_classique_doc3.jpg" alt="Doc classique 3" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s20_classique_doc4.jpg" alt="Doc classique 4" style="width:100%;display:block"></div>\n          </div>'
)
print("Classique docs grid OK")

# Premium docs (6 images, width:80px) dans flex -> phone-grid-3
html = html.replace(
    '<div style="display:flex;gap:6px;flex-wrap:wrap">\n            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc1.jpg" alt="Doc premium 1" style="width:100%;display:block"></div>\n            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc2.jpg" alt="Doc premium 2" style="width:100%;display:block"></div>\n            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc3.jpg" alt="Doc premium 3" style="width:100%;display:block"></div>\n            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc4.jpg" alt="Doc premium 4" style="width:100%;display:block"></div>\n            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc5.jpg" alt="Doc premium 5" style="width:100%;display:block"></div>\n            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc6.jpg" alt="Doc premium 6" style="width:100%;display:block"></div>\n          </div>',
    '<div class="phone-grid-3">\n            <div class="phone-frame"><img src="img_m4/s17_premium_doc1.jpg" alt="Doc premium 1" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s17_premium_doc2.jpg" alt="Doc premium 2" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s17_premium_doc3.jpg" alt="Doc premium 3" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s17_premium_doc4.jpg" alt="Doc premium 4" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s17_premium_doc5.jpg" alt="Doc premium 5" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s17_premium_doc6.jpg" alt="Doc premium 6" style="width:100%;display:block"></div>\n          </div>'
)
print("Premium docs grid OK")

# ============================================================
# 6. CORRIGER le grid retrait restant avec max-width:280px
# ============================================================
html = html.replace(
    '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;flex-shrink:0;max-width:280px">',
    '<div class="phone-grid-3">'
)
print("Retrait grid 280px -> phone-grid-3 OK")

# ============================================================
# 7. CORRIGER les display:flex;gap:8px restants avec des phone-frames
#    (historique: 2 images, remboursement: 3 images)
# ============================================================
html = html.replace(
    '<div style="display:flex;gap:8px">\n            <div class="phone-frame"><img src="img_m4/s14_historique1.jpg"',
    '<div class="phone-grid-2">\n            <div class="phone-frame"><img src="img_m4/s14_historique1.jpg"'
)
html = html.replace(
    '<div style="display:flex;gap:8px">\n            <div class="phone-frame"><img src="img_m4/s15_remboursement1.jpg"',
    '<div class="phone-grid-3">\n            <div class="phone-frame"><img src="img_m4/s15_remboursement1.jpg"'
)
print("Historique/remboursement flex -> grid OK")

# ============================================================
# 8. CORRIGER les sections transfert (texte + 3 phone-frames en flex)
#    -> texte au-dessus, images en grille en-dessous
# ============================================================

# Transfert a soi-meme
OLD_TRANSFERT_SOI = '<div style="display:flex;gap:12px;align-items:flex-start">\n            <ol style="padding-left:16px;font-size:13px;color:#2d3748;line-height:2.1;flex:1">\n              <li>Cliquer \u00ab\u00a0Transfert\u00a0\u00bb</li>\n              <li>Choisir \u00ab\u00a0\u00e0 moi-m\u00eame\u00a0\u00bb</li>\n              <li>Saisir le montant</li>\n              <li>Confirmer avec son code secret</li>\n            </ol>\n            <div class="phone-frame"><img src="img_m4/s12_transfert_soi1.jpg" alt="Transfert soi 1" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s12_transfert_soi2.jpg" alt="Transfert soi 2" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s12_transfert_soi3.jpg" alt="Transfert soi 3" style="width:100%;display:block"></div>\n          </div>'

NEW_TRANSFERT_SOI = '<div>\n            <ol style="padding-left:16px;font-size:13px;color:#2d3748;line-height:2.1">\n              <li>Cliquer \u00ab\u00a0Transfert\u00a0\u00bb</li>\n              <li>Choisir \u00ab\u00a0\u00e0 moi-m\u00eame\u00a0\u00bb</li>\n              <li>Saisir le montant</li>\n              <li>Confirmer avec son code secret</li>\n            </ol>\n            <div class="phone-grid-3" style="margin-top:12px">\n              <div class="phone-frame"><img src="img_m4/s12_transfert_soi1.jpg" alt="Transfert soi 1" style="width:100%;display:block"></div>\n              <div class="phone-frame"><img src="img_m4/s12_transfert_soi2.jpg" alt="Transfert soi 2" style="width:100%;display:block"></div>\n              <div class="phone-frame"><img src="img_m4/s12_transfert_soi3.jpg" alt="Transfert soi 3" style="width:100%;display:block"></div>\n            </div>\n          </div>'

if OLD_TRANSFERT_SOI in html:
    html = html.replace(OLD_TRANSFERT_SOI, NEW_TRANSFERT_SOI)
    print("Transfert soi restructure OK")
else:
    print("WARN: Transfert soi pattern not found - checking...")
    # Try to find a simpler version
    if 's12_transfert_soi1.jpg' in html:
        print("  -> Images present but pattern different")

# Transfert a un tiers
OLD_TRANSFERT_TIERS = '<div style="display:flex;gap:12px;align-items:flex-start">\n            <ol style="padding-left:16px;font-size:13px;color:#2d3748;line-height:2.1;flex:1">\n              <li>Cliquer \u00ab\u00a0Transfert\u00a0\u00bb</li>\n              <li>Choisir \u00ab\u00a0Autre transfert\u00a0\u00bb</li>\n              <li>S\u00e9lectionner le contact + montant</li>\n              <li>Confirmer avec son code secret</li>\n            </ol>\n            <div class="phone-frame"><img src="img_m4/s12_transfert_tiers1.jpg" alt="Transfert tiers 1" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s12_transfert_tiers2.jpg" alt="Transfert tiers 2" style="width:100%;display:block"></div>\n            <div class="phone-frame"><img src="img_m4/s12_transfert_tiers3.jpg" alt="Transfert tiers 3" style="width:100%;display:block"></div>\n          </div>'

NEW_TRANSFERT_TIERS = '<div>\n            <ol style="padding-left:16px;font-size:13px;color:#2d3748;line-height:2.1">\n              <li>Cliquer \u00ab\u00a0Transfert\u00a0\u00bb</li>\n              <li>Choisir \u00ab\u00a0Autre transfert\u00a0\u00bb</li>\n              <li>S\u00e9lectionner le contact + montant</li>\n              <li>Confirmer avec son code secret</li>\n            </ol>\n            <div class="phone-grid-3" style="margin-top:12px">\n              <div class="phone-frame"><img src="img_m4/s12_transfert_tiers1.jpg" alt="Transfert tiers 1" style="width:100%;display:block"></div>\n              <div class="phone-frame"><img src="img_m4/s12_transfert_tiers2.jpg" alt="Transfert tiers 2" style="width:100%;display:block"></div>\n              <div class="phone-frame"><img src="img_m4/s12_transfert_tiers3.jpg" alt="Transfert tiers 3" style="width:100%;display:block"></div>\n            </div>\n          </div>'

if OLD_TRANSFERT_TIERS in html:
    html = html.replace(OLD_TRANSFERT_TIERS, NEW_TRANSFERT_TIERS)
    print("Transfert tiers restructure OK")
else:
    print("WARN: Transfert tiers pattern not found")

# ============================================================
# 9. AMELIORER la section creation (Etapes) en grille pleine largeur
#    Les sections creation deja en phone-grid-3 restent telles quelles
# ============================================================

# Corriger les grilles creation OM/Non-OM qui sont dans des div flex
# Chercher les patterns restants
count_flex12 = html.count('style="display:flex;gap:12px;align-items:flex-start">')
print(f"Flex gap:12px restants: {count_flex12}")

# Changer tous les flex restants avec gap:12px qui contiennent des phone-frames
# (ceux lies aux sections creation qui avaient flex:1)
html = html.replace(
    'style="display:flex;gap:12px;align-items:flex-start">\n            <div style="flex:1">',
    'style="display:block">\n            <div>'
)
html = html.replace(
    'style="display:flex;gap:12px;align-items:flex-start">\n              <div style="flex:1">',
    'style="display:block">\n              <div>'
)

# Also remove flex:1 from remaining sub-divs that lost their parent flex context
html = html.replace(
    'style="display:flex;gap:12px;align-items:flex-start">',
    'style="display:block">'
)
print("Remaining flex gap:12px -> block OK")

# ============================================================
# 10. ECRIRE le fichier
# ============================================================
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nindex.html: {len(html):,} chars ({len(html)//1024} KB)")
print("Done!")
