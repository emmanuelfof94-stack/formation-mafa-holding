"""
Fusionne Formation_Complete.html dans index.html
- Garde le design du portail index.html
- Intègre les 5 modules dans des overlays plein écran
- Corrige le bug duplicate updateScore()
"""
import re, shutil, os

SRC = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\Formation_Complete.html"
IDX = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"
OUT = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"
BAK = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index_BACKUP.html"

# Backup
shutil.copy(IDX, BAK)
print(f"Backup: {BAK}")

with open(SRC, "r", encoding="utf-8") as f:
    fc = f.read()

# ── 1. Extraire le CSS de Formation_Complete ──────────────────────────────────
css_match = re.search(r'<style>(.*?)</style>', fc, re.DOTALL)
formation_css = css_match.group(1) if css_match else ""

# Supprimer les règles qui entrent en conflit avec index.html
# (layout sidebar, .main, .topbar, .app, .hero de Formation_Complete)
conflict_classes = [
    r'\.app\s*\{[^}]+\}',
    r'\.sidebar[\s,{][^}]+\}',
    r'\.sidebar\.[^{]+\{[^}]+\}',
    r'\.main\s*\{[^}]+\}',
    r'\.topbar[^{]*\{[^}]+\}',
    r'\.nav-section[^{]*\{[^}]+\}',
    r'\.nav-label[^{]*\{[^}]+\}',
    r'\.nav-item[^{]*\{[^}]+\}',
    r'\.nav-progress[^{]*\{[^}]+\}',
    r'\.content\s*\{[^}]+\}',
    # hero de Formation_Complete est différent de celui d'index
    r'\.hero\s*\{[^}]+\}',
    r'\.hero\s+h2[^{]*\{[^}]+\}',
    r'\.hero\s+p[^{]*\{[^}]+\}',
    r'\.hero-stats[^{]*\{[^}]+\}',
    r'\.hero-stat[^{]*\{[^}]+\}',
    # .module-card est redéfini dans Formation_Complete - on garde index
    r'\.module-card[^{]*\{[^}]+\}',
    r'\.home-grid[^{]*\{[^}]+\}',
    # topbar
    r'\.topbar-[^{]+\{[^}]+\}',
]
for pat in conflict_classes:
    formation_css = re.sub(pat, '/* removed */', formation_css, flags=re.DOTALL)

# ── 2. Extraire les 5 modules ─────────────────────────────────────────────────
modules_html = ""
for mid in ['m1', 'm2', 'm3', 'm4', 'm5']:
    pattern = rf'(<div class="module-page" id="module-{mid}".*?)</div>\s*\n\s*\n\s*<div class="module-page" id="module-'
    # Trouver le début
    start_tag = f'<div class="module-page" id="module-{mid}"'
    start = fc.find(start_tag)
    if start == -1:
        print(f"Module {mid} non trouvé!")
        continue

    # Trouver la fin : prochain module-page ou fermeture du conteneur
    next_mid_map = {'m1': 'm2', 'm2': 'm3', 'm3': 'm4', 'm4': 'm5', 'm5': None}
    next_id = next_mid_map[mid]
    if next_id:
        end_tag = f'<div class="module-page" id="module-{next_id}"'
        end = fc.find(end_tag, start)
    else:
        # m5: finit avant </body>
        end = fc.rfind('</body>')
        # Chercher le dernier </div> avant </body>
        # On prend jusqu'à </div>\n\n\n<script>
        script_start = fc.rfind('<script>', 0, end)
        end = script_start

    if end == -1:
        print(f"Fin du module {mid} non trouvée!")
        continue

    mod_html = fc[start:end].rstrip()
    # Retirer le style="display:none" pour qu'on puisse contrôler via overlay
    mod_html = mod_html.replace(' style="display:none"', '', 1)
    modules_html += f"\n{mod_html}\n"
    print(f"Module {mid}: {len(mod_html)} chars")

# ── 3. Extraire le JS ─────────────────────────────────────────────────────────
js_match = re.search(r'<script>(.*?)</script>', fc, re.DOTALL)
formation_js = js_match.group(1) if js_match else ""

# Supprimer les fonctions sidebar/navigation Formation_Complete (on les remplace)
# On garde: answerM1..M5, updateScore variants, showModuleTab, scrollTo
nav_fns_to_remove = [
    r'function toggleSidebar\(\)[^}]+\}',
    r'function closeSidebar\(\)[^}]+\}',
    r'function showHome\([^)]*\)[^{]*\{.*?\n\}',
    r'function showModule\([^)]*\)[^{]*\{.*?\n\}',
    r'function showModuleTab\([^)]*\)[^{]*\{.*?\n\}',
    r'function printResults\([^)]*\)[^{]*\{[^}]+\}',
    r'document\.addEventListener\(\'DOMContentLoaded\'.*?\}\);',
]
for pat in nav_fns_to_remove:
    formation_js = re.sub(pat, '', formation_js, flags=re.DOTALL)

# Corriger le bug duplicate updateScore()
# M1 a updateScore() sans suffixe, M2 aussi -> renommer
formation_js = formation_js.replace(
    '/* ── Quiz M1 — Call Center ── */\nlet scoresM1',
    '/* ── Quiz M1 — Call Center ── */\nlet scoresM1'
)
# Remplacer la 2e occurrence de updateScore par updateScoreM2
parts = formation_js.split('function updateScore()')
if len(parts) == 3:
    # M1 updateScore -> updateScoreM1, M2 -> updateScoreM2
    formation_js = parts[0] + 'function updateScoreM1()' + parts[1] + 'function updateScoreM2()' + parts[2]
    formation_js = formation_js.replace(
        'scoresM1[qid] = correct;\n  updateScore();',
        'scoresM1[qid] = correct;\n  updateScoreM1();'
    )
    formation_js = formation_js.replace(
        'scoresM2[qid] = correct;\n  updateScore();',
        'scoresM2[qid] = correct;\n  updateScoreM2();'
    )
    print("updateScore() dupliqué corrigé")

# ── 4. Lire index.html ────────────────────────────────────────────────────────
with open(IDX, "r", encoding="utf-8") as f:
    idx = f.read()

# ── 5. Injecter le CSS Formation dans index.html ──────────────────────────────
# Ajouter avant </style> dans index.html
idx = idx.replace('</style>', f"""
/* ═══════════════════════════════════════════
   CSS MODULES DE FORMATION (Formation_Complete)
   ═══════════════════════════════════════════ */
{formation_css}

/* ── MODULE OVERLAY ── */
.module-overlay {{
  display: none;
  position: fixed;
  inset: 0;
  background: var(--bg);
  z-index: 500;
  overflow-y: auto;
  animation: slideIn .25s ease;
}}
.module-overlay.open {{ display: block; }}
@keyframes slideIn {{
  from {{ opacity: 0; transform: translateY(20px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}
.overlay-topbar {{
  position: sticky;
  top: 0;
  background: white;
  border-bottom: 2px solid var(--blue-pale);
  padding: 14px 28px;
  display: flex;
  align-items: center;
  gap: 16px;
  z-index: 10;
  box-shadow: 0 2px 12px rgba(141,12,35,0.08);
}}
.overlay-back {{
  background: var(--blue-pale);
  color: var(--blue);
  border: none;
  border-radius: 8px;
  padding: 8px 16px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: 'Sora', sans-serif;
  transition: background .2s;
}}
.overlay-back:hover {{ background: var(--blue-pale); opacity:.8; }}
.overlay-topbar-title {{
  font-size: 1rem;
  font-weight: 700;
  color: var(--blue);
}}
.overlay-content {{
  max-width: 1000px;
  margin: 0 auto;
  padding: 28px 24px;
}}
.module-page {{
  /* reset display: none from Formation_Complete */
}}

/* Module tabs bar */
.module-tabs-clean {{
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
  flex-wrap: wrap;
  background: white;
  padding: 12px 16px;
  border-radius: 14px;
  box-shadow: 0 1px 8px rgba(0,0,0,.06);
}}
.tab-btn-clean {{
  padding: 9px 20px;
  border-radius: 8px;
  border: none;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  background: var(--grey-light);
  color: var(--grey);
  font-family: 'Sora', sans-serif;
  transition: all .2s;
}}
.tab-btn-clean.active-red {{
  background: var(--blue);
  color: white;
}}
.tab-btn-clean:hover:not(.active-red) {{
  background: var(--blue-pale);
  color: var(--blue);
}}
.tab-section {{ display: none; }}
.tab-section.active {{ display: block; }}

/* Progress bar */
.progress-bar {{
  background: var(--grey-light);
  border-radius: 10px;
  height: 8px;
  overflow: hidden;
}}
.progress-fill {{
  height: 100%;
  border-radius: 10px;
  background: linear-gradient(90deg, var(--blue), var(--orange));
  transition: width .4s;
}}

/* quiz-option disabled */
.quiz-option.disabled {{ opacity:.6; pointer-events:none; cursor:not-allowed; }}
.quiz-feedback.show {{ display:block; }}
.quiz-feedback.fb-correct {{ background: var(--teal-pale); color: var(--teal); border-radius:8px; padding:10px 14px; font-size:13px; margin-top:8px; }}
.quiz-feedback.fb-incorrect {{ background: var(--red-pale); color: var(--red); border-radius:8px; padding:10px 14px; font-size:13px; margin-top:8px; }}
.correct {{ border-color: var(--teal) !important; background: var(--teal-pale) !important; color: var(--teal) !important; }}
.incorrect {{ border-color: var(--red) !important; background: var(--red-pale) !important; color: var(--red) !important; }}

</style>""", 1)

# ── 6. Modifier les cartes pour ouvrir les overlays (onclick au lieu de href) ─
card_map = {
    'Formation_Complete.html?m=m1': ("openModule('m1')", "Call Center"),
    'Formation_Complete.html?m=m2': ("openModule('m2')", "Back Office"),
    'Formation_Complete.html?m=m3': ("openModule('m3')", "Inspecteurs"),
    'Formation_Complete.html?m=m4': ("openModule('m4')", "OM Business"),
    'Formation_Complete.html?m=m5': ("openModule('m5')", "Agent &amp; Superviseur"),
}
for href, (onclick, label) in card_map.items():
    idx = idx.replace(
        f'<a class="module-card" href="{href}">',
        f'<button class="module-card" onclick="{onclick}" style="border:none;cursor:pointer;text-align:left;">'
    )
    # Fermer le <a> → </button>
idx = re.sub(r'(</div>\s*</div>\s*</div>\s*\n\s*)</a>', r'\1</button>', idx)

# ── 7. Injecter l'overlay + modules avant </body> ─────────────────────────────
module_titles = {
    'm1': '📞 Call Center — ID30 &amp; Orange Money',
    'm2': '📂 Back Office — ID30 &amp; Orange Money',
    'm3': '🔍 Inspecteurs — ID30 &amp; Orange QR Code',
    'm4': '🏪 Orange Business — Plateforme Marchande',
    'm5': '📱 Application Agent &amp; Superviseur Orange',
}

overlay_html = '\n<!-- ══ MODULE OVERLAYS ══ -->\n'
for mid in ['m1','m2','m3','m4','m5']:
    title = module_titles[mid]
    overlay_html += f"""
<div class="module-overlay" id="overlay-{mid}">
  <div class="overlay-topbar">
    <button class="overlay-back" onclick="closeModule()">← Retour au portail</button>
    <span class="overlay-topbar-title">{title}</span>
  </div>
  <div class="overlay-content" id="overlay-content-{mid}">
    <!-- module content injected below -->
  </div>
</div>
"""

# Container pour les modules (caché, sera déplacé par JS dans l'overlay)
overlay_html += '\n<div id="modules-store" style="display:none">\n'
overlay_html += modules_html
overlay_html += '\n</div>\n'

# Script
overlay_html += f"""
<script>
// ── Navigation Overlay ─────────────────────────────
var _currentModule = null;

function openModule(mid) {{
  // Déplacer le module dans l'overlay content
  var store = document.getElementById('module-' + mid);
  var container = document.getElementById('overlay-content-' + mid);
  if (store && container && container.children.length === 0) {{
    container.appendChild(store);
  }}
  // Afficher l'overlay
  document.getElementById('overlay-' + mid).classList.add('open');
  document.body.style.overflow = 'hidden';
  _currentModule = mid;
  // Montrer onglet cours par défaut
  if (store) {{
    store.style.display = 'flex';
    store.style.flexDirection = 'column';
  }}
  showModuleTab(mid, 'cours');
  window.scrollTo(0,0);
}}

function closeModule() {{
  if (_currentModule) {{
    var overlay = document.getElementById('overlay-' + _currentModule);
    overlay.classList.remove('open');
    document.body.style.overflow = '';
    _currentModule = null;
  }}
}}

function showModuleTab(moduleId, tabName) {{
  var mod = document.getElementById('module-' + moduleId);
  if (!mod) return;
  mod.querySelectorAll('.tab-section').forEach(function(s) {{ s.style.display='none'; }});
  var tab = document.getElementById('tab-' + moduleId + '-' + tabName);
  if (tab) tab.style.display = 'block';
  var bar = mod.querySelector('.module-tabs-clean');
  if (bar) {{
    bar.querySelectorAll('[data-tab]').forEach(function(btn) {{
      btn.classList.remove('active-red','active-orange','active-green','active-blue','active');
    }});
    var active = bar.querySelector('[data-tab="' + tabName + '"]');
    if (active) active.classList.add('active-red');
  }}
}}

// Fermer avec Escape
document.addEventListener('keydown', function(e) {{
  if (e.key === 'Escape') closeModule();
}});

// ── Quiz Functions ─────────────────────────────────
{formation_js}

</script>
"""

idx = idx.replace('</body>', overlay_html + '\n</body>')

# ── 8. Supprimer les liens CTA vers Formation_Complete.html (section banner + footer) ─
# Les liens hero-cta et la section banner peuvent rester mais pointer vers le bon endroit
# On laisse tels quels - ils mènent toujours à Formation_Complete.html
# Pour cohérence, on peut les supprimer ou les garder comme backup

# ── 9. Écrire ─────────────────────────────────────────────────────────────────
with open(OUT, "w", encoding="utf-8") as f:
    f.write(idx)

print(f"\nindex.html final: {len(idx):,} chars ({len(idx)//1024} KB)")
print("Done!")
