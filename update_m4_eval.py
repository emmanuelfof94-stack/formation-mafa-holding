"""
Mise à jour M4 + intégration évaluation finale
"""

IDX = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"

with open(IDX, "r", encoding="utf-8") as f:
    html = f.read()

print(f"Lu {len(html):,} chars")

# -- 1. Renommer les images existantes
renames = {
    'img_m4/creation_om_etape1.jpg': 'img_m4/s09_creation_om1.jpg',
    'img_m4/creation_om_etape2.jpg': 'img_m4/s09_creation_om2.jpg',
    'img_m4/creation_nonom_etape1.jpg': 'img_m4/s09_creation_nonom1.jpg',
    'img_m4/creation_nonom_etape2.jpg': 'img_m4/s09_creation_nonom2.jpg',
    'img_m4/encaissement_qr1.jpg': 'img_m4/s10_encaissement1.jpg',
    'img_m4/encaissement_qr2.jpg': 'img_m4/s10_encaissement2.jpg',
    'img_m4/encaissement_qr3.jpg': 'img_m4/s10_encaissement3.jpg',
    'img_m4/lien_etape1.jpg': 'img_m4/s11_lien1.jpg',
    'img_m4/lien_etape2.jpg': 'img_m4/s11_lien2.jpg',
    'img_m4/lien_etape3.jpg': 'img_m4/s11_lien3.jpg',
    'img_m4/transfert_soi1.jpg': 'img_m4/s12_transfert_soi1.jpg',
    'img_m4/transfert_tiers1.jpg': 'img_m4/s12_transfert_tiers1.jpg',
    'img_m4/retrait_etape1.jpg': 'img_m4/s13_retrait1.jpg',
    'img_m4/retrait_etape2.jpg': 'img_m4/s13_retrait2.jpg',
    'img_m4/retrait_etape3.jpg': 'img_m4/s13_retrait3.jpg',
    'img_m4/historique_liste.jpg': 'img_m4/s14_historique1.jpg',
    'img_m4/historique_detail.jpg': 'img_m4/s14_historique2.jpg',
    'img_m4/remboursement1.jpg': 'img_m4/s15_remboursement1.jpg',
    'img_m4/remboursement2.jpg': 'img_m4/s15_remboursement2.jpg',
}
for old, new in renames.items():
    count = html.count(old)
    if count:
        html = html.replace(old, new)
        print(f"  {old.split('/')[-1]} -> {new.split('/')[-1]} ({count}x)")
    else:
        print(f"  NOT FOUND: {old}")

# -- 2. Ajouter images Création OM (6 images au lieu de 2)
old_om_block = (
    '<div style="display:flex;flex-direction:column;gap:8px;flex-shrink:0">\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_om1.jpg" alt="\u00c9tape 1" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_om2.jpg" alt="\u00c9tape 2" style="width:100%;display:block"></div>\n'
    '            </div>'
)
new_om_block = (
    '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;flex-shrink:0;max-width:340px">\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_om1.jpg" alt="\u00c9tape 1" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_om2.jpg" alt="\u00c9tape 2" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_om3.jpg" alt="\u00c9tape 3" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_om4.jpg" alt="\u00c9tape 4" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_om5.jpg" alt="\u00c9tape 5" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_om6.jpg" alt="\u00c9tape 6" style="width:100%;display:block"></div>\n'
    '            </div>'
)
if old_om_block in html:
    html = html.replace(old_om_block, new_om_block, 1)
    print("  ok Creation OM: 6 images")
else:
    print("  MISS: Creation OM block")

# -- 3. Ajouter images Création Non-OM (cours) 6 images
old_nonom = (
    '<div style="display:flex;flex-direction:column;gap:8px;flex-shrink:0">\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_nonom1.jpg" alt="Non-OM \u00e9tape 1" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_nonom2.jpg" alt="Non-OM \u00e9tape 2" style="width:100%;display:block"></div>\n'
    '            </div>'
)
new_nonom = (
    '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;flex-shrink:0;max-width:340px">\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_nonom1.jpg" alt="Non-OM 1" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_nonom2.jpg" alt="Non-OM 2" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_nonom3.jpg" alt="Non-OM 3" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_nonom4.jpg" alt="Non-OM 4" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_nonom5.jpg" alt="Non-OM 5" style="width:100%;display:block"></div>\n'
    '              <div class="phone-frame"><img src="img_m4/s09_creation_nonom6.jpg" alt="Non-OM 6" style="width:100%;display:block"></div>\n'
    '            </div>'
)
if old_nonom in html:
    html = html.replace(old_nonom, new_nonom, 1)
    print("  ok Creation Non-OM cours: 6 images")
else:
    print("  MISS: Creation Non-OM cours block")

# -- 4. Transfert soi: ajouter 2 images
OLD_SOI = (
    '            <div class="phone-frame"><img src="img_m4/s12_transfert_soi1.jpg" alt="Transfert soi" style="width:100%;display:block"></div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <div>\n'
    '          <div style="font-size:13px;font-weight:700;color:#584B26;margin-bottom:12px">Transfert \u00e0 un tiers</div>'
)
NEW_SOI = (
    '            <div class="phone-frame"><img src="img_m4/s12_transfert_soi1.jpg" alt="Transfert soi 1" style="width:100%;display:block"></div>\n'
    '            <div class="phone-frame"><img src="img_m4/s12_transfert_soi2.jpg" alt="Transfert soi 2" style="width:100%;display:block"></div>\n'
    '            <div class="phone-frame"><img src="img_m4/s12_transfert_soi3.jpg" alt="Transfert soi 3" style="width:100%;display:block"></div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <div>\n'
    '          <div style="font-size:13px;font-weight:700;color:#584B26;margin-bottom:12px">Transfert \u00e0 un tiers</div>'
)
if OLD_SOI in html:
    html = html.replace(OLD_SOI, NEW_SOI, 1)
    print("  ok Transfert soi: 3 images")
else:
    print("  MISS: Transfert soi")

# -- 5. Transfert tiers: ajouter 2 images
OLD_TIERS = (
    '            <div class="phone-frame"><img src="img_m4/s12_transfert_tiers1.jpg" alt="Transfert tiers" style="width:100%;display:block"></div>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>\n'
    '    </div>\n'
    '\n'
    '    <div class="card">\n'
    '      <div class="card-title">\U0001f3e7 Parcours \u2014 Retrait'
)
NEW_TIERS = (
    '            <div class="phone-frame"><img src="img_m4/s12_transfert_tiers1.jpg" alt="Transfert tiers 1" style="width:100%;display:block"></div>\n'
    '            <div class="phone-frame"><img src="img_m4/s12_transfert_tiers2.jpg" alt="Transfert tiers 2" style="width:100%;display:block"></div>\n'
    '            <div class="phone-frame"><img src="img_m4/s12_transfert_tiers3.jpg" alt="Transfert tiers 3" style="width:100%;display:block"></div>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>\n'
    '    </div>\n'
    '\n'
    '    <div class="card">\n'
    '      <div class="card-title">\U0001f3e7 Parcours \u2014 Retrait'
)
if OLD_TIERS in html:
    html = html.replace(OLD_TIERS, NEW_TIERS, 1)
    print("  ok Transfert tiers: 3 images")
else:
    print("  MISS: Transfert tiers")

# -- 6. Retrait: 6 images
OLD_RETRAIT = (
    '        <div style="display:flex;gap:8px;flex-shrink:0">\n'
    '          <div class="phone-frame"><img src="img_m4/s13_retrait1.jpg" alt="Retrait 1" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s13_retrait2.jpg" alt="Retrait 2" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s13_retrait3.jpg" alt="Retrait 3" style="width:100%;display:block"></div>\n'
    '        </div>'
)
NEW_RETRAIT = (
    '        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;flex-shrink:0;max-width:280px">\n'
    '          <div class="phone-frame"><img src="img_m4/s13_retrait1.jpg" alt="Retrait 1" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s13_retrait2.jpg" alt="Retrait 2" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s13_retrait3.jpg" alt="Retrait 3" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s13_retrait4.jpg" alt="Retrait 4" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s13_retrait5.jpg" alt="Retrait 5" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s13_retrait6.jpg" alt="Retrait 6" style="width:100%;display:block"></div>\n'
    '        </div>'
)
if OLD_RETRAIT in html:
    html = html.replace(OLD_RETRAIT, NEW_RETRAIT, 1)
    print("  ok Retrait: 6 images")
else:
    print("  MISS: Retrait")

# -- 7. Remboursement: 3 images
OLD_REMB = (
    '          <div style="display:flex;gap:8px">\n'
    '            <div class="phone-frame"><img src="img_m4/s15_remboursement1.jpg" alt="Remboursement 1" style="width:100%;display:block"></div>\n'
    '            <div class="phone-frame"><img src="img_m4/s15_remboursement2.jpg" alt="Remboursement 2" style="width:100%;display:block"></div>\n'
    '          </div>'
)
NEW_REMB = (
    '          <div style="display:flex;gap:8px">\n'
    '            <div class="phone-frame"><img src="img_m4/s15_remboursement1.jpg" alt="Remboursement 1" style="width:100%;display:block"></div>\n'
    '            <div class="phone-frame"><img src="img_m4/s15_remboursement2.jpg" alt="Remboursement 2" style="width:100%;display:block"></div>\n'
    '            <div class="phone-frame"><img src="img_m4/s15_remboursement3.jpg" alt="Remboursement 3" style="width:100%;display:block"></div>\n'
    '          </div>'
)
if OLD_REMB in html:
    html = html.replace(OLD_REMB, NEW_REMB, 1)
    print("  ok Remboursement: 3 images")
else:
    print("  MISS: Remboursement")

# -- 8. Nouvelles sections Assistance + Annexes
NOUVELLES_SECTIONS = """
    <!-- Assistance client -->
    <div class="card">
      <div class="card-title">&#127911; Assistance client</div>
      <div style="display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap">
        <div style="flex:1;min-width:200px">
          <p style="font-size:13px;color:#455A64;line-height:1.7;margin-bottom:12px">
            En cas de probl&#232;me (paiement bloqu&#233;, solde incorrect, QR non fonctionnel), le marchand peut contacter le support directement depuis l'application ou via les canaux d&#233;di&#233;s.
          </p>
          <div style="display:flex;flex-direction:column;gap:8px">
            <div style="display:flex;gap:10px;align-items:center;background:#F9E8EC;border-radius:8px;padding:10px 14px">
              <span style="font-size:18px">&#128222;</span>
              <div><div style="font-size:12px;font-weight:700;color:#8D0C23">Hotline d&#233;di&#233;e</div><div style="font-size:11px;color:#455A64">Acc&#232;s depuis le menu "Aide" de l'application</div></div>
            </div>
            <div style="display:flex;gap:10px;align-items:center;background:#F9E8EC;border-radius:8px;padding:10px 14px">
              <span style="font-size:18px">&#128172;</span>
              <div><div style="font-size:12px;font-weight:700;color:#8D0C23">Chat int&#233;gr&#233;</div><div style="font-size:11px;color:#455A64">Support en temps r&#233;el dans l'application</div></div>
            </div>
            <div style="display:flex;gap:10px;align-items:center;background:#F9E8EC;border-radius:8px;padding:10px 14px">
              <span style="font-size:18px">&#127978;</span>
              <div><div style="font-size:12px;font-weight:700;color:#8D0C23">Point de Vente</div><div style="font-size:11px;color:#455A64">Assistance physique en agence ou PDV Orange</div></div>
            </div>
          </div>
        </div>
        <div style="display:flex;gap:8px;flex-shrink:0">
          <div class="phone-frame"><img src="img_m4/s18_assistance1.jpg" alt="Assistance 1" style="width:100%;display:block"></div>
          <div class="phone-frame"><img src="img_m4/s18_assistance2.jpg" alt="Assistance 2" style="width:100%;display:block"></div>
          <div class="phone-frame"><img src="img_m4/s18_assistance3.jpg" alt="Assistance 3" style="width:100%;display:block"></div>
        </div>
      </div>
    </div>

    <!-- Annexe -- Documents requis -->
    <div class="card">
      <div class="card-title">&#128206; Annexes &#8212; Documents requis pour d&#233;plafonnement</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
        <div>
          <div style="font-size:13px;font-weight:700;color:#8D0C23;margin-bottom:12px">Annexe 1 &#8212; Profil Classique</div>
          <div style="background:#F9E8EC;border-radius:10px;padding:14px;margin-bottom:14px">
            <div style="font-size:12px;color:#6A091A;line-height:1.8">
              <div>&#128196; Pi&#232;ce d'identit&#233; valide</div>
              <div>&#128196; Justificatif de domicile</div>
              <div>&#128196; Registre du commerce (RCCM)</div>
              <div>&#128196; Attestation fiscale (DGI)</div>
            </div>
          </div>
          <div style="display:flex;gap:6px;flex-wrap:wrap">
            <div class="phone-frame" style="width:100px"><img src="img_m4/s20_classique_doc1.jpg" alt="Doc classique 1" style="width:100%;display:block"></div>
            <div class="phone-frame" style="width:100px"><img src="img_m4/s20_classique_doc2.jpg" alt="Doc classique 2" style="width:100%;display:block"></div>
            <div class="phone-frame" style="width:100px"><img src="img_m4/s20_classique_doc3.jpg" alt="Doc classique 3" style="width:100%;display:block"></div>
            <div class="phone-frame" style="width:100px"><img src="img_m4/s20_classique_doc4.jpg" alt="Doc classique 4" style="width:100%;display:block"></div>
          </div>
        </div>
        <div>
          <div style="font-size:13px;font-weight:700;color:#584B26;margin-bottom:12px">Annexe 2 &#8212; Profil Premium</div>
          <div style="background:#F3EDD8;border-radius:10px;padding:14px;margin-bottom:14px">
            <div style="font-size:12px;color:#584B26;line-height:1.8">
              <div>&#128196; Statuts de la soci&#233;t&#233;</div>
              <div>&#128196; Formulaire de souscription sign&#233;</div>
              <div>&#128196; Pi&#232;ce d'identit&#233; dirigeant</div>
              <div>&#128196; RCCM + D&#233;claration fiscale annuelle</div>
              <div>&#128196; Formulaire KYC Premium</div>
              <div>&#128196; Bilan financier (si disponible)</div>
            </div>
          </div>
          <div style="display:flex;gap:6px;flex-wrap:wrap">
            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc1.jpg" alt="Doc premium 1" style="width:100%;display:block"></div>
            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc2.jpg" alt="Doc premium 2" style="width:100%;display:block"></div>
            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc3.jpg" alt="Doc premium 3" style="width:100%;display:block"></div>
            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc4.jpg" alt="Doc premium 4" style="width:100%;display:block"></div>
            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc5.jpg" alt="Doc premium 5" style="width:100%;display:block"></div>
            <div class="phone-frame" style="width:80px"><img src="img_m4/s17_premium_doc6.jpg" alt="Doc premium 6" style="width:100%;display:block"></div>
          </div>
        </div>
      </div>
    </div>
"""

OLD_END_COURS = '  </div><!-- fin tab-m4-cours -->'
if OLD_END_COURS in html:
    html = html.replace(OLD_END_COURS, NOUVELLES_SECTIONS + OLD_END_COURS, 1)
    print("  ok Sections Assistance + Annexes")
else:
    print("  MISS: fin tab-m4-cours")

# -- 9. Exercice 2 Non-OM: 4 images
OLD_EXO = (
    '        <div style="display:flex;flex-direction:column;gap:8px;align-items:center;flex-shrink:0">\n'
    '          <div class="phone-frame"><img src="img_m4/s09_creation_nonom1.jpg" alt="Non-OM 1" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s09_creation_nonom2.jpg" alt="Non-OM 2" style="width:100%;display:block"></div>\n'
    '        </div>'
)
NEW_EXO = (
    '        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;align-items:start;flex-shrink:0">\n'
    '          <div class="phone-frame"><img src="img_m4/s09_creation_nonom1.jpg" alt="Non-OM 1" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s09_creation_nonom2.jpg" alt="Non-OM 2" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s09_creation_nonom3.jpg" alt="Non-OM 3" style="width:100%;display:block"></div>\n'
    '          <div class="phone-frame"><img src="img_m4/s09_creation_nonom4.jpg" alt="Non-OM 4" style="width:100%;display:block"></div>\n'
    '        </div>'
)
if OLD_EXO in html:
    html = html.replace(OLD_EXO, NEW_EXO, 1)
    print("  ok Exercice 2 Non-OM: 4 images")
else:
    print("  MISS: Exercice 2 Non-OM")

# -- 10. Bandeau Evaluation Finale avant footer
EVAL_BANNER = """
<!-- BANDEAU EVALUATION FINALE -->
<div class="section" id="evaluation-section" style="margin-top:32px">
  <div style="background:linear-gradient(135deg,#1565C0,#0D47A1);border-radius:20px;padding:36px 32px;color:white;display:flex;align-items:center;gap:24px;flex-wrap:wrap">
    <div style="flex:1;min-width:200px">
      <div style="font-size:11px;font-weight:700;opacity:.75;text-transform:uppercase;letter-spacing:.1em;margin-bottom:8px">Apr&#232;s la formation</div>
      <h2 style="font-size:1.6rem;font-weight:800;margin-bottom:10px;line-height:1.3">&#128221; &#201;valuation Finale MAFA</h2>
      <p style="opacity:.85;font-size:14px;line-height:1.7;max-width:480px">Testez vos connaissances avec l'&#233;valuation officielle. QCM, Vrai/Faux et questions ouvertes &#8212; correction automatique. Chaque candidat obtient un code personnel pour consulter ses r&#233;sultats priv&#233;ment.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:10px;flex-shrink:0">
      <a href="evaluation.html" style="background:white;color:#1565C0;border:none;padding:14px 28px;border-radius:12px;font-family:'Sora',sans-serif;font-size:0.9rem;font-weight:700;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;gap:8px;white-space:nowrap;box-shadow:0 4px 16px rgba(0,0,0,0.15)">
        &#9654; Commencer l'&#233;valuation
      </a>
      <p style="font-size:11px;opacity:.7;text-align:center;margin:0">&#201;valuation officielle MAFA Holding</p>
    </div>
  </div>
</div>
"""

if '<footer' in html:
    html = html.replace('<footer', EVAL_BANNER + '<footer', 1)
    print("  ok Bandeau Evaluation Finale")
else:
    print("  MISS: footer")

# -- Ecrire
with open(IDX, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nindex.html: {len(html):,} chars ({len(html)//1024} KB)")
print("Done!")
