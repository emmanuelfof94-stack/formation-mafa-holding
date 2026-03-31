"""
Fix quiz bugs + expand to 20 questions + drag-to-scroll
"""

IN  = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"
OUT = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"

with open(IN, "r", encoding="utf-8") as f:
    html = f.read()

# ══════════════════════════════════════════════════════════════
# 1. FIX JS FUNCTIONS — answerM1 / M2 / M3 / M5
# ══════════════════════════════════════════════════════════════

OLD_M1_JS = """function answerM1(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  const opts = block.querySelectorAll('.quiz-option');
  opts.forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM1[qid] = correct;
  updateScoreM1();
}"""

NEW_M1_JS = """function answerM1(el, qid, correct, feedback) {
  const block = document.getElementById('m1-' + qid);
  if (!block || block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('m1-fb-' + qid);
  if (fb) { fb.textContent = (correct ? '✅ ' : '❌ ') + feedback; fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect'); }
  scoresM1[qid] = correct;
  updateScoreM1();
}"""

OLD_M2_JS = """function answerM2(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM2[qid] = correct;
  updateScoreM2();
}"""

NEW_M2_JS = """function answerM2(el, qid, correct, feedback) {
  const block = document.getElementById('m2-' + qid);
  if (!block || block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('m2-fb-' + qid);
  if (fb) { fb.textContent = (correct ? '✅ ' : '❌ ') + feedback; fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect'); }
  scoresM2[qid] = correct;
  updateScoreM2();
}"""

OLD_M3_JS = """function answerM3(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM3[qid] = correct;
  const total = Object.values(scoresM3).filter(v => v === true).length;
  const answered = Object.values(scoresM3).filter(v => v !== null).length;
  document.getElementById('m3-score-display').innerHTML = total + ' <span>/ 6</span>';
  document.getElementById('m3-prog-label').textContent = answered + ' / 6';
  document.getElementById('m3-prog-fill').style.width = (answered / 6 * 100) + '%';
}"""

NEW_M3_JS = """function answerM3(el, qid, correct, feedback) {
  const block = document.getElementById('m3-' + qid);
  if (!block || block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('m3-fb-' + qid);
  if (fb) { fb.textContent = (correct ? '✅ ' : '❌ ') + feedback; fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect'); }
  scoresM3[qid] = correct;
  const total = Object.values(scoresM3).filter(v => v === true).length;
  const answered = Object.values(scoresM3).filter(v => v !== null).length;
  document.getElementById('m3-score-display').innerHTML = total + ' <span>/ 20</span>';
  document.getElementById('m3-prog-label').textContent = answered + ' / 20';
  document.getElementById('m3-prog-fill').style.width = (answered / 20 * 100) + '%';
}"""

OLD_M5_JS = """function answerM5(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM5[qid] = correct;
  const total = Object.values(scoresM5).filter(v => v === true).length;
  const answered = Object.values(scoresM5).filter(v => v !== null).length;
  document.getElementById('m5-score-display').innerHTML = total + ' <span>/ 5</span>';
  document.getElementById('m5-prog-label').textContent = answered + ' / 5';
  document.getElementById('m5-prog-fill').style.width = (answered / 5 * 100) + '%';
}"""

NEW_M5_JS = """function answerM5(el, qid, correct, feedback) {
  const block = document.getElementById('m5-' + qid);
  if (!block || block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('m5-fb-' + qid);
  if (fb) { fb.textContent = (correct ? '✅ ' : '❌ ') + feedback; fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect'); }
  scoresM5[qid] = correct;
  const total = Object.values(scoresM5).filter(v => v === true).length;
  const answered = Object.values(scoresM5).filter(v => v !== null).length;
  document.getElementById('m5-score-display').innerHTML = total + ' <span>/ 20</span>';
  document.getElementById('m5-prog-label').textContent = answered + ' / 20';
  document.getElementById('m5-prog-fill').style.width = (answered / 20 * 100) + '%';
}"""

assert OLD_M1_JS in html, "answerM1 not found"
assert OLD_M2_JS in html, "answerM2 not found"
assert OLD_M3_JS in html, "answerM3 not found"
assert OLD_M5_JS in html, "answerM5 not found"

html = html.replace(OLD_M1_JS, NEW_M1_JS)
html = html.replace(OLD_M2_JS, NEW_M2_JS)
html = html.replace(OLD_M3_JS, NEW_M3_JS)
html = html.replace(OLD_M5_JS, NEW_M5_JS)
print("JS functions fixed OK")

# ══════════════════════════════════════════════════════════════
# 2. UPDATE scores objects (20 keys)
# ══════════════════════════════════════════════════════════════
SCORES_20 = "{ q1:null, q2:null, q3:null, q4:null, q5:null, q6:null, q7:null, q8:null, q9:null, q10:null, q11:null, q12:null, q13:null, q14:null, q15:null, q16:null, q17:null, q18:null, q19:null, q20:null }"

html = html.replace(
    "let scoresM1 = { q1:null, q2:null, q3:null, q4:null, q5:null };",
    f"let scoresM1 = {SCORES_20};"
)
html = html.replace(
    "let scoresM2 = { q1:null, q2:null, q3:null, q4:null, q5:null };",
    f"let scoresM2 = {SCORES_20};"
)
html = html.replace(
    "let scoresM3 = { q1:null, q2:null, q3:null, q4:null, q5:null, q6:null };",
    f"let scoresM3 = {SCORES_20};"
)
html = html.replace(
    "let scoresM4 = { q1:null, q2:null, q3:null, q4:null, q5:null };",
    f"let scoresM4 = {SCORES_20};"
)
html = html.replace(
    "let scoresM5 = { q1:null, q2:null, q3:null, q4:null, q5:null };",
    f"let scoresM5 = {SCORES_20};"
)
print("Scores objects updated OK")

# ══════════════════════════════════════════════════════════════
# 3. UPDATE updateScoreM1 / M2 to show /20
# ══════════════════════════════════════════════════════════════
html = html.replace(
    "document.getElementById('m1-score-display').innerHTML = total + ' <span>/ 5</span>';\n  document.getElementById('m1-prog-label').textContent = answered + ' / 5';\n  document.getElementById('m1-prog-fill').style.width = (answered / 5 * 100) + '%';",
    "document.getElementById('m1-score-display').innerHTML = total + ' <span>/ 20</span>';\n  document.getElementById('m1-prog-label').textContent = answered + ' / 20';\n  document.getElementById('m1-prog-fill').style.width = (answered / 20 * 100) + '%';"
)
html = html.replace(
    "document.getElementById('m2-score-display').innerHTML = total + ' <span>/ 5</span>';\n  document.getElementById('m2-prog-label').textContent = answered + ' / 5';\n  document.getElementById('m2-prog-fill').style.width = (answered / 5 * 100) + '%';",
    "document.getElementById('m2-score-display').innerHTML = total + ' <span>/ 20</span>';\n  document.getElementById('m2-prog-label').textContent = answered + ' / 20';\n  document.getElementById('m2-prog-fill').style.width = (answered / 20 * 100) + '%';"
)
print("updateScore updated OK")

# ══════════════════════════════════════════════════════════════
# 4. UPDATE answerM4 to show /20
# ══════════════════════════════════════════════════════════════
html = html.replace(
    "var s4 = total + ' <span style=\"font-size:16px;color:#888\">/ 5</span>';\n  ['m4-score-display','m4-score-display-r'].forEach(function(id){var e=document.getElementById(id);if(e)e.innerHTML=s4;});\n  ['m4-prog-label','m4-prog-label-r'].forEach(function(id){var e=document.getElementById(id);if(e)e.textContent=answered+' / 5';});\n  var f4=document.getElementById('m4-prog-fill');if(f4)f4.style.width=(answered/5*100)+'%';",
    "var s4 = total + ' <span style=\"font-size:16px;color:#888\">/ 20</span>';\n  ['m4-score-display','m4-score-display-r'].forEach(function(id){var e=document.getElementById(id);if(e)e.innerHTML=s4;});\n  ['m4-prog-label','m4-prog-label-r'].forEach(function(id){var e=document.getElementById(id);if(e)e.textContent=answered+' / 20';});\n  var f4=document.getElementById('m4-prog-fill');if(f4)f4.style.width=(answered/20*100)+'%';"
)
print("answerM4 updated OK")

# ══════════════════════════════════════════════════════════════
# 5. UPDATE HTML score displays /5 → /20 and /6 → /20
# ══════════════════════════════════════════════════════════════
# M1 quiz tab header
html = html.replace(
    '<span class="meta-chip chip-red">5 questions</span>\n          <span class="meta-chip chip-gold">Feedback immédiat</span>\n        </div>\n      </div>\n\n      <div class="quiz-score-bar">\n        <h3>Votre score</h3>\n        <div class="score-display" id="m1-score-display">0 <span>/ 5</span></div>',
    '<span class="meta-chip chip-red">20 questions</span>\n          <span class="meta-chip chip-gold">Feedback immédiat</span>\n        </div>\n      </div>\n\n      <div class="quiz-score-bar">\n        <h3>Votre score</h3>\n        <div class="score-display" id="m1-score-display">0 <span>/ 20</span></div>'
)
# M1 results tab
html = html.replace(
    'id="m1-score-display">0 <span style="font-size:18px;color:#888">/ 5</span>',
    'id="m1-score-display">0 <span style="font-size:18px;color:#888">/ 20</span>'
)
html = html.replace(
    'id="m1-prog-label">0 / 5 questions</div>',
    'id="m1-prog-label">0 / 20 questions</div>'
)
# M2
html = html.replace(
    '<span class="meta-chip chip-red">5 questions</span>\n          <span class="meta-chip chip-gold">Feedback immédiat</span>\n        </div>\n      </div>\n      <div class="quiz-score-bar">\n        <h3>Votre score</h3>\n        <div class="score-display" id="m2-score-display">0 <span>/ 5</span></div>',
    '<span class="meta-chip chip-red">20 questions</span>\n          <span class="meta-chip chip-gold">Feedback immédiat</span>\n        </div>\n      </div>\n      <div class="quiz-score-bar">\n        <h3>Votre score</h3>\n        <div class="score-display" id="m2-score-display">0 <span>/ 20</span></div>'
)
html = html.replace(
    'id="m2-score-display">0 <span style="font-size:18px;color:#888">/ 5</span>',
    'id="m2-score-display">0 <span style="font-size:18px;color:#888">/ 20</span>'
)
html = html.replace(
    'id="m2-prog-label">0 / 5 questions</div>',
    'id="m2-prog-label">0 / 20 questions</div>'
)
# M3
html = html.replace(
    '<span class="meta-chip chip-red">6 questions</span>\n          <span class="meta-chip chip-gold">Feedback immédiat</span>\n        </div>\n      </div>\n      <div class="quiz-score-bar">\n        <h3>Votre score</h3>\n        <div class="score-display" id="m3-score-display">0 <span>/ 6</span></div>',
    '<span class="meta-chip chip-red">20 questions</span>\n          <span class="meta-chip chip-gold">Feedback immédiat</span>\n        </div>\n      </div>\n      <div class="quiz-score-bar">\n        <h3>Votre score</h3>\n        <div class="score-display" id="m3-score-display">0 <span>/ 20</span></div>'
)
html = html.replace(
    'id="m3-score-display">0 <span style="font-size:18px;color:#888">/ 5</span>',
    'id="m3-score-display">0 <span style="font-size:18px;color:#888">/ 20</span>'
)
html = html.replace(
    'id="m3-prog-label">0 / 5 questions</div>',
    'id="m3-prog-label">0 / 20 questions</div>'
)
# M4
html = html.replace(
    '<h3>✅ Quiz — Module OM Business</h3>\n        <p>5 questions · Basé sur le Brief OM Business V9</p>',
    '<h3>✅ Quiz — Module OM Business</h3>\n        <p>20 questions · Basé sur le Brief OM Business V9</p>'
)
html = html.replace(
    'id="m4-score-display">0 <span style="font-size:16px;color:#888">/ 5</span>',
    'id="m4-score-display">0 <span style="font-size:16px;color:#888">/ 20</span>'
)
html = html.replace(
    'id="m4-prog-label">0 / 5 questions</div>',
    'id="m4-prog-label">0 / 20 questions</div>'
)
html = html.replace(
    'id="m4-score-display-r">0 <span style="font-size:18px;color:#888">/ 5</span>',
    'id="m4-score-display-r">0 <span style="font-size:18px;color:#888">/ 20</span>'
)
html = html.replace(
    'id="m4-prog-label-r">0 / 5 questions</div>',
    'id="m4-prog-label-r">0 / 20 questions</div>'
)
# M5
html = html.replace(
    '<span class="meta-chip chip-red">5 questions</span>\n          <span class="meta-chip chip-gold">Feedback immédiat</span>\n        </div>\n      </div>\n      <div class="quiz-score-bar">\n        <h3>Votre score</h3>\n        <div class="score-display" id="m5-score-display">0 <span>/ 5</span></div>',
    '<span class="meta-chip chip-red">20 questions</span>\n          <span class="meta-chip chip-gold">Feedback immédiat</span>\n        </div>\n      </div>\n      <div class="quiz-score-bar">\n        <h3>Votre score</h3>\n        <div class="score-display" id="m5-score-display">0 <span>/ 20</span></div>'
)
html = html.replace(
    'id="m5-score-display">0 <span style="font-size:18px;color:#888">/ 5</span>',
    'id="m5-score-display">0 <span style="font-size:18px;color:#888">/ 20</span>'
)
html = html.replace(
    'id="m5-prog-label">0 / 5 questions</div>',
    'id="m5-prog-label">0 / 20 questions</div>'
)
print("HTML displays updated OK")

# Also update question numbers in existing questions
for m, total_old, total_new in [('m1','05','20'),('m2','05','20'),('m3','06','20'),('m5','05','20')]:
    for q in range(1, int(total_old)+1):
        html = html.replace(
            f'<div class="quiz-q-num">Question {q:02d} / {total_old}</div>',
            f'<div class="quiz-q-num">Question {q:02d} / 20</div>'
        )
# M4 existing questions
for q in range(1, 6):
    html = html.replace(
        f'<div class="quiz-q-num">Question {q:02d} / 05</div>\n          <div class="quiz-q-text">',
        f'<div class="quiz-q-num">Question {q:02d} / 20</div>\n          <div class="quiz-q-text">'
    )
print("Question numbers updated OK")

# ══════════════════════════════════════════════════════════════
# 6. BUILD new questions HTML
# ══════════════════════════════════════════════════════════════

def q_block(module, qnum, total, text, options):
    """
    options: list of (letter, answer_text, is_correct, feedback)
    """
    opts_html = ""
    for letter, ans, correct, fb in options:
        c_str = "true" if correct else "false"
        if module == "m4":
            qid_str = f"m4-q{qnum}"
            fn = f"answerM4(this,'{qid_str}',{c_str},'{fb}')"
            fb_id = f"fb-m4-q{qnum}"
            block_id = f"m4-q{qnum}"
        else:
            qid_str = f"q{qnum}"
            fn = f"answer{module.upper()}(this,'{qid_str}',{c_str},'{fb}')"
            fb_id = f"{module}-fb-q{qnum}"
            block_id = f"{module}-q{qnum}"
        opts_html += f'\n            <div class="quiz-option" onclick="{fn}"><span class="option-letter">{letter}</span> {ans}</div>'

    if module == "m4":
        fb_div = f'<div class="quiz-feedback" id="fb-m4-q{qnum}"></div>'
        bid = f"m4-q{qnum}"
    else:
        fb_div = f'<div class="quiz-feedback" id="{module}-fb-q{qnum}"></div>'
        bid = f"{module}-q{qnum}"

    return f"""
        <div class="quiz-question-block" id="{bid}">
          <div class="quiz-q-num">Question {qnum:02d} / {total}</div>
          <div class="quiz-q-text">{text}</div>
          <div class="quiz-options">{opts_html}
          </div>
          {fb_div}
        </div>"""

# ─── M1 nouvelles questions q6-q20 ───────────────────────────
m1_new = ""
m1_questions = [
    (6, "Lors d'un premier appel infructueux, combien de tentatives au total l'agent doit-il effectuer avant de classer le dossier ?", [
        ("A","1 tentative uniquement",False,"3 tentatives au total sont requises avant classement."),
        ("B","2 tentatives",False,"3 tentatives au total (la 1ère + 2 supplémentaires) sont nécessaires."),
        ("C","3 tentatives au total",True,"Correct ! L'agent effectue 3 tentatives d'appel avant de classer le dossier."),
        ("D","5 tentatives",False,"5 tentatives dépassent le protocole. 3 sont suffisantes."),
    ]),
    (7, "Quel délai minimum est recommandé entre deux tentatives d'appel sur un même dossier ?", [
        ("A","15 minutes",False,"15 minutes est insuffisant. Le délai recommandé est 2 heures."),
        ("B","30 minutes",False,"30 minutes est insuffisant pour laisser le temps à l'entrepreneur."),
        ("C","2 heures",True,"Correct ! Un délai de 2 heures minimum est recommandé entre deux tentatives d'appel."),
        ("D","24 heures",False,"24 heures est trop long entre les tentatives sur un même dossier."),
    ]),
    (8, "Que signifie le statut 'Refus ferme' dans Connectel ?", [
        ("A","L'entrepreneur a raccroché sans répondre",False,"Raccrocher correspond à un appel sans réponse, pas à un refus ferme."),
        ("B","L'entrepreneur refuse définitivement toute mise à jour",True,"Correct ! 'Refus ferme' signifie que l'entrepreneur refuse catégoriquement — le dossier est classé."),
        ("C","Le numéro de téléphone est invalide",False,"Numéro invalide est un statut technique différent du refus ferme."),
        ("D","Le rendez-vous n'est pas confirmé",False,"RDV non confirmé est un statut distinct. Refus ferme = refus définitif."),
    ]),
    (9, "Quel document l'entrepreneur doit-il présenter lors du rendez-vous terrain pour valider son dossier ID30 ?", [
        ("A","Passeport biométrique uniquement",False,"Le passeport seul n'est pas suffisant. La CNI est le document principal."),
        ("B","CNI ou attestation d'identité valide",True,"Correct ! La CNI (ou attestation d'identité valide) est le document requis lors du rendez-vous terrain."),
        ("C","Carte de séjour",False,"La carte de séjour n'est pas le document principal requis pour ID30."),
        ("D","Permis de conduire",False,"Le permis de conduire n'est pas un document d'identité accepté pour ID30."),
    ]),
    (10, "La Carte Entreprenant est remise à l'entrepreneur dans quel délai après validation du dossier ?", [
        ("A","Immédiatement lors du rendez-vous terrain",True,"Correct ! La carte est imprimée sur place via le FAMOCO PX400 et remise immédiatement."),
        ("B","Sous 48 heures par courrier",False,"La carte est remise immédiatement sur le terrain, pas envoyée par courrier."),
        ("C","Sous 7 jours ouvrés",False,"7 jours est beaucoup trop long. La carte est imprimée sur place."),
        ("D","Après validation du Ministère",False,"La validation du Ministère est en amont — la carte est remise directement lors du RDV."),
    ]),
    (11, "Quel est l'objectif principal du projet ID30 en Côte d'Ivoire ?", [
        ("A","Développer le réseau commercial d'Orange CI",False,"Orange CI est un partenaire, mais l'objectif premier est la formalisation du secteur informel."),
        ("B","Formaliser les entrepreneurs du secteur informel",True,"Correct ! ID30 vise à identifier et formaliser les entrepreneurs du secteur informel dans 30 grandes villes."),
        ("C","Collecter les impôts des commerçants",False,"ID30 n'est pas un programme de collecte d'impôts."),
        ("D","Créer de nouveaux emplois dans l'administration",False,"ID30 formalise l'existant — ce n'est pas un programme de création d'emplois."),
    ]),
    (12, "Comment l'agent Call Center doit-il se présenter en début d'appel ?", [
        ("A","Par son prénom uniquement",False,"Se présenter par le prénom seul est insuffisant et peu professionnel."),
        ("B","En donnant son nom, prénom et l'entreprise MAFA Holding",True,"Correct ! L'agent se présente avec son nom complet et au nom de MAFA Holding mandatée par le Ministère."),
        ("C","Sans se présenter, directement dans le sujet",False,"Ne pas se présenter est contraire au protocole d'appel professionnel."),
        ("D","Au nom du Ministère uniquement",False,"L'agent représente MAFA Holding, mandatée par le Ministère — les deux doivent être mentionnés."),
    ]),
    (13, "Quel est le rôle du superviseur Call Center par rapport aux agents ?", [
        ("A","Prendre tous les appels difficiles à la place des agents",False,"Le superviseur encadre — il n'est pas là pour remplacer systématiquement les agents."),
        ("B","Valider les dossiers directement en Back Office",False,"La validation en Back Office est une fonction distincte du Call Center."),
        ("C","Encadrer, suivre la performance et soutenir les agents",True,"Correct ! Le superviseur encadre son équipe, suit les KPIs et intervient en support si nécessaire."),
        ("D","Gérer uniquement les impressions de cartes",False,"L'impression de cartes est du ressort de l'agent terrain, pas du superviseur Call Center."),
    ]),
    (14, "Que fait l'agent si l'entrepreneur demande un rendez-vous dans une zone non encore couverte ?", [
        ("A","Refuse la demande et clôture le dossier",False,"Refuser sans alternative est contraire au protocole. La demande doit être signalée."),
        ("B","Transfère directement au superviseur sans rien noter",False,"Transférer sans documentation ne permet pas de planifier la couverture."),
        ("C","Note la demande et la signale pour planification de couverture",True,"Correct ! L'agent note et signale la demande afin que la couverture terrain puisse être planifiée."),
        ("D","Propose un RDV dans la ville la plus proche",False,"Proposer une autre ville sans accord préalable n'est pas le protocole."),
    ]),
    (15, "Quelle information est prioritaire à vérifier lors de la prise de rendez-vous ?", [
        ("A","La couleur préférée de la Carte Entreprenant",False,"La couleur de la carte n'est pas un critère de prise de RDV."),
        ("B","Le montant du chiffre d'affaires de l'entrepreneur",False,"Le CA est une donnée KYB collectée sur le terrain, pas lors de la prise de RDV."),
        ("C","La validité du numéro et la disponibilité à l'heure proposée",True,"Correct ! Vérifier que le numéro est joignable et que l'entrepreneur est disponible à l'heure proposée est prioritaire."),
        ("D","L'adresse email de l'entrepreneur",False,"L'email n'est pas requis pour la prise de RDV Call Center."),
    ]),
    (16, "Comment l'agent doit-il traiter un entrepreneur mécontent ou agressif au téléphone ?", [
        ("A","Raccrocher immédiatement",False,"Raccrocher est une escalade — l'agent doit d'abord tenter de désamorcer."),
        ("B","Rester calme, écouter et proposer un rappel ultérieur",True,"Correct ! Le protocole impose de rester calme, d'écouter les doléances et de proposer un rappel si nécessaire."),
        ("C","Transférer systématiquement au superviseur dès le 1er signe",False,"Le transfert au superviseur n'est pas automatique — l'agent tente d'abord de gérer la situation."),
        ("D","Ignorer les remarques et continuer le script",False,"Ignorer les remarques aggraverait la situation. L'écoute active est essentielle."),
    ]),
    (17, "Dans Connectel, qu'indique le statut 'RDV confirmé' ?", [
        ("A","Le dossier est entièrement validé et archivé",False,"Validé et archivé correspond à un statut post-visite, pas à la confirmation de RDV."),
        ("B","L'entrepreneur a accepté la date et l'heure du rendez-vous",True,"Correct ! 'RDV confirmé' signifie que l'entrepreneur a accepté le créneau proposé."),
        ("C","La Carte Entreprenant a été imprimée",False,"L'impression de la carte se fait lors de la visite terrain, pas à la confirmation du RDV."),
        ("D","L'agent a transmis le dossier au Back Office",False,"La transmission au Back Office est une étape ultérieure, après la visite terrain."),
    ]),
    (18, "Quelle langue est principalement utilisée dans les appels du Call Center ID30 ?", [
        ("A","Anglais uniquement",False,"L'anglais n'est pas la langue principale des appels ID30 en Côte d'Ivoire."),
        ("B","Dioula uniquement",False,"Le Dioula peut être utilisé, mais il n'est pas la seule langue."),
        ("C","Français et langues locales selon l'entrepreneur",True,"Correct ! Le français est la langue principale, mais l'agent peut adapter avec les langues locales (Dioula, Baoulé, etc.)."),
        ("D","Espagnol",False,"L'espagnol n'est pas utilisé dans le projet ID30 en Côte d'Ivoire."),
    ]),
    (19, "Que doit faire l'agent si le numéro enregistré dans Connectel est erroné ?", [
        ("A","Clôturer le dossier immédiatement",False,"Clôturer un dossier pour numéro erroné serait une perte de données précieuse."),
        ("B","Mettre à jour le numéro dans Connectel et continuer",False,"L'agent ne doit pas modifier directement les données — il doit signaler."),
        ("C","Signaler au Back Office pour correction et mise à jour",True,"Correct ! Toute correction de données doit passer par le Back Office pour garder la traçabilité."),
        ("D","Appeler un autre entrepreneur en attendant",False,"Sauter un dossier sans résolution n'est pas la procédure correcte."),
    ]),
    (20, "Quel comportement est strictement interdit pendant les appels du Call Center ID30 ?", [
        ("A","Prendre des notes sur le dossier",False,"Prendre des notes est encouragé pendant les appels."),
        ("B","Utiliser un script d'appel",False,"L'utilisation d'un script est recommandée pour maintenir la qualité."),
        ("C","Promouvoir d'autres offres commerciales non liées à ID30",True,"Correct ! Les agents doivent rester focalisés sur ID30 — promouvoir d'autres offres est strictement interdit."),
        ("D","Confirmer le rendez-vous à voix haute",False,"Confirmer le RDV à voix haute est une bonne pratique pour éviter les malentendus."),
    ]),
]
for qnum, text, opts in m1_questions:
    m1_new += q_block("m1", qnum, 20, text, opts)

# ─── M2 nouvelles questions q6-q20 ───────────────────────────
m2_new = ""
m2_questions = [
    (6, "Quel est le délai maximum pour traiter un dossier reçu en Back Office ?", [
        ("A","24 heures",False,"24h est le délai de certaines alertes urgentes, mais le délai standard Back Office est 48h."),
        ("B","48 heures",True,"Correct ! Le Back Office dispose de 48 heures maximum pour traiter un dossier reçu."),
        ("C","72 heures",False,"72h dépasse le délai standard Back Office de 48h."),
        ("D","1 semaine",False,"Une semaine est bien trop long — le délai maximum est 48h."),
    ]),
    (7, "Que désigne le terme 'Proof of Life' dans le processus de vérification ?", [
        ("A","Une attestation médicale de l'entrepreneur",False,"Le Proof of Life n'est pas une attestation médicale."),
        ("B","Une preuve biométrique que l'entrepreneur est bien présent lors de la capture",True,"Correct ! Le Proof of Life est un score biométrique confirmant la présence et la vivacité de la personne lors de la capture."),
        ("C","Une lettre de témoignage d'un voisin",False,"Une lettre de témoignage n'est pas ce que désigne le Proof of Life."),
        ("D","Un test de personnalité de l'entrepreneur",False,"Le Proof of Life est une mesure biométrique, pas un test psychologique."),
    ]),
    (8, "Que doit vérifier le Back Office concernant les coordonnées GPS du dossier ?", [
        ("A","Que le lieu se situe impérativement au centre-ville",False,"La localisation n'est pas limitée au centre-ville — elle doit correspondre au lieu déclaré."),
        ("B","Que les coordonnées correspondent réellement au lieu d'activité déclaré",True,"Correct ! Le Back Office vérifie la cohérence entre les coordonnées GPS et l'adresse d'activité déclarée."),
        ("C","Que le GPS du FAMOCO est activé",False,"L'activation du GPS est vérifiée sur le terrain, pas en Back Office."),
        ("D","La distance entre le lieu et Abidjan",False,"La distance par rapport à Abidjan n'est pas un critère de validation Back Office."),
    ]),
    (9, "Quel statut est attribué à un dossier dont les images de documents sont floues ou illisibles ?", [
        ("A","Validé avec réserve",False,"Aucun dossier avec des images illisibles ne peut être validé, même avec réserve."),
        ("B","Mis en attente",False,"Un dossier avec images illisibles n'est pas mis en attente — il est rejeté."),
        ("C","Rejeté — retour terrain requis",True,"Correct ! Des images floues ou illisibles entraînent un rejet avec demande de nouvelle visite terrain."),
        ("D","Archivé automatiquement",False,"L'archivage automatique n'existe pas pour les dossiers incomplets — ils sont rejetés."),
    ]),
    (10, "Que contient typiquement la fiche de visite complétée par l'agent terrain ?", [
        ("A","Seulement les photos biométriques",False,"La fiche de visite contient bien plus que des photos — elle est complète."),
        ("B","Les coordonnées GPS, informations KYC/KYB et photos",True,"Correct ! La fiche de visite regroupe les coordonnées GPS, les informations KYC (identité) et KYB (activité) ainsi que les photos."),
        ("C","Le montant du solde Orange Money de l'entrepreneur",False,"Le solde Orange Money n'est pas collecté dans la fiche de visite."),
        ("D","Le code QR uniquement",False,"Le code QR est généré après validation — il ne fait pas partie de la fiche de visite initiale."),
    ]),
    (11, "En cas de dossier doublon (même entrepreneur enregistré deux fois), que fait le Back Office ?", [
        ("A","Valide les deux dossiers",False,"Valider deux dossiers identiques créerait des données dupliquées — c'est interdit."),
        ("B","Conserve le plus récent et archive l'ancien après vérification",True,"Correct ! Le Back Office conserve le dossier le plus complet/récent et archive l'ancien après vérification."),
        ("C","Supprime les deux dossiers",False,"Supprimer les deux entraînerait une perte de données. L'un est conservé."),
        ("D","Transfère au Call Center pour re-contact",False,"La gestion des doublons est une tâche Back Office, pas Call Center."),
    ]),
    (12, "Quel champ du formulaire KYB concerne l'activité principale de l'entrepreneur ?", [
        ("A","Nom complet de l'entrepreneur",False,"Le nom complet appartient aux données KYC (identité personnelle), pas KYB."),
        ("B","Numéro de la CNI",False,"Le numéro CNI est une donnée KYC, pas KYB."),
        ("C","Secteur d'activité",True,"Correct ! Le secteur d'activité (commerce, artisanat, etc.) est la donnée KYB principale."),
        ("D","Adresse email personnelle",False,"L'adresse email personnelle n'est pas un champ KYB principal."),
    ]),
    (13, "Quel est le score minimum Proof of Life accepté par le système (seuil minimal, pas recommandé) ?", [
        ("A","40",False,"40 est en dessous du seuil minimal — le dossier serait automatiquement rejeté."),
        ("B","50",False,"50 est encore en dessous du seuil minimal accepté qui est de 60."),
        ("C","60",True,"Correct ! 60 est le score minimum accepté par le système (le score recommandé est 70)."),
        ("D","70",False,"70 est le score recommandé, mais pas le minimum absolu — le seuil minimal est 60."),
    ]),
    (14, "Lorsqu'un dossier est validé par le Back Office, quelle étape suit immédiatement ?", [
        ("A","Envoi automatique au Ministère du Commerce",False,"L'envoi au Ministère est une étape différente, pas immédiatement après la validation Back Office."),
        ("B","Impression de la Carte Entreprenant par l'agent terrain",True,"Correct ! Après validation Back Office, la Carte Entreprenant peut être imprimée par l'agent terrain via le FAMOCO PX400."),
        ("C","Appel de confirmation au superviseur",False,"Un appel de confirmation n'est pas l'étape immédiatement suivante."),
        ("D","Paiement Orange Money de frais",False,"Il n'y a pas de paiement Orange Money lié à la validation Back Office."),
    ]),
    (15, "Comment le Back Office signale-t-il un dossier nécessitant une nouvelle visite terrain ?", [
        ("A","Par téléphone au superviseur terrain",False,"Le téléphone n'est pas le canal officiel pour signaler un retour terrain."),
        ("B","Par email à l'agent concerné",False,"L'email n'est pas le canal de signalement officiel utilisé dans ce processus."),
        ("C","Via le statut 'Rejeté — Retour terrain' dans le système",True,"Correct ! Le Back Office applique le statut officiel dans le système, ce qui déclenche automatiquement l'action terrain."),
        ("D","Par courrier postal au chef d'équipe",False,"Le courrier postal n'est pas utilisé dans ce processus numérique."),
    ]),
    (16, "Le Back Office peut-il modifier directement les informations KYC d'un dossier ?", [
        ("A","Oui, librement sans restriction",False,"Modifier directement les KYC sans traçabilité serait une violation des protocoles."),
        ("B","Non, toute correction nécessite une nouvelle visite terrain",True,"Correct ! Les informations KYC ne peuvent être corrigées que via une nouvelle visite terrain — garantissant la fiabilité des données."),
        ("C","Oui, mais uniquement avec accord du superviseur",False,"Même avec l'accord du superviseur, une correction directe n'est pas autorisée sans nouvelle visite."),
        ("D","Non, jamais même en cas d'erreur évidente",False,"Une correction est possible, mais via le processus officiel (nouvelle visite), pas directement."),
    ]),
    (17, "Combien de photos minimum sont requises dans un dossier pour validation Back Office ?", [
        ("A","1 photo (portrait)",False,"Une seule photo est insuffisante. Le minimum requis est 3."),
        ("B","2 photos",False,"2 photos ne suffisent pas. 3 photos minimum sont requises."),
        ("C","3 photos minimum",True,"Correct ! Au minimum 3 photos sont requises : portrait, CNI recto/verso et lieu d'activité."),
        ("D","5 photos",False,"5 photos est la cible recommandée, mais le minimum absolu est 3."),
    ]),
    (18, "Quel est le rôle de l'inspecteur par rapport au travail du Back Office ?", [
        ("A","Remplacer le Back Office pour les cas complexes",False,"L'inspecteur ne remplace pas le Back Office — ce sont deux fonctions complémentaires."),
        ("B","Valider physiquement sur le terrain ce que le Back Office vérifie à distance",True,"Correct ! L'inspecteur effectue la vérification terrain (physique) qui complète la vérification documentaire du Back Office."),
        ("C","Imprimer les cartes à la place des agents",False,"L'impression de cartes n'est pas le rôle de l'inspecteur."),
        ("D","Gérer les accès à la plateforme Connectel",False,"La gestion des accès Connectel relève de l'administrateur, pas de l'inspecteur."),
    ]),
    (19, "Quelle est la résolution minimum acceptable pour les photos de documents scannés ?", [
        ("A","72 DPI",False,"72 DPI est la résolution d'affichage écran — insuffisant pour les documents officiels."),
        ("B","150 DPI",False,"150 DPI est trop faible pour une lecture correcte des documents."),
        ("C","300 DPI",True,"Correct ! 300 DPI est la résolution minimum requise pour que les documents soient lisibles et exploitables."),
        ("D","600 DPI",False,"600 DPI est recommandé pour l'archivage haute qualité, mais 300 DPI est le minimum."),
    ]),
    (20, "Que doit faire le Back Office si les données GPS et les données déclarées sont très éloignées géographiquement ?", [
        ("A","Valider quand même si les photos sont bonnes",False,"Des données GPS incohérentes invalident le dossier, même si les photos sont correctes."),
        ("B","Rejeter le dossier et demander une nouvelle visite avec correction GPS",True,"Correct ! Une incohérence GPS importante entraîne le rejet du dossier — une nouvelle visite est requise pour corriger les coordonnées."),
        ("C","Modifier manuellement les coordonnées GPS en Back Office",False,"Modifier manuellement les GPS sans vérification terrain est interdit."),
        ("D","Ignorer l'écart si inférieur à 10 km",False,"Tout écart significatif doit être investigué — il n'y a pas de tolérance de 10 km."),
    ]),
]
for qnum, text, opts in m2_questions:
    m2_new += q_block("m2", qnum, 20, text, opts)

# ─── M3 nouvelles questions q7-q20 ───────────────────────────
m3_new = ""
m3_questions = [
    (7, "Combien de visites d'inspection minimum par jour est recommandé pour un inspecteur ?", [
        ("A","5 visites",False,"5 visites est en dessous de l'objectif. La cible recommandée est 10 visites/jour."),
        ("B","8 visites",False,"8 visites n'atteint pas l'objectif quotidien de 10 visites minimum."),
        ("C","10 visites",True,"Correct ! L'objectif minimum est de 10 visites d'inspection par jour."),
        ("D","15 visites",False,"15 visites est un objectif premium — la cible minimum recommandée est 10."),
    ]),
    (8, "Quel outil l'inspecteur utilise-t-il pour scanner le QR Code sur la Carte Entreprenant ?", [
        ("A","Un lecteur code-barres laser de bureau",False,"Un lecteur laser de bureau n'est pas utilisé sur le terrain par l'inspecteur."),
        ("B","L'application mobile Inspector Orange sur smartphone",True,"Correct ! L'application mobile Inspector Orange est l'outil dédié pour scanner les QR Codes terrain."),
        ("C","Un scanner de documents portable",False,"Un scanner de documents portable n'est pas l'outil utilisé pour cette tâche."),
        ("D","L'appareil FAMOCO PX400",False,"Le FAMOCO PX400 est utilisé par les agents terrain pour l'enrôlement, pas par les inspecteurs pour le contrôle."),
    ]),
    (9, "Que vérifie principalement l'inspecteur lors d'une visite de contrôle ?", [
        ("A","Le chiffre d'affaires mensuel de l'entrepreneur",False,"Le CA n'est pas le principal point de contrôle de l'inspecteur."),
        ("B","La concordance entre la Carte Entreprenant et la réalité terrain",True,"Correct ! L'inspecteur vérifie que les informations de la carte correspondent bien à la réalité observée sur le terrain."),
        ("C","La qualité du réseau Orange dans la zone",False,"La qualité réseau n'est pas le rôle de l'inspecteur."),
        ("D","L'état du compte Orange Money de l'entrepreneur",False,"Le compte Orange Money n'est pas directement contrôlé lors d'une visite d'inspection ID30."),
    ]),
    (10, "Que doit faire l'inspecteur s'il constate que l'activité déclarée ne correspond pas à la réalité terrain ?", [
        ("A","Ignorer l'écart et valider quand même",False,"Ignorer une non-conformité est une faute professionnelle grave."),
        ("B","Corriger lui-même les données dans l'application",False,"L'inspecteur ne corrige pas directement les données — il signale."),
        ("C","Signaler comme non-conforme et remonter au superviseur",True,"Correct ! L'inspecteur marque le dossier comme non-conforme et remonte l'information au superviseur pour action."),
        ("D","Retirer physiquement la Carte Entreprenant au commerçant",False,"L'inspecteur ne peut pas retirer la carte — il signale et le superviseur décide de la suite."),
    ]),
    (11, "Le QR Code sur la Carte Entreprenant renvoie vers quelles informations ?", [
        ("A","Le solde du compte Orange Money du marchand",False,"Le QR Code ne donne pas accès au solde — c'est une information confidentielle."),
        ("B","La fiche d'identité officielle de l'entreprenant",True,"Correct ! Le QR Code renvoie vers la fiche officielle de l'entreprenant (nom, activité, localisation, statut)."),
        ("C","La liste des prix Orange disponibles",False,"Les prix Orange ne sont pas liés au QR Code de la Carte Entreprenant."),
        ("D","La liste des agents ayant traité le dossier",False,"L'historique des agents n'est pas accessible via le QR Code public."),
    ]),
    (12, "Comment l'inspecteur documente-t-il sa visite terrain dans l'application ?", [
        ("A","Par un appel téléphonique au superviseur",False,"Un appel téléphonique seul n'est pas suffisant pour documenter une visite officielle."),
        ("B","Via un rapport papier envoyé au bureau",False,"Les rapports papier ne sont pas utilisés — le processus est entièrement numérique."),
        ("C","Via l'application : photos, GPS, statut de conformité",True,"Correct ! L'inspecteur documente via l'application mobile : photos du lieu, coordonnées GPS et statut de conformité."),
        ("D","Par email avec photos en pièce jointe",False,"L'email n'est pas le canal officiel de documentation des visites inspection."),
    ]),
    (13, "Quelle action est absolument interdite pour un inspecteur lors d'une visite terrain ?", [
        ("A","Scanner le QR Code de la carte",False,"Scanner le QR Code est la tâche principale de l'inspecteur."),
        ("B","Accepter de l'argent ou des cadeaux de l'entrepreneur",True,"Correct ! Accepter tout avantage financier ou cadeau est strictement interdit — c'est une faute grave."),
        ("C","Prendre des photos du lieu d'activité",False,"Prendre des photos fait partie intégrante du processus d'inspection."),
        ("D","Remplir le rapport de visite",False,"Remplir le rapport est obligatoire après chaque visite."),
    ]),
    (14, "En cas d'entrepreneur absent lors de la visite de contrôle, l'inspecteur doit :", [
        ("A","Clôturer le dossier comme conforme",False,"Clôturer comme conforme sans rencontrer l'entrepreneur est une erreur grave."),
        ("B","Attendre sur place aussi longtemps que nécessaire",False,"Attendre indéfiniment n'est pas la procédure — une absence doit être gérée autrement."),
        ("C","Reprogrammer la visite et signaler l'absence",True,"Correct ! L'inspecteur reprogramme la visite et signale l'absence dans l'application pour suivi."),
        ("D","Contacter directement le Call Center",False,"Contacter le Call Center n'est pas la procédure — l'inspecteur remonte à son superviseur."),
    ]),
    (15, "Quel est le délai maximum pour soumettre son rapport après une visite d'inspection ?", [
        ("A","6 heures après la visite",False,"6 heures est trop court — le délai accordé est de 24 heures."),
        ("B","24 heures après la visite",True,"Correct ! Le rapport d'inspection doit être soumis dans les 24 heures suivant la visite."),
        ("C","48 heures",False,"48 heures dépasse le délai imparti. Le rapport doit être soumis sous 24h."),
        ("D","En fin de semaine",False,"Attendre la fin de semaine est contraire aux exigences de délai — 24h maximum."),
    ]),
    (16, "Que signifie le statut 'Conforme' attribué par l'inspecteur à un dossier ?", [
        ("A","La Carte Entreprenant a été physiquement remise",False,"La remise de la carte est une étape antérieure à l'inspection."),
        ("B","L'entrepreneur et son activité correspondent exactement aux données enregistrées",True,"Correct ! 'Conforme' signifie que tout correspond : identité, activité, localisation — cohérence totale avec le dossier."),
        ("C","Le paiement Orange Money a été effectué",False,"Un paiement Orange Money n'est pas lié au statut de conformité d'inspection."),
        ("D","Le dossier est archivé définitivement",False,"L'archivage est une étape distincte — 'Conforme' est un statut de visite, pas d'archivage."),
    ]),
    (17, "Combien de points de contrôle minimum l'inspecteur vérifie-t-il lors d'une visite ?", [
        ("A","3 points",False,"3 points sont insuffisants. La fiche de visite comporte 5 points minimum à vérifier."),
        ("B","5 points minimum",True,"Correct ! L'inspecteur vérifie au minimum 5 points : identité, carte, activité, localisation, photos."),
        ("C","7 points",False,"7 points est le niveau avancé — le minimum requis est 5 points."),
        ("D","10 points",False,"10 points est la vérification exhaustive. Le minimum est 5 points."),
    ]),
    (18, "L'inspecteur peut-il modifier directement les données d'un dossier dans l'application ?", [
        ("A","Oui, il a accès complet en modification",False,"L'inspecteur n'a pas accès en modification — il signale uniquement."),
        ("B","Non, il signale uniquement les non-conformités",True,"Correct ! L'inspecteur est en lecture + signalement uniquement. Les modifications sont traitées par le Back Office après retour terrain."),
        ("C","Oui, mais seulement avec la confirmation du superviseur",False,"Même avec confirmation, l'inspecteur ne modifie pas directement les données."),
        ("D","Oui, uniquement les coordonnées GPS",False,"Les coordonnées GPS ne peuvent pas être modifiées directement par l'inspecteur."),
    ]),
    (19, "Que doit faire l'inspecteur si le QR Code imprimé sur la Carte Entreprenant est illisible ?", [
        ("A","Valider quand même et noter dans le rapport",False,"Valider avec un QR Code illisible empêche tout contrôle futur — c'est inacceptable."),
        ("B","Ignorer et passer à la prochaine visite",False,"Ignorer un défaut technique est une faute dans le processus qualité."),
        ("C","Signaler comme défaut technique et demander le remplacement de la carte",True,"Correct ! L'inspecteur signale le défaut dans l'application et déclenche le remplacement de la carte."),
        ("D","Appeler directement l'imprimante FAMOCO",False,"L'inspecteur ne gère pas l'impression — il signale le défaut via l'application."),
    ]),
    (20, "Quel est le principal indicateur de performance d'un inspecteur ?", [
        ("A","Le nombre d'entrepreneurs signalés comme non-conformes",False,"Maximiser les non-conformités n'est pas un indicateur de performance — c'est la conformité globale."),
        ("B","Le taux de conformité des visites effectuées",True,"Correct ! Le principal KPI d'un inspecteur est son taux de conformité : proportion de dossiers vérifiés et validés dans les délais."),
        ("C","Le nombre de kilomètres parcourus par jour",False,"La distance parcourue n'est pas un indicateur de performance pertinent."),
        ("D","La vitesse de scan des QR Codes",False,"La vitesse de scan n'est pas un KPI officiel de l'inspecteur."),
    ]),
]
for qnum, text, opts in m3_questions:
    m3_new += q_block("m3", qnum, 20, text, opts)

# ─── M4 nouvelles questions q6-q20 ───────────────────────────
m4_new = ""
m4_questions = [
    (6, "Quel profil OM Business convient à une entreprise avec un CA annuel supérieur à 400 millions FCFA et plus de 10 employés ?", [
        ("A","OM Business Essentiel",False,"L'Essentiel cible les micro-entreprises avec CA inférieur à 150 000 FCFA/an."),
        ("B","OM Business Classique",False,"Le Classique cible les petits commerces formels avec CA entre 150 000 et 400 millions FCFA/an."),
        ("C","OM Business Premium",True,"Correct ! Le Premium est réservé aux grandes entreprises avec CA > 400 millions FCFA/an et plus de 10 employés."),
        ("D","OM Business Pro",False,"Ce profil n'existe pas dans la gamme OM Business Orange CI."),
    ]),
    (7, "Quel est le plafond mensuel d'encaissement gratuit pour un marchand Essentiel ?", [
        ("A","100 000 FCFA/mois",False,"100 000 FCFA est insuffisant. Le plafond gratuit Essentiel est 500 000 FCFA/mois."),
        ("B","250 000 FCFA/mois",False,"250 000 FCFA n'est pas le plafond correct. C'est 500 000 FCFA/mois."),
        ("C","500 000 FCFA/mois",True,"Correct ! Le marchand Essentiel bénéficie de 0% d'encaissement jusqu'à 50 000 FCFA/jour, soit 500 000 FCFA/mois."),
        ("D","1 000 000 FCFA/mois",False,"1 000 000 FCFA/mois correspond au profil Classique, pas Essentiel."),
    ]),
    (8, "Lors de la création d'un compte OM Business pour un client déjà Orange Money, quelle étape est spécifique ?", [
        ("A","Refaire entièrement le parcours KYC",False,"Le client OM existant n'a pas besoin de refaire le KYC complet."),
        ("B","Vérifier et compléter le KYC existant puis associer le compte marchand",True,"Correct ! Pour un client OM existant, l'agent vérifie et complète le KYC existant puis associe le compte marchand."),
        ("C","Créer un nouveau numéro Orange Money",False,"Il n'est pas nécessaire de créer un nouveau numéro — le compte existant est utilisé."),
        ("D","Passer par le Back Office systématiquement",False,"Le Back Office n'intervient que si nécessaire — la procédure est simplifiée pour les clients OM existants."),
    ]),
    (9, "Comment le marchand effectue-t-il un encaissement via QR Code avec l'application OM Business ?", [
        ("A","En appelant le *144# et en saisissant le montant",False,"L'USSD *144# n'est pas la procédure d'encaissement QR Code OM Business."),
        ("B","En affichant son QR Code marchand et en attendant le scan par le client",True,"Correct ! Le marchand affiche son QR Code, le client scanne avec son application OM et la transaction est confirmée par SMS."),
        ("C","En envoyant une demande de paiement par SMS au client",False,"L'envoi par SMS n'est pas la procédure QR Code OM Business."),
        ("D","En se rendant en agence Orange avec le client",False,"La procédure QR Code est entièrement dématérialisée — aucune agence n'est nécessaire."),
    ]),
    (10, "Quel est le tarif d'un transfert Orange Money vers un compte tiers pour un profil Classique ?", [
        ("A","0% gratuit",False,"Le transfert vers un tiers n'est pas gratuit — des frais s'appliquent."),
        ("B","Tarif standard Orange Money en vigueur",True,"Correct ! Le transfert vers un compte tiers applique le tarif standard Orange Money — OM Business ne modifie pas ce tarif."),
        ("C","Forfait fixe de 200 FCFA",False,"Un forfait fixe de 200 FCFA n'est pas le tarif applicable."),
        ("D","2% du montant transféré",False,"2% n'est pas le tarif de transfert tiers pour OM Business."),
    ]),
    (11, "Combien de temps maximum pour qu'un dossier KYC soit traité en corbeille Back Office ?", [
        ("A","1 heure",False,"1 heure est trop court pour le traitement Back Office."),
        ("B","6 heures",False,"6 heures est en dessous du délai standard."),
        ("C","24 heures",True,"Correct ! Le Back Office dispose de 24 heures pour traiter un dossier KYC en corbeille."),
        ("D","72 heures",False,"72 heures dépasse le délai standard de 24 heures pour le KYC OM Business."),
    ]),
    (12, "Que permet la fonctionnalité 'Lien de paiement' dans l'application OM Business ?", [
        ("A","Envoyer un QR Code par email au client",False,"Le lien de paiement n'est pas limité à l'email — il est partageable sur tous les canaux."),
        ("B","Créer un lien de paiement personnalisé partageable par SMS ou WhatsApp",True,"Correct ! Le marchand génère un lien de paiement avec le montant pré-renseigné et le partage par SMS, WhatsApp ou autres canaux."),
        ("C","Payer les factures d'Orange CI",False,"Le lien de paiement concerne les transactions marchandes, pas les factures Orange."),
        ("D","Effectuer des retraits à distance",False,"Le lien de paiement sert à encaisser, pas à effectuer des retraits."),
    ]),
    (13, "Quel document est obligatoire pour un déplafonnement vers le profil Premium ?", [
        ("A","Uniquement la CNI du gérant",False,"La CNI seule n'est pas suffisante pour le profil Premium."),
        ("B","Registre de Commerce (RCCM) et documents financiers",True,"Correct ! Le profil Premium nécessite le RCCM et des justificatifs financiers (bilan, etc.) prouvant le CA > 400M FCFA."),
        ("C","Une photo de la devanture du commerce",False,"La photo de devanture n'est pas un document de déplafonnement Premium."),
        ("D","Le contrat de bail du local commercial",False,"Le contrat de bail n'est pas parmi les documents requis pour le déplafonnement Premium."),
    ]),
    (14, "Que se passe-t-il si le marchand dépasse son plafond mensuel d'encaissement Essentiel ?", [
        ("A","Les transactions sont automatiquement rejetées",False,"Les transactions ne sont pas automatiquement rejetées — elles sont facturées."),
        ("B","Des frais s'appliquent sur les montants au-delà du plafond",True,"Correct ! Au-delà du plafond gratuit (500 000 FCFA/mois), les encaissements sont facturés au tarif standard."),
        ("C","Le compte est suspendu jusqu'au mois suivant",False,"Le compte n'est pas suspendu — les transactions continuent avec des frais."),
        ("D","Le profil est automatiquement mis à niveau en Classique",False,"La mise à niveau n'est pas automatique — elle nécessite une demande de déplafonnement."),
    ]),
    (15, "Comment l'agent consulte-t-il l'historique des transactions d'un marchand dans l'application ?", [
        ("A","Via le menu 'Profil' > 'Mon compte'",False,"Le menu Profil concerne les informations du compte, pas l'historique des transactions."),
        ("B","Via le menu 'Historique' ou 'Transactions' dédié",True,"Correct ! L'historique des transactions est accessible via le menu dédié 'Historique' ou 'Transactions' de l'application."),
        ("C","En composant le *144# suivi du code marchand",False,"L'USSD *144# n'affiche pas l'historique complet des transactions."),
        ("D","En contactant le service client Orange",False,"L'historique est directement accessible dans l'application — pas besoin de contacter le service client."),
    ]),
    (16, "Quelle est la principale différence entre un retrait en PDV et un retrait en agence Orange pour un marchand ?", [
        ("A","Le retrait en PDV est plus lent",False,"La vitesse n'est pas la principale différence — c'est le coût."),
        ("B","Le retrait en PDV est gratuit pour Essentiel et Classique, l'agence peut avoir des frais",True,"Correct ! Le retrait en PDV est à 0 FCFA pour les profils Essentiel et Classique — l'agence peut avoir des tarifs différents."),
        ("C","Le retrait en agence est obligatoire pour les gros montants",False,"Les gros montants peuvent être retirés en PDV — il n'y a pas d'obligation d'agence."),
        ("D","Le retrait en PDV nécessite une validation superviseur",False,"Le retrait en PDV est direct — il ne nécessite pas de validation superviseur."),
    ]),
    (17, "Quel numéro doit appeler un marchand en cas de problème avec son application OM Business ?", [
        ("A","Le 15 (urgences)",False,"Le 15 est le numéro des urgences médicales, pas du support Orange Money."),
        ("B","Le 0808 (service client Orange Money)",True,"Correct ! Le 0808 est le numéro du service client Orange Money pour tout problème avec l'application OM Business."),
        ("C","Le 117 (police)",False,"Le 117 est la police — non applicable à un problème d'application."),
        ("D","Le 1313 (Orange CI)",False,"Le 1313 est le service client général Orange CI — le 0808 est spécifique Orange Money."),
    ]),
    (18, "Lors de l'enrôlement d'un client Non-OM, combien d'étapes comporte le parcours KYC standard ?", [
        ("A","2 étapes",False,"2 étapes est insuffisant pour le parcours KYC complet."),
        ("B","3 étapes",False,"Le parcours KYC complet pour un Non-OM comporte plus que 3 étapes."),
        ("C","5 étapes",True,"Correct ! Le parcours KYC Non-OM comporte 5 étapes : identité, photo, CNI scan, Proof of Life, validation."),
        ("D","8 étapes",False,"8 étapes dépasse le parcours standard — le KYC Non-OM en comporte 5."),
    ]),
    (19, "Que signifie l'acronyme PDV dans le contexte OM Business ?", [
        ("A","Produit De Vente",False,"PDV ne signifie pas Produit De Vente dans ce contexte."),
        ("B","Point De Vente",True,"Correct ! PDV = Point De Vente — c'est le lieu physique (boutique, kiosque) où le marchand opère."),
        ("C","Processus De Validation",False,"PDV n'est pas un acronyme de processus dans ce contexte."),
        ("D","Programme De Virtualisation",False,"PDV ne désigne pas un programme informatique dans OM Business."),
    ]),
    (20, "Un marchand Essentiel souhaite encaisser 80 000 FCFA en une seule transaction. Que se passe-t-il ?", [
        ("A","La transaction est refusée car elle dépasse le plafond journalier",False,"Le plafond de 50 000 FCFA concerne le seuil de gratuité, pas un refus de transaction."),
        ("B","La transaction est acceptée mais des frais s'appliquent sur la partie au-delà de 50 000 FCFA",True,"Correct ! Le plafond gratuit est 50 000 FCFA/jour — au-delà, les frais standard s'appliquent sur l'excédent."),
        ("C","La transaction est entièrement gratuite",False,"80 000 FCFA dépasse le seuil de gratuité de 50 000 FCFA/jour."),
        ("D","Le marchand doit passer au profil Classique pour effectuer cette transaction",False,"Le marchand Essentiel peut effectuer cette transaction avec des frais — pas besoin de changer de profil."),
    ]),
]
for qnum, text, opts in m4_questions:
    m4_new += q_block("m4", qnum, 20, text, opts)

# ─── M5 nouvelles questions q6-q20 ───────────────────────────
m5_new = ""
m5_questions = [
    (6, "Quel est le rôle du superviseur dans l'application Superviseur Orange ?", [
        ("A","Effectuer lui-même les enrôlements O'calm",False,"Les enrôlements sont effectués par les agents, pas par le superviseur."),
        ("B","Piloter la performance, valider les déploiements et gérer son équipe d'agents",True,"Correct ! Le superviseur pilote la performance de son équipe, valide les déploiements QR et gère les agents via l'application Superviseur."),
        ("C","Imprimer les QR Codes pour les marchands",False,"L'impression des QR Codes est une tâche agent, pas superviseur."),
        ("D","Gérer directement les comptes Orange Money des marchands",False,"La gestion des comptes Orange Money n'est pas le rôle du superviseur dans cette application."),
    ]),
    (7, "Quelle étape suit immédiatement le scan du QR Code à blanc lors d'un enrôlement O'calm ?", [
        ("A","L'envoi de l'OTP au marchand",False,"L'OTP n'est envoyé qu'après la vérification du formulaire pré-rempli."),
        ("B","Le pré-remplissage automatique du formulaire d'enrôlement",True,"Correct ! Après le scan du QR Code à blanc, le formulaire d'enrôlement se pré-remplit automatiquement avec les données du kit marchand."),
        ("C","La validation Back Office",False,"La validation Back Office n'est pas l'étape immédiatement suivante au scan."),
        ("D","La synchronisation des données",False,"La synchronisation n'est pas l'étape suivant immédiatement le scan du QR Code."),
    ]),
    (8, "Comment l'agent accède-t-il à la liste de ses marchands enrôlés dans l'application Agent ?", [
        ("A","Via le menu 'Profil Agent'",False,"Le Profil Agent contient les informations de l'agent, pas la liste des marchands."),
        ("B","Via le menu 'Mes Marchands' ou 'Portefeuille'",True,"Correct ! La liste des marchands enrôlés est accessible via le menu dédié 'Mes Marchands' ou 'Portefeuille' de l'application."),
        ("C","En contactant le superviseur",False,"La liste des marchands est directement accessible dans l'application — pas besoin de contacter le superviseur."),
        ("D","Via le *144# d'Orange Money",False,"L'USSD *144# ne donne pas accès à la liste des marchands enrôlés."),
    ]),
    (9, "Que doit faire l'agent si le marchand ne reçoit pas le code OTP lors de l'enrôlement ?", [
        ("A","Annuler l'enrôlement et repartir",False,"Annuler directement serait une perte de temps — des alternatives existent."),
        ("B","Renseigner n'importe quel code à 4 chiffres",False,"Saisir un code aléatoire est une fraude grave."),
        ("C","Attendre 2 minutes puis demander un renvoi du code",True,"Correct ! L'agent attend 2 minutes (délai réseau) puis utilise la fonction 'Renvoyer le code' dans l'application."),
        ("D","Appeler le superviseur pour saisir le code à sa place",False,"Le superviseur ne peut pas saisir le code OTP à la place du marchand — c'est une procédure d'authentification personnelle."),
    ]),
    (10, "Quelle est la fréquence de synchronisation recommandée pour l'application Agent ?", [
        ("A","Une fois par semaine",False,"Une synchronisation hebdomadaire est insuffisante pour maintenir les données à jour."),
        ("B","À chaque fois qu'une connexion Internet est disponible",True,"Correct ! La synchronisation doit être effectuée dès qu'une connexion Internet est disponible pour éviter les pertes de données."),
        ("C","Uniquement quand le superviseur le demande",False,"La synchronisation ne doit pas être conditionnée à la demande du superviseur — elle doit être régulière."),
        ("D","Une fois par mois",False,"Une synchronisation mensuelle est totalement insuffisante pour ce type d'opérations terrain."),
    ]),
    (11, "Dans l'application Superviseur, que permet l'indicateur 'Taux de déploiement' ?", [
        ("A","Mesurer la qualité du réseau Orange dans le secteur",False,"Le taux de déploiement ne mesure pas la qualité réseau."),
        ("B","Suivre le pourcentage de marchands cibles effectivement enrôlés par les agents",True,"Correct ! Le taux de déploiement mesure le ratio marchands enrôlés / objectif — c'est le KPI principal de performance du superviseur."),
        ("C","Calculer le montant total des transactions marchandes",False,"Le volume de transactions n'est pas ce que mesure le taux de déploiement."),
        ("D","Contrôler l'autonomie de la batterie des terminaux",False,"L'autonomie des terminaux n'est pas un indicateur dans l'application Superviseur."),
    ]),
    (12, "Que se passe-t-il si un agent tente d'enrôler un marchand déjà enregistré dans le système ?", [
        ("A","L'enrôlement se fait normalement en créant un doublon",False,"Un doublon serait créé — l'application doit détecter et bloquer cela."),
        ("B","L'application affiche une alerte 'Marchand déjà enregistré' et bloque l'enrôlement",True,"Correct ! Le système détecte les doublons et bloque l'enrôlement avec une alerte pour éviter les redondances."),
        ("C","L'ancien enrôlement est automatiquement écrasé",False,"Écraser l'ancien enrôlement sans alerte entraînerait des pertes de données."),
        ("D","L'enrôlement est accepté mais mis en attente de validation",False,"Un doublon détecté est bloqué, pas mis en attente."),
    ]),
    (13, "Comment le superviseur valide-t-il un déploiement QR Code effectué par un agent ?", [
        ("A","En appelant le marchand par téléphone",False,"L'appel téléphonique n'est pas la procédure de validation officielle."),
        ("B","Via l'application Superviseur : sélection du déploiement > Valider",True,"Correct ! Le superviseur accède au déploiement en attente dans son application et clique sur 'Valider' après vérification."),
        ("C","En se déplaçant systématiquement chez chaque marchand",False,"Un déplacement physique pour chaque validation n'est pas la procédure standard."),
        ("D","Automatiquement sans action de sa part",False,"La validation superviseur nécessite une action explicite dans l'application."),
    ]),
    (14, "Quelle information l'agent doit-il absolument vérifier avant de quitter un point de vente après un déploiement ?", [
        ("A","Le nombre de clients du marchand",False,"Le nombre de clients n'est pas une vérification post-déploiement."),
        ("B","Que le test de transaction a été effectué avec succès",True,"Correct ! Le test de transaction est obligatoire — il confirme que le QR Code fonctionne parfaitement avant le départ de l'agent."),
        ("C","La taille du QR Code affiché",False,"La taille du QR Code n'est pas une vérification critique post-déploiement."),
        ("D","Le nom du propriétaire du local",False,"Le nom du propriétaire est une donnée KYB collectée lors de l'enrôlement, pas lors du déploiement."),
    ]),
    (15, "Dans quel cas l'application Agent fonctionne-t-elle uniquement avec une connexion Internet active ?", [
        ("A","Pour la saisie des données d'enrôlement",False,"La saisie peut se faire hors-ligne."),
        ("B","Pour le déploiement du QR Code et la synchronisation finale",True,"Correct ! Le déploiement QR Code et la synchronisation des données nécessitent obligatoirement une connexion Internet active."),
        ("C","Pour afficher la liste des marchands",False,"La liste des marchands peut être consultée hors-ligne après synchronisation."),
        ("D","Pour ouvrir l'application",False,"L'application peut s'ouvrir hors-ligne — une connexion n'est pas requise au démarrage."),
    ]),
    (16, "Quel est l'objectif quotidien minimum recommandé pour un agent en termes de déploiements QR Code ?", [
        ("A","2 déploiements",False,"2 déploiements est largement en dessous de l'objectif."),
        ("B","5 déploiements",True,"Correct ! L'objectif minimum recommandé est de 5 déploiements QR Code validés par jour pour un agent."),
        ("C","10 déploiements",False,"10 déploiements est l'objectif premium — le minimum recommandé est 5."),
        ("D","15 déploiements",False,"15 déploiements est un objectif très ambitieux — le minimum est 5."),
    ]),
    (17, "Que doit faire l'agent si le scan du QR Code à blanc échoue (code non reconnu) ?", [
        ("A","Saisir manuellement le numéro marchand",False,"La saisie manuelle n'est pas la première option — l'agent doit tenter de rescanner."),
        ("B","Vérifier que le QR Code est dans le bon kit et rescanner",True,"Correct ! L'agent vérifie que le bon QR Code est utilisé (non endommagé, non déjà utilisé) puis tente un nouveau scan."),
        ("C","Contacter le 0808 immédiatement",False,"Contacter le 0808 n'est pas la première étape — l'agent vérifie d'abord le QR Code."),
        ("D","Annuler et informer le marchand que l'enrôlement est impossible",False,"Annuler immédiatement est prématuré — des solutions doivent être tentées."),
    ]),
    (18, "Comment l'application Agent gère-t-elle les données collectées hors-ligne ?", [
        ("A","Elle les supprime si non synchronisées sous 24h",False,"Les données hors-ligne ne sont pas supprimées automatiquement."),
        ("B","Elle les stocke localement et les synchronise à la prochaine connexion",True,"Correct ! Les données sont stockées localement sur l'appareil et synchronisées automatiquement lors de la prochaine connexion Internet."),
        ("C","Elle bloque toute nouvelle saisie jusqu'à synchronisation",False,"L'application continue de fonctionner hors-ligne — elle ne bloque pas la saisie."),
        ("D","Elle envoie les données par SMS au superviseur",False,"L'envoi SMS n'est pas le mécanisme de synchronisation de l'application Agent."),
    ]),
    (19, "Que peut consulter un superviseur dans son tableau de bord en temps réel ?", [
        ("A","Uniquement ses propres statistiques personnelles",False,"Le superviseur voit les statistiques de toute son équipe, pas seulement les siennes."),
        ("B","La performance de chaque agent, les déploiements en attente et le taux global",True,"Correct ! Le tableau de bord superviseur affiche en temps réel : performance individuelle des agents, déploiements en attente et KPIs globaux."),
        ("C","Le solde des comptes Orange Money des marchands",False,"Le solde des comptes OM n'est pas accessible dans le tableau de bord superviseur."),
        ("D","L'historique des appels téléphoniques des agents",False,"Les appels téléphoniques ne sont pas tracés dans l'application Superviseur."),
    ]),
    (20, "Quelle action permet de finaliser un enrôlement O'calm et activer le compte marchand ?", [
        ("A","Appuyer sur 'Terminer' dans l'application sans autre vérification",False,"Appuyer sur Terminer seul ne finalise pas — la saisie de l'OTP est obligatoire."),
        ("B","Saisir le code OTP à 4 chiffres reçu par le marchand puis confirmer",True,"Correct ! La saisie de l'OTP à 4 chiffres reçu par SMS par le marchand est l'étape finale qui active le compte."),
        ("C","Envoyer une photo du QR Code au superviseur",False,"L'envoi de photo au superviseur n'est pas la procédure de finalisation."),
        ("D","Attendre 24h pour l'activation automatique",False,"L'activation est immédiate après saisie de l'OTP — pas de délai de 24h."),
    ]),
]
for qnum, text, opts in m5_questions:
    m5_new += q_block("m5", qnum, 20, text, opts)

# ── Insert new questions before closing tag of each quiz container ──
# M1: before </div>\n    <!-- /page-quiz -->
html = html.replace(
    '\n      </div>\n    <!-- /page-quiz -->\n      </div>',
    m1_new + '\n      </div>\n    <!-- /page-quiz -->\n      </div>',
    1  # only first occurrence
)
print("M1 new questions inserted OK")

# M2: before </div>\n      </div>  (after last m2 question)
html = html.replace(
    '          <div class="quiz-feedback" id="m2-fb-q5"></div>\n        </div>\n      </div>\n      </div>',
    '          <div class="quiz-feedback" id="m2-fb-q5"></div>\n        </div>' + m2_new + '\n      </div>\n      </div>'
)
print("M2 new questions inserted OK")

# M3: before </div>\n      </div>  (after last m3 question)
html = html.replace(
    '          <div class="quiz-feedback" id="m3-fb-q6"></div>\n        </div>\n      </div>\n      </div>',
    '          <div class="quiz-feedback" id="m3-fb-q6"></div>\n        </div>' + m3_new + '\n      </div>\n      </div>'
)
print("M3 new questions inserted OK")

# M4: before closing div of quiz-body
html = html.replace(
    '          <div class="quiz-feedback" id="fb-m4-q5"></div>\n        </div>\n        <div style="margin-top:24px',
    '          <div class="quiz-feedback" id="fb-m4-q5"></div>\n        </div>' + m4_new + '\n        <div style="margin-top:24px'
)
print("M4 new questions inserted OK")

# M5: before </div>\n      </div>  (after last m5 question)
html = html.replace(
    '          <div class="quiz-feedback" id="m5-fb-q5"></div>\n        </div>\n      </div>\n      </div>',
    '          <div class="quiz-feedback" id="m5-fb-q5"></div>\n        </div>' + m5_new + '\n      </div>\n      </div>'
)
print("M5 new questions inserted OK")

# ══════════════════════════════════════════════════════════════
# 7. ADD DRAG-TO-SCROLL JS
# ══════════════════════════════════════════════════════════════
DRAG_JS = """
// ── Drag-to-scroll (page + overlays) ────────────────────────
(function() {
  var isDragging = false, startX, startY, scrollLeft, scrollTop, dragTarget;
  var THRESHOLD = 5;
  var moved = false;

  function getScrollTarget(el) {
    while (el && el !== document.body) {
      var style = window.getComputedStyle(el);
      var overflowY = style.overflowY;
      var overflowX = style.overflowX;
      if ((overflowY === 'auto' || overflowY === 'scroll') && el.scrollHeight > el.clientHeight) return el;
      if ((overflowX === 'auto' || overflowX === 'scroll') && el.scrollWidth > el.clientWidth) return el;
      el = el.parentElement;
    }
    return document.documentElement;
  }

  document.addEventListener('mousedown', function(e) {
    if (e.button !== 0) return;
    if (e.target.tagName === 'BUTTON' || e.target.tagName === 'INPUT' || e.target.tagName === 'A' || e.target.tagName === 'SELECT') return;
    if (e.target.closest('button') || e.target.closest('a') || e.target.closest('.quiz-option')) return;
    isDragging = true;
    moved = false;
    startX = e.clientX;
    startY = e.clientY;
    dragTarget = getScrollTarget(e.target);
    scrollLeft = dragTarget.scrollLeft;
    scrollTop = dragTarget.scrollTop;
  }, { passive: true });

  document.addEventListener('mousemove', function(e) {
    if (!isDragging) return;
    var dx = e.clientX - startX;
    var dy = e.clientY - startY;
    if (!moved && Math.abs(dy) < THRESHOLD && Math.abs(dx) < THRESHOLD) return;
    moved = true;
    document.body.style.cursor = 'grabbing';
    dragTarget.scrollLeft = scrollLeft - dx;
    dragTarget.scrollTop = scrollTop - dy;
  }, { passive: true });

  function stopDrag() {
    if (!isDragging) return;
    isDragging = false;
    document.body.style.cursor = '';
  }
  document.addEventListener('mouseup', stopDrag);
  document.addEventListener('mouseleave', stopDrag);
})();
"""

html = html.replace('</script>\n\n</body>', DRAG_JS + '\n</script>\n\n</body>')
print("Drag-to-scroll added OK")

# ══════════════════════════════════════════════════════════════
# 8. WRITE OUTPUT
# ══════════════════════════════════════════════════════════════
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nindex.html: {len(html):,} chars ({len(html)//1024} KB)")
print("Done!")
