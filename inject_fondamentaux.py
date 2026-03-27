"""
Intégrer le Module Fondamentaux dans index.html
- Carte portail (avant M1)
- Overlay complet (9 sections, exercices, quiz 20 questions)
- Fonctions JS
- Compteur 6 → 7
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

IN  = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"
OUT = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"

with open(IN, "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================
# 1. CARTE PORTAIL — insérer avant la carte M1
# ============================================================
CARD_MARKER = '    <button class="module-card" onclick="openModule(\'m1\')"'

CARD_M0 = '''    <button class="module-card" onclick="openModule('m0')" style="border:none;cursor:pointer;text-align:left;background:white;">
      <div class="card-header" style="background:linear-gradient(135deg,#1a237e,#283593);">
        <div class="card-icon" style="background:rgba(255,255,255,0.15);color:white;">🏛️</div>
        <div class="card-meta">
          <div class="card-num" style="color:rgba(255,255,255,0.75);">Fondamentaux</div>
          <h3 style="color:white;">Fondamentaux Métier</h3>
        </div>
      </div>
      <div class="card-body">
        <p class="card-desc">Contexte MAFA &amp; ID30, définitions clés, rôles et métiers, environnement de travail, communication professionnelle, comportements terrain et rémunération.</p>
        <div class="card-tags">
          <span class="tag tag-public">👥 Commun CC &amp; Back Office</span>
          <span class="tag tag-duration">⏱ 2h00</span>
        </div>
      </div>
      <div class="card-footer">
        <span class="card-link-btn">Accéder au module</span>
        <span class="progress-mini">20 quiz · 2 exercices</span>
      </div>
    </button>

'''

assert CARD_MARKER in html, "Card M1 marker not found"
html = html.replace(CARD_MARKER, CARD_M0 + CARD_MARKER, 1)
print("Carte Fondamentaux OK")

# ============================================================
# 2. OVERLAY — insérer avant <!-- ══ OVERLAYS MODULES ══ -->
# ============================================================
OVERLAY_MARKER = "<!-- ══ OVERLAYS MODULES ══ -->"

OVERLAY_M0 = """<!-- ══════════════════════════════════════════════════════
     OVERLAY FONDAMENTAUX — Accueil & Fondamentaux Métier
══════════════════════════════════════════════════════════ -->
<div class="module-overlay" id="overlay-m0">
  <div class="overlay-topbar">
    <button class="overlay-back" onclick="closeModule()">← Retour au portail</button>
    <span class="overlay-topbar-title">🏛️ Fondamentaux Métier</span>
  </div>
  <div class="overlay-content">
<div class="module-page" id="module-m0">

  <!-- Breadcrumb -->
  <div class="module-breadcrumb">Fondamentaux · Contexte · Définitions · Métiers · Communication · Rémunération</div>

  <!-- Tabs -->
  <div class="module-tabs">
    <button class="tab-btn active" onclick="showModuleTab('m0','cours')">📚 Cours</button>
    <button class="tab-btn" onclick="showModuleTab('m0','exo')">✏️ Exercices</button>
    <button class="tab-btn" onclick="showModuleTab('m0','quiz')">✅ Quiz</button>
    <button class="tab-btn" onclick="showModuleTab('m0','resultats')">🏆 Résultats</button>
  </div>

  <!-- ═══ COURS ═══ -->
  <div class="tab-section" id="tab-m0-cours">
    <div class="module-hero">
      <div class="module-hero-icon">🏛️</div>
      <h1>Fondamentaux Métier</h1>
      <div class="module-hero-meta">
        <span class="meta-chip chip-blue">👥 Commun CC &amp; Back Office</span>
        <span class="meta-chip chip-green">⏱ 2h00</span>
        <span class="meta-chip chip-orange">🎓 Tous nouveaux agents</span>
      </div>
    </div>

    <div class="info-card" style="background:linear-gradient(135deg,#e8eaf6,#c5cae9);border-left:4px solid #3949ab">
      <h3 style="color:#1a237e">🎯 Objectifs pédagogiques</h3>
      <ul style="margin:8px 0 0;padding-left:18px;color:#283593;line-height:2">
        <li>Comprendre les missions d'un agent Call Center et Back Office</li>
        <li>Maîtriser les règles de communication professionnelle</li>
        <li>Connaître l'environnement de travail : outils, plateformes, équipe</li>
        <li>Adopter la posture et l'attitude attendues sur le terrain</li>
      </ul>
    </div>

    <!-- S1 -->
    <div class="section-heading">
      <div class="section-num">1</div>
      <h2>Qui sommes-nous ? — Contexte MAFA &amp; ID30</h2>
    </div>

    <p style="font-size:14px;color:#374151;line-height:1.8">MAFA Holding est une entreprise mandatée par le <strong>Ministère du Commerce et de l'Industrie</strong> pour procéder à l'identification et l'enrôlement de tous les entreprenants de Côte d'Ivoire dans <strong>30 grandes villes</strong> du territoire national. Le projet s'appelle <strong>ID30</strong>.</p>

    <div style="text-align:center;margin:16px 0">
      <img src="img_m0/fondamentaux_image1.jpg" alt="MAFA — Rendre l'informel visible" style="max-width:100%;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.12)">
      <p style="font-size:11px;color:#888;margin-top:8px">MAFA Holding — Rendre l'informel visible et lisible</p>
    </div>

    <div class="info-card" style="border-left:4px solid #1a237e">
      <h3>🎯 Notre mission</h3>
      <ul style="margin:8px 0 0;padding-left:18px;line-height:2">
        <li>Identifier et enrôler tous les entreprenants de Côte d'Ivoire</li>
        <li>Couvrir <strong>30 villes</strong> — travail organisé îlot par îlot</li>
        <li>Alimenter la base nationale de la Plateforme des Entrepreneurs (<strong>pde.ci</strong>)</li>
        <li>Permettre aux entrepreneurs d'accéder à des services digitaux et services de l'État</li>
      </ul>
    </div>

    <div class="info-card" style="border-left:4px solid #FF6D00;background:#fff8f3">
      <h3 style="color:#E65100">🟠 Partenariat Orange Côte d'Ivoire</h3>
      <p style="color:#374151;font-size:14px">Dans le cadre de son expansion commerciale, Orange Côte d'Ivoire a également sollicité MAFA Holding pour l'accompagner dans son déploiement marchand à travers plusieurs villes du pays.</p>
      <ul style="margin:8px 0 0;padding-left:18px;line-height:2;color:#374151">
        <li>Enrôlement et activation des marchands Orange Money sur le terrain</li>
        <li>Déploiement du réseau de points Orange dans les villes ciblées</li>
        <li>Formation et suivi des agents dédiés à cette mission Orange</li>
      </ul>
    </div>

    <!-- S2 -->
    <div class="section-heading">
      <div class="section-num">2</div>
      <h2>Définitions &amp; Mots clés</h2>
    </div>

    <div class="def-grid">
      <div class="def-card">
        <div class="def-term">🧑‍💼 Entreprenant</div>
        <div class="def-def">Personne physique / unité économique exerçant une activité professionnelle civile, commerciale, artisanale ou agricole — formelle ou informelle.</div>
      </div>
      <div class="def-card">
        <div class="def-term">🏪 Secteur informel</div>
        <div class="def-def">Unités économiques sans comptabilité formelle écrite et complète, même si elles ont un NCC ou RC.</div>
      </div>
      <div class="def-card">
        <div class="def-term">🏢 Unité économique</div>
        <div class="def-def">Entité (personne morale ou physique) qui exerce une activité économique.</div>
      </div>
      <div class="def-card">
        <div class="def-term">🗺️ Îlot statistique</div>
        <div class="def-def">Espace entouré de tous côtés par des limites naturelles (cours d'eau, collines…) ou artificielles (rues, routes…). Le travail se fait îlot par îlot.</div>
      </div>
      <div class="def-card">
        <div class="def-term">📍 ZD — Zone de Dénombrement</div>
        <div class="def-def">Périmètre géographique attribué à une équipe terrain pour organiser le travail de collecte.</div>
      </div>
      <div class="def-card">
        <div class="def-term">🪪 KYC</div>
        <div class="def-def">Know Your Customer — informations d'identité sur l'entreprenant (nom, prénom, photo, pièce d'identité).</div>
      </div>
      <div class="def-card">
        <div class="def-term">📊 KYB</div>
        <div class="def-def">Know Your Business — informations sur l'activité de l'entreprenant (secteur, localisation, chiffre d'affaires).</div>
      </div>
      <div class="def-card">
        <div class="def-term">💰 TCE</div>
        <div class="def-def">Taxe Communale de l'Entreprenant — applicable si le chiffre d'affaires est inférieur à 5 millions FCFA.</div>
      </div>
      <div class="def-card">
        <div class="def-term">💼 TEE</div>
        <div class="def-def">Taxe d'État de l'Entreprenant — applicable si le CA est entre 5 et 50 millions FCFA.</div>
      </div>
      <div class="def-card">
        <div class="def-term">🔢 NCC</div>
        <div class="def-def">Numéro de Compte Contribuable — identifiant fiscal unique attribué à chaque entreprenant enrôlé.</div>
      </div>
      <div class="def-card">
        <div class="def-term">📋 RC</div>
        <div class="def-def">Registre de Commerce — document officiel attestant de l'existence légale d'une activité commerciale.</div>
      </div>
    </div>

    <!-- S3 -->
    <div class="section-heading">
      <div class="section-num">3</div>
      <h2>Le métier d'agent</h2>
    </div>

    <p style="font-size:14px;color:#374151;line-height:1.8">Notre équipe opère sur deux types de postes complémentaires : le <strong>Call Center</strong> (contact direct client par téléphone) et le <strong>Back Office</strong> (traitement administratif des dossiers).</p>

    <div style="text-align:center;margin:16px 0">
      <img src="img_m0/fondamentaux_image2.jpg" alt="Matériels terrain — FAMOCO et smartphone" style="max-width:100%;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.12)">
      <p style="font-size:11px;color:#888;margin-top:8px">Matériels terrain utilisés par les agents — FAMOCO &amp; Smartphone</p>
    </div>

    <table class="styled-table">
      <thead>
        <tr><th>Fonction</th><th>Mission principale</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Agent Call Center (CC)</strong></td><td>Contacter les entrepreneurs par téléphone via Connectel pour mettre à jour leurs informations ou vérifier leur activité.</td></tr>
        <tr><td><strong>Agent Back Office (BO)</strong></td><td>Traiter les dossiers transmis : vérifier, corriger, valider ou rejeter chaque fiche entrepreneur.</td></tr>
        <tr><td><strong>Chef d'équipe</strong></td><td>Supervise et encadre les agents, contrôle la qualité des données et remonte les difficultés terrain.</td></tr>
        <tr><td><strong>Inspecteur</strong></td><td>Effectue des contre-enquêtes terrain, contrôle le passage GPS des agents, vérifie l'exhaustivité du ratissage.</td></tr>
        <tr><td><strong>Responsable de Ville (RV)</strong></td><td>Coordonne toutes les équipes sur la ville, valide les zones couvertes, traite les cas complexes.</td></tr>
      </tbody>
    </table>

    <div class="info-card" style="border-left:4px solid #1a237e;background:#f0f4ff">
      <h3 style="color:#1a237e">🏗️ Structure hiérarchique terrain</h3>
      <div style="display:flex;flex-direction:column;gap:8px;margin-top:12px">
        <div style="background:#1a237e;color:white;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px">🏙️ Responsable Ville → pilote l'ensemble des opérations sur la ville</div>
        <div style="background:#283593;color:white;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px;margin-left:20px">🔍 Inspecteur → contrôle qualité et contre-enquêtes</div>
        <div style="background:#3949ab;color:white;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px;margin-left:40px">👤 Chef d'équipe → encadre 9 agents identificateurs</div>
        <div style="background:#5c6bc0;color:white;padding:10px 16px;border-radius:8px;font-weight:700;font-size:13px;margin-left:60px">👥 9 Agents (AI) → identification et enrôlement îlot par îlot</div>
      </div>
    </div>

    <!-- S4 -->
    <div class="section-heading">
      <div class="section-num">4</div>
      <h2>L'environnement de travail</h2>
    </div>

    <div class="info-card" style="border-left:4px solid #0288D1;background:#f0f8ff">
      <h3 style="color:#01579B">🔷 Plateforme Connectel</h3>
      <p style="color:#374151;font-size:14px">Plateforme CCaaS cloud — centralisée pour toutes les activités téléphoniques des agents Call Center.</p>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:12px">
        <div style="background:#e1f5fe;border-radius:8px;padding:12px;text-align:center">
          <div style="font-weight:800;color:#01579B;font-size:18px">N1</div>
          <div style="font-size:12px;color:#374151;margin-top:4px">Numérotation automatique (auto-dial)</div>
        </div>
        <div style="background:#b3e5fc;border-radius:8px;padding:12px;text-align:center">
          <div style="font-weight:800;color:#01579B;font-size:18px">N2</div>
          <div style="font-size:12px;color:#374151;margin-top:4px">Agent IA avancé de qualification</div>
        </div>
        <div style="background:#0288D1;border-radius:8px;padding:12px;text-align:center;border:3px solid #01579B">
          <div style="font-weight:800;color:white;font-size:18px">N3</div>
          <div style="font-size:12px;color:white;margin-top:4px;font-weight:700">Votre niveau — Escalade agent humain</div>
        </div>
      </div>
    </div>

    <table class="styled-table">
      <thead>
        <tr><th>Projet</th><th>Description</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>ID30</strong></td><td>Mise à jour de la base entrepreneurs. L'agent contacte les entrepreneurs pour vérifier et mettre à jour leurs informations d'identification.</td></tr>
        <tr><td><strong>Orange QR</strong></td><td>Suivi et réactivation des marchands Orange Money. L'agent détecte l'activité, collecte les infos et encourage la réactivation.</td></tr>
      </tbody>
    </table>

    <!-- S5 -->
    <div class="section-heading">
      <div class="section-num">5</div>
      <h2>Communication professionnelle</h2>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:16px 0">
      <div style="background:linear-gradient(135deg,#1565C0,#1976D2);color:white;border-radius:12px;padding:16px;text-align:center">
        <div style="font-size:22px;margin-bottom:6px">💬</div>
        <div style="font-weight:800;font-size:14px">CLARTÉ</div>
        <div style="font-size:12px;margin-top:6px;opacity:0.9">Parler lentement, articuler, utiliser des mots simples</div>
      </div>
      <div style="background:linear-gradient(135deg,#2E7D32,#388E3C);color:white;border-radius:12px;padding:16px;text-align:center">
        <div style="font-size:22px;margin-bottom:6px">👂</div>
        <div style="font-weight:800;font-size:14px">ÉCOUTE</div>
        <div style="font-size:12px;margin-top:6px;opacity:0.9">Laisser le client parler, ne jamais couper</div>
      </div>
      <div style="background:linear-gradient(135deg,#6A1B9A,#7B1FA2);color:white;border-radius:12px;padding:16px;text-align:center">
        <div style="font-size:22px;margin-bottom:6px">🤝</div>
        <div style="font-weight:800;font-size:14px">EMPATHIE</div>
        <div style="font-size:12px;margin-top:6px;opacity:0.9">Reconnaître l'émotion du client avant de répondre</div>
      </div>
      <div style="background:linear-gradient(135deg,#E65100,#F57C00);color:white;border-radius:12px;padding:16px;text-align:center">
        <div style="font-size:22px;margin-bottom:6px">✅</div>
        <div style="font-weight:800;font-size:14px">SOLUTIONS</div>
        <div style="font-size:12px;margin-top:6px;opacity:0.9">Toujours proposer une action concrète</div>
      </div>
    </div>

    <h3 style="margin:20px 0 10px;color:#1a237e">📞 Les 6 étapes d'un appel réussi</h3>
    <table class="styled-table">
      <thead>
        <tr><th>Étape</th><th>Ce que l'agent fait</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>1. Accueil</strong></td><td>Saluer, se présenter, annoncer le projet</td></tr>
        <tr><td><strong>2. Identification</strong></td><td>Vérifier que l'on parle à la bonne personne</td></tr>
        <tr><td><strong>3. Objet</strong></td><td>Expliquer clairement la raison du contact en 2 phrases</td></tr>
        <tr><td><strong>4. Collecte</strong></td><td>Poser les questions, noter les réponses, effectuer les mises à jour</td></tr>
        <tr><td><strong>5. Objections</strong></td><td>Écouter, reformuler, répondre calmement avec les arguments préparés</td></tr>
        <tr><td><strong>6. Clôture</strong></td><td>Résumer, remercier, souhaiter une bonne journée</td></tr>
      </tbody>
    </table>

    <h3 style="margin:20px 0 10px;color:#1a237e">🗣️ Formulations à retenir</h3>
    <table class="styled-table">
      <thead>
        <tr><th>❌ À éviter</th><th>✅ Dire à la place</th></tr>
      </thead>
      <tbody>
        <tr><td>« Je sais pas »</td><td>« Je vais vérifier et vous revenir »</td></tr>
        <tr><td>« C'est pas mon problème »</td><td>« Permettez-moi de vous orienter »</td></tr>
        <tr><td>« Attendez »</td><td>« Je vous demande un instant, merci »</td></tr>
        <tr><td>« Vous avez tort »</td><td>« Je comprends, laissez-moi vous expliquer »</td></tr>
        <tr><td>« C'est impossible »</td><td>« Voici ce que je peux faire pour vous »</td></tr>
      </tbody>
    </table>

    <!-- S6 -->
    <div class="section-heading">
      <div class="section-num">6</div>
      <h2>Comportements &amp; attitudes sur le terrain</h2>
    </div>

    <table class="styled-table">
      <thead>
        <tr><th>✅ À FAIRE</th><th>❌ À ÉVITER / INTERDIT</th></tr>
      </thead>
      <tbody>
        <tr><td>Se présenter en tenue correcte, porter son badge</td><td>Se présenter accompagné d'un parent ou ami</td></tr>
        <tr><td>Expliquer clairement le but de la visite, montrer sa carte professionnelle</td><td>Écrire des messages téléphoniques pendant un entretien</td></tr>
        <tr><td>Avoir un langage rassurant, respectueux et adapté</td><td>Déléguer ses fonctions à une autre personne</td></tr>
        <tr><td>Respecter les coutumes et pratiques religieuses locales</td><td>Travailler hors de son îlot ou de sa ZD assignée</td></tr>
        <tr><td>Faire preuve de patience et d'habileté dans la conduite des entretiens</td><td>Saisir des renseignements faux, fantaisistes ou invraisemblables</td></tr>
        <tr><td>Remonter tout problème au chef d'équipe immédiatement</td><td>Communiquer ou commenter les renseignements collectés</td></tr>
        <tr><td>Décliner poliment toute offre de boissons alcooliques</td><td>Être agressif ou menacer les répondants</td></tr>
        <tr><td>Informer le chef d'équipe en cas de maladie ou absence</td><td>Avoir des discussions sans rapport avec la mission</td></tr>
      </tbody>
    </table>

    <!-- S7 -->
    <div class="section-heading">
      <div class="section-num">7</div>
      <h2>Obligations professionnelles</h2>
    </div>

    <div class="info-card" style="border-left:4px solid #2E7D32;background:#f0faf0">
      <h3 style="color:#1B5E20">📌 Ce que chaque agent doit faire</h3>
      <ul style="margin:8px 0 0;padding-left:18px;line-height:2.2;color:#374151">
        <li>Assister régulièrement à toutes les séances de formation</li>
        <li>S'approprier les documents de référence remis à la prise de poste</li>
        <li>Soumettre régulièrement les données collectées au contrôle du chef d'équipe</li>
        <li>Répondre à toute convocation du chef d'équipe sans délai</li>
        <li>Toute permission doit être demandée formellement — <strong>maximum 2 jours</strong></li>
        <li>En cas de réticence d'un entrepreneur, faire appel au chef d'équipe</li>
      </ul>
    </div>

    <div class="alert alert-warn">
      <div class="alert-icon">🚫</div>
      <div class="alert-text">
        <strong>Pratiques formellement interdites — Tolérance zéro :</strong>
        <ul style="margin:8px 0 0;padding-left:18px;line-height:2.2">
          <li>Déléguer ses fonctions à une autre personne</li>
          <li>Travailler hors de son îlot assigné</li>
          <li>Montrer les documents cartographiques à des tiers non autorisés</li>
          <li>Saisir des informations fausses, fantaisistes ou illogiques</li>
          <li>Abandonner la mission avant l'expiration de la période d'engagement</li>
          <li>Demander des renseignements autres que ceux prévus dans le formulaire</li>
        </ul>
      </div>
    </div>

    <!-- S8 -->
    <div class="section-heading">
      <div class="section-num">8</div>
      <h2>Attitude commerciale — Les 7 piliers</h2>
    </div>

    <p style="font-size:14px;color:#374151;line-height:1.8">L'attitude commerciale est la manière dont un professionnel aborde ses relations avec ses clients, prospects et partenaires. Elle englobe les comportements, stratégies et valeurs qui guident les interactions pour atteindre des objectifs.</p>

    <table class="styled-table">
      <thead>
        <tr><th>Pilier</th><th>Ce que cela signifie en pratique</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>👔 Tenue vestimentaire</strong></td><td>Tenue propre, repassée, bien ajustée. Adapter les codes vestimentaires au secteur. Éviter les parfums trop forts. Une tenue adaptée renforce la crédibilité.</td></tr>
        <tr><td><strong>🎯 Orientation client</strong></td><td>Comprendre et anticiper les besoins. Adopter une écoute active pour proposer des solutions adaptées. Faire preuve d'empathie et de professionnalisme.</td></tr>
        <tr><td><strong>🗣️ Persuasion &amp; négociation</strong></td><td>Savoir présenter les avantages d'un produit ou service de manière convaincante. Adapter le discours en fonction des priorités du client.</td></tr>
        <tr><td><strong>🤝 Éthique &amp; transparence</strong></td><td>Agir avec intégrité, respecter ses engagements. Éviter toute pratique trompeuse.</td></tr>
        <tr><td><strong>💪 Résilience &amp; proactivité</strong></td><td>Persévérance face aux objections ou aux refus. Être proactif dans la recherche de nouvelles opportunités.</td></tr>
        <tr><td><strong>💬 Communication efficace</strong></td><td>Langage clair et adapté au client. Posture professionnelle et positive.</td></tr>
        <tr><td><strong>🔄 Adaptabilité</strong></td><td>S'adapter aux différents profils de clients et aux évolutions du marché. Être réactif face aux changements.</td></tr>
      </tbody>
    </table>

    <!-- S9 -->
    <div class="section-heading">
      <div class="section-num">9</div>
      <h2>Rémunération &amp; objectifs de performance</h2>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;margin:16px 0">
      <div class="db-card" style="background:linear-gradient(135deg,#1a237e,#283593);color:white;padding:20px;border-radius:14px;text-align:center">
        <div style="font-size:28px;font-weight:800">200 000 F</div>
        <div style="font-size:12px;margin-top:6px;opacity:0.9">Salaire fixe mensuel<br>(26 jours — 15 fiches/jour validées)</div>
      </div>
      <div class="db-card" style="background:linear-gradient(135deg,#2E7D32,#388E3C);color:white;padding:20px;border-radius:14px;text-align:center">
        <div style="font-size:28px;font-weight:800">40 000 F</div>
        <div style="font-size:12px;margin-top:6px;opacity:0.9">Prime qualitative MAFA<br>(≥15 fiches/j + présence ≥90%)</div>
      </div>
      <div class="db-card" style="background:linear-gradient(135deg,#E65100,#F57C00);color:white;padding:20px;border-radius:14px;text-align:center">
        <div style="font-size:28px;font-weight:800">15 fiches</div>
        <div style="font-size:12px;margin-top:6px;opacity:0.9">Objectif journalier minimum<br>validées par le Back Office</div>
      </div>
    </div>

    <table class="styled-table">
      <thead>
        <tr><th>Scénario</th><th>Salaire fixe</th><th>Prime</th><th>Total</th></tr>
      </thead>
      <tbody>
        <tr style="background:#e8f5e9"><td><strong>26 jours — objectifs atteints</strong></td><td>200 000 F</td><td>40 000 F</td><td><strong>240 000 F</strong></td></tr>
        <tr><td>26 jours — objectifs non atteints</td><td>200 000 F</td><td>0 F</td><td>200 000 F</td></tr>
        <tr style="background:#e8f5e9"><td><strong>16 jours — objectifs atteints</strong></td><td>123 076 F</td><td>40 000 F</td><td><strong>163 076 F</strong></td></tr>
        <tr><td>16 jours — objectifs non atteints</td><td>123 076 F</td><td>0 F</td><td>123 076 F</td></tr>
      </tbody>
    </table>

    <div class="alert alert-info">
      <div class="alert-icon">💡</div>
      <div class="alert-text"><strong>Important :</strong> La validation des fiches est effectuée par le Back Office. Une fiche mal remplie, incomplète ou contenant des informations fantaisistes ne compte pas dans le quota journalier. La présence effective doit être ≥ 90% pour bénéficier de la prime qualitative.</div>
    </div>

  </div><!-- fin tab-m0-cours -->

  <!-- ═══ EXERCICES ═══ -->
  <div class="tab-section" id="tab-m0-exo" style="display:none">
    <div class="module-hero">
      <div class="module-hero-icon">✏️</div>
      <h1>Exercices — Fondamentaux</h1>
    </div>

    <div class="exo-card">
      <div class="exo-header">
        <span class="exo-num">Exercice 1</span>
        <span class="exo-title">Simulation d'appel — Mise en situation ID30</span>
      </div>
      <div class="exo-body">
        <p><strong>Contexte :</strong> Vous êtes agent Call Center sur le projet ID30. Vous devez contacter M. Konaté, entrepreneur dans le secteur de la restauration à Abidjan, pour mettre à jour ses informations dans la base nationale.</p>
        <p style="margin-top:10px"><strong>Votre tâche :</strong> Rédigez le script complet de votre appel en respectant les <strong>6 étapes</strong> vues en cours (Accueil → Identification → Objet → Collecte → Objections → Clôture).</p>
        <div style="background:#f8fafc;border-radius:8px;padding:14px;margin-top:12px;border:1px dashed #cbd5e1">
          <p style="font-size:13px;color:#64748b;font-weight:600">Informations à collecter :</p>
          <ul style="font-size:13px;color:#374151;line-height:2;margin-top:6px;padding-left:18px">
            <li>Nom et prénom de l'entrepreneur</li>
            <li>Numéro de téléphone principal et alternatif</li>
            <li>Secteur d'activité et localisation précise</li>
            <li>Vérification du NCC si disponible</li>
          </ul>
        </div>
        <div class="alert alert-info" style="margin-top:14px">
          <div class="alert-icon">💡</div>
          <div class="alert-text">Si M. Konaté dit : <em>« Je n'ai pas le temps, rappelez plus tard »</em> — comment répondez-vous selon les règles de communication vues en cours ?</div>
        </div>
      </div>
    </div>

    <div class="exo-card">
      <div class="exo-header">
        <span class="exo-num">Exercice 2</span>
        <span class="exo-title">Calcul de rémunération &amp; scénarios</span>
      </div>
      <div class="exo-body">
        <p>Pour chacun des agents ci-dessous, calculez la <strong>rémunération totale du mois</strong> en appliquant les règles vues en cours :</p>
        <table class="styled-table" style="margin-top:14px">
          <thead>
            <tr><th>Agent</th><th>Jours travaillés</th><th>Fiches validées/jour (moy.)</th><th>Présence effective</th><th>Salaire total ?</th></tr>
          </thead>
          <tbody>
            <tr><td>Agent A</td><td>26 jours</td><td>17 fiches</td><td>95%</td><td style="background:#e8f5e9;font-weight:700">?</td></tr>
            <tr><td>Agent B</td><td>26 jours</td><td>12 fiches</td><td>100%</td><td style="background:#fff3e0;font-weight:700">?</td></tr>
            <tr><td>Agent C</td><td>16 jours</td><td>16 fiches</td><td>92%</td><td style="background:#e8f5e9;font-weight:700">?</td></tr>
            <tr><td>Agent D</td><td>20 jours</td><td>15 fiches</td><td>85%</td><td style="background:#fce4ec;font-weight:700">?</td></tr>
          </tbody>
        </table>
        <div class="alert alert-warn" style="margin-top:14px">
          <div class="alert-icon">⚠️</div>
          <div class="alert-text"><strong>Rappel :</strong> Le salaire fixe est proratisé sur 26 jours. La prime qualitative (40 000 F) n'est accordée que si ≥ 15 fiches/jour ET présence ≥ 90%.</div>
        </div>
      </div>
    </div>
  </div><!-- fin tab-m0-exo -->

  <!-- ═══ QUIZ ═══ -->
  <div class="tab-section" id="tab-m0-quiz" style="display:none">
    <div class="module-hero">
      <div class="module-hero-icon">🎯</div>
      <h1>Quiz — Fondamentaux Métier</h1>
      <div class="module-hero-meta">
        <span class="meta-chip chip-red">20 questions</span>
        <span class="meta-chip chip-blue">Toutes sections</span>
      </div>
    </div>
    <div class="quiz-score-bar">
      Score : <span id="m0-score-display">0 / 20</span>
    </div>

    <!-- Q1 -->
    <div class="quiz-question-block" id="m0-q1">
      <div class="quiz-q-num">Question 1 / 20</div>
      <div class="quiz-q-text">Par qui MAFA Holding est-elle mandatée pour le projet ID30 ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q1',false,'La Banque Mondiale n\\'est pas le mandataire direct du projet ID30.')"><span class="option-letter">A</span> La Banque Mondiale</div>
        <div class="quiz-option" onclick="answerM0(this,'q1',false,'Orange CI est un partenaire commercial, pas le mandataire du projet ID30.')"><span class="option-letter">B</span> Orange Côte d'Ivoire</div>
        <div class="quiz-option" onclick="answerM0(this,'q1',true,'Correct ! MAFA Holding est mandatée par le Ministère du Commerce et de l\\'Industrie de Côte d\\'Ivoire.')"><span class="option-letter">C</span> Le Ministère du Commerce et de l'Industrie</div>
        <div class="quiz-option" onclick="answerM0(this,'q1',false,'La Chambre de Commerce n\\'est pas le mandataire de ce projet.')"><span class="option-letter">D</span> La Chambre de Commerce</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q1"></div>
    </div>

    <!-- Q2 -->
    <div class="quiz-question-block" id="m0-q2">
      <div class="quiz-q-num">Question 2 / 20</div>
      <div class="quiz-q-text">Combien de villes sont couvertes par le projet ID30 ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q2',false,'10 villes est insuffisant — le projet couvre l\\'ensemble des 30 grandes villes.')"><span class="option-letter">A</span> 10 villes</div>
        <div class="quiz-option" onclick="answerM0(this,'q2',false,'20 villes est insuffisant.')"><span class="option-letter">B</span> 20 villes</div>
        <div class="quiz-option" onclick="answerM0(this,'q2',true,'Correct ! ID30 signifie Identification dans 30 grandes villes de Côte d\\'Ivoire.')"><span class="option-letter">C</span> 30 villes</div>
        <div class="quiz-option" onclick="answerM0(this,'q2',false,'50 villes est excessif — ID30 = 30 grandes villes.')"><span class="option-letter">D</span> 50 villes</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q2"></div>
    </div>

    <!-- Q3 -->
    <div class="quiz-question-block" id="m0-q3">
      <div class="quiz-q-num">Question 3 / 20</div>
      <div class="quiz-q-text">Qu'est-ce qu'un entreprenant ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q3',false,'Un entreprenant n\\'est pas nécessairement une personne morale — cela inclut les personnes physiques.')"><span class="option-letter">A</span> Une personne morale disposant d'un RC enregistré</div>
        <div class="quiz-option" onclick="answerM0(this,'q3',true,'Correct ! Un entreprenant est une personne physique / unité économique exerçant une activité civile, commerciale, artisanale ou agricole — formelle ou informelle.')"><span class="option-letter">B</span> Personne physique / unité économique exerçant une activité professionnelle, formelle ou informelle</div>
        <div class="quiz-option" onclick="answerM0(this,'q3',false,'Un fonctionnaire n\\'est pas un entreprenant — il n\\'exerce pas d\\'activité économique autonome.')"><span class="option-letter">C</span> Tout fonctionnaire exerçant une mission de service public</div>
        <div class="quiz-option" onclick="answerM0(this,'q3',false,'Un agent MAFA n\\'est pas un entreprenant dans ce contexte.')"><span class="option-letter">D</span> Un agent de terrain mandaté par MAFA</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q3"></div>
    </div>

    <!-- Q4 -->
    <div class="quiz-question-block" id="m0-q4">
      <div class="quiz-q-num">Question 4 / 20</div>
      <div class="quiz-q-text">Que signifie l'acronyme KYC ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q4',false,'KYC ne se traduit pas par Know Your City.')"><span class="option-letter">A</span> Know Your City</div>
        <div class="quiz-option" onclick="answerM0(this,'q4',true,'Correct ! KYC = Know Your Customer — informations d\\'identité sur l\\'entreprenant (nom, prénom, photo, pièce d\\'identité).')"><span class="option-letter">B</span> Know Your Customer</div>
        <div class="quiz-option" onclick="answerM0(this,'q4',false,'KYC ne signifie pas Know Your Contract.')"><span class="option-letter">C</span> Know Your Contract</div>
        <div class="quiz-option" onclick="answerM0(this,'q4',false,'KYC ne signifie pas Keep Your Contacts.')"><span class="option-letter">D</span> Keep Your Contacts</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q4"></div>
    </div>

    <!-- Q5 -->
    <div class="quiz-question-block" id="m0-q5">
      <div class="quiz-q-num">Question 5 / 20</div>
      <div class="quiz-q-text">Quel est le montant du salaire fixe mensuel d'un agent (26 jours complets) ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q5',false,'150 000 F n\\'est pas le salaire fixe dans la grille de rémunération.')"><span class="option-letter">A</span> 150 000 FCFA</div>
        <div class="quiz-option" onclick="answerM0(this,'q5',true,'Correct ! Le salaire fixe est de 200 000 FCFA pour 26 jours de travail avec minimum 15 fiches validées par jour.')"><span class="option-letter">B</span> 200 000 FCFA</div>
        <div class="quiz-option" onclick="answerM0(this,'q5',false,'240 000 F est le total fixe + prime, pas le salaire fixe seul.')"><span class="option-letter">C</span> 240 000 FCFA</div>
        <div class="quiz-option" onclick="answerM0(this,'q5',false,'250 000 F ne correspond pas à la grille de rémunération.')"><span class="option-letter">D</span> 250 000 FCFA</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q5"></div>
    </div>

    <!-- Q6 -->
    <div class="quiz-question-block" id="m0-q6">
      <div class="quiz-q-num">Question 6 / 20</div>
      <div class="quiz-q-text">Quel est l'objectif journalier minimum pour valider le salaire fixe ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q6',false,'10 fiches est en dessous du seuil minimum requis.')"><span class="option-letter">A</span> 10 fiches validées par jour</div>
        <div class="quiz-option" onclick="answerM0(this,'q6',true,'Correct ! L\\'objectif est de 15 fiches journalières validées par le Back Office pour maintenir le salaire fixe.')"><span class="option-letter">B</span> 15 fiches validées par jour</div>
        <div class="quiz-option" onclick="answerM0(this,'q6',false,'20 fiches est au-dessus du seuil minimum requis.')"><span class="option-letter">C</span> 20 fiches validées par jour</div>
        <div class="quiz-option" onclick="answerM0(this,'q6',false,'25 fiches est excessif — l\\'objectif est de 15 fiches/jour.')"><span class="option-letter">D</span> 25 fiches validées par jour</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q6"></div>
    </div>

    <!-- Q7 -->
    <div class="quiz-question-block" id="m0-q7">
      <div class="quiz-q-num">Question 7 / 20</div>
      <div class="quiz-q-text">Quel est le montant de la prime qualitative MAFA ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q7',false,'20 000 F n\\'est pas le montant de la prime qualitative.')"><span class="option-letter">A</span> 20 000 FCFA</div>
        <div class="quiz-option" onclick="answerM0(this,'q7',false,'30 000 F n\\'est pas le montant de la prime qualitative.')"><span class="option-letter">B</span> 30 000 FCFA</div>
        <div class="quiz-option" onclick="answerM0(this,'q7',true,'Correct ! La prime qualitative est de 40 000 FCFA, accordée si minimum 15 fiches/j validées + présence effective ≥ 90%.')"><span class="option-letter">C</span> 40 000 FCFA</div>
        <div class="quiz-option" onclick="answerM0(this,'q7',false,'50 000 F est supérieur au montant réel de la prime qualitative.')"><span class="option-letter">D</span> 50 000 FCFA</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q7"></div>
    </div>

    <!-- Q8 -->
    <div class="quiz-question-block" id="m0-q8">
      <div class="quiz-q-num">Question 8 / 20</div>
      <div class="quiz-q-text">Quelle est la présence effective minimale pour bénéficier de la prime qualitative ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q8',false,'75% est insuffisant — le seuil est fixé à 90%.')"><span class="option-letter">A</span> 75%</div>
        <div class="quiz-option" onclick="answerM0(this,'q8',false,'80% est insuffisant — le seuil est fixé à 90%.')"><span class="option-letter">B</span> 80%</div>
        <div class="quiz-option" onclick="answerM0(this,'q8',true,'Correct ! La présence effective doit être ≥ 90% pour bénéficier de la prime qualitative MAFA.')"><span class="option-letter">C</span> 90%</div>
        <div class="quiz-option" onclick="answerM0(this,'q8',false,'100% est le maximum mais pas le seuil minimum requis.')"><span class="option-letter">D</span> 100%</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q8"></div>
    </div>

    <!-- Q9 -->
    <div class="quiz-question-block" id="m0-q9">
      <div class="quiz-q-num">Question 9 / 20</div>
      <div class="quiz-q-text">Qu'est-ce qu'un îlot statistique ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q9',false,'Un îlot n\\'est pas un quartier administratif — c\\'est un espace délimité par des frontières naturelles ou artificielles.')"><span class="option-letter">A</span> Un quartier administratif délimité par la mairie</div>
        <div class="quiz-option" onclick="answerM0(this,'q9',true,'Correct ! Un îlot statistique est un espace entouré de tous côtés par des limites naturelles (cours d\\'eau) ou artificielles (rues, routes).')"><span class="option-letter">B</span> Un espace entouré de limites naturelles ou artificielles, délimitant le travail de collecte</div>
        <div class="quiz-option" onclick="answerM0(this,'q9',false,'Un îlot n\\'est pas un secteur fiscal.')"><span class="option-letter">C</span> Un secteur fiscal défini par le Ministère des Finances</div>
        <div class="quiz-option" onclick="answerM0(this,'q9',false,'Un îlot n\\'est pas une zone de résidence exclusive.')"><span class="option-letter">D</span> Une zone de résidence réservée aux agents de terrain</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q9"></div>
    </div>

    <!-- Q10 -->
    <div class="quiz-question-block" id="m0-q10">
      <div class="quiz-q-num">Question 10 / 20</div>
      <div class="quiz-q-text">Quelle est la mission principale d'un agent Call Center dans le projet ID30 ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q10',false,'Valider les dossiers est le rôle du Back Office, pas du Call Center.')"><span class="option-letter">A</span> Valider et rejeter les dossiers entrepreneurs</div>
        <div class="quiz-option" onclick="answerM0(this,'q10',false,'Le Call Center ne se rend pas sur le terrain — c\\'est le rôle des agents identificateurs.')"><span class="option-letter">B</span> Effectuer des visites terrain îlot par îlot</div>
        <div class="quiz-option" onclick="answerM0(this,'q10',true,'Correct ! L\\'agent Call Center contacte les entrepreneurs par téléphone via Connectel pour vérifier et mettre à jour leurs informations.')"><span class="option-letter">C</span> Contacter les entrepreneurs par téléphone pour vérifier et mettre à jour leurs informations</div>
        <div class="quiz-option" onclick="answerM0(this,'q10',false,'La supervision des équipes terrain est le rôle du Responsable de Ville ou du Chef d\\'équipe.')"><span class="option-letter">D</span> Superviser les équipes terrain sur le terrain</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q10"></div>
    </div>

    <!-- Q11 -->
    <div class="quiz-question-block" id="m0-q11">
      <div class="quiz-q-num">Question 11 / 20</div>
      <div class="quiz-q-text">À quel niveau l'agent humain intervient-il dans la plateforme Connectel ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q11',false,'Le Niveau 1 est la numérotation automatique — pas le niveau de l\\'agent humain.')"><span class="option-letter">A</span> Niveau 1 — Numérotation automatique</div>
        <div class="quiz-option" onclick="answerM0(this,'q11',false,'Le Niveau 2 est l\\'agent IA de qualification — pas l\\'agent humain.')"><span class="option-letter">B</span> Niveau 2 — Agent IA de qualification</div>
        <div class="quiz-option" onclick="answerM0(this,'q11',true,'Correct ! L\\'agent humain intervient au Niveau 3 — escalade après les niveaux automatiques et IA.')"><span class="option-letter">C</span> Niveau 3 — Escalade agent humain</div>
        <div class="quiz-option" onclick="answerM0(this,'q11',false,'Il n\\'existe pas de Niveau 4 dans l\\'architecture Connectel décrite.')"><span class="option-letter">D</span> Niveau 4 — Supervision directe</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q11"></div>
    </div>

    <!-- Q12 -->
    <div class="quiz-question-block" id="m0-q12">
      <div class="quiz-q-num">Question 12 / 20</div>
      <div class="quiz-q-text">Qu'est-ce que le KYB ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q12',false,'KYB ne signifie pas Know Your Budget.')"><span class="option-letter">A</span> Know Your Budget — le budget de l'activité</div>
        <div class="quiz-option" onclick="answerM0(this,'q12',true,'Correct ! KYB = Know Your Business — informations sur l\\'activité de l\\'entreprenant : secteur, localisation, chiffre d\\'affaires.')"><span class="option-letter">B</span> Know Your Business — informations sur l'activité de l'entreprenant</div>
        <div class="quiz-option" onclick="answerM0(this,'q12',false,'KYB ne signifie pas Keep Your Business.')"><span class="option-letter">C</span> Keep Your Business — fidélisation des entrepreneurs</div>
        <div class="quiz-option" onclick="answerM0(this,'q12',false,'KYB ne signifie pas Know Your Bank.')"><span class="option-letter">D</span> Know Your Bank — informations bancaires de l'entrepreneur</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q12"></div>
    </div>

    <!-- Q13 -->
    <div class="quiz-question-block" id="m0-q13">
      <div class="quiz-q-num">Question 13 / 20</div>
      <div class="quiz-q-text">Quelle taxe s'applique si le chiffre d'affaires d'un entrepreneur est inférieur à 5 millions FCFA ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q13',true,'Correct ! La TCE (Taxe Communale de l\\'Entreprenant) s\\'applique si le CA est inférieur à 5 millions FCFA.')"><span class="option-letter">A</span> La TCE — Taxe Communale de l'Entreprenant</div>
        <div class="quiz-option" onclick="answerM0(this,'q13',false,'La TEE s\\'applique quand le CA est entre 5 et 50 millions FCFA.')"><span class="option-letter">B</span> La TEE — Taxe d'État de l'Entreprenant</div>
        <div class="quiz-option" onclick="answerM0(this,'q13',false,'La TVA ne s\\'applique pas dans ce contexte de fiscalité des entreprenants.')"><span class="option-letter">C</span> La TVA — Taxe sur la Valeur Ajoutée</div>
        <div class="quiz-option" onclick="answerM0(this,'q13',false,'Le NCC est un identifiant fiscal, pas une taxe.')"><span class="option-letter">D</span> Le NCC — Numéro de Compte Contribuable</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q13"></div>
    </div>

    <!-- Q14 -->
    <div class="quiz-question-block" id="m0-q14">
      <div class="quiz-q-num">Question 14 / 20</div>
      <div class="quiz-q-text">Laquelle de ces pratiques est formellement interdite et sanctionnable ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q14',false,'Porter son badge est obligatoire — ce n\\'est pas interdit.')"><span class="option-letter">A</span> Porter son badge lors des visites terrain</div>
        <div class="quiz-option" onclick="answerM0(this,'q14',false,'Remonter les problèmes est une obligation professionnelle.')"><span class="option-letter">B</span> Remonter les problèmes au chef d'équipe</div>
        <div class="quiz-option" onclick="answerM0(this,'q14',true,'Correct ! Déléguer ses fonctions à une autre personne est formellement interdit — tolérance zéro.')"><span class="option-letter">C</span> Déléguer ses fonctions à une autre personne</div>
        <div class="quiz-option" onclick="answerM0(this,'q14',false,'Décliner poliment les boissons alcooliques est une règle à respecter.')"><span class="option-letter">D</span> Décliner poliment les offres de boissons alcooliques</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q14"></div>
    </div>

    <!-- Q15 -->
    <div class="quiz-question-block" id="m0-q15">
      <div class="quiz-q-num">Question 15 / 20</div>
      <div class="quiz-q-text">Selon les règles de communication, que doit dire un agent au lieu de « Je sais pas » ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q15',false,'Raccrocher est une réponse inadaptée et non professionnelle.')"><span class="option-letter">A</span> Raccrocher et rappeler plus tard</div>
        <div class="quiz-option" onclick="answerM0(this,'q15',true,'Correct ! « Je vais vérifier et vous revenir » est la formulation professionnelle qui remplace « Je sais pas ».')"><span class="option-letter">B</span> « Je vais vérifier et vous revenir »</div>
        <div class="quiz-option" onclick="answerM0(this,'q15',false,'Rediriger sans aide est une réponse incomplète et peu professionnelle.')"><span class="option-letter">C</span> « Ce n'est pas mon domaine, appelez ailleurs »</div>
        <div class="quiz-option" onclick="answerM0(this,'q15',false,'Admettre l\\'incompétence sans proposer d\\'alternative n\\'est pas professionnel.')"><span class="option-letter">D</span> « Désolé, je ne suis pas formé pour ça »</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q15"></div>
    </div>

    <!-- Q16 -->
    <div class="quiz-question-block" id="m0-q16">
      <div class="quiz-q-num">Question 16 / 20</div>
      <div class="quiz-q-text">Qu'est-ce que la ZD dans le contexte terrain ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q16',false,'ZD ne signifie pas Zone Digitale.')"><span class="option-letter">A</span> Zone Digitale — la plateforme numérique des agents</div>
        <div class="quiz-option" onclick="answerM0(this,'q16',true,'Correct ! ZD = Zone de Dénombrement — périmètre géographique attribué à une équipe terrain pour organiser la collecte.')"><span class="option-letter">B</span> Zone de Dénombrement — périmètre géographique attribué à une équipe</div>
        <div class="quiz-option" onclick="answerM0(this,'q16',false,'ZD ne signifie pas Zone Douanière.')"><span class="option-letter">C</span> Zone Douanière — secteur de contrôle des importations</div>
        <div class="quiz-option" onclick="answerM0(this,'q16',false,'ZD ne signifie pas Zone de Déploiement Orange.')"><span class="option-letter">D</span> Zone de Déploiement — réseau Orange dans la ville</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q16"></div>
    </div>

    <!-- Q17 -->
    <div class="quiz-question-block" id="m0-q17">
      <div class="quiz-q-num">Question 17 / 20</div>
      <div class="quiz-q-text">Combien de jours maximum un agent peut-il demander de permission ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q17',true,'Correct ! Toute permission doit être demandée formellement — maximum 2 jours.')"><span class="option-letter">A</span> 2 jours maximum</div>
        <div class="quiz-option" onclick="answerM0(this,'q17',false,'3 jours dépasse le maximum autorisé.')"><span class="option-letter">B</span> 3 jours maximum</div>
        <div class="quiz-option" onclick="answerM0(this,'q17',false,'5 jours dépasse largement le maximum autorisé.')"><span class="option-letter">C</span> 5 jours maximum</div>
        <div class="quiz-option" onclick="answerM0(this,'q17',false,'7 jours est bien au-delà du maximum autorisé.')"><span class="option-letter">D</span> 7 jours maximum</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q17"></div>
    </div>

    <!-- Q18 -->
    <div class="quiz-question-block" id="m0-q18">
      <div class="quiz-q-num">Question 18 / 20</div>
      <div class="quiz-q-text">Quelles sont les 4 règles d'or de la communication professionnelle ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q18',false,'Vitesse, précision, rigueur, résultats ne correspondent pas aux 4 règles d\\'or définies.')"><span class="option-letter">A</span> Vitesse, Précision, Rigueur, Résultats</div>
        <div class="quiz-option" onclick="answerM0(this,'q18',true,'Correct ! Les 4 règles d\\'or sont : Clarté, Écoute, Empathie et Solutions.')"><span class="option-letter">B</span> Clarté, Écoute, Empathie, Solutions</div>
        <div class="quiz-option" onclick="answerM0(this,'q18',false,'Sourire, Patience, Respect, Ponctualité sont des qualités mais pas les 4 règles d\\'or définies.')"><span class="option-letter">C</span> Sourire, Patience, Respect, Ponctualité</div>
        <div class="quiz-option" onclick="answerM0(this,'q18',false,'Discipline, Efficacité, Transparence, Engagement ne correspondent pas aux 4 règles d\\'or.')"><span class="option-letter">D</span> Discipline, Efficacité, Transparence, Engagement</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q18"></div>
    </div>

    <!-- Q19 -->
    <div class="quiz-question-block" id="m0-q19">
      <div class="quiz-q-num">Question 19 / 20</div>
      <div class="quiz-q-text">Qu'est-ce que le NCC ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q19',false,'Le NCC n\\'est pas un Numéro de Carte de Contact.')"><span class="option-letter">A</span> Numéro de Carte de Contact — identifiant téléphonique de l'agent</div>
        <div class="quiz-option" onclick="answerM0(this,'q19',false,'Le NCC n\\'est pas un Numéro de Carte de Commerçant — c\\'est un identifiant fiscal.')"><span class="option-letter">B</span> Numéro de Carte de Commerçant — pour les marchands Orange</div>
        <div class="quiz-option" onclick="answerM0(this,'q19',true,'Correct ! NCC = Numéro de Compte Contribuable — identifiant fiscal unique attribué à chaque entreprenant enrôlé.')"><span class="option-letter">C</span> Numéro de Compte Contribuable — identifiant fiscal unique attribué à chaque entreprenant</div>
        <div class="quiz-option" onclick="answerM0(this,'q19',false,'Le NCC n\\'est pas une Note de Conformité.')"><span class="option-letter">D</span> Note de Conformité Client — score attribué après validation Back Office</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q19"></div>
    </div>

    <!-- Q20 -->
    <div class="quiz-question-block" id="m0-q20">
      <div class="quiz-q-num">Question 20 / 20</div>
      <div class="quiz-q-text">Un agent travaille 26 jours, réalise en moyenne 15 fiches validées/jour et a une présence effective de 95%. Quel est son salaire total ?</div>
      <div class="quiz-options">
        <div class="quiz-option" onclick="answerM0(this,'q20',false,'200 000 F est le salaire fixe seul — la prime qualitative s\\'ajoute car toutes les conditions sont remplies.')"><span class="option-letter">A</span> 200 000 FCFA</div>
        <div class="quiz-option" onclick="answerM0(this,'q20',true,'Correct ! 200 000 F (fixe) + 40 000 F (prime qualitative — toutes conditions remplies) = 240 000 FCFA.')"><span class="option-letter">B</span> 240 000 FCFA</div>
        <div class="quiz-option" onclick="answerM0(this,'q20',false,'260 000 F ne correspond à aucune combinaison de la grille de rémunération.')"><span class="option-letter">C</span> 260 000 FCFA</div>
        <div class="quiz-option" onclick="answerM0(this,'q20',false,'La prime est de 40 000 F, pas 50 000 F — le total serait 250 000 F.')"><span class="option-letter">D</span> 250 000 FCFA</div>
      </div>
      <div class="quiz-feedback" id="m0-fb-q20"></div>
    </div>

    <div style="text-align:center;margin-top:24px">
      <button onclick="resetM0()" style="background:var(--blue);color:white;border:none;padding:12px 28px;border-radius:10px;font-family:'Sora',sans-serif;font-size:14px;font-weight:700;cursor:pointer">🔄 Recommencer le quiz</button>
    </div>
  </div><!-- fin tab-m0-quiz -->

  <!-- ═══ RÉSULTATS ═══ -->
  <div class="tab-section" id="tab-m0-resultats" style="display:none">
    <div class="module-hero">
      <div class="module-hero-icon">🏆</div>
      <h1>Résultats — Fondamentaux</h1>
    </div>
    <div style="text-align:center;padding:32px;background:#f8fafc;border-radius:16px;margin:16px 0">
      <div style="font-size:48px;font-weight:900;color:var(--blue)" id="m0-res-score">0 / 20</div>
      <div style="font-size:14px;color:#64748b;margin-top:8px">Score obtenu au quiz Fondamentaux</div>
    </div>
    <div class="alert alert-info">
      <div class="alert-icon">💡</div>
      <div class="alert-text">Un score ≥ 14/20 (70%) valide votre maîtrise des fondamentaux avant de passer aux modules spécialisés. En dessous, relisez les sections concernées et recommencez.</div>
    </div>
  </div><!-- fin tab-m0-resultats -->

</div><!-- fin module-page -->
  </div><!-- fin overlay-content -->
</div><!-- fin overlay-m0 -->

"""

assert OVERLAY_MARKER in html, "Overlay marker not found"
html = html.replace(OVERLAY_MARKER, OVERLAY_M0 + OVERLAY_MARKER, 1)
print("Overlay Fondamentaux OK")

# ============================================================
# 3. JS — insérer avant Quiz M1
# ============================================================
JS_MARKER = "/* ── Quiz M1 — Call Center ── */"

JS_M0 = """/* ── Quiz M0 — Fondamentaux ── */
let scoresM0 = { q1:null, q2:null, q3:null, q4:null, q5:null, q6:null, q7:null, q8:null, q9:null, q10:null, q11:null, q12:null, q13:null, q14:null, q15:null, q16:null, q17:null, q18:null, q19:null, q20:null };
function answerM0(el, qid, correct, feedback) {
  var block = document.getElementById('m0-' + qid);
  if (!block || block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(function(o) { o.classList.add('disabled'); });
  el.classList.add(correct ? 'correct' : 'incorrect');
  var fb = document.getElementById('m0-fb-' + qid);
  if (fb) { fb.textContent = (correct ? '✅ ' : '❌ ') + feedback; fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect'); }
  scoresM0[qid] = correct;
  updateScoreM0();
}
function updateScoreM0() {
  var vals = Object.values(scoresM0), correct = vals.filter(Boolean).length;
  document.getElementById('m0-score-display').textContent = correct + ' / 20';
  if (document.getElementById('m0-res-score')) document.getElementById('m0-res-score').textContent = correct + ' / 20';
}
function resetM0() {
  Object.keys(scoresM0).forEach(function(k){ scoresM0[k]=null; });
  document.querySelectorAll('#tab-m0-quiz .quiz-question-block').forEach(function(block) {
    block.querySelectorAll('.quiz-option').forEach(function(o){ o.className='quiz-option'; });
    var fb = block.querySelector('.quiz-feedback');
    if (fb) { fb.className='quiz-feedback'; fb.textContent=''; }
  });
  updateScoreM0();
}

"""

assert JS_MARKER in html, "JS M1 marker not found"
html = html.replace(JS_MARKER, JS_M0 + JS_MARKER, 1)
print("JS M0 OK")

# ============================================================
# 4. COMPTEUR 6 → 7
# ============================================================
html = html.replace("6 modules disponibles", "7 modules disponibles")
print("Compteur 6 → 7 OK")

# ============================================================
# ÉCRIRE
# ============================================================
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nindex.html: {len(html):,} chars ({len(html)//1024} KB)")
print("Done!")
