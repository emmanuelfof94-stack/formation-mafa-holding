"""
Remplace le contenu du module M4 Orange Business dans index.html
Basé sur Brief_OM_Business___V9__Formation___20251113.pptx (21 slides)
"""
import re, shutil

IDX = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"
BAK = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index_m4backup.html"

shutil.copy(IDX, BAK)
print("Backup OK")

# ── Nouveau contenu M4 complet ────────────────────────────────────────────────
NEW_M4 = r"""
<div class="module-overlay" id="overlay-m4">
  <div class="overlay-topbar">
    <button class="overlay-back" onclick="closeModule()">&#8592; Retour au portail</button>
    <span class="overlay-topbar-title">🏪 Orange Business — Plateforme Marchande</span>
  </div>
  <div class="overlay-content">

<div class="module-page" id="module-m4" style="display:flex;flex-direction:column">

  <!-- En-tête module -->
  <div class="module-header">
    <div class="module-header-bg om-orange-theme">
      <div class="module-num">MODULE 04 · OM BUSINESS</div>
      <div class="module-title">Orange Business — Plateforme Marchande</div>
      <div class="module-meta">
        <span class="module-chip">🏪 Commerciaux OM Business</span>
        <span class="module-chip">⏱ 1h30</span>
        <span class="module-chip">📊 5 quiz · 2 exercices</span>
      </div>
    </div>
    <div class="module-objectives">
      <p>Objectifs pédagogiques</p>
      <ul class="obj-list">
        <li>Comprendre la vision et la promesse OM Business</li>
        <li>Maîtriser les 3 profils (Essentiel, Classique, Premium) et leur cible</li>
        <li>Connaître toutes les fonctionnalités de la plateforme</li>
        <li>Appliquer la grille tarifaire selon le profil</li>
        <li>Guider un marchand dans les parcours de création de compte et d'usage</li>
      </ul>
    </div>
  </div>

  <!-- Onglets -->
  <div class="module-tabs-clean">
    <button class="tab-btn-clean active-red" data-tab="cours" onclick="showModuleTab('m4','cours')">📚 Cours</button>
    <button class="tab-btn-clean" data-tab="exo" onclick="showModuleTab('m4','exo')">✏️ Exercices</button>
    <button class="tab-btn-clean" data-tab="quiz" onclick="showModuleTab('m4','quiz')">✅ Quiz</button>
    <button class="tab-btn-clean" data-tab="resultats" onclick="showModuleTab('m4','resultats')">📊 Résultats</button>
  </div>

  <!-- ══ COURS ══ -->
  <div class="tab-section" id="tab-m4-cours" style="display:block">

    <!-- Section 1 : Vision -->
    <div class="card">
      <div class="card-title">🌟 Vision OM Business</div>
      <div class="info-box orange" style="margin-bottom:20px">
        <div class="info-box-title">Promesse Orange</div>
        <p style="font-size:14px;font-style:italic;color:#584B26;line-height:1.7">
          « Toujours là pour vous connecter à l'essentiel »<br>
          La nouvelle application marchande Orange Money centralise toutes les fonctionnalités essentielles dans une seule plateforme unifiée, conçue pour accompagner tous les profils de commerçants, du plus informel au plus structuré.
        </p>
      </div>
      <div class="info-box blue">
        <div class="info-box-title">Ce que disent nos clients (Insight)</div>
        <p style="font-size:13px;line-height:1.7">« Je recherche une solution de paiement offrant toutes les fonctionnalités nécessaires pour soutenir mon activité commerciale. »</p>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin-top:16px">
        <div style="background:#FFF0E6;border-radius:10px;padding:16px;border-top:3px solid #FF6600">
          <div style="font-size:11px;font-weight:700;color:#FF6600;text-transform:uppercase;margin-bottom:6px">Digitalisation</div>
          <p style="font-size:13px;color:#2d3748">Onboarding 100% digital</p>
        </div>
        <div style="background:#FFF0E6;border-radius:10px;padding:16px;border-top:3px solid #FF6600">
          <div style="font-size:11px;font-weight:700;color:#FF6600;text-transform:uppercase;margin-bottom:6px">Simplicité</div>
          <p style="font-size:13px;color:#2d3748">Des parcours intuitifs</p>
        </div>
        <div style="background:#FFF0E6;border-radius:10px;padding:16px;border-top:3px solid #FF6600">
          <div style="font-size:11px;font-weight:700;color:#FF6600;text-transform:uppercase;margin-bottom:6px">Sécurité</div>
          <p style="font-size:13px;color:#2d3748">Haut niveau de sécurité et traçabilité sur les transactions</p>
        </div>
      </div>
      <div class="info-box teal" style="margin-top:16px">
        <div class="info-box-title">Objectifs stratégiques</div>
        <ul>
          <li>Uniformiser et démocratiser l'offre business</li>
          <li>Accroître la proposition de valeur au sein des activités marchandes</li>
          <li>Intégration de tous les besoins marchands sur une plateforme unique accessible sans SIM</li>
        </ul>
      </div>
    </div>

    <!-- Section 2 : Les 3 profils -->
    <div class="card">
      <div class="card-title">👥 Les 3 Profils OM Business</div>
      <p style="font-size:13px;color:#455A64;margin-bottom:20px;line-height:1.7">
        OM Business cible tous les commerçants en Côte d'Ivoire, qu'ils soient formels ou informels, clients Orange Money ou non.
        L'offre s'adresse aussi bien aux personnes non clientes OM qui souhaitent encaisser facilement (avec ou sans SIM Orange),
        qu'aux marchands actuels (O'calm, Small Business, Classiques) utilisant USSD, applis ou web.
      </p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px">

        <!-- Profil Essentiel -->
        <div style="border:2px solid #FF6600;border-radius:14px;overflow:hidden">
          <div style="background:linear-gradient(135deg,#FF6600,#FF8C00);padding:16px 20px;color:white">
            <div style="font-size:10px;font-weight:700;letter-spacing:.1em;opacity:.8;margin-bottom:4px">PROFIL 1</div>
            <div style="font-size:18px;font-weight:800">OM Business Essentiel</div>
            <div style="font-size:12px;opacity:.85;margin-top:4px">Commerces informels / Micro-entreprises</div>
          </div>
          <div style="padding:16px 20px;background:white">
            <div style="font-size:11px;font-weight:700;color:#FF6600;margin-bottom:8px">EXEMPLES</div>
            <p style="font-size:12px;color:#455A64;line-height:1.6">Épiciers, vendeurs de rue, ambulants, artisans, VTC, auto-entrepreneurs, micro-entreprises débutantes, boutiquiers</p>
            <div style="margin-top:12px;font-size:11px;font-weight:700;color:#FF6600">TAILLE</div>
            <p style="font-size:12px;color:#455A64">CA &lt; 150 000 FCFA/an · 1 à 5 employés</p>
            <div style="margin-top:12px;font-size:11px;font-weight:700;color:#FF6600">BESOINS PRINCIPAUX</div>
            <ul style="list-style:none;margin-top:6px">
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px"><span style="color:#FF6600">→</span> Encaisser partout avec un QR code mobile</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px"><span style="color:#FF6600">→</span> Bénéficier d'un lien de paiement à distance</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px"><span style="color:#FF6600">→</span> Retirer facilement et sans frais</li>
            </ul>
            <div style="margin-top:12px;background:#FFF0E6;border-radius:8px;padding:10px 12px">
              <div style="font-size:10px;font-weight:700;color:#FF6600">VARIANTES</div>
              <p style="font-size:12px;color:#2d3748;margin-top:4px"><strong>Lite :</strong> plafond 200K FCFA/jour<br><strong>Full :</strong> plafond 2M FCFA/jour</p>
            </div>
          </div>
        </div>

        <!-- Profil Classique -->
        <div style="border:2px solid #8D0C23;border-radius:14px;overflow:hidden">
          <div style="background:linear-gradient(135deg,#8D0C23,#B5112C);padding:16px 20px;color:white">
            <div style="font-size:10px;font-weight:700;letter-spacing:.1em;opacity:.8;margin-bottom:4px">PROFIL 2</div>
            <div style="font-size:18px;font-weight:800">OM Business Classique</div>
            <div style="font-size:12px;opacity:.85;margin-top:4px">Petits commerces formels</div>
          </div>
          <div style="padding:16px 20px;background:white">
            <div style="font-size:11px;font-weight:700;color:#8D0C23;margin-bottom:8px">EXEMPLES</div>
            <p style="font-size:12px;color:#455A64;line-height:1.6">Détaillants, supérettes, maquis, bars, magasins, quincailleries, boulangeries</p>
            <div style="margin-top:12px;font-size:11px;font-weight:700;color:#8D0C23">TAILLE</div>
            <p style="font-size:12px;color:#455A64">CA entre 150K et 400M FCFA/an · 2 à 10 employés</p>
            <div style="margin-top:12px;font-size:11px;font-weight:700;color:#8D0C23">BESOINS PRINCIPAUX</div>
            <ul style="list-style:none;margin-top:6px">
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px"><span style="color:#8D0C23">→</span> Bénéficier de plusieurs QR codes imprimés</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px"><span style="color:#8D0C23">→</span> Retirer facilement et sans frais</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px"><span style="color:#8D0C23">→</span> Bonne traçabilité des transactions</li>
            </ul>
            <div style="margin-top:12px;background:#F9E8EC;border-radius:8px;padding:10px 12px">
              <div style="font-size:10px;font-weight:700;color:#8D0C23">PLAFONDS</div>
              <p style="font-size:12px;color:#2d3748;margin-top:4px">Solde : 15M FCFA · Transactions/mois : 30M FCFA</p>
            </div>
          </div>
        </div>

        <!-- Profil Premium -->
        <div style="border:2px solid #584B26;border-radius:14px;overflow:hidden">
          <div style="background:linear-gradient(135deg,#584B26,#CF9E41);padding:16px 20px;color:white">
            <div style="font-size:10px;font-weight:700;letter-spacing:.1em;opacity:.8;margin-bottom:4px">PROFIL 3</div>
            <div style="font-size:18px;font-weight:800">OM Business Premium</div>
            <div style="font-size:12px;opacity:.85;margin-top:4px">Moyens &amp; Grands commerces</div>
          </div>
          <div style="padding:16px 20px;background:white">
            <div style="font-size:11px;font-weight:700;color:#584B26;margin-bottom:8px">EXEMPLES</div>
            <p style="font-size:12px;color:#455A64;line-height:1.6">Commerces structurés, stations-services, supermarchés, pharmacies, hôtels, restaurants, organismes publics</p>
            <div style="margin-top:12px;font-size:11px;font-weight:700;color:#584B26">TAILLE</div>
            <p style="font-size:12px;color:#455A64">CA &gt; 400M FCFA/an · +10 employés</p>
            <div style="margin-top:12px;font-size:11px;font-weight:700;color:#584B26">BESOINS PRINCIPAUX</div>
            <ul style="list-style:none;margin-top:6px">
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px"><span style="color:#584B26">→</span> Gérer les rôles de son personnel</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px"><span style="color:#584B26">→</span> Analyser les performances de l'activité</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px"><span style="color:#584B26">→</span> Facilité de reversement</li>
            </ul>
            <div style="margin-top:12px;background:#F3EDD8;border-radius:8px;padding:10px 12px">
              <div style="font-size:10px;font-weight:700;color:#584B26">PLAFONDS</div>
              <p style="font-size:12px;color:#2d3748;margin-top:4px">Illimité (9 999 999 999 FCFA)</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section 3 : Fonctionnalités -->
    <div class="card">
      <div class="card-title">⚙️ Fonctionnalités de la Plateforme</div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">
        <div style="background:#FFF0E6;border-radius:10px;padding:14px 16px;border-left:3px solid #FF6600">
          <div style="font-size:18px;margin-bottom:6px">📲</div>
          <div style="font-size:13px;font-weight:700;color:#FF6600;margin-bottom:4px">Encaissement QR Code</div>
          <p style="font-size:12px;color:#455A64">0% jusqu'à 50 000 FCFA/jour et 500 000 FCFA/mois · 1% au-delà</p>
        </div>
        <div style="background:#FFF0E6;border-radius:10px;padding:14px 16px;border-left:3px solid #FF6600">
          <div style="font-size:18px;margin-bottom:6px">🔗</div>
          <div style="font-size:13px;font-weight:700;color:#FF6600;margin-bottom:4px">Lien de paiement à distance</div>
          <p style="font-size:12px;color:#455A64">Saisir le montant, choisir le canal de partage, valider</p>
        </div>
        <div style="background:#FFF0E6;border-radius:10px;padding:14px 16px;border-left:3px solid #FF6600">
          <div style="font-size:18px;margin-bottom:6px">💸</div>
          <div style="font-size:13px;font-weight:700;color:#FF6600;margin-bottom:4px">Transfert gratuit</div>
          <p style="font-size:12px;color:#455A64">Transfert à soi-même ou à tiers — 0 FCFA (Essentiel, Classique, Premium)</p>
        </div>
        <div style="background:#FFF0E6;border-radius:10px;padding:14px 16px;border-left:3px solid #FF6600">
          <div style="font-size:18px;margin-bottom:6px">🏧</div>
          <div style="font-size:13px;font-weight:700;color:#FF6600;margin-bottom:4px">Retrait gratuit en PDV</div>
          <p style="font-size:12px;color:#455A64">Retrait par QR code / numéro de téléphone / USSD — 0 FCFA</p>
        </div>
        <div style="background:#FFF0E6;border-radius:10px;padding:14px 16px;border-left:3px solid #FF6600">
          <div style="font-size:18px;margin-bottom:6px">📋</div>
          <div style="font-size:13px;font-weight:700;color:#FF6600;margin-bottom:4px">Historique en temps réel</div>
          <p style="font-size:12px;color:#455A64">Affichage miniature + détails de chaque transaction · Option de remboursement</p>
        </div>
        <div style="background:#FFF0E6;border-radius:10px;padding:14px 16px;border-left:3px solid #FF6600">
          <div style="font-size:18px;margin-bottom:6px">↩️</div>
          <div style="font-size:13px;font-weight:700;color:#FF6600;margin-bottom:4px">Remboursement</div>
          <p style="font-size:12px;color:#455A64">Remboursement d'une transaction directement depuis l'historique</p>
        </div>
        <div style="background:#FFF0E6;border-radius:10px;padding:14px 16px;border-left:3px solid #FF6600">
          <div style="font-size:18px;margin-bottom:6px">📈</div>
          <div style="font-size:13px;font-weight:700;color:#FF6600;margin-bottom:4px">Déplafonnement</div>
          <p style="font-size:12px;color:#455A64">Monter en profil (Essentiel → Classique → Premium) via les paramètres</p>
        </div>
        <div style="background:#FFF0E6;border-radius:10px;padding:14px 16px;border-left:3px solid #FF6600">
          <div style="font-size:18px;margin-bottom:6px">🎓</div>
          <div style="font-size:13px;font-weight:700;color:#FF6600;margin-bottom:4px">Tutoriels intégrés</div>
          <p style="font-size:12px;color:#455A64">Guides d'utilisation accessibles depuis les paramètres de l'application</p>
        </div>
        <div style="background:#FFF0E6;border-radius:10px;padding:14px 16px;border-left:3px solid #FF6600">
          <div style="font-size:18px;margin-bottom:6px">📞</div>
          <div style="font-size:13px;font-weight:700;color:#FF6600;margin-bottom:4px">Assistance client 0808</div>
          <p style="font-size:12px;color:#455A64">Appel au service client depuis l'application (facturation applicable)</p>
        </div>
      </div>
      <div class="info-box teal" style="margin-top:16px">
        <div class="info-box-title">🚀 À venir</div>
        <p style="font-size:13px;color:#2d3748">Le service de crédit et d'épargne <strong>Tik Tak Pro</strong></p>
      </div>
    </div>

    <!-- Section 4 : Tarification -->
    <div class="card">
      <div class="card-title">💰 Grille Tarifaire</div>
      <p style="font-size:13px;color:#455A64;margin-bottom:16px;line-height:1.7">
        OM Business propose une grille tarifaire repensée pour alléger les charges des commerçants et encourager l'usage quotidien.
      </p>
      <div class="tbl-wrap">
        <table class="tbl-orange">
          <thead><tr><th>Opération</th><th>Tarif</th><th>Profil(s)</th></tr></thead>
          <tbody>
            <tr><td>📲 Encaissement QR Code</td><td><strong>0%</strong> jusqu'à 50 000 FCFA/jour (cap 500 000 FCFA/mois)<br>1% au-delà</td><td>Essentiel</td></tr>
            <tr><td>📲 Encaissement QR Code</td><td><strong>1%</strong> par encaissement</td><td>Premium</td></tr>
            <tr><td>🏧 Retrait en PDV</td><td><strong>0 FCFA</strong></td><td>Essentiel · Classique</td></tr>
            <tr><td>💸 Transfert à soi-même et à tiers</td><td><strong>0 FCFA</strong></td><td>Essentiel · Classique · Premium</td></tr>
          </tbody>
        </table>
      </div>
      <div style="margin-top:20px">
        <div style="font-size:12px;font-weight:700;color:#455A64;text-transform:uppercase;letter-spacing:.08em;margin-bottom:12px">Plafonds par profil</div>
        <div class="tbl-wrap">
          <table class="tbl-orange">
            <thead><tr><th>Profil</th><th>Variante</th><th>Solde max</th><th>Trx/Jour</th><th>Trx/Semaine</th><th>Trx/Mois</th></tr></thead>
            <tbody>
              <tr><td rowspan="2">Essentiel</td><td>Lite</td><td>200 000</td><td>200 000</td><td>200 000</td><td>200 000</td></tr>
              <tr><td>Full</td><td>2 000 000</td><td>7 500 000</td><td>10 000 000</td><td>10 000 000</td></tr>
              <tr><td>Classique</td><td>—</td><td>15 000 000</td><td>15 000 000</td><td>N/A</td><td>30 000 000</td></tr>
              <tr><td>Premium</td><td>—</td><td>9 999 999 999</td><td>9 999 999 999</td><td>9 999 999 999</td><td>9 999 999 999</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Section 5 : Parcours clients -->
    <div class="card">
      <div class="card-title">🗺️ Parcours Clients OM Business</div>

      <!-- Création de compte -->
      <div class="info-box orange" style="margin-bottom:16px">
        <div class="info-box-title">1. Création de compte</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:10px">
          <div>
            <div style="font-size:12px;font-weight:700;color:#FF6600;margin-bottom:8px">👤 Clients OM (déjà Orange Money)</div>
            <ul style="list-style:none">
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">1</span> Saisie du numéro</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">2</span> Parcours de catégorisation du commerce (nom, secteur)</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">3</span> Accès à la localisation</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">4</span> Validation des CGU</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">5</span> Génération / Récupération du QR code marchand</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">6</span> Activation des notifications</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">7</span> Accès à l'interface OM Business</li>
            </ul>
            <div style="background:#FFF0E6;border-radius:8px;padding:8px 12px;margin-top:8px;font-size:11px;color:#584B26">
              <strong>Migration O'calm</strong> → Essentiel Full<br>
              <strong>Migration SMB</strong> → Classique<br>
              <strong>Migration Classique</strong> → Premium
            </div>
          </div>
          <div>
            <div style="font-size:12px;font-weight:700;color:#FF6600;margin-bottom:8px">🆕 Clients Non-OM</div>
            <ul style="list-style:none">
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">1</span> Saisie du numéro</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">2</span> Demande de création de compte</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">3</span> Parcours KYC : nom, prénom, date de naissance, n° de pièce, photo</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">4</span> Corbeille de validation Back-Office</li>
              <li style="font-size:12px;padding:3px 0;display:flex;gap:8px;color:#2d3748"><span style="font-weight:700">5</span> Notification : compte activé</li>
            </ul>
            <div style="background:#FFF0E6;border-radius:8px;padding:8px 12px;margin-top:8px;font-size:11px;color:#584B26">
              Fonctionne aussi pour les clients <strong>Non-Orange telco</strong> (sans SIM Orange / en OTT)
            </div>
          </div>
        </div>
      </div>

      <!-- Encaissement -->
      <div style="background:#F9E8EC;border-radius:10px;padding:14px 16px;margin-bottom:12px">
        <div style="font-size:13px;font-weight:700;color:#8D0C23;margin-bottom:8px">📲 Encaissement par QR Code</div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <span style="background:#8D0C23;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">1 · Exposer son QR code au client</span>
          <span style="color:#8D0C23;font-weight:700;align-self:center">→</span>
          <span style="background:#8D0C23;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">2 · Le client scanne, saisit le montant et confirme</span>
          <span style="color:#8D0C23;font-weight:700;align-self:center">→</span>
          <span style="background:#8D0C23;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">3 · Réception de la confirmation</span>
        </div>
      </div>

      <!-- Lien encaissement -->
      <div style="background:#F9E8EC;border-radius:10px;padding:14px 16px;margin-bottom:12px">
        <div style="font-size:13px;font-weight:700;color:#8D0C23;margin-bottom:8px">🔗 Envoi de lien d'encaissement à distance</div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <span style="background:#8D0C23;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">1 · Cliquer "Envoi de lien"</span>
          <span style="color:#8D0C23;font-weight:700;align-self:center">→</span>
          <span style="background:#8D0C23;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">2 · Saisir le montant (optionnel)</span>
          <span style="color:#8D0C23;font-weight:700;align-self:center">→</span>
          <span style="background:#8D0C23;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">3 · Choisir le canal</span>
          <span style="color:#8D0C23;font-weight:700;align-self:center">→</span>
          <span style="background:#8D0C23;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">4 · Valider le partage</span>
        </div>
      </div>

      <!-- Transfert -->
      <div style="background:#F3EDD8;border-radius:10px;padding:14px 16px;margin-bottom:12px">
        <div style="font-size:13px;font-weight:700;color:#584B26;margin-bottom:8px">💸 Transfert (Gratuit)</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
          <div>
            <div style="font-size:11px;font-weight:700;color:#584B26;margin-bottom:6px">À soi-même</div>
            <div style="display:flex;flex-direction:column;gap:4px">
              <span style="font-size:12px;color:#2d3748">1 · Cliquer "Transfert"</span>
              <span style="font-size:12px;color:#2d3748">2 · Choisir "à moi-même"</span>
              <span style="font-size:12px;color:#2d3748">3 · Saisir le montant</span>
              <span style="font-size:12px;color:#2d3748">4 · Confirmer avec code secret</span>
            </div>
          </div>
          <div>
            <div style="font-size:11px;font-weight:700;color:#584B26;margin-bottom:6px">À un tiers</div>
            <div style="display:flex;flex-direction:column;gap:4px">
              <span style="font-size:12px;color:#2d3748">1 · Cliquer "Transfert"</span>
              <span style="font-size:12px;color:#2d3748">2 · Choisir "Autre transfert"</span>
              <span style="font-size:12px;color:#2d3748">3 · Sélectionner/saisir le contact + montant</span>
              <span style="font-size:12px;color:#2d3748">4 · Confirmer avec code secret</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Retrait -->
      <div style="background:#F3EDD8;border-radius:10px;padding:14px 16px;margin-bottom:12px">
        <div style="font-size:13px;font-weight:700;color:#584B26;margin-bottom:8px">🏧 Retrait en PDV (Gratuit)</div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <span style="background:#584B26;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">1 · Cliquer "Retrait"</span>
          <span style="color:#584B26;font-weight:700;align-self:center">→</span>
          <span style="background:#584B26;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">2 · Exposer son QR code au PDV</span>
          <span style="color:#584B26;font-weight:700;align-self:center">→</span>
          <span style="background:#584B26;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">3 · Confirmer sur la liste d'attente</span>
          <span style="color:#584B26;font-weight:700;align-self:center">→</span>
          <span style="background:#584B26;color:white;border-radius:20px;padding:4px 12px;font-size:12px;font-weight:700">4 · Vérifier l'historique</span>
        </div>
        <p style="font-size:11px;color:#455A64;margin-top:8px">Alternative USSD : #145*2#</p>
      </div>

      <!-- Déplafonnement -->
      <div style="background:#E3F2FD;border-radius:10px;padding:14px 16px;border-left:3px solid #1565C0">
        <div style="font-size:13px;font-weight:700;color:#1565C0;margin-bottom:8px">📈 Déplafonnement</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
          <div>
            <div style="font-size:11px;font-weight:700;color:#1565C0;margin-bottom:6px">Vers Profil Classique</div>
            <ol style="padding-left:16px;font-size:12px;color:#2d3748;line-height:1.8">
              <li>Menu options (haut gauche)</li>
              <li>Cliquer "Demander déplafonnement"</li>
              <li>Sélectionner "Profil Classique"</li>
              <li>Fournir les pièces requises (annexe 1)</li>
              <li>Retour client sous 24H</li>
            </ol>
          </div>
          <div>
            <div style="font-size:11px;font-weight:700;color:#1565C0;margin-bottom:6px">Vers Profil Premium</div>
            <ol style="padding-left:16px;font-size:12px;color:#2d3748;line-height:1.8">
              <li>Menu options (haut gauche)</li>
              <li>Cliquer "Demander déplafonnement"</li>
              <li>Sélectionner "Profil Premium"</li>
              <li>Sélectionner la forme juridique</li>
              <li>Fournir la documentation (annexe 2)</li>
              <li>Retour client sous 24H</li>
            </ol>
          </div>
        </div>
      </div>
    </div>

  </div><!-- fin tab-m4-cours -->

  <!-- ══ EXERCICES ══ -->
  <div class="tab-section" id="tab-m4-exo" style="display:none">
    <div class="card">
      <div class="card-title">✏️ Exercice 1 — Qualifier le bon profil marchand</div>
      <div class="exercise-box">
        <div class="exercise-title">📋 Mise en situation</div>
        <p>Pour chacun des commerçants ci-dessous, identifiez le profil OM Business approprié (Essentiel Lite / Essentiel Full / Classique / Premium) et justifiez votre choix.</p>
      </div>
      <div style="display:flex;flex-direction:column;gap:14px;margin-top:16px">
        <div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px">
          <div style="font-size:12px;font-weight:700;color:#455A64;margin-bottom:8px">CAS A — Mireille</div>
          <p style="font-size:13px;color:#2d3748">Vendeuse ambulante de fruits au marché d'Adjamé. Travaille seule. Ses recettes mensuelles dépassent rarement 80 000 FCFA. Elle veut pouvoir encaisser avec un QR code depuis son téléphone.</p>
          <div style="margin-top:10px;background:#f8fafc;border-radius:8px;padding:10px;font-size:12px;color:#455A64">
            <strong>Réponse :</strong> OM Business <strong>Essentiel Lite</strong> — CA &lt; 150K/an, besoin d'encaissement mobile simple, plafond 200 000 FCFA/jour suffisant.
          </div>
        </div>
        <div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px">
          <div style="font-size:12px;font-weight:700;color:#455A64;margin-bottom:8px">CAS B — M. Kouamé</div>
          <p style="font-size:13px;color:#2d3748">Propriétaire d'une supérette à Cocody. 5 employés. CA mensuel d'environ 8 millions FCFA. Il veut tracer toutes ses transactions, imprimer plusieurs QR codes pour ses caisses et retirer sans frais.</p>
          <div style="margin-top:10px;background:#f8fafc;border-radius:8px;padding:10px;font-size:12px;color:#455A64">
            <strong>Réponse :</strong> OM Business <strong>Classique</strong> — besoin de traçabilité, multi-QR codes, CA entre 150K et 400M/an.
          </div>
        </div>
        <div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px">
          <div style="font-size:12px;font-weight:700;color:#455A64;margin-bottom:8px">CAS C — Hôtel Ôasis</div>
          <p style="font-size:13px;color:#2d3748">Hôtel 3 étoiles à Abidjan Plateau. 30 employés. CA annuel : 2 milliards FCFA. Besoin de gestion des rôles du personnel, d'analyse des performances et de reversements faciles.</p>
          <div style="margin-top:10px;background:#f8fafc;border-radius:8px;padding:10px;font-size:12px;color:#455A64">
            <strong>Réponse :</strong> OM Business <strong>Premium</strong> — CA &gt; 400M/an, besoins de gestion multi-utilisateurs et d'analyse avancée.
          </div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">✏️ Exercice 2 — Simulation parcours création de compte Non-OM</div>
      <div class="exercise-box">
        <div class="exercise-title">📋 Mise en situation</div>
        <p>Un commerçant se présente à vous. Il n'a pas de compte Orange Money. Il veut ouvrir un compte OM Business Essentiel. Décrivez étape par étape le parcours à suivre et indiquez quels documents il doit fournir.</p>
      </div>
      <div style="margin-top:16px">
        <div style="font-size:13px;font-weight:700;color:#8D0C23;margin-bottom:12px">Étapes du parcours Non-OM :</div>
        <div style="display:flex;flex-direction:column;gap:8px">
          <div style="display:flex;gap:12px;align-items:flex-start;background:#f8fafc;border-radius:8px;padding:10px 14px">
            <span style="background:#8D0C23;color:white;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0">1</span>
            <p style="font-size:13px;color:#2d3748">Saisir le numéro du commerçant dans l'application</p>
          </div>
          <div style="display:flex;gap:12px;align-items:flex-start;background:#f8fafc;border-radius:8px;padding:10px 14px">
            <span style="background:#8D0C23;color:white;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0">2</span>
            <p style="font-size:13px;color:#2d3748">Lancer la demande de création de compte marchand</p>
          </div>
          <div style="display:flex;gap:12px;align-items:flex-start;background:#f8fafc;border-radius:8px;padding:10px 14px">
            <span style="background:#8D0C23;color:white;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0">3</span>
            <p style="font-size:13px;color:#2d3748">Renseigner : Nom, Prénom, Date de naissance, Numéro de pièce d'identité, Photo de la pièce recto/verso</p>
          </div>
          <div style="display:flex;gap:12px;align-items:flex-start;background:#f8fafc;border-radius:8px;padding:10px 14px">
            <span style="background:#8D0C23;color:white;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0">4</span>
            <p style="font-size:13px;color:#2d3748">Le dossier passe en corbeille de validation Back-Office</p>
          </div>
          <div style="display:flex;gap:12px;align-items:flex-start;background:#F9E8EC;border-radius:8px;padding:10px 14px">
            <span style="background:#8D0C23;color:white;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0">5</span>
            <p style="font-size:13px;color:#2d3748">Le commerçant reçoit une notification de confirmation : compte activé ✅</p>
          </div>
        </div>
      </div>
    </div>
  </div><!-- fin tab-m4-exo -->

  <!-- ══ QUIZ ══ -->
  <div class="tab-section" id="tab-m4-quiz" style="display:none">
    <div class="quiz-area">
      <div class="quiz-header">
        <h3>✅ Quiz — Module OM Business</h3>
        <p>5 questions · Basé sur le Brief OM Business V9</p>
      </div>
      <div class="quiz-body">

        <div class="quiz-question-block" id="m4-q1">
          <div class="quiz-q-num">Question 01 / 05</div>
          <div class="quiz-q-text">Quel profil OM Business convient à un commerçant avec un CA annuel inférieur à 150 000 FCFA et 1 à 5 employés ?</div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="answerM4(this,'m4-q1',false,'Le profil Classique cible les petits commerces formels avec un CA entre 150K et 400M FCFA/an.')"><span class="option-letter">A</span> OM Business Classique</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q1',true,'Correct ! L\'Essentiel cible les commerces informels / micro-entreprises avec CA &lt; 150K FCFA/an et 1 à 5 employés.')"><span class="option-letter">B</span> OM Business Essentiel</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q1',false,'Le Premium est réservé aux grandes entreprises avec CA &gt; 400M FCFA/an et plus de 10 employés.')"><span class="option-letter">C</span> OM Business Premium</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q1',false,'Ce profil n\'existe pas dans la gamme OM Business.')"><span class="option-letter">D</span> OM Business Pro</div>
          </div>
          <div class="quiz-feedback" id="fb-m4-q1"></div>
        </div>

        <div class="quiz-question-block" id="m4-q2">
          <div class="quiz-q-num">Question 02 / 05</div>
          <div class="quiz-q-text">Quel est le tarif d'encaissement par QR Code pour un marchand Essentiel jusqu'à 50 000 FCFA/jour ?</div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="answerM4(this,'m4-q2',false,'Non, le taux de 1% s\'applique uniquement au-delà de 50 000 FCFA/jour ou pour le profil Premium.')"><span class="option-letter">A</span> 1% de la transaction</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q2',false,'500 FCFA n\'est pas un tarif OM Business.')"><span class="option-letter">B</span> 500 FCFA forfait</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q2',true,'Correct ! L\'encaissement est à 0% jusqu\'à 50 000 FCFA/jour (plafonné à 500 000 FCFA/mois cumulés) pour le profil Essentiel.')"><span class="option-letter">C</span> 0% jusqu'à 50 000 FCFA/jour</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q2',false,'0,5% n\'est pas le tarif appliqué.')"><span class="option-letter">D</span> 0,5%</div>
          </div>
          <div class="quiz-feedback" id="fb-m4-q2"></div>
        </div>

        <div class="quiz-question-block" id="m4-q3">
          <div class="quiz-q-num">Question 03 / 05</div>
          <div class="quiz-q-text">Un client Non-OM veut ouvrir un compte OM Business. Quelle étape suit la soumission du dossier KYC ?</div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="answerM4(this,'m4-q3',false,'Le QR code n\'est généré qu\'après validation du compte, pas directement après le KYC.')"><span class="option-letter">A</span> Génération immédiate du QR code marchand</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q3',true,'Correct ! Après le parcours KYC, le dossier passe en corbeille de validation Back-Office avant l\'activation.')"><span class="option-letter">B</span> Le dossier passe en corbeille de validation Back-Office</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q3',false,'L\'accès à l\'interface OM Business n\'est accordé qu\'après la validation du compte.')"><span class="option-letter">C</span> Accès immédiat à l'interface OM Business</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q3',false,'Le paiement de frais n\'est pas requis à l\'inscription.')"><span class="option-letter">D</span> Paiement de frais d'inscription</div>
          </div>
          <div class="quiz-feedback" id="fb-m4-q3"></div>
        </div>

        <div class="quiz-question-block" id="m4-q4">
          <div class="quiz-q-num">Question 04 / 05</div>
          <div class="quiz-q-text">Un marchand Essentiel Full veut augmenter ses plafonds. Quelle action doit-il effectuer ?</div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="answerM4(this,'m4-q4',false,'Appeler le 0808 n\'est pas la procédure de déplafonnement.')"><span class="option-letter">A</span> Appeler le service client au 0808</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q4',false,'Créer un nouveau compte n\'est pas la procédure requise.')"><span class="option-letter">B</span> Créer un nouveau compte OM Business</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q4',true,'Correct ! Il doit aller dans les options, cliquer "Demander déplafonnement", sélectionner le nouveau profil et fournir les pièces justificatives. Retour sous 24H.')"><span class="option-letter">C</span> Aller dans les paramètres → "Demander déplafonnement" → fournir les pièces</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q4',false,'Le déplafonnement ne se fait pas en agence Orange directement.')"><span class="option-letter">D</span> Se rendre en agence Orange avec un dossier physique</div>
          </div>
          <div class="quiz-feedback" id="fb-m4-q4"></div>
        </div>

        <div class="quiz-question-block" id="m4-q5">
          <div class="quiz-q-num">Question 05 / 05</div>
          <div class="quiz-q-text">Quel est le coût d'un retrait en PDV pour un marchand OM Business Essentiel ou Classique ?</div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="answerM4(this,'m4-q5',false,'Ce n\'est pas le tarif appliqué aux profils Essentiel et Classique.')"><span class="option-letter">A</span> 1% du montant</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q5',false,'500 FCFA n\'est pas le tarif de retrait.')"><span class="option-letter">B</span> 500 FCFA forfait</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q5',true,'Correct ! Le retrait en PDV est gratuit (0 FCFA) pour les profils Essentiel et Classique.')"><span class="option-letter">C</span> 0 FCFA (gratuit)</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q5',false,'Le retrait en PDV n\'est pas interdit, il est gratuit.')"><span class="option-letter">D</span> Non disponible pour ces profils</div>
          </div>
          <div class="quiz-feedback" id="fb-m4-q5"></div>
        </div>

        <div style="margin-top:24px;padding-top:20px;border-top:1px solid #e2e8f0;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-size:24px;font-weight:800;color:#8D0C23" id="m4-score-display">0 <span style="font-size:16px;color:#888">/ 5</span></div>
            <div style="font-size:12px;color:#888" id="m4-prog-label">0 / 5 questions</div>
          </div>
          <button class="btn btn-primary" onclick="showModuleTab('m4','resultats')">Voir les résultats →</button>
        </div>
      </div>
    </div>
  </div><!-- fin tab-m4-quiz -->

  <!-- ══ RÉSULTATS ══ -->
  <div class="tab-section" id="tab-m4-resultats" style="display:none">
    <div class="card" style="text-align:center;padding:60px 20px">
      <div style="font-size:48px;margin-bottom:16px">📊</div>
      <h3 style="margin-bottom:8px;color:#FF6600">Résultats du quiz</h3>
      <div style="font-size:32px;font-weight:700;color:#FF6600;margin:20px 0" id="m4-score-display-r">0 <span style="font-size:18px;color:#888">/ 5</span></div>
      <div class="progress-bar" style="margin:0 auto 20px;max-width:300px">
        <div class="progress-fill" id="m4-prog-fill" style="width:0%;background:linear-gradient(90deg,#FF6600,#FF8C00)"></div>
      </div>
      <div style="color:#888;font-size:14px" id="m4-prog-label-r">0 / 5 questions</div>
    </div>
    <div class="card" style="text-align:center">
      <div class="card-title">🔄 Actions</div>
      <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
        <button class="btn btn-outline" onclick="showModuleTab('m4','quiz')">🔄 Reprendre le quiz</button>
        <button class="btn btn-primary" onclick="showModuleTab('m4','cours')">📚 Revoir le cours</button>
      </div>
    </div>
  </div><!-- fin tab-m4-resultats -->

</div><!-- fin module-m4 -->

  </div><!-- fin overlay-content -->
</div><!-- fin overlay-m4 -->
"""

# ── Remplacer le bloc overlay-m4 dans index.html ─────────────────────────────
with open(IDX, "r", encoding="utf-8") as f:
    txt = f.read()

# Trouver le début et la fin de l'overlay-m4
start_marker = '<div class="module-overlay" id="overlay-m4">'
end_marker   = '<div class="module-overlay" id="overlay-m5">'

start = txt.find(start_marker)
end   = txt.find(end_marker)

if start == -1 or end == -1:
    print("ERREUR: marqueurs non trouvés!")
    exit(1)

new_txt = txt[:start] + NEW_M4 + '\n\n' + txt[end:]

# Corriger answerM4 pour mettre à jour les deux displays score (quiz + résultats)
# Le quiz utilise m4-score-display et m4-prog-label
# Les résultats utilisent m4-score-display-r et m4-prog-label-r
# On met à jour la fonction answerM4 dans le JS
old_fn = """/* ── Quiz M4 — OM Business ── */
let scoresM4 = { q1:null, q2:null, q3:null, q4:null, q5:null };
function answerM4(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM4[qid] = correct;
  const total = Object.values(scoresM4).filter(v => v === true).length;
  const answered = Object.values(scoresM4).filter(v => v !== null).length;
  document.getElementById('m4-score-display').innerHTML = total + ' <span>/ 5</span>';
  document.getElementById('m4-prog-label').textContent = answered + ' / 5';
  document.getElementById('m4-prog-fill').style.width = (answered / 5 * 100) + '%';
}"""

new_fn = """/* ── Quiz M4 — OM Business ── */
let scoresM4 = { q1:null, q2:null, q3:null, q4:null, q5:null };
function answerM4(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM4[qid] = correct;
  const total = Object.values(scoresM4).filter(v => v === true).length;
  const answered = Object.values(scoresM4).filter(v => v !== null).length;
  const scoreHtml = total + ' <span style="font-size:16px;color:#888">/ 5</span>';
  if (document.getElementById('m4-score-display')) document.getElementById('m4-score-display').innerHTML = scoreHtml;
  if (document.getElementById('m4-score-display-r')) document.getElementById('m4-score-display-r').innerHTML = scoreHtml;
  if (document.getElementById('m4-prog-label')) document.getElementById('m4-prog-label').textContent = answered + ' / 5';
  if (document.getElementById('m4-prog-label-r')) document.getElementById('m4-prog-label-r').textContent = answered + ' / 5';
  if (document.getElementById('m4-prog-fill')) document.getElementById('m4-prog-fill').style.width = (answered / 5 * 100) + '%';
}"""

new_txt = new_txt.replace(old_fn, new_fn)

with open(IDX, "w", encoding="utf-8") as f:
    f.write(new_txt)

print(f"index.html: {len(new_txt):,} chars ({len(new_txt)//1024} KB)")
print("Module M4 remplacé avec succès!")
