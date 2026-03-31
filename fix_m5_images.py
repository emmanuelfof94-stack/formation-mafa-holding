"""
Integrer les captures d'ecran extraites des PPTX dans le Module 5 (Application Agent) de index.html
- Connexion : login screenshot
- Carte entreprises + Apercu activite
- KYC form screenshot
- KYB/Save form screenshot
- Etapes 0-2 (O'calm QR) en grille
- Synchronisation screenshots
- Tableau de bord screenshot
- Nouvelle section : Guide visuel pas-a-pas (13 captures Guide_Application_Agent)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

IN  = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"
OUT = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"

with open(IN, "r", encoding="utf-8") as f:
    html = f.read()

# Helper : inserer NEW_HTML apres MARKER
def insert_after(html, marker, new_html):
    idx = html.find(marker)
    if idx == -1:
        raise ValueError(f"Marker not found: {marker[:60]}...")
    pos = idx + len(marker)
    return html[:pos] + new_html + html[pos:]

# ============================================================
# 1. Screenshot CONNEXION apres le premier info-card de S1
# ============================================================
MARKER_LOGIN = """          <li>En cas d'oubli : contacter le Responsable Ville ou le superviseur</li>
        </ul>
      </div>
      <div class="info-card">
        <h3>🗺️ Carte des entreprises — Vue principale</h3>"""

LOGIN_IMG = """          <li>En cas d'oubli : contacter le Responsable Ville ou le superviseur</li>
        </ul>
      </div>

      <div style="text-align:center;margin:16px 0">
        <div class="phone-frame" style="width:260px;margin:0 auto">
          <img src="img_agent/formation_image5.jpg" alt="Page de connexion" style="width:100%;display:block">
        </div>
        <p style="font-size:11px;color:#888;margin-top:8px">Page de connexion — Application Agent</p>
      </div>

      <div class="info-card">
        <h3>🗺️ Carte des entreprises — Vue principale</h3>"""

html = html.replace(MARKER_LOGIN, LOGIN_IMG, 1)
print("Login screenshot OK")

# ============================================================
# 2. Screenshots CARTE + APERCU ACTIVITE apres la def-grid de S1
#    (apres le dernier def-card de S1 avant <!-- S2 -->)
# ============================================================
MARKER_CARTE = """        <div class="def-card">
          <div class="def-term">Statut "Déjà visité"</div>
          <div class="def-def">Indique si l'entrepreneur a déjà été vu lors d'une session précédente. Évite les doubles visites.</div>
        </div>
      </div>

      <!-- S2 -->"""

CARTE_IMG = """        <div class="def-card">
          <div class="def-term">Statut "Déjà visité"</div>
          <div class="def-def">Indique si l'entrepreneur a déjà été vu lors d'une session précédente. Évite les doubles visites.</div>
        </div>
      </div>

      <div class="phone-grid-2" style="max-width:540px;margin:16px auto">
        <div class="phone-frame">
          <img src="img_agent/formation_image6.jpg" alt="Carte des entreprises" style="width:100%;display:block">
        </div>
        <div class="phone-frame">
          <img src="img_agent/formation_image9.jpg" alt="Apercu activite" style="width:100%;display:block">
        </div>
      </div>
      <p style="font-size:11px;color:#888;text-align:center;margin-bottom:16px">Gauche : Vue carte des entreprises · Droite : Aperçu des détails d'une activité</p>

      <!-- S2 -->"""

html = html.replace(MARKER_CARTE, CARTE_IMG, 1)
print("Carte + Apercu screenshots OK")

# ============================================================
# 3. Screenshot KYC FORM apres la liste KYC
# ============================================================
MARKER_KYC = """          <li><strong>Numéro de téléphone</strong> — principal et alternatif si disponible</li>
        </ul>
      </div>
      <div class="info-card">
        <h3>🏪 Formulaire KYB — Informations sur l'activité</h3>"""

KYC_IMG = """          <li><strong>Numéro de téléphone</strong> — principal et alternatif si disponible</li>
        </ul>
      </div>

      <div style="text-align:center;margin:12px 0">
        <div class="phone-frame" style="width:260px;margin:0 auto">
          <img src="img_agent/formation_image7.jpg" alt="Formulaire KYC" style="width:100%;display:block">
        </div>
        <p style="font-size:11px;color:#888;margin-top:6px">Formulaire KYC — Informations entrepreneur</p>
      </div>

      <div class="info-card">
        <h3>🏪 Formulaire KYB — Informations sur l'activité</h3>"""

html = html.replace(MARKER_KYC, KYC_IMG, 1)
print("KYC screenshot OK")

# ============================================================
# 4. Screenshot KYB / SAVE apres la liste KYB (avant alert)
# ============================================================
MARKER_KYB = """          <li><strong>Historique d'enrôlement</strong> — premier enrôlement ou mise à jour</li>
        </ul>
      </div>
      <div class="alert alert-warn">"""

KYB_IMG = """          <li><strong>Historique d'enrôlement</strong> — premier enrôlement ou mise à jour</li>
        </ul>
      </div>

      <div style="text-align:center;margin:12px 0">
        <div class="phone-frame" style="width:260px;margin:0 auto">
          <img src="img_agent/formation_image8.jpg" alt="Formulaire KYB et enregistrement" style="width:100%;display:block">
        </div>
        <p style="font-size:11px;color:#888;margin-top:6px">Formulaire KYB — Enregistrement local et synchronisation</p>
      </div>

      <div class="alert alert-warn">"""

html = html.replace(MARKER_KYB, KYB_IMG, 1)
print("KYB screenshot OK")

# ============================================================
# 5. Screenshots ETAPES O'CALM (0, 1, 2) apres la section enrol-flow
#    et avant la table recapitulative
# ============================================================
MARKER_ETAPES = """      </div>

      <table class="styled-table">
        <thead><tr><th>Étape</th><th>Action de l'agent</th><th>Rôle du marchand</th><th>Résultat attendu</th></tr></thead>"""

ETAPES_IMG = """      </div>

      <div class="phone-grid-3" style="margin:16px 0">
        <div class="phone-frame">
          <img src="img_agent/formation_image10.jpg" alt="Etape 0 - Selectionner service" style="width:100%;display:block">
        </div>
        <div class="phone-frame">
          <img src="img_agent/formation_image11.jpg" alt="Etape 1 - Scanner QR" style="width:100%;display:block">
        </div>
        <div class="phone-frame">
          <img src="img_agent/formation_image13.jpg" alt="Etape 2 - Verification" style="width:100%;display:block">
        </div>
      </div>
      <p style="font-size:11px;color:#888;text-align:center;margin-bottom:16px">Étape 0 : Sélectionner le service · Étape 1 : Scanner le QR Code · Étape 2 : Vérifier les informations</p>

      <table class="styled-table">
        <thead><tr><th>Étape</th><th>Action de l'agent</th><th>Rôle du marchand</th><th>Résultat attendu</th></tr></thead>"""

html = html.replace(MARKER_ETAPES, ETAPES_IMG, 1)
print("Etapes O'calm screenshots OK")

# ============================================================
# 6. Screenshots SYNCHRONISATION apres la connect-grid
# ============================================================
MARKER_SYNC = """      </div>
      <div class="alert alert-info">
        <div class="alert-icon">💡</div>
        <div class="alert-text"><strong>Conseil terrain :</strong> L'application est conçue pour fonctionner dans des zones à faible couverture réseau."""

SYNC_IMG = """      </div>

      <div class="phone-grid-2" style="max-width:540px;margin:16px auto">
        <div class="phone-frame">
          <img src="img_agent/formation_image14.jpg" alt="Ecran synchronisation 1" style="width:100%;display:block">
        </div>
        <div class="phone-frame">
          <img src="img_agent/formation_image15.jpg" alt="Ecran synchronisation 2" style="width:100%;display:block">
        </div>
      </div>
      <p style="font-size:11px;color:#888;text-align:center;margin-bottom:16px">Écrans de synchronisation — mode offline et sync</p>

      <div class="alert alert-info">
        <div class="alert-icon">💡</div>
        <div class="alert-text"><strong>Conseil terrain :</strong> L'application est conçue pour fonctionner dans des zones à faible couverture réseau."""

html = html.replace(MARKER_SYNC, SYNC_IMG, 1)
print("Synchronisation screenshots OK")

# ============================================================
# 7. Screenshot TABLEAU DE BORD apres la dashboard-grid
# ============================================================
MARKER_DASHBOARD = """        <div class="db-card"><div class="db-icon">🔄</div><div class="db-label">Dernière synchro</div><div class="db-note">Date et heure</div></div>
      </div>

      <!-- S6 -->"""

DASHBOARD_IMG = """        <div class="db-card"><div class="db-icon">🔄</div><div class="db-label">Dernière synchro</div><div class="db-note">Date et heure</div></div>
      </div>

      <div style="text-align:center;margin:16px 0">
        <div class="phone-frame" style="width:280px;margin:0 auto">
          <img src="img_agent/formation_image16.jpg" alt="Tableau de bord agent" style="width:100%;display:block">
        </div>
        <p style="font-size:11px;color:#888;margin-top:8px">Tableau de bord — indicateurs globaux et journaliers</p>
      </div>

      <!-- S6 -->"""

html = html.replace(MARKER_DASHBOARD, DASHBOARD_IMG, 1)
print("Dashboard screenshot OK")

# ============================================================
# 8. NOUVELLE SECTION 7 — Guide visuel pas-a-pas
#    (13 captures Guide_Application_Agent) avant la fermeture du cours
# ============================================================
GUIDE_SECTION = """
      <!-- S7 — Guide visuel -->
      <div id="s7" class="section-heading" style="margin-top:40px">
        <div class="section-num">7</div>
        <h2>Guide Visuel — Pas-à-Pas Application Agent</h2>
      </div>
      <div class="alert alert-info">
        <div class="alert-icon">📱</div>
        <div class="alert-text"><strong>Guide illustré complet :</strong> Les captures ci-dessous reprennent l'ensemble du parcours agent dans l'application, de la connexion au déploiement du QR Code.</div>
      </div>

      <div class="phone-grid">
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
      </div>
      <p style="font-size:11px;color:#888;text-align:center;margin:8px 0 20px">Cliquer sur une capture pour l'agrandir en plein ecran</p>

"""

MARKER_END_COURS = "      </div>\n\n      <div class=\"tab-section\" id=\"tab-m5-exo\""

html = html.replace(
    MARKER_END_COURS,
    GUIDE_SECTION + "      </div>\n\n      <div class=\"tab-section\" id=\"tab-m5-exo\"",
    1
)
print("Guide visuel section OK")

# ============================================================
# ECRIRE
# ============================================================
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nindex.html: {len(html):,} chars ({len(html)//1024} KB)")
print("Done!")
