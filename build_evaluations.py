"""
Script de génération des évaluations séparées Orange et ID30.
Lit evaluation.html et produit evaluation_orange.html + evaluation_id30.html
"""
import re

with open('evaluation.html', 'r', encoding='utf-8') as f:
    src = f.read()

# ──────────────────────────────────────────────────────────
# 1. LOGO MAFA — remplacer <div class="logo-icon">🏢</div>
# ──────────────────────────────────────────────────────────
LOGO_OLD = '<div class="logo-icon">🏢</div>'
LOGO_NEW = '<img src="img_m4/s01_logo_mafa.jpg" alt="MAFA" class="logo-icon" style="object-fit:contain;background:none;box-shadow:none;">'

src = src.replace(LOGO_OLD, LOGO_NEW)

# Ajuster le style .logo-icon pour que l'image s'affiche bien
src = src.replace(
    '  .logo-icon {\n    width: 38px;\n    height: 38px;\n    background: linear-gradient(135deg, var(--accent), #60a5fa);\n    border-radius: 9px;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    font-size: 1.1rem;\n    flex-shrink: 0;\n    box-shadow: 0 2px 8px rgba(37,99,235,0.3);\n  }',
    '  .logo-icon {\n    width: 38px;\n    height: 38px;\n    border-radius: 9px;\n    flex-shrink: 0;\n    display: block;\n  }'
)

# ──────────────────────────────────────────────────────────
# 2. SUPPORT MULTI-RÉPONSES
#    - Nouvelle fonction selectMultiAnswer
#    - renderExam modifié pour gérer q.multi
#    - finalizeExam avec correction multi
# ──────────────────────────────────────────────────────────

# Ajouter selectMultiAnswer après selectAnswer
MULTI_FN = """
function selectMultiAnswer(qId, optionIdx, maxSelect) {
  let current = Array.isArray(state.currentAnswers[qId]) ? [...state.currentAnswers[qId]] : [];
  if(current.includes(optionIdx)) {
    current = current.filter(i => i !== optionIdx);
  } else {
    if(current.length >= maxSelect) current = current.slice(1);
    current.push(optionIdx);
  }
  state.currentAnswers[qId] = current;
  renderExam();
}

"""
src = src.replace(
    'function navigate(dir) {',
    MULTI_FN + 'function navigate(dir) {'
)

# Dans renderExam, remplacer la génération d'options pour gérer le multi
# Trouver le bloc qui génère optionsHTML pour qcm/vf
OLD_OPTIONS_BLOCK = """  if(q.type === 'qcm' || q.type === 'vf') {
    optionsHTML = `<div class="exam-options">` + q.options.map((opt, oi) => `
      <label class="exam-option ${state.currentAnswers[q.id] === oi ? 'selected' : ''}" onclick="selectAnswer(${q.id}, ${oi})">
        <input type="radio" name="exam_q" value="${oi}" ${state.currentAnswers[q.id] === oi ? 'checked' : ''} style="pointer-events:none">
        <span class="exam-option-letter">${letters[oi]}</span>
        <span>${opt}</span>
      </label>`).join('') + `</div>`;"""

NEW_OPTIONS_BLOCK = """  if(q.multi) {
    const curSel = Array.isArray(state.currentAnswers[q.id]) ? state.currentAnswers[q.id] : [];
    optionsHTML = `<div class="alert alert-info" style="margin-bottom:0.8rem;font-size:0.85rem;padding:10px 14px">☑️ Sélectionnez <strong>${q.multi} réponses</strong> pour cette question.</div>
    <div class="exam-options">` + q.options.map((opt, oi) => `
      <label class="exam-option ${curSel.includes(oi) ? 'selected' : ''}" onclick="selectMultiAnswer(${q.id}, ${oi}, ${q.multi})">
        <input type="checkbox" value="${oi}" ${curSel.includes(oi) ? 'checked' : ''} style="pointer-events:none;width:16px;height:16px;accent-color:var(--accent)">
        <span class="exam-option-letter">${letters[oi]}</span>
        <span>${opt}</span>
      </label>`).join('') + `</div>`;
  } else if(q.type === 'qcm' || q.type === 'vf') {
    optionsHTML = `<div class="exam-options">` + q.options.map((opt, oi) => `
      <label class="exam-option ${state.currentAnswers[q.id] === oi ? 'selected' : ''}" onclick="selectAnswer(${q.id}, ${oi})">
        <input type="radio" name="exam_q" value="${oi}" ${state.currentAnswers[q.id] === oi ? 'checked' : ''} style="pointer-events:none">
        <span class="exam-option-letter">${letters[oi]}</span>
        <span>${opt}</span>
      </label>`).join('') + `</div>`;"""

src = src.replace(OLD_OPTIONS_BLOCK, NEW_OPTIONS_BLOCK)

# Fermer le else ajouté — trouver le bloc else du textarea et ajouter une accolade de fermeture
# Le bloc else existant se termine par:  } else { ... textarea ... }
# On a ajouté un if...else if... donc on n'a pas besoin de modifier la fermeture du bloc principal

# Dans finalizeExam, modifier le calcul isCorrect pour multi
OLD_SCORE = """    const ans = state.currentAnswers[q.id];
    if(ans === undefined) { wrong++; score -= state.config.pointsWrong; }
    else if(ans === q.correct) { correct++; score += q.points; }
    else { wrong++; score -= state.config.pointsWrong; }"""

NEW_SCORE = """    const ans = state.currentAnswers[q.id];
    const isCorrect = q.multi
      ? (Array.isArray(ans) && JSON.stringify([...ans].sort((a,b)=>a-b)) === JSON.stringify([...q.correct].sort((a,b)=>a-b)))
      : ans === q.correct;
    if(ans === undefined || (q.multi && (!Array.isArray(ans) || ans.length === 0))) { wrong++; score -= state.config.pointsWrong; }
    else if(isCorrect) { correct++; score += q.points; }
    else { wrong++; score -= state.config.pointsWrong; }"""

src = src.replace(OLD_SCORE, NEW_SCORE)

# Dans showCandidateResults, corriger aussi le isCorrect pour affichage
OLD_DISPLAY = """    const ans = result.answers[q.id];
    const isCorrect = ans === q.correct;
    const icon = ans === undefined ? '⬜' : isCorrect ? '✅' : '❌';
    return `
      <div class="result-item">
        <div class="result-item-icon">${icon}</div>
        <div class="result-item-text">
          <div class="q-text">Q${idx+1}. ${q.text || 'Question'}</div>
          <div class="q-answer">Votre réponse : ${ans !== undefined ? (letters[ans] + '. ' + q.options[ans]) : 'Sans réponse'}</div>
          ${!isCorrect ? `<div class="q-correct">✓ Bonne réponse : ${letters[q.correct]}. ${q.options[q.correct]}</div>` : ''}
        </div>
      </div>`;\n"""

NEW_DISPLAY = """    const ans = result.answers[q.id];
    const isCorrect = q.multi
      ? (Array.isArray(ans) && JSON.stringify([...ans].sort((a,b)=>a-b)) === JSON.stringify([...q.correct].sort((a,b)=>a-b)))
      : ans === q.correct;
    const icon = (ans === undefined || ans === null) ? '⬜' : isCorrect ? '✅' : '❌';
    const ansDisplay = q.multi
      ? (Array.isArray(ans) && ans.length > 0 ? ans.map(i => letters[i] + '. ' + q.options[i]).join(' + ') : 'Sans réponse')
      : (ans !== undefined ? (letters[ans] + '. ' + q.options[ans]) : 'Sans réponse');
    const correctDisplay = q.multi
      ? q.correct.map(i => letters[i] + '. ' + q.options[i]).join(' + ')
      : (letters[q.correct] + '. ' + q.options[q.correct]);
    return `
      <div class="result-item">
        <div class="result-item-icon">${icon}</div>
        <div class="result-item-text">
          <div class="q-text">Q${idx+1}. ${q.text || 'Question'}${q.multi ? ' <em style="font-size:0.75rem;color:var(--text-muted)">(2 réponses)</em>' : ''}</div>
          <div class="q-answer">Votre réponse : ${ansDisplay}</div>
          ${!isCorrect ? `<div class="q-correct">✓ Bonne réponse : ${correctDisplay}</div>` : ''}
        </div>
      </div>`;\n"""

src = src.replace(OLD_DISPLAY, NEW_DISPLAY)

# ──────────────────────────────────────────────────────────
# 3. Nouvelles questions marchands cibles (à injecter dans les banques)
# ──────────────────────────────────────────────────────────

# Questions Orange — cibles marchands (insérer avant la fermeture de 'agent-orange': [...])
NEW_ORANGE_MERCHANT_QUESTIONS = """  { type:'qcm', text:"Parmi les profils suivants, lesquels sont des cibles prioritaires pour OM Business Essentiel ? (Sélectionnez 2 réponses)", options:["Chauffeur VTC / Uber sans local fixe","Entreprise cotée en bourse","Vendeur ambulant de fruits et légumes","Grande surface internationale"], correct:[0,2], multi:2, points:1 },
  { type:'qcm', text:"Un vendeur en ligne qui vend via WhatsApp et réseaux sociaux souhaite encaisser ses clients à distance. Quel profil OM Business lui proposez-vous ?", options:["OM Business Premium — ventes en ligne uniquement","OM Business Essentiel — pas de local requis, lien de paiement adapté","Non éligible — les vendeurs en ligne ne sont pas une cible OM Business","OM Business Classique — le e-commerce est réservé au Classique"], correct:1, points:1 },
  { type:'qcm', text:"Quels types de marchands sans local fixe peuvent bénéficier du profil OM Business Essentiel ?", options:["Uniquement les épiciers avec boutique","Les vendeurs ambulants, chauffeurs VTC, vendeurs en ligne et prestataires de service mobile","Uniquement les marchands enregistrés à la mairie","Les chauffeurs de taxi uniquement"], correct:1, points:1 },
  { type:'qcm', text:"Un chauffeur VTC vous dit : 'Je ne suis pas un commerçant, OM Business ne me concerne pas.' Comment répondez-vous ?", options:["Il a raison — les VTC sont hors cible","OM Business Essentiel est fait pour lui : encaissement à distance via lien de paiement, dossier CNI seule, pas de local requis","Il faut d'abord qu'il ouvre une boutique pour être éligible","Lui proposer d'abord un compte Orange Money standard"], correct:1, points:1 },
  { type:'qcm', text:"Parmi ces activités, lesquelles sont éligibles à OM Business Essentiel sans registre de commerce ? (Sélectionnez 2 réponses)", options:["Vendeur ambulant de rue","Directeur général de SA","Couturière à domicile","PDG d'une multinationale"], correct:[0,2], multi:2, points:1 },
  { type:'qcm', text:"Un agent hésite à prospecter les vendeurs ambulants car 'ils bougent tout le temps'. Quelle est la bonne approche ?", options:["L'agent a raison — les ambulants sont difficiles à fidéliser","Les ambulants sont une cible idéale : profil Essentiel sans local, CNI seule, lien de paiement pour encaisser à distance","Attendre que l'ambulant se sédentarise avant de le prospecter","Les orienter vers un compte Orange Money standard"], correct:1, points:1 },
"""

# Insérer avant la fermeture de 'agent-orange' (avant '],\n\n\'rv-orange\'')
src = src.replace(
    "  { type:'qcm', text:\"Sur la carte de l'Application Agent, que représente un point VERT ?\"",
    NEW_ORANGE_MERCHANT_QUESTIONS + "  { type:'qcm', text:\"Sur la carte de l'Application Agent, que représente un point VERT ?\""
)

# Questions ID30 — cibles entrepreneurs (insérer dans 'call-center')
NEW_ID30_MERCHANT_QUESTIONS = """  { type:'qcm', text:"Parmi les profils d'entrepreneurs suivants, lesquels sont éligibles à la Carte Entreprenant ID30 ? (Sélectionnez 2 réponses)", options:["Vendeur ambulant de rue sans local fixe","Fonctionnaire de l'État salarié","Chauffeur VTC indépendant","Actionnaire majoritaire d'une multinationale"], correct:[0,2], multi:2, points:1 },
  { type:'qcm', text:"Un vendeur en ligne qui commercialise ses produits via Instagram peut-il bénéficier de la Carte Entreprenant ID30 ?", options:["Non — le commerce en ligne n'est pas reconnu","Oui — toute activité génératrice de revenus est éligible, y compris le commerce en ligne","Uniquement s'il a un compte bancaire professionnel","Non — il doit d'abord ouvrir une boutique physique"], correct:1, points:1 },
  { type:'qcm', text:"Un prospect dit être 'ambulant' et ne pas avoir d'adresse fixe. L'agent doit-il traiter son dossier ?", options:["Non — une adresse fixe est obligatoire pour la Carte Entreprenant","Oui — l'activité ambulante est éligible ; l'adresse de résidence suffit pour le dossier","Non — les ambulants doivent d'abord s'enregistrer à la mairie","Suspendre le dossier en attente de régularisation"], correct:1, points:1 },
  { type:'qcm', text:"Quels types d'entrepreneurs sans local commercial sont éligibles à la Carte Entreprenant ? (Sélectionnez 2 réponses)", options:["Prestataire de services à domicile (coiffeur, plombier)","Retraité sans activité","Chauffeur indépendant (taxi, VTC)","Fonctionnaire en activité"], correct:[0,2], multi:2, points:1 },
"""

# Insérer dans 'call-center' après la première question
src = src.replace(
    "  { type:'qcm', text:\"Connectel affiche pour un dossier le statut 'Doublon détecté'.",
    NEW_ID30_MERCHANT_QUESTIONS + "  { type:'qcm', text:\"Connectel affiche pour un dossier le statut 'Doublon détecté'."
)

# ──────────────────────────────────────────────────────────
# ÉTAPE FINALE : src est maintenant la base commune
# On va créer deux versions spécifiques
# ──────────────────────────────────────────────────────────

def make_orange(base):
    txt = base

    # Titre
    txt = txt.replace(
        '<title>Système d\'Évaluation — MAFA HOLDING / COLIBRI TECHNOLOGIES</title>',
        '<title>Évaluation Orange Money Business — MAFA HOLDING</title>'
    )

    # Couleurs accent → orange
    txt = txt.replace('--primary: #2563eb;', '--primary: #f97316;')
    txt = txt.replace('--accent: #2563eb;', '--accent: #f97316;')
    txt = txt.replace('--accent2: #f97316;', '--accent2: #ea580c;')
    txt = txt.replace('--shadow-blue: 0 4px 14px rgba(37,99,235,0.22);', '--shadow-blue: 0 4px 14px rgba(249,115,22,0.22);')
    # gradient barre haut
    txt = txt.replace(
        'background: linear-gradient(90deg, var(--accent), #60a5fa, var(--accent2));',
        'background: linear-gradient(90deg, #f97316, #fb923c, #ea580c);'
    )
    # header-badge couleur
    txt = txt.replace(
        '    background: #eff6ff;\n    border: 1px solid #bfdbfe;\n    color: var(--accent);',
        '    background: #fff7ed;\n    border: 1px solid #fed7aa;\n    color: #c2410c;'
    )

    # Supprimer screen-operation-choice
    txt = re.sub(
        r'  <!-- SCREEN: OPERATION CHOICE -->.*?</div>\n\n  <!-- SCREEN: ADMIN LOGIN -->',
        '  <!-- SCREEN: ADMIN LOGIN -->',
        txt, flags=re.DOTALL
    )

    # Bouton landing → direct candidate entry
    txt = txt.replace(
        "onclick=\"showScreen('screen-operation-choice')\" style=\"padding:13px 28px;font-size:0.95rem\">\n          ▶&nbsp; Commencer l'évaluation",
        "onclick=\"goToEvaluation()\" style=\"padding:13px 28px;font-size:0.95rem\">\n          🟠&nbsp; Commencer — Orange Money Business"
    )

    # Landing titre
    txt = txt.replace(
        '        <div>Système</div>\n        <div><span class="accent">d\'Évaluation</span></div>\n        <div><span class="accent2">en ligne</span></div>',
        '        <div>Évaluation</div>\n        <div><span class="accent">Orange Money</span></div>\n        <div><span class="accent2">Business</span></div>'
    )

    # currentOperation dans state
    txt = txt.replace(
        '  currentOperation: null,',
        '  currentOperation: \'orange\','
    )

    # goToEvaluation function
    txt = txt.replace(
        '// ===================== OPERATION SELECTION =====================\nfunction selectOperation(op) {\n  state.currentOperation = op;\n  const opLabels = { orange: \'🟠 ORANGE\', id30: \'🔵 ID30\' };\n  document.getElementById(\'currentMode\').textContent = opLabels[op] || op.toUpperCase();\n  setupCandidateEntry();\n  showScreen(\'screen-candidate-entry\');\n}',
        '// ===================== OPERATION SELECTION =====================\nfunction selectOperation(op) {\n  state.currentOperation = op;\n  setupCandidateEntry();\n  showScreen(\'screen-candidate-entry\');\n}\nfunction goToEvaluation() {\n  state.currentOperation = \'orange\';\n  setupCandidateEntry();\n  showScreen(\'screen-candidate-entry\');\n}'
    )

    # setupCandidateEntry — garder seulement Orange
    OLD_SETUP = """  if(state.currentOperation === 'orange') {
    if(hero) hero.innerHTML = 'Évaluation <span>Orange Money Business</span>';
    if(heroSub) heroSub.textContent = 'Opération ORANGE — Renseignez vos informations pour commencer';
    posteSelect.innerHTML = `
      <option value="">-- Sélectionnez votre rôle --</option>
      <option value="agent-orange">Agent OM Business</option>
      <option value="superviseur-orange">Superviseur OM Business</option>
      <option value="inspecteur-orange">Inspecteur OM Business</option>
      <option value="rv-orange">Responsable Ville (OM Business)</option>
    `;
  } else if(state.currentOperation === 'id30') {
    if(hero) hero.innerHTML = 'Bienvenue sur <span>l\'évaluation</span>';
    if(heroSub) heroSub.textContent = 'Opération ID30 — Renseignez vos informations pour commencer le test';
    posteSelect.innerHTML = `
      <option value="">-- Sélectionnez votre poste --</option>
      <option value="call-center">Agent Call Center (ID30)</option>
      <option value="back-office">Agent Back Office (ID30)</option>
      <option value="inspecteur">Inspecteur (ID30 &amp; Orange QR)</option>
      <option value="superviseur">Superviseur (Agent &amp; Orange Money)</option>
    `;
  }"""

    NEW_SETUP_ORANGE = """  if(hero) hero.innerHTML = 'Évaluation <span>Orange Money Business</span>';
  if(heroSub) heroSub.textContent = 'Opération ORANGE — Renseignez vos informations pour commencer';
  posteSelect.innerHTML = `
    <option value="">-- Sélectionnez votre rôle --</option>
    <option value="agent-orange">Agent OM Business</option>
    <option value="superviseur-orange">Superviseur OM Business</option>
    <option value="inspecteur-orange">Inspecteur OM Business</option>
    <option value="rv-orange">Responsable Ville (OM Business)</option>
  `;"""

    txt = txt.replace(OLD_SETUP, NEW_SETUP_ORANGE)

    # startExam — banque Orange
    txt = txt.replace(
        '  const bank = state.currentOperation === \'orange\' ? QUESTIONS_BY_POSTE_ORANGE : QUESTIONS_BY_POSTE;\n  // Niveau intermédiaire uniquement pour l\'opération Orange (points:1 = intermédiaire)\n  let rawQuestions = bank[poste] || [];\n  if(state.currentOperation === \'orange\') {\n    rawQuestions = rawQuestions.filter(q => q.points === 1 && q.type !== \'open\');\n  }',
        '  const bank = QUESTIONS_BY_POSTE_ORANGE;\n  let rawQuestions = bank[poste] || [];'
    )

    # Supprimer QUESTIONS_BY_POSTE (ID30)
    txt = re.sub(
        r'const QUESTIONS_BY_POSTE = \{.*?\}; // fin QUESTIONS_BY_POSTE',
        '// QUESTIONS ID30 retirées (fichier Orange uniquement)',
        txt, flags=re.DOTALL
    )

    # Admin filter — simplifier (garder seulement orange)
    txt = txt.replace(
        "      <button id=\"admin-filter-orange\" class=\"btn btn-secondary btn-sm\" onclick=\"setAdminFilter('orange')\" style=\"border-color:#f97316;color:#c2410c\">🟠 Orange</button>\n      <button id=\"admin-filter-id30\" class=\"btn btn-secondary btn-sm\" onclick=\"setAdminFilter('id30')\" style=\"border-color:#2563eb;color:#1e40af\">🔵 ID30</button>",
        "      <span style=\"font-size:0.85rem;color:var(--text-muted);padding:6px 0\">🟠 Évaluation Orange Money Business</span>"
    )

    # Retirer les filtres admin inutiles
    txt = txt.replace(
        "  ['all','orange','id30'].forEach(f => {\n    const btn = document.getElementById('admin-filter-' + f);\n    if(btn) btn.className = 'btn btn-sm ' + (f === filter ? 'btn-primary' : 'btn-secondary');\n  });",
        "  // filtres non utilisés en mode Orange"
    )

    return txt


def make_id30(base):
    txt = base

    # Titre
    txt = txt.replace(
        '<title>Système d\'Évaluation — MAFA HOLDING / COLIBRI TECHNOLOGIES</title>',
        '<title>Évaluation Connectel ID30 — MAFA HOLDING</title>'
    )

    # Supprimer screen-operation-choice
    txt = re.sub(
        r'  <!-- SCREEN: OPERATION CHOICE -->.*?</div>\n\n  <!-- SCREEN: ADMIN LOGIN -->',
        '  <!-- SCREEN: ADMIN LOGIN -->',
        txt, flags=re.DOTALL
    )

    # Bouton landing → direct candidate entry
    txt = txt.replace(
        "onclick=\"showScreen('screen-operation-choice')\" style=\"padding:13px 28px;font-size:0.95rem\">\n          ▶&nbsp; Commencer l'évaluation",
        "onclick=\"goToEvaluation()\" style=\"padding:13px 28px;font-size:0.95rem\">\n          🔵&nbsp; Commencer — Connectel ID30"
    )

    # Landing titre
    txt = txt.replace(
        '        <div>Système</div>\n        <div><span class="accent">d\'Évaluation</span></div>\n        <div><span class="accent2">en ligne</span></div>',
        '        <div>Évaluation</div>\n        <div><span class="accent">Connectel</span></div>\n        <div><span class="accent2">ID30</span></div>'
    )

    # currentOperation dans state
    txt = txt.replace(
        '  currentOperation: null,',
        '  currentOperation: \'id30\','
    )

    # goToEvaluation function
    txt = txt.replace(
        '// ===================== OPERATION SELECTION =====================\nfunction selectOperation(op) {\n  state.currentOperation = op;\n  const opLabels = { orange: \'🟠 ORANGE\', id30: \'🔵 ID30\' };\n  document.getElementById(\'currentMode\').textContent = opLabels[op] || op.toUpperCase();\n  setupCandidateEntry();\n  showScreen(\'screen-candidate-entry\');\n}',
        '// ===================== OPERATION SELECTION =====================\nfunction selectOperation(op) {\n  state.currentOperation = op;\n  setupCandidateEntry();\n  showScreen(\'screen-candidate-entry\');\n}\nfunction goToEvaluation() {\n  state.currentOperation = \'id30\';\n  setupCandidateEntry();\n  showScreen(\'screen-candidate-entry\');\n}'
    )

    # setupCandidateEntry — garder seulement ID30
    OLD_SETUP = """  if(state.currentOperation === 'orange') {
    if(hero) hero.innerHTML = 'Évaluation <span>Orange Money Business</span>';
    if(heroSub) heroSub.textContent = 'Opération ORANGE — Renseignez vos informations pour commencer';
    posteSelect.innerHTML = `
      <option value="">-- Sélectionnez votre rôle --</option>
      <option value="agent-orange">Agent OM Business</option>
      <option value="superviseur-orange">Superviseur OM Business</option>
      <option value="inspecteur-orange">Inspecteur OM Business</option>
      <option value="rv-orange">Responsable Ville (OM Business)</option>
    `;
  } else if(state.currentOperation === 'id30') {
    if(hero) hero.innerHTML = 'Bienvenue sur <span>l\'évaluation</span>';
    if(heroSub) heroSub.textContent = 'Opération ID30 — Renseignez vos informations pour commencer le test';
    posteSelect.innerHTML = `
      <option value="">-- Sélectionnez votre poste --</option>
      <option value="call-center">Agent Call Center (ID30)</option>
      <option value="back-office">Agent Back Office (ID30)</option>
      <option value="inspecteur">Inspecteur (ID30 &amp; Orange QR)</option>
      <option value="superviseur">Superviseur (Agent &amp; Orange Money)</option>
    `;
  }"""

    NEW_SETUP_ID30 = """  if(hero) hero.innerHTML = 'Bienvenue sur <span>l\'évaluation</span>';
  if(heroSub) heroSub.textContent = 'Opération ID30 — Renseignez vos informations pour commencer le test';
  posteSelect.innerHTML = `
    <option value="">-- Sélectionnez votre poste --</option>
    <option value="call-center">Agent Call Center (ID30)</option>
    <option value="back-office">Agent Back Office (ID30)</option>
    <option value="inspecteur">Inspecteur (ID30 &amp; Orange QR)</option>
    <option value="superviseur">Superviseur (Agent &amp; Orange Money)</option>
  `;"""

    txt = txt.replace(OLD_SETUP, NEW_SETUP_ID30)

    # startExam — banque ID30
    txt = txt.replace(
        '  const bank = state.currentOperation === \'orange\' ? QUESTIONS_BY_POSTE_ORANGE : QUESTIONS_BY_POSTE;\n  // Niveau intermédiaire uniquement pour l\'opération Orange (points:1 = intermédiaire)\n  let rawQuestions = bank[poste] || [];\n  if(state.currentOperation === \'orange\') {\n    rawQuestions = rawQuestions.filter(q => q.points === 1 && q.type !== \'open\');\n  }',
        '  const bank = QUESTIONS_BY_POSTE;\n  let rawQuestions = bank[poste] || [];'
    )

    # Supprimer QUESTIONS_BY_POSTE_ORANGE
    txt = re.sub(
        r'const QUESTIONS_BY_POSTE_ORANGE = \{.*?\};\n\n',
        '// QUESTIONS ORANGE retirées (fichier ID30 uniquement)\n\n',
        txt, flags=re.DOTALL
    )

    # Admin filter — simplifier (garder seulement id30)
    txt = txt.replace(
        "      <button id=\"admin-filter-orange\" class=\"btn btn-secondary btn-sm\" onclick=\"setAdminFilter('orange')\" style=\"border-color:#f97316;color:#c2410c\">🟠 Orange</button>\n      <button id=\"admin-filter-id30\" class=\"btn btn-secondary btn-sm\" onclick=\"setAdminFilter('id30')\" style=\"border-color:#2563eb;color:#1e40af\">🔵 ID30</button>",
        "      <span style=\"font-size:0.85rem;color:var(--text-muted);padding:6px 0\">🔵 Évaluation Connectel ID30</span>"
    )

    txt = txt.replace(
        "  ['all','orange','id30'].forEach(f => {\n    const btn = document.getElementById('admin-filter-' + f);\n    if(btn) btn.className = 'btn btn-sm ' + (f === filter ? 'btn-primary' : 'btn-secondary');\n  });",
        "  // filtres non utilisés en mode ID30"
    )

    return txt


orange_html = make_orange(src)
id30_html = make_id30(src)

with open('evaluation_orange.html', 'w', encoding='utf-8') as f:
    f.write(orange_html)

with open('evaluation_id30.html', 'w', encoding='utf-8') as f:
    f.write(id30_html)

print("OK: evaluation_orange.html créé ({} lignes)".format(orange_html.count('\n')))
print("OK: evaluation_id30.html créé ({} lignes)".format(id30_html.count('\n')))
