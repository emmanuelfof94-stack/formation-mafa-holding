"""
Build index.html v2 — contenu modules directement dans les overlays (pas de DOM move)
"""
import re, shutil

SRC = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\Formation_Complete.html"
IDX_BAK = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index_BACKUP.html"
OUT = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"

with open(SRC, "r", encoding="utf-8") as f:
    fc = f.read()

with open(IDX_BAK, "r", encoding="utf-8") as f:
    idx = f.read()

# ── 1. Extraire le CSS de Formation_Complete ──────────────────────────────────
css_start = fc.find('<style>') + len('<style>')
css_end   = fc.find('</style>')
formation_css = fc[css_start:css_end]

# Supprimer règles conflictuelles (sidebar, .app, .main, .hero, .module-card de FC)
to_remove_patterns = [
    r'/\* ══ LAYOUT ══ \*/\s*\.app \{[^}]+\}',
    r'/\* ══ SIDEBAR ══ \*/.*?(?=/\* ══ MAIN)',
    r'/\* ══ MAIN CONTENT ══ \*/\s*\.main \{[^}]+\}',
    r'/\* ══ TOPBAR ══ \*/.*?(?=/\* ══ CONTENT)',
    r'/\* ══ CONTENT AREA ══ \*/\s*\.content \{[^}]+\}',
    r'/\* ══ HOME SCREEN ══ \*/.*?(?=/\* ══ SECTIONS)',
]
for pat in to_remove_patterns:
    formation_css = re.sub(pat, '/* removed */', formation_css, flags=re.DOTALL)

# Supprimer .hero (conflict avec index.html) et .module-card (conflict)
formation_css = re.sub(r'\.hero \{[^}]+\}', '/* hero removed */', formation_css)
formation_css = re.sub(r'\.hero h2[^{]*\{[^}]+\}', '', formation_css)
formation_css = re.sub(r'\.hero p[^{]*\{[^}]+\}', '', formation_css)
formation_css = re.sub(r'\.hero-stats \{[^}]+\}', '', formation_css)
formation_css = re.sub(r'\.hero-stat[^{]*\{[^}]+\}', '', formation_css)
formation_css = re.sub(r'\.module-card \{[^}]+\}', '/* module-card removed */', formation_css)
formation_css = re.sub(r'\.module-card:[^{]+\{[^}]+\}', '', formation_css)
formation_css = re.sub(r'\.module-card \.[^{]+\{[^}]+\}', '', formation_css)
formation_css = re.sub(r'\.home-grid \{[^}]+\}', '', formation_css)

# ── 2. Extraire chaque module ─────────────────────────────────────────────────
def extract_module(html, mid):
    start_tag = f'<div class="module-page" id="module-{mid}"'
    start = html.find(start_tag)
    if start == -1:
        return ""
    next_map = {'m1':'m2','m2':'m3','m3':'m4','m4':'m5','m5':None}
    nxt = next_map[mid]
    if nxt:
        end = html.find(f'<div class="module-page" id="module-{nxt}"', start)
    else:
        end = html.rfind('<script>', 0, html.rfind('</body>'))
    content = html[start:end].rstrip()
    # Enlever display:none initial
    content = content.replace(' style="display:none"', '', 1)
    return content

modules = {}
for mid in ['m1','m2','m3','m4','m5']:
    modules[mid] = extract_module(fc, mid)
    print(f"Module {mid}: {len(modules[mid])} chars")

# ── 3. Extraire le JS ─────────────────────────────────────────────────────────
js_start = fc.rfind('<script>') + len('<script>')
js_end   = fc.rfind('</script>')
formation_js = fc[js_start:js_end]

# Supprimer les fonctions de navigation FC (sidebar, showHome, showModule, etc.)
for pat in [
    r'function printResults\([^)]*\)\s*\{[^}]+\}',
    r'function toggleSidebar\(\)\s*\{[^}]+\}',
    r'function closeSidebar\(\)\s*\{[^}]+\}',
    r'function showHome\([^)]*\)\s*\{.*?\n\}',
    r'function showModule\([^)]*\)\s*\{.*?\n\}',
    r'function showModuleTab\([^)]*\)\s*\{.*?\n\}',
    r'document\.addEventListener\(\'DOMContentLoaded\'.*?\}\);',
]:
    formation_js = re.sub(pat, '', formation_js, flags=re.DOTALL)

# Corriger duplicate updateScore()
count = formation_js.count('function updateScore()')
print(f"updateScore() occurrences: {count}")
if count == 2:
    # Première pour M1, deuxième pour M2
    pos1 = formation_js.find('function updateScore()')
    pos2 = formation_js.find('function updateScore()', pos1+1)
    formation_js = (
        formation_js[:pos1] +
        'function updateScoreM1()' +
        formation_js[pos1+len('function updateScore()'):pos2] +
        'function updateScoreM2()' +
        formation_js[pos2+len('function updateScore()'):]
    )
    formation_js = formation_js.replace(
        'scoresM1[qid] = correct;\n  updateScore();',
        'scoresM1[qid] = correct;\n  updateScoreM1();'
    )
    formation_js = formation_js.replace(
        'scoresM2[qid] = correct;\n  updateScore();',
        'scoresM2[qid] = correct;\n  updateScoreM2();'
    )
    print("updateScore() fix OK")

# ── 4. CSS overlay + modules ─────────────────────────────────────────────────
overlay_css = """
/* ═══ CSS MODULES DE FORMATION ═══ */
""" + formation_css + """

/* ── OVERLAY PLEIN ÉCRAN ── */
.module-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: #FCFBF8;
  z-index: 500;
  overflow-y: auto;
}
.module-overlay.open { display: block; }

.overlay-topbar {
  position: sticky;
  top: 0;
  background: white;
  border-bottom: 2px solid #F9E8EC;
  padding: 14px 28px;
  display: flex;
  align-items: center;
  gap: 16px;
  z-index: 10;
  box-shadow: 0 2px 12px rgba(141,12,35,0.08);
}
.overlay-back {
  background: #F9E8EC;
  color: #8D0C23;
  border: none;
  border-radius: 8px;
  padding: 8px 18px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  font-family: 'Sora', sans-serif;
  flex-shrink: 0;
}
.overlay-back:hover { opacity: 0.8; }
.overlay-topbar-title {
  font-size: 1rem;
  font-weight: 700;
  color: #8D0C23;
}
.overlay-content {
  max-width: 1000px;
  margin: 0 auto;
  padding: 28px 24px 60px;
}

/* Module display */
.module-page {
  display: flex;
  flex-direction: column;
  min-height: 60vh;
}

/* Tabs */
.module-tabs-clean {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
  flex-wrap: wrap;
  background: white;
  padding: 12px 16px;
  border-radius: 14px;
  box-shadow: 0 1px 8px rgba(0,0,0,.06);
}
.tab-btn-clean {
  padding: 9px 20px;
  border-radius: 8px;
  border: none;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  background: #ECEFF1;
  color: #455A64;
  font-family: 'Sora', sans-serif;
  transition: all .2s;
}
.tab-btn-clean.active-red { background: #8D0C23; color: white; }
.tab-btn-clean:hover:not(.active-red) { background: #F9E8EC; color: #8D0C23; }

/* Tab sections */
.tab-section { display: none; }

/* Progress bar */
.progress-bar {
  background: #ECEFF1;
  border-radius: 10px;
  height: 8px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  border-radius: 10px;
  background: linear-gradient(90deg, #8D0C23, #CF9E41);
  transition: width .4s;
}

/* Quiz states */
.quiz-option.disabled { opacity:.6; pointer-events:none; cursor:not-allowed; }
.quiz-feedback { display: none; }
.quiz-feedback.show { display: block; border-radius: 8px; padding: 10px 14px; font-size: 13px; margin-top: 8px; }
.quiz-feedback.fb-correct { background: #F3EDD8; color: #584B26; }
.quiz-feedback.fb-incorrect { background: #F2D6DC; color: #6A091A; }
.quiz-option.correct { border-color: #584B26 !important; background: #F3EDD8 !important; color: #584B26 !important; }
.quiz-option.incorrect { border-color: #6A091A !important; background: #F2D6DC !important; color: #6A091A !important; }
"""

# ── 5. Construire les overlays HTML ──────────────────────────────────────────
module_titles = {
    'm1': '📞 Call Center — ID30 &amp; Orange Money',
    'm2': '📂 Back Office — ID30 &amp; Orange Money',
    'm3': '🔍 Inspecteurs — ID30 &amp; Orange QR Code',
    'm4': '🏪 Orange Business — Plateforme Marchande',
    'm5': '📱 Application Agent &amp; Superviseur Orange',
}

overlays_html = '\n<!-- ══ OVERLAYS MODULES ══ -->\n'
for mid in ['m1','m2','m3','m4','m5']:
    overlays_html += f"""
<div class="module-overlay" id="overlay-{mid}">
  <div class="overlay-topbar">
    <button class="overlay-back" onclick="closeModule()">&#8592; Retour au portail</button>
    <span class="overlay-topbar-title">{module_titles[mid]}</span>
  </div>
  <div class="overlay-content">
{modules[mid]}
  </div>
</div>
"""

# ── 6. JS navigation ─────────────────────────────────────────────────────────
nav_js = """
<script>
// ── Navigation Overlay ──────────────────────────────────
var _currentModule = null;

function openModule(mid) {
  document.getElementById('overlay-' + mid).classList.add('open');
  document.body.style.overflow = 'hidden';
  _currentModule = mid;
  showModuleTab(mid, 'cours');
}

function closeModule() {
  if (_currentModule) {
    document.getElementById('overlay-' + _currentModule).classList.remove('open');
    document.body.style.overflow = '';
    _currentModule = null;
  }
}

function showModuleTab(moduleId, tabName) {
  var overlay = document.getElementById('overlay-' + moduleId);
  if (!overlay) return;
  overlay.querySelectorAll('.tab-section').forEach(function(s) { s.style.display = 'none'; });
  var tab = document.getElementById('tab-' + moduleId + '-' + tabName);
  if (tab) tab.style.display = 'block';
  var bar = overlay.querySelector('.module-tabs-clean');
  if (bar) {
    bar.querySelectorAll('[data-tab]').forEach(function(btn) {
      btn.classList.remove('active-red');
    });
    var active = bar.querySelector('[data-tab="' + tabName + '"]');
    if (active) active.classList.add('active-red');
  }
}

// Fermer avec Échap
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') closeModule();
});

// ── Fonctions Quiz ──────────────────────────────────────
""" + formation_js + """
</script>
"""

# ── 7. Assembler index.html ───────────────────────────────────────────────────
# Injecter CSS
result = idx.replace('</style>', overlay_css + '\n</style>', 1)

# Remettre les cartes module-card de index_BACKUP avec onclick (pas href)
# Les cartes dans index_BACKUP pointent vers Formation_Complete.html?m=mX
# (ajoutés lors des edits précédents)
href_to_onclick = {
    'href="Formation_Complete.html?m=m1"': f'onclick="openModule(\'m1\')" style="border:none;cursor:pointer;text-align:left;background:white;"',
    'href="Formation_Complete.html?m=m2"': f'onclick="openModule(\'m2\')" style="border:none;cursor:pointer;text-align:left;background:white;"',
    'href="Formation_Complete.html?m=m3"': f'onclick="openModule(\'m3\')" style="border:none;cursor:pointer;text-align:left;background:white;"',
    'href="Formation_Complete.html?m=m4"': f'onclick="openModule(\'m4\')" style="border:none;cursor:pointer;text-align:left;background:white;"',
    'href="Formation_Complete.html?m=m5"': f'onclick="openModule(\'m5\')" style="border:none;cursor:pointer;text-align:left;background:white;"',
}
for href, onclick in href_to_onclick.items():
    result = result.replace(f'<a class="module-card" {href}>', f'<button class="module-card" {onclick}>')
# Fermer </a> → </button> pour les 5 cartes
result = re.sub(r'(<span class="progress-mini">.*?</span>\s*</div>\s*)\s*</a>', r'\1</button>', result, flags=re.DOTALL)

# Liens CTA → scroll ou openModule
result = result.replace(
    'href="Formation_Complete.html" class="hero-cta"',
    'href="#modules-section" class="hero-cta" onclick="document.getElementById(\'modules-section\').scrollIntoView({behavior:\'smooth\'});return false;"'
)
result = result.replace(
    'href="Formation_Complete.html" style="background:linear-gradient(135deg,#CF9E41,#DDB55A)',
    'href="#" onclick="openModule(\'m1\');return false;" style="background:linear-gradient(135deg,#CF9E41,#DDB55A)'
)
result = result.replace(
    'href="Formation_Complete.html" style="color:var(--orange)',
    'href="#modules-section" onclick="document.getElementById(\'modules-section\').scrollIntoView({behavior:\'smooth\'});return false;" style="color:var(--orange)'
)

# id modules-section
result = result.replace(
    '<div class="section">\n  <div class="section-title">Modules disponibles</div>',
    '<div class="section" id="modules-section">\n  <div class="section-title">Modules disponibles</div>'
)

# Injecter overlays + JS avant </body>
result = result.replace('</body>', overlays_html + nav_js + '\n</body>')

with open(OUT, "w", encoding="utf-8") as f:
    f.write(result)

print(f"\nindex.html: {len(result):,} chars ({len(result)//1024} KB)")
print("Done!")
