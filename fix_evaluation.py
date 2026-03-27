"""
Mise a jour evaluation.html :
- Ajout champ poste (Call Center / Back Office / Inspecteur / Superviseur)
- 30 questions par poste chargees automatiquement
- Conservation du systeme de code personnel
"""

IN  = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\evaluation.html"
OUT = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\evaluation.html"

with open(IN, "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================
# 1. AJOUTER LE SELECT POSTE dans le formulaire candidat
# ============================================================
OLD_PHONE = '''      <div class="form-group">
        <label>Contact (téléphone)</label>
        <input type="tel" id="candidate-phone" placeholder="+225 XX XX XX XX XX">
      </div>

      <div id="candidate-entry-error"'''

NEW_PHONE = '''      <div class="form-group">
        <label>Contact (téléphone)</label>
        <input type="tel" id="candidate-phone" placeholder="+225 XX XX XX XX XX">
      </div>
      <div class="form-group">
        <label>Votre poste *</label>
        <select id="candidate-poste" style="width:100%;padding:10px 14px;border:1.5px solid var(--border);border-radius:var(--radius);font-size:0.95rem;font-family:inherit;background:var(--surface);color:var(--text);cursor:pointer">
          <option value="">-- Sélectionnez votre poste --</option>
          <option value="call-center">Agent Call Center (ID30)</option>
          <option value="back-office">Agent Back Office (ID30)</option>
          <option value="inspecteur">Inspecteur (ID30 &amp; Orange QR)</option>
          <option value="superviseur">Superviseur (Agent &amp; Orange Money)</option>
        </select>
      </div>

      <div id="candidate-entry-error"'''

assert OLD_PHONE in html, "Phone section not found"
html = html.replace(OLD_PHONE, NEW_PHONE)
print("Poste select added OK")

# ============================================================
# 2. MODIFIER startExam() — lire poste + charger questions
# ============================================================
OLD_START = '''function startExam() {
  const firstname = document.getElementById('candidate-firstname').value.trim();
  const lastname = document.getElementById('candidate-lastname').value.trim();
  const email = document.getElementById('candidate-email').value.trim();
  const phone = document.getElementById('candidate-phone').value.trim();
  const errorEl = document.getElementById('candidate-entry-error');

  if(!firstname || !lastname || !email) {
    errorEl.style.display = 'flex';
    errorEl.textContent = '❌ Veuillez remplir tous les champs obligatoires (*).';
    return;
  }
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    errorEl.style.display = 'flex';
    errorEl.textContent = '❌ Adresse email invalide.';
    return;
  }
  if(state.config.accessCode) {
    const code = document.getElementById('candidate-access-code').value.trim().toUpperCase();
    if(code !== state.config.accessCode.toUpperCase()) {
      errorEl.style.display = 'flex';
      errorEl.textContent = '❌ Code d\\'accès incorrect.';
      return;
    }
  }
  if(state.questions.length === 0) {
    errorEl.style.display = 'flex';
    errorEl.textContent = '❌ Aucune question disponible. Contactez l\\'administrateur.';
    return;
  }

  errorEl.style.display = 'none';
  state.currentCandidate = { firstname, lastname, email, phone };'''

NEW_START = '''function startExam() {
  const firstname = document.getElementById('candidate-firstname').value.trim();
  const lastname = document.getElementById('candidate-lastname').value.trim();
  const email = document.getElementById('candidate-email').value.trim();
  const phone = document.getElementById('candidate-phone').value.trim();
  const poste = document.getElementById('candidate-poste').value;
  const errorEl = document.getElementById('candidate-entry-error');

  if(!firstname || !lastname || !email) {
    errorEl.style.display = 'flex';
    errorEl.textContent = '❌ Veuillez remplir tous les champs obligatoires (*).';
    return;
  }
  if(!poste) {
    errorEl.style.display = 'flex';
    errorEl.textContent = '❌ Veuillez sélectionner votre poste.';
    return;
  }
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    errorEl.style.display = 'flex';
    errorEl.textContent = '❌ Adresse email invalide.';
    return;
  }
  if(state.config.accessCode) {
    const code = document.getElementById('candidate-access-code').value.trim().toUpperCase();
    if(code !== state.config.accessCode.toUpperCase()) {
      errorEl.style.display = 'flex';
      errorEl.textContent = '❌ Code d\\'accès incorrect.';
      return;
    }
  }

  // Charger les questions adaptees au poste
  const posteLabels = {
    'call-center': 'Agent Call Center',
    'back-office': 'Agent Back Office',
    'inspecteur': 'Inspecteur',
    'superviseur': 'Superviseur'
  };
  state.questions = (QUESTIONS_BY_POSTE[poste] || []).map((q, i) => ({...q, id: i + 1}));
  if(state.questions.length === 0) {
    errorEl.style.display = 'flex';
    errorEl.textContent = '❌ Aucune question disponible pour ce poste.';
    return;
  }
  state.config.title = 'Evaluation — ' + posteLabels[poste];

  errorEl.style.display = 'none';
  state.currentCandidate = { firstname, lastname, email, phone, poste, posteLabel: posteLabels[poste] };'''

assert OLD_START in html, "startExam not found"
html = html.replace(OLD_START, NEW_START)
print("startExam updated OK")

# ============================================================
# 3. AFFICHER LE POSTE dans les resultats
# ============================================================
OLD_RESULT_NAME = "  document.getElementById('result-candidate-name').textContent = `${result.firstname} ${result.lastname}`;"
NEW_RESULT_NAME = "  document.getElementById('result-candidate-name').textContent = `${result.firstname} ${result.lastname}${result.posteLabel ? ' — ' + result.posteLabel : ''}`;"
html = html.replace(OLD_RESULT_NAME, NEW_RESULT_NAME)
print("result display updated OK")

# ============================================================
# 4. AJOUTER QUESTIONS_BY_POSTE avant loadSampleQuestions
# ============================================================

QUESTIONS_JS = r"""
// ============================================================
// BANQUE DE QUESTIONS PAR POSTE — 30 questions chacun
// ============================================================
const QUESTIONS_BY_POSTE = {

// ─────────────────────────────────────────────────────────────
// AGENT CALL CENTER
// ─────────────────────────────────────────────────────────────
'call-center': [
  { type:'qcm', text:"Quel est l'objectif quotidien minimum d'un agent Call Center sur le projet ID30 ?", options:["10 fiches validées","15 fiches validées","20 fiches validées","5 fiches validées"], correct:1, points:1 },
  { type:'qcm', text:"MAFA Holding est mandatée par quelle institution pour conduire le projet ID30 ?", options:["Orange CI","La mairie d'Abidjan","Le Ministère du Commerce et de l'Industrie","La Banque Mondiale"], correct:2, points:1 },
  { type:'qcm', text:"Que signifie l'acronyme KYC dans le contexte du projet ID30 ?", options:["Know Your Company","Know Your Customer","Keep Your Contact","Know Your Country"], correct:1, points:1 },
  { type:'qcm', text:"Quel outil CRM est utilisé par les agents Call Center pour gérer les appels ID30 ?", options:["Salesforce","HubSpot","Connectel","Excel"], correct:2, points:1 },
  { type:'qcm', text:"En phase actuelle, quelle est la mission principale du Call Center ID30 ?", options:["Enrôler de nouveaux entrepreneurs","Prendre des rendez-vous et mettre à jour les dossiers existants","Vendre des produits Orange Money","Recruter des agents terrain"], correct:1, points:1 },
  { type:'qcm', text:"Lors d'un premier appel infructueux, combien de tentatives au total l'agent doit-il effectuer avant de classer le dossier ?", options:["1 tentative uniquement","2 tentatives","3 tentatives au total","5 tentatives"], correct:2, points:1 },
  { type:'qcm', text:"Quel délai minimum est recommandé entre deux tentatives d'appel sur un même dossier ?", options:["15 minutes","30 minutes","2 heures","24 heures"], correct:2, points:1 },
  { type:'qcm', text:"Que signifie le statut 'Refus ferme' dans Connectel ?", options:["L'entrepreneur a raccroché sans répondre","L'entrepreneur refuse définitivement toute mise à jour","Le numéro de téléphone est invalide","Le rendez-vous n'est pas confirmé"], correct:1, points:1 },
  { type:'qcm', text:"Quel document l'entrepreneur doit-il présenter lors du rendez-vous terrain pour valider son dossier ID30 ?", options:["Passeport biométrique uniquement","CNI ou attestation d'identité valide","Carte de séjour","Permis de conduire"], correct:1, points:1 },
  { type:'qcm', text:"La Carte Entreprenant est remise à l'entrepreneur dans quel délai après validation du dossier ?", options:["Immédiatement lors du rendez-vous terrain","Sous 48 heures par courrier","Sous 7 jours ouvrés","Après validation du Ministère"], correct:0, points:1 },
  { type:'qcm', text:"Comment l'agent Call Center doit-il se présenter en début d'appel ?", options:["Par son prénom uniquement","En donnant son nom, prénom et l'entreprise MAFA Holding","Sans se présenter, directement dans le sujet","Au nom du Ministère uniquement"], correct:1, points:1 },
  { type:'qcm', text:"Quel est le rôle du superviseur Call Center par rapport aux agents ?", options:["Prendre tous les appels difficiles à la place des agents","Valider les dossiers directement en Back Office","Encadrer, suivre la performance et soutenir les agents","Gérer uniquement les impressions de cartes"], correct:2, points:1 },
  { type:'qcm', text:"Que fait l'agent si l'entrepreneur demande un rendez-vous dans une zone non encore couverte ?", options:["Refuse la demande et clôture le dossier","Transfère directement au superviseur sans rien noter","Note la demande et la signale pour planification de couverture","Propose un RDV dans la ville la plus proche"], correct:2, points:1 },
  { type:'qcm', text:"Comment l'agent doit-il traiter un entrepreneur mécontent ou agressif au téléphone ?", options:["Raccrocher immédiatement","Rester calme, écouter et proposer un rappel ultérieur","Transférer systématiquement au superviseur dès le 1er signe","Ignorer les remarques et continuer le script"], correct:1, points:1 },
  { type:'qcm', text:"Dans Connectel, qu'indique le statut 'RDV confirmé' ?", options:["Le dossier est entièrement validé et archivé","L'entrepreneur a accepté la date et l'heure du rendez-vous","La Carte Entreprenant a été imprimée","L'agent a transmis le dossier au Back Office"], correct:1, points:1 },
  { type:'qcm', text:"Quelle langue est principalement utilisée dans les appels du Call Center ID30 ?", options:["Anglais uniquement","Dioula uniquement","Français et langues locales selon l'entrepreneur","Espagnol"], correct:2, points:1 },
  { type:'qcm', text:"Que doit faire l'agent si le numéro enregistré dans Connectel est erroné ?", options:["Clôturer le dossier immédiatement","Mettre à jour le numéro dans Connectel directement","Signaler au Back Office pour correction et mise à jour","Appeler un autre entrepreneur en attendant"], correct:2, points:1 },
  { type:'qcm', text:"Quel comportement est strictement interdit pendant les appels du Call Center ID30 ?", options:["Prendre des notes sur le dossier","Utiliser un script d'appel","Promouvoir d'autres offres commerciales non liées à ID30","Confirmer le rendez-vous à voix haute"], correct:2, points:1 },
  { type:'vf', text:"Le Call Center ID30 peut clôturer définitivement un dossier dès le premier appel sans réponse.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"L'agent Call Center doit toujours vérifier le numéro de téléphone du dossier avant de lancer l'appel.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'vf', text:"Un entrepreneur peut refuser la mise à jour de son dossier ID30 sans que l'agent puisse l'en empêcher.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'vf', text:"L'agent Call Center est autorisé à modifier directement les informations KYC dans Connectel.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'qcm', text:"Que signifie 'Dossier mis en attente' dans Connectel ?", options:["Le dossier a été validé par le Back Office","L'action est suspendue temporairement en attendant une information ou une disponibilité","L'entrepreneur a été contacté avec succès","La Carte Entreprenant est prête"], correct:1, points:1 },
  { type:'qcm', text:"Quelle information est obligatoire pour créer une prise de RDV dans Connectel ?", options:["La couleur de la Carte Entreprenant souhaitée","La date et l'heure précises du rendez-vous","L'adresse email de l'entrepreneur","Le nombre d'employés de l'entrepreneur"], correct:1, points:1 },
  { type:'qcm', text:"Combien de tentatives maximum sont recommandées par jour sur un même dossier ?", options:["1 seule","2 maximum","3 minimum","Sans limite"], correct:1, points:1 },
  { type:'qcm', text:"Que doit faire l'agent si l'entrepreneur confirme avoir déjà reçu sa Carte Entreprenant ?", options:["Recommencer l'enrôlement","Ignorer l'information","Marquer le dossier comme 'Déjà traité' et le clôturer","Supprimer le dossier"], correct:2, points:1 },
  { type:'qcm', text:"Quel ton doit adopter l'agent Call Center lors des appels ?", options:["Familier et décontracté","Professionnel, courtois et clair","Autoritaire et directif","Rapide sans formules de politesse"], correct:1, points:1 },
  { type:'qcm', text:"Quelle est la durée maximale recommandée d'un appel Call Center ID30 ?", options:["5 minutes","10 minutes","20 minutes","30 minutes"], correct:1, points:1 },
  { type:'vf', text:"Le superviseur Call Center peut accéder à Connectel pour suivre les dossiers de son équipe.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'open', text:"Expliquez en quelques lignes comment vous géreriez un entrepreneur qui refuse catégoriquement la mise à jour de son dossier ID30 lors de votre appel.", options:[], correct:0, points:3 }
],

// ─────────────────────────────────────────────────────────────
// AGENT BACK OFFICE
// ─────────────────────────────────────────────────────────────
'back-office': [
  { type:'qcm', text:"Quel est le taux de complétion minimum requis pour valider un dossier Back Office ID30 ?", options:["70%","80%","90%","95%"], correct:2, points:1 },
  { type:'qcm', text:"Que signifie l'acronyme KYB dans le contexte du projet ID30 ?", options:["Know Your Business","Keep Your Balance","Know Your Budget","Key Your Base"], correct:0, points:1 },
  { type:'qcm', text:"Quel appareil est utilisé par les agents pour imprimer la Carte Entreprenant sur le terrain ?", options:["HP LaserJet","FAMOCO PX400","Zebra ZT230","Epson L3150"], correct:1, points:1 },
  { type:'qcm', text:"Quel score minimum de Proof of Life est recommandé par les agents sur le terrain ?", options:["50","60","70","80"], correct:2, points:1 },
  { type:'qcm', text:"Si le nom sur la CNI diffère du nom dans le formulaire, quelle décision prend le Back Office ?", options:["Validé quand même","Mis en attente","Rejeté","Transmis au superviseur"], correct:2, points:1 },
  { type:'qcm', text:"Quel est le délai maximum pour traiter un dossier reçu en Back Office ?", options:["24 heures","48 heures","72 heures","1 semaine"], correct:1, points:1 },
  { type:'qcm', text:"Que désigne le terme 'Proof of Life' dans le processus de vérification ?", options:["Une attestation médicale de l'entrepreneur","Une preuve biométrique que l'entrepreneur est bien présent lors de la capture","Une lettre de témoignage d'un voisin","Un test de personnalité de l'entrepreneur"], correct:1, points:1 },
  { type:'qcm', text:"Que doit vérifier le Back Office concernant les coordonnées GPS du dossier ?", options:["Que le lieu se situe impérativement au centre-ville","Que les coordonnées correspondent réellement au lieu d'activité déclaré","Que le GPS du FAMOCO est activé","La distance entre le lieu et Abidjan"], correct:1, points:1 },
  { type:'qcm', text:"Quel statut est attribué à un dossier dont les images de documents sont floues ou illisibles ?", options:["Validé avec réserve","Mis en attente","Rejeté — retour terrain requis","Archivé automatiquement"], correct:2, points:1 },
  { type:'qcm', text:"Que contient typiquement la fiche de visite complétée par l'agent terrain ?", options:["Seulement les photos biométriques","Les coordonnées GPS, informations KYC/KYB et photos","Le montant du solde Orange Money de l'entrepreneur","Le code QR uniquement"], correct:1, points:1 },
  { type:'qcm', text:"En cas de dossier doublon (même entrepreneur enregistré deux fois), que fait le Back Office ?", options:["Valide les deux dossiers","Conserve le plus récent et archive l'ancien après vérification","Supprime les deux dossiers","Transfère au Call Center pour re-contact"], correct:1, points:1 },
  { type:'qcm', text:"Quel champ du formulaire KYB concerne l'activité principale de l'entrepreneur ?", options:["Nom complet de l'entrepreneur","Numéro de la CNI","Secteur d'activité","Adresse email personnelle"], correct:2, points:1 },
  { type:'qcm', text:"Quel est le score minimum Proof of Life accepté par le système (seuil minimal) ?", options:["40","50","60","70"], correct:2, points:1 },
  { type:'qcm', text:"Lorsqu'un dossier est validé par le Back Office, quelle étape suit immédiatement ?", options:["Envoi automatique au Ministère","Impression de la Carte Entreprenant par l'agent terrain","Appel de confirmation au superviseur","Paiement Orange Money de frais"], correct:1, points:1 },
  { type:'qcm', text:"Comment le Back Office signale-t-il un dossier nécessitant une nouvelle visite terrain ?", options:["Par téléphone au superviseur terrain","Par email à l'agent concerné","Via le statut 'Rejeté — Retour terrain' dans le système","Par courrier postal au chef d'équipe"], correct:2, points:1 },
  { type:'qcm', text:"Le Back Office peut-il modifier directement les informations KYC d'un dossier ?", options:["Oui, librement sans restriction","Non, toute correction nécessite une nouvelle visite terrain","Oui, mais uniquement avec accord du superviseur","Non, jamais même en cas d'erreur évidente"], correct:1, points:1 },
  { type:'qcm', text:"Combien de photos minimum sont requises dans un dossier pour validation Back Office ?", options:["1 photo (portrait)","2 photos","3 photos minimum","5 photos"], correct:2, points:1 },
  { type:'qcm', text:"Que doit faire le Back Office si les données GPS et les données déclarées sont très éloignées géographiquement ?", options:["Valider quand même si les photos sont bonnes","Rejeter le dossier et demander une nouvelle visite avec correction GPS","Modifier manuellement les coordonnées GPS en Back Office","Ignorer l'écart si inférieur à 10 km"], correct:1, points:1 },
  { type:'qcm', text:"Quelle est la résolution minimum acceptable pour les photos de documents scannés ?", options:["72 DPI","150 DPI","300 DPI","600 DPI"], correct:2, points:1 },
  { type:'qcm', text:"Quel est le rôle de l'inspecteur par rapport au travail du Back Office ?", options:["Remplacer le Back Office pour les cas complexes","Valider physiquement sur le terrain ce que le Back Office vérifie à distance","Imprimer les cartes à la place des agents","Gérer les accès à la plateforme Connectel"], correct:1, points:1 },
  { type:'vf', text:"Le Back Office peut valider un dossier même si le score Proof of Life est inférieur à 60.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"La Carte Entreprenant peut être imprimée avant la validation du dossier par le Back Office.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Un dossier rejeté par le Back Office nécessite obligatoirement une nouvelle visite terrain.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'vf', text:"Le Back Office est responsable de la vérification de la cohérence entre les données CNI et le formulaire.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'qcm', text:"Que signifie 'Dossier en corbeille Back Office' ?", options:["Le dossier a été supprimé","Le dossier est en attente de traitement par un agent Back Office","Le dossier a été envoyé au Ministère","Le dossier est archivé définitivement"], correct:1, points:1 },
  { type:'qcm', text:"Quel indicateur de performance est primordial pour le Back Office ?", options:["Le nombre d'appels passés par jour","Le taux de validation de dossiers dans les délais","Le nombre de cartes imprimées","La distance parcourue par les agents terrain"], correct:1, points:1 },
  { type:'qcm', text:"En cas de CNI expirée présentée lors de la visite, que décide le Back Office ?", options:["Valider quand même si la photo correspond","Rejeter et demander une CNI valide","Contacter le Ministère directement","Archiver le dossier"], correct:1, points:1 },
  { type:'qcm', text:"Combien de jours maximum pour qu'un dossier rejeté revienne avec corrections ?", options:["24 heures","3 jours","5 jours ouvrés","2 semaines"], correct:2, points:1 },
  { type:'vf', text:"Le Back Office peut contacter directement l'entrepreneur pour demander des documents complémentaires.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'open', text:"Vous recevez un dossier où la photo biométrique montre une personne différente de celle sur la CNI. Décrivez la procédure complète que vous appliquez.", options:[], correct:0, points:3 }
],

// ─────────────────────────────────────────────────────────────
// INSPECTEUR
// ─────────────────────────────────────────────────────────────
'inspecteur': [
  { type:'qcm', text:"Que signifie le projet ID30 dans le contexte de MAFA Holding ?", options:["Identifier 30 marchés en Côte d'Ivoire","Identification des entreprenants dans 30 grandes villes","Un identifiant numérique à 30 chiffres","30 inspecteurs assignés par ville"], correct:1, points:1 },
  { type:'qcm', text:"Sur la carte de l'application Inspector, que représente un point ORANGE ?", options:["Un problème technique signalé","Un entrepreneur enrôlé par un agent, en attente de confirmation","Un inspecteur actuellement actif sur le secteur","Un point GPS avec coordonnées incorrectes"], correct:1, points:1 },
  { type:'qcm', text:"Quelle précision GPS est considérée comme 'Excellent' dans l'application Inspector Orange ?", options:["≤ 15 mètres","≤ 10 mètres","≤ 5 mètres","≤ 20 mètres"], correct:2, points:1 },
  { type:'qcm', text:"Combien d'étapes comporte la Fiche de Visite dans l'application Inspector Orange ?", options:["5 étapes","6 étapes","7 étapes","8 étapes"], correct:3, points:1 },
  { type:'qcm', text:"Un problème de niveau P1 doit être traité dans quel délai maximum ?", options:["< 2 heures","< 24 heures","< 5 jours","Dans la semaine"], correct:0, points:1 },
  { type:'qcm', text:"Quel est le format correct du code marchand Orange Money dans l'application Inspector ?", options:["CI-OM-XXXXX","OM-CI-XXXXX","OR-CI-XXXXX","OM-XX-XXXXX"], correct:1, points:1 },
  { type:'qcm', text:"Combien de visites d'inspection minimum par jour est recommandé pour un inspecteur ?", options:["5 visites","8 visites","10 visites","15 visites"], correct:2, points:1 },
  { type:'qcm', text:"Quel outil l'inspecteur utilise-t-il pour scanner le QR Code sur la Carte Entreprenant ?", options:["Un lecteur code-barres laser de bureau","L'application mobile Inspector Orange sur smartphone","Un scanner de documents portable","L'appareil FAMOCO PX400"], correct:1, points:1 },
  { type:'qcm', text:"Que vérifie principalement l'inspecteur lors d'une visite de contrôle ?", options:["Le chiffre d'affaires mensuel de l'entrepreneur","La concordance entre la Carte Entreprenant et la réalité terrain","La qualité du réseau Orange dans la zone","L'état du compte Orange Money de l'entrepreneur"], correct:1, points:1 },
  { type:'qcm', text:"Que doit faire l'inspecteur s'il constate que l'activité déclarée ne correspond pas à la réalité terrain ?", options:["Ignorer l'écart et valider quand même","Corriger lui-même les données dans l'application","Signaler comme non-conforme et remonter au superviseur","Retirer physiquement la Carte Entreprenant au commerçant"], correct:2, points:1 },
  { type:'qcm', text:"Le QR Code sur la Carte Entreprenant renvoie vers quelles informations ?", options:["Le solde du compte Orange Money du marchand","La fiche d'identité officielle de l'entreprenant","La liste des prix Orange disponibles","La liste des agents ayant traité le dossier"], correct:1, points:1 },
  { type:'qcm', text:"Comment l'inspecteur documente-t-il sa visite terrain dans l'application ?", options:["Par un appel téléphonique au superviseur","Via un rapport papier envoyé au bureau","Via l'application : photos, GPS, statut de conformité","Par email avec photos en pièce jointe"], correct:2, points:1 },
  { type:'qcm', text:"Quelle action est absolument interdite pour un inspecteur lors d'une visite terrain ?", options:["Scanner le QR Code de la carte","Accepter de l'argent ou des cadeaux de l'entrepreneur","Prendre des photos du lieu d'activité","Remplir le rapport de visite"], correct:1, points:1 },
  { type:'qcm', text:"En cas d'entrepreneur absent lors de la visite de contrôle, l'inspecteur doit :", options:["Clôturer le dossier comme conforme","Attendre sur place aussi longtemps que nécessaire","Reprogrammer la visite et signaler l'absence","Contacter directement le Call Center"], correct:2, points:1 },
  { type:'qcm', text:"Quel est le délai maximum pour soumettre son rapport après une visite d'inspection ?", options:["6 heures après la visite","24 heures après la visite","48 heures","En fin de semaine"], correct:1, points:1 },
  { type:'qcm', text:"Que signifie le statut 'Conforme' attribué par l'inspecteur à un dossier ?", options:["La Carte Entreprenant a été physiquement remise","L'entrepreneur et son activité correspondent exactement aux données enregistrées","Le paiement Orange Money a été effectué","Le dossier est archivé définitivement"], correct:1, points:1 },
  { type:'qcm', text:"Combien de points de contrôle minimum l'inspecteur vérifie-t-il lors d'une visite ?", options:["3 points","5 points minimum","7 points","10 points"], correct:1, points:1 },
  { type:'qcm', text:"L'inspecteur peut-il modifier directement les données d'un dossier dans l'application ?", options:["Oui, il a accès complet en modification","Non, il signale uniquement les non-conformités","Oui, mais seulement avec la confirmation du superviseur","Oui, uniquement les coordonnées GPS"], correct:1, points:1 },
  { type:'qcm', text:"Que doit faire l'inspecteur si le QR Code imprimé sur la Carte Entreprenant est illisible ?", options:["Valider quand même et noter dans le rapport","Ignorer et passer à la prochaine visite","Signaler comme défaut technique et demander le remplacement de la carte","Appeler directement l'imprimante FAMOCO"], correct:2, points:1 },
  { type:'qcm', text:"Quel est le principal indicateur de performance d'un inspecteur ?", options:["Le nombre d'entrepreneurs signalés comme non-conformes","Le taux de conformité des visites effectuées","Le nombre de kilomètres parcourus par jour","La vitesse de scan des QR Codes"], correct:1, points:1 },
  { type:'vf', text:"L'inspecteur peut valider un dossier comme conforme sans avoir scanné le QR Code de la carte.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Un inspecteur doit soumettre son rapport dans les 24 heures suivant chaque visite.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'vf', text:"L'inspecteur est autorisé à prendre des photos supplémentaires du lieu d'activité pour renforcer son rapport.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'vf', text:"Un point VERT sur la carte Inspector signifie que l'entrepreneur a déjà été confirmé comme conforme.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'qcm', text:"Que signifie le niveau P2 dans la gestion des problèmes Inspector Orange ?", options:["URGENT — traitement < 2h","HAUTE priorité — traitement < 24h","STANDARD — traitement < 5 jours","FAIBLE — traitement < 2 semaines"], correct:1, points:1 },
  { type:'qcm', text:"Quelle précision GPS est jugée 'Acceptable' (mais pas excellente) par l'application Inspector ?", options:["≤ 3 mètres","≤ 5 mètres","≤ 10 mètres","≤ 25 mètres"], correct:2, points:1 },
  { type:'qcm', text:"Sur la carte Inspector, un point VERT représente :", options:["Un entrepreneur en cours d'enrôlement","Un entrepreneur confirmé comme actif et conforme","Un entrepreneur signalé comme non-conforme","Un inspecteur disponible dans le secteur"], correct:1, points:1 },
  { type:'qcm', text:"Lors d'un refus de scan QR Code par l'entrepreneur, l'inspecteur doit :", options:["Forcer le scan sans consentement","Accepter et valider quand même","Documenter le refus et signaler au superviseur","Annuler la visite sans rapport"], correct:2, points:1 },
  { type:'vf', text:"L'application Inspector Orange fonctionne uniquement avec une connexion Internet active.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'open', text:"Lors d'une visite d'inspection, vous constatez que le commerce déclaré n'existe plus à l'adresse indiquée. Décrivez la procédure complète que vous suivez.", options:[], correct:0, points:3 }
],

// ─────────────────────────────────────────────────────────────
// SUPERVISEUR
// ─────────────────────────────────────────────────────────────
'superviseur': [
  { type:'qcm', text:"L'application Agent peut-elle fonctionner sans connexion Internet ?", options:["Non, elle nécessite toujours une connexion active","Oui, pour le chargement et le transfert de données d'activités","Oui, toutes les fonctions sont disponibles hors-ligne","Non, aucune fonction ne marche sans connexion"], correct:1, points:1 },
  { type:'qcm', text:"Lors de l'enrôlement O'calm, combien de chiffres comporte le code OTP envoyé au marchand ?", options:["3 chiffres","4 chiffres","6 chiffres","8 chiffres"], correct:1, points:1 },
  { type:'qcm', text:"Après un déploiement QR Code réussi, quelle est l'action obligatoire de l'agent avant de quitter le point de vente ?", options:["Se déconnecter de l'application","Appeler immédiatement le superviseur","Effectuer un test de transaction avec le marchand","Synchroniser immédiatement les données"], correct:2, points:1 },
  { type:'qcm', text:"Quel est le rôle du superviseur dans l'application Superviseur Orange ?", options:["Effectuer lui-même les enrôlements O'calm","Piloter la performance, valider les déploiements et gérer son équipe d'agents","Imprimer les QR Codes pour les marchands","Gérer directement les comptes Orange Money des marchands"], correct:1, points:1 },
  { type:'qcm', text:"Quelle étape suit immédiatement le scan du QR Code à blanc lors d'un enrôlement O'calm ?", options:["L'envoi de l'OTP au marchand","Le pré-remplissage automatique du formulaire d'enrôlement","La validation Back Office","La synchronisation des données"], correct:1, points:1 },
  { type:'qcm', text:"Comment l'agent accède-t-il à la liste de ses marchands enrôlés dans l'application Agent ?", options:["Via le menu 'Profil Agent'","Via le menu 'Mes Marchands' ou 'Portefeuille'","En contactant le superviseur","Via le *144# d'Orange Money"], correct:1, points:1 },
  { type:'qcm', text:"Que doit faire l'agent si le marchand ne reçoit pas le code OTP lors de l'enrôlement ?", options:["Annuler l'enrôlement et repartir","Renseigner n'importe quel code à 4 chiffres","Attendre 2 minutes puis demander un renvoi du code","Appeler le superviseur pour saisir le code à sa place"], correct:2, points:1 },
  { type:'qcm', text:"Quelle est la fréquence de synchronisation recommandée pour l'application Agent ?", options:["Une fois par semaine","À chaque fois qu'une connexion Internet est disponible","Uniquement quand le superviseur le demande","Une fois par mois"], correct:1, points:1 },
  { type:'qcm', text:"Dans l'application Superviseur, que permet l'indicateur 'Taux de déploiement' ?", options:["Mesurer la qualité du réseau Orange dans le secteur","Suivre le pourcentage de marchands cibles effectivement enrôlés par les agents","Calculer le montant total des transactions marchandes","Contrôler l'autonomie de la batterie des terminaux"], correct:1, points:1 },
  { type:'qcm', text:"Que se passe-t-il si un agent tente d'enrôler un marchand déjà enregistré dans le système ?", options:["L'enrôlement se fait normalement en créant un doublon","L'application affiche une alerte 'Marchand déjà enregistré' et bloque l'enrôlement","L'ancien enrôlement est automatiquement écrasé","L'enrôlement est accepté mais mis en attente de validation"], correct:1, points:1 },
  { type:'qcm', text:"Comment le superviseur valide-t-il un déploiement QR Code effectué par un agent ?", options:["En appelant le marchand par téléphone","Via l'application Superviseur : sélection du déploiement > Valider","En se déplaçant systématiquement chez chaque marchand","Automatiquement sans action de sa part"], correct:1, points:1 },
  { type:'qcm', text:"Quelle information l'agent doit-il absolument vérifier avant de quitter un point de vente après un déploiement ?", options:["Le nombre de clients du marchand","Que le test de transaction a été effectué avec succès","La taille du QR Code affiché","Le nom du propriétaire du local"], correct:1, points:1 },
  { type:'qcm', text:"Dans quel cas l'application Agent fonctionne-t-elle uniquement avec une connexion Internet active ?", options:["Pour la saisie des données d'enrôlement","Pour le déploiement du QR Code et la synchronisation finale","Pour afficher la liste des marchands","Pour ouvrir l'application"], correct:1, points:1 },
  { type:'qcm', text:"Quel est l'objectif quotidien minimum recommandé pour un agent en termes de déploiements QR Code ?", options:["2 déploiements","5 déploiements","10 déploiements","15 déploiements"], correct:1, points:1 },
  { type:'qcm', text:"Que doit faire l'agent si le scan du QR Code à blanc échoue (code non reconnu) ?", options:["Saisir manuellement le numéro marchand","Vérifier que le QR Code est dans le bon kit et rescanner","Contacter le 0808 immédiatement","Annuler et informer le marchand que l'enrôlement est impossible"], correct:1, points:1 },
  { type:'qcm', text:"Comment l'application Agent gère-t-elle les données collectées hors-ligne ?", options:["Elle les supprime si non synchronisées sous 24h","Elle les stocke localement et les synchronise à la prochaine connexion","Elle bloque toute nouvelle saisie jusqu'à synchronisation","Elle envoie les données par SMS au superviseur"], correct:1, points:1 },
  { type:'qcm', text:"Que peut consulter un superviseur dans son tableau de bord en temps réel ?", options:["Uniquement ses propres statistiques personnelles","La performance de chaque agent, les déploiements en attente et le taux global","Le solde des comptes Orange Money des marchands","L'historique des appels téléphoniques des agents"], correct:1, points:1 },
  { type:'qcm', text:"Quelle action permet de finaliser un enrôlement O'calm et activer le compte marchand ?", options:["Appuyer sur 'Terminer' dans l'application sans autre vérification","Saisir le code OTP à 4 chiffres reçu par le marchand puis confirmer","Envoyer une photo du QR Code au superviseur","Attendre 24h pour l'activation automatique"], correct:1, points:1 },
  { type:'qcm', text:"Quel profil OM Business convient à un commerçant avec un CA annuel inférieur à 150 000 FCFA ?", options:["OM Business Classique","OM Business Essentiel","OM Business Premium","OM Business Pro"], correct:1, points:1 },
  { type:'qcm', text:"Quel est le tarif d'encaissement QR Code pour un marchand Essentiel jusqu'à 50 000 FCFA/jour ?", options:["1% de la transaction","500 FCFA forfait","0% jusqu'à 50 000 FCFA/jour","0,5%"], correct:2, points:1 },
  { type:'vf', text:"Le superviseur peut annuler un déploiement QR Code validé si une erreur est détectée.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'vf', text:"Un agent peut valider lui-même ses propres déploiements sans intervention du superviseur.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Le test de transaction après déploiement QR Code est facultatif si le scan a réussi.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"L'application Superviseur permet de visualiser la géolocalisation des agents en temps réel.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'qcm', text:"Que doit faire le superviseur si un agent atteint systématiquement moins de 3 déploiements par jour ?", options:["Ignorer si cela ne dure qu'une journée","Organiser un entretien individuel pour identifier les blocages et apporter du soutien","Remplacer l'agent immédiatement","Doubler la zone de l'agent concerné"], correct:1, points:1 },
  { type:'qcm', text:"Lors de la création d'un compte OM Business Non-OM, combien d'étapes comporte le parcours KYC standard ?", options:["2 étapes","3 étapes","5 étapes","8 étapes"], correct:2, points:1 },
  { type:'qcm', text:"Quel numéro doit appeler un marchand en cas de problème avec son application OM Business ?", options:["Le 15 (urgences)","Le 0808 (service client Orange Money)","Le 117 (police)","Le 1313 (Orange CI)"], correct:1, points:1 },
  { type:'qcm', text:"Comment le superviseur répartit-il équitablement les zones de déploiement entre ses agents ?", options:["Par tirage au sort","En fonction du lieu de résidence des agents","En analysant les capacités, la mobilité et les performances de chaque agent","Alphabétiquement par nom d'agent"], correct:2, points:1 },
  { type:'vf', text:"Le superviseur est responsable des résultats collectifs de son équipe devant la hiérarchie.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'open', text:"En tant que superviseur, un de vos agents a un taux de déploiement de 40% alors que l'équipe est à 85%. Décrivez les étapes de votre plan d'action pour l'aider à améliorer ses performances.", options:[], correct:0, points:3 }
]

}; // fin QUESTIONS_BY_POSTE

"""

# Insérer avant loadSampleQuestions
assert "function loadSampleQuestions()" in html, "loadSampleQuestions not found"
html = html.replace("function loadSampleQuestions()", QUESTIONS_JS + "function loadSampleQuestions()")
print("QUESTIONS_BY_POSTE inserted OK")

# ============================================================
# 5. AJOUTER le poste dans la sauvegarde localStorage
# ============================================================
OLD_RESULT_OBJ = """  const result = {
    ...state.currentCandidate,
    score, maxScore, percentage, correct, wrong,
    duration: durationStr,
    date: new Date().toLocaleString('fr-FR'),
    answers: {...state.currentAnswers},
    resultCode
  };"""

NEW_RESULT_OBJ = """  const result = {
    ...state.currentCandidate,
    score, maxScore, percentage, correct, wrong,
    duration: durationStr,
    date: new Date().toLocaleString('fr-FR'),
    answers: {...state.currentAnswers},
    resultCode,
    examTitle: state.config.title
  };"""

html = html.replace(OLD_RESULT_OBJ, NEW_RESULT_OBJ)
print("Result object updated OK")

# ============================================================
# 6. AFFICHER LE POSTE dans le bloc code candidat
# ============================================================
OLD_CODE_BLOCK = """      codeBlock.innerHTML = `
      <div style="font-size:0.75rem;opacity:.8;text-transform:uppercase;letter-spacing:.1em;margin-bottom:8px">Votre code personnel</div>
      <div style="font-size:2.2rem;font-weight:800;letter-spacing:0.25em;font-family:'Syne',sans-serif;margin-bottom:8px">${result.resultCode}</div>
      <div style="font-size:0.82rem;opacity:.85;line-height:1.6">Notez ce code pour consulter vos résultats ultérieurement.<br>Depuis l'accueil → <strong>Consulter mes résultats</strong></div>`;"""

NEW_CODE_BLOCK = """      codeBlock.innerHTML = `
      <div style="font-size:0.75rem;opacity:.8;text-transform:uppercase;letter-spacing:.1em;margin-bottom:8px">Votre code personnel</div>
      <div style="font-size:2.2rem;font-weight:800;letter-spacing:0.25em;font-family:'Syne',sans-serif;margin-bottom:8px">${result.resultCode}</div>
      ${result.posteLabel ? `<div style="font-size:0.8rem;opacity:.9;margin-bottom:6px;background:rgba(255,255,255,0.15);padding:4px 12px;border-radius:20px;display:inline-block">${result.posteLabel}</div>` : ''}
      <div style="font-size:0.82rem;opacity:.85;line-height:1.6">Notez ce code pour consulter vos résultats ultérieurement.<br>Depuis l'accueil → <strong>Consulter mes résultats</strong></div>`;"""

html = html.replace(OLD_CODE_BLOCK, NEW_CODE_BLOCK)
print("Code block updated OK")

# ============================================================
# 7. AFFICHER LE POSTE dans lookupResultByCode
# ============================================================
OLD_LOOKUP_RESULT = """    resultBlock.innerHTML = `
      <div style="font-size:1.2rem;font-weight:700;margin-bottom:6px">${found.firstname} ${found.lastname}</div>
      <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:16px">${found.date}</div>"""

NEW_LOOKUP_RESULT = """    resultBlock.innerHTML = `
      <div style="font-size:1.2rem;font-weight:700;margin-bottom:6px">${found.firstname} ${found.lastname}</div>
      ${found.posteLabel ? `<div style="font-size:0.82rem;color:var(--accent);font-weight:600;margin-bottom:4px">${found.posteLabel}</div>` : ''}
      <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:16px">${found.date}</div>"""

if OLD_LOOKUP_RESULT in html:
    html = html.replace(OLD_LOOKUP_RESULT, NEW_LOOKUP_RESULT)
    print("Lookup result updated OK")
else:
    print("Lookup result - pattern not found, skipping")

# ============================================================
# WRITE
# ============================================================
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nevaluation.html: {len(html):,} chars ({len(html)//1024} KB)")
print("Done!")
