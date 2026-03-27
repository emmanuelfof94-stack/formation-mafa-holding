#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

fpath = 'C:/Users/MAFA HOLDING/CREATIONS FOF/Formation/index.html'
with open(fpath, encoding='utf-8') as f:
    content = f.read()

# ─── 1. ORGANIGRAMME VISUEL (section 10) ───
old_org = (
    '<div style="overflow-x:auto;margin:18px 0">\n'
    '      <div style="display:flex;flex-direction:column;align-items:center;gap:0;min-width:420px">\n'
    '        <!-- Inspecteur -->\n'
    '        <div style="background:linear-gradient(135deg,#8D0C23,#5A0815);color:white;padding:14px 32px;border-radius:12px;font-weight:700;font-size:14px;text-align:center;box-shadow:0 4px 16px rgba(141,12,35,.3)">\n'
    '          \U0001f50d INSPECTEUR<br><span style="font-size:11px;font-weight:400;opacity:.85">Supervision technique &amp; qualit\xe9</span>\n'
    '        </div>\n'
    '        <div style="width:2px;height:22px;background:#8D0C23;opacity:.4"></div>\n'
    '        <!-- RV -->\n'
    '        <div style="background:linear-gradient(135deg,#CF9E41,#a07a28);color:white;padding:14px 32px;border-radius:12px;font-weight:700;font-size:14px;text-align:center;box-shadow:0 4px 16px rgba(207,158,65,.3)">\n'
    '          \U0001f3d9\ufe0f RESPONSABLE DE VILLE (RV)<br><span style="font-size:11px;font-weight:400;opacity:.9">Pilotage op\xe9rationnel \xb7 Brief/Debrief \xb7 Mat\xe9riel</span>\n'
    '        </div>\n'
    '        <div style="width:2px;height:22px;background:#CF9E41;opacity:.5"></div>\n'
    '        <!-- Superviseurs -->\n'
    '        <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">\n'
    '          <div style="background:linear-gradient(135deg,#1565C0,#0d47a1);color:white;padding:12px 18px;border-radius:10px;font-weight:600;font-size:12px;text-align:center;min-width:120px">\n'
    '            \U0001f465 SUPERVISEUR 1<br><span style="font-size:10px;opacity:.85">9 \xe0 15 agents</span>\n'
    '          </div>\n'
    '          <div style="background:linear-gradient(135deg,#1565C0,#0d47a1);color:white;padding:12px 18px;border-radius:10px;font-weight:600;font-size:12px;text-align:center;min-width:120px">\n'
    '            \U0001f465 SUPERVISEUR 2<br><span style="font-size:10px;opacity:.85">9 \xe0 15 agents</span>\n'
    '          </div>\n'
    '          <div style="background:linear-gradient(135deg,#1565C0,#0d47a1);color:white;padding:12px 18px;border-radius:10px;font-weight:600;font-size:12px;text-align:center;min-width:120px">\n'
    '            \U0001f465 SUPERVISEUR 3<br><span style="font-size:10px;opacity:.85">9 \xe0 15 agents</span>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>\n'
    '    </div>'
)

new_org = (
    '<div style="overflow-x:auto;margin:18px 0">\n'
    '      <div style="display:flex;flex-direction:column;align-items:center;gap:0;min-width:560px">\n\n'
    '        <!-- Responsable des Operations -->\n'
    '        <div style="background:linear-gradient(135deg,#4a0e72,#2d0048);color:white;padding:14px 36px;border-radius:12px;font-weight:700;font-size:14px;text-align:center;box-shadow:0 4px 16px rgba(74,14,114,.35)">\n'
    '          \u2699\ufe0f RESPONSABLE DES OP\xc9RATIONS<br><span style="font-size:11px;font-weight:400;opacity:.85">Strat\xe9gie \xb7 Pilotage global \xb7 Consignes terrain</span>\n'
    '        </div>\n\n'
    '        <!-- Deux branches -->\n'
    '        <div style="display:flex;width:100%;justify-content:center;gap:60px;margin-top:0">\n\n'
    '          <!-- BRANCHE GAUCHE : RV -> Superviseurs -->\n'
    '          <div style="display:flex;flex-direction:column;align-items:center">\n'
    '            <div style="width:2px;height:22px;background:#CF9E41;opacity:.6"></div>\n'
    '            <div style="background:linear-gradient(135deg,#CF9E41,#a07a28);color:white;padding:14px 24px;border-radius:12px;font-weight:700;font-size:13px;text-align:center;box-shadow:0 4px 16px rgba(207,158,65,.3)">\n'
    '              \U0001f3d9\ufe0f RESPONSABLE DE VILLE (RV)<br><span style="font-size:11px;font-weight:400;opacity:.9">Re\xe7oit les consignes \xb7 Brief/Debrief \xb7 Mat\xe9riel</span>\n'
    '            </div>\n'
    '            <div style="width:2px;height:22px;background:#CF9E41;opacity:.5"></div>\n'
    '            <div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center">\n'
    '              <div style="background:linear-gradient(135deg,#1565C0,#0d47a1);color:white;padding:12px 14px;border-radius:10px;font-weight:600;font-size:12px;text-align:center;min-width:110px">\n'
    '                \U0001f465 SUPERVISEUR 1<br><span style="font-size:10px;opacity:.85">15 \xe0 20 agents</span>\n'
    '              </div>\n'
    '              <div style="background:linear-gradient(135deg,#1565C0,#0d47a1);color:white;padding:12px 14px;border-radius:10px;font-weight:600;font-size:12px;text-align:center;min-width:110px">\n'
    '                \U0001f465 SUPERVISEUR 2<br><span style="font-size:10px;opacity:.85">15 \xe0 20 agents</span>\n'
    '              </div>\n'
    '              <div style="background:linear-gradient(135deg,#1565C0,#0d47a1);color:white;padding:12px 14px;border-radius:10px;font-weight:600;font-size:12px;text-align:center;min-width:110px">\n'
    '                \U0001f465 SUPERVISEUR 3<br><span style="font-size:10px;opacity:.85">15 \xe0 20 agents</span>\n'
    '              </div>\n'
    '            </div>\n'
    '          </div>\n\n'
    '          <!-- BRANCHE DROITE : Resp. Cartographie -> Inspecteurs -->\n'
    '          <div style="display:flex;flex-direction:column;align-items:center">\n'
    '            <div style="width:2px;height:22px;background:#8D0C23;opacity:.5"></div>\n'
    '            <div style="background:linear-gradient(135deg,#5A0815,#3d0510);color:white;padding:14px 24px;border-radius:12px;font-weight:700;font-size:13px;text-align:center;box-shadow:0 4px 16px rgba(90,8,21,.3)">\n'
    '              \U0001f5fa\ufe0f RESPONSABLE CARTOGRAPHIE<br><span style="font-size:11px;font-weight:400;opacity:.85">Coordination technique \xb7 Suivi cartographique</span>\n'
    '            </div>\n'
    '            <div style="width:2px;height:22px;background:#8D0C23;opacity:.4"></div>\n'
    '            <div style="background:linear-gradient(135deg,#8D0C23,#5A0815);color:white;padding:14px 24px;border-radius:12px;font-weight:700;font-size:13px;text-align:center;box-shadow:0 4px 16px rgba(141,12,35,.3)">\n'
    '              \U0001f50d INSPECTEUR<br><span style="font-size:11px;font-weight:400;opacity:.85">Contr\xf4le qualit\xe9 \xb7 Contre-enqu\xeates \xb7 Tracking GPS</span>\n'
    '            </div>\n'
    '          </div>\n\n'
    '        </div>\n'
    '      </div>\n'
    '    </div>'
)

if old_org in content:
    content = content.replace(old_org, new_org)
    print("OK: Organigramme visuel section 10 remplace")
else:
    print("ERREUR: Organigramme visuel non trouve - recherche par regex")
    m = re.search(r'<!-- Inspecteur -->', content)
    if m:
        print(f"  Commentaire trouve a pos {m.start()}")

# ─── 2. TABLEAU DES ROLES ───
old_insp_row = '<tr><td><strong>\U0001f50d Inspecteur</strong></td><td>Supervision technique, v\xe9rification qualit\xe9 des donn\xe9es, missions terrain, contr\xf4les inopins</td><td>Direction des op\xe9rations MAFA</td></tr>'
new_insp_row = '<tr><td><strong>\U0001f50d Inspecteur</strong></td><td>Supervision technique, v\xe9rification qualit\xe9 des donn\xe9es, missions terrain, contr\xf4les inopins</td><td>Responsable Cartographie</td></tr>'

# Recherche plus souple
m = re.search(r'(<tr><td><strong>.*?Inspecteur</strong></td><td>[^<]+</td><td>)(Direction des op\xe9rations MAFA)(</td></tr>)', content)
if m:
    content = content[:m.start(2)] + 'Responsable Cartographie' + content[m.end(2):]
    print("OK: Tableau - Inspecteur rend compte a Responsable Cartographie")
else:
    print("ERREUR: Ligne Inspecteur non trouvee dans tableau")

m = re.search(r'(<tr><td><strong>.*?Responsable de Ville.*?</strong></td><td>[^<]+</td><td>)(Inspecteur)(</td></tr>)', content)
if m:
    content = content[:m.start(2)] + 'Responsable des Operations' + content[m.end(2):]
    print("OK: Tableau - RV rend compte a Responsable des Operations")
else:
    print("ERREUR: Ligne RV non trouvee dans tableau")

# ─── 3. REGLE DE COMPOSITION ───
content = re.sub(
    r'Chaque \xe9quipe terrain = 1 Superviseur \+ 9 agents identificateurs = <strong>10 personnes</strong>\. Un RV supervise en moyenne <strong>3 \xe9quipes</strong>, soit ~30 personnes au total\.',
    'Chaque \xe9quipe terrain = 1 Superviseur + 15 \xe0 20 agents identificateurs = <strong>16 \xe0 21 personnes</strong>. Un RV supervise en moyenne <strong>3 \xe9quipes</strong>, soit 50 \xe0 65 personnes au total.',
    content
)
print("OK: Regle de composition mise a jour")

# ─── 4. DESCRIPTION DU RV (section 11) ───
content = content.replace(
    "Il est l\u2019interface directe entre l\u2019Inspecteur et les \xe9quipes d\u2019agents.",
    "Il est l\u2019interface directe entre le Responsable des Op\xe9rations et les \xe9quipes de Superviseurs."
)
# Variante avec apostrophe simple
content = content.replace(
    "Il est l'interface directe entre l'Inspecteur et les \xe9quipes d'agents.",
    "Il est l'interface directe entre le Responsable des Op\xe9rations et les \xe9quipes de Superviseurs."
)
print("OK: Description RV corrigee")

# ─── 5. SECOND BLOC HIERARCHIE (simplifie) ───
# Chercher le bloc avec Responsable Ville -> pilote
m = re.search(r'\U0001f3d9\ufe0f Responsable Ville \u2192 pilote', content)
if m:
    # Trouver le debut du parent div
    start = content.rfind('<div style="display:flex;flex-direction:column;gap:8px;margin-top:12px">', 0, m.start())
    # Trouver la fin: le prochain </div> apres le 3e item
    # Compter les divs
    pos = start
    depth = 0
    while pos < len(content):
        if content[pos:pos+4] == '<div':
            depth += 1
        elif content[pos:pos+6] == '</div>':
            depth -= 1
            if depth == 0:
                end = pos + 6
                break
        pos += 1

    old_bloc = content[start:end]
    print(f"  Bloc trouve: {old_bloc[:200]}")

    new_bloc = (
        '<div style="display:flex;flex-direction:column;gap:8px;margin-top:12px">\n'
        '        <div style="background:#4a0e72;color:white;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px">\u2699\ufe0f Responsable des Op\xe9rations \u2192 consignes et pilotage global</div>\n'
        '        <div style="background:#1a237e;color:white;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px;margin-left:20px">\U0001f3d9\ufe0f Responsable de Ville (RV) \u2192 re\xe7oit les consignes, pilote les \xe9quipes terrain</div>\n'
        '        <div style="background:#3949ab;color:white;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px;margin-left:40px">\U0001f465 Superviseur \u2192 encadre 15 \xe0 20 agents identificateurs</div>'
    )
    # Garder la suite du bloc original (le 4e item et au-dela)
    # Trouver le 4e item dans old_bloc
    items = re.findall(r'<div style[^>]+>[^<]+</div>', old_bloc)
    if len(items) >= 4:
        new_bloc += '\n        ' + items[3]
    new_bloc += '\n        <div style="background:#8D0C23;color:white;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px;margin-left:20px">\U0001f5fa\ufe0f Responsable Cartographie \u2192 coordination technique</div>\n'
    new_bloc += '        <div style="background:#b71c1c;color:white;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px;margin-left:40px">\U0001f50d Inspecteur \u2192 contr\xf4le qualit\xe9 et contre-enqu\xeates (rattach\xe9 au Resp. Cartographie)</div>\n'
    new_bloc += '      </div>'

    content = content[:start] + new_bloc + content[end:]
    print("OK: Second bloc hierarchie corrige")
else:
    # Remplacement simple si le texte est different
    content = content.replace(
        '\U0001f3d9\ufe0f Responsable Ville \u2192 pilote l\u2019ensemble des op\xe9rations sur la ville',
        '\u2699\ufe0f Responsable des Op\xe9rations \u2192 consignes et pilotage global'
    )
    print("OK (remplacement simple): RV -> Resp. Operations")

# ─── 6. BADGE "9 Agents (AI)" ───
content = content.replace(
    '\U0001f465 9 Agents (AI) \u2192 identification et enr\xf4lement \xeelot par \xeelot',
    '\U0001f465 15 \xe0 20 Agents (AI) \u2192 identification et enr\xf4lement \xeelot par \xeelot'
)
print("OK: Badge agents mis a jour")

# ─── SAUVEGARDE ───
with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)
print("\nFichier Formation/index.html sauvegarde avec succes.")
