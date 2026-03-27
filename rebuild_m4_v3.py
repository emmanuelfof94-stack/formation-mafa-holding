"""
Rebuild M4 avec images intégrées (captures d'écran app OM Business)
"""
import re, shutil

IDX = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index.html"
BAK = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\index_m4v3bak.html"
shutil.copy(IDX, BAK)

IMG = "img_m4"  # chemin relatif depuis index.html

NEW_M4 = f"""
<div class="module-overlay" id="overlay-m4">
  <div class="overlay-topbar">
    <button class="overlay-back" onclick="closeModule()">&#8592; Retour au portail</button>
    <span class="overlay-topbar-title">🏪 Orange Business — Plateforme Marchande</span>
  </div>
  <div class="overlay-content">
<div class="module-page" id="module-m4" style="display:flex;flex-direction:column">

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
        <li>Maîtriser les 3 profils (Essentiel, Classique, Premium)</li>
        <li>Connaître toutes les fonctionnalités de la plateforme</li>
        <li>Appliquer la grille tarifaire selon le profil</li>
        <li>Guider un marchand dans chaque parcours d'usage</li>
      </ul>
    </div>
  </div>

  <div class="module-tabs-clean">
    <button class="tab-btn-clean active-red" data-tab="cours" onclick="showModuleTab('m4','cours')">📚 Cours</button>
    <button class="tab-btn-clean" data-tab="exo" onclick="showModuleTab('m4','exo')">✏️ Exercices</button>
    <button class="tab-btn-clean" data-tab="quiz" onclick="showModuleTab('m4','quiz')">✅ Quiz</button>
    <button class="tab-btn-clean" data-tab="resultats" onclick="showModuleTab('m4','resultats')">📊 Résultats</button>
  </div>

  <!-- ══ COURS ══ -->
  <div class="tab-section" id="tab-m4-cours" style="display:block">

    <!-- Vision -->
    <div class="card">
      <div class="card-title">🌟 Vision OM Business</div>
      <div class="info-box orange" style="margin-bottom:16px">
        <div class="info-box-title">Promesse Orange</div>
        <p style="font-size:14px;font-style:italic;color:#584B26;line-height:1.7">« Toujours là pour vous connecter à l'essentiel »<br>
        La nouvelle application marchande Orange Money centralise toutes les fonctionnalités essentielles dans une seule plateforme unifiée, conçue pour accompagner tous les profils de commerçants, du plus informel au plus structuré.</p>
      </div>
      <div style="display:grid;grid-template-columns:1fr auto;gap:20px;align-items:start">
        <div>
          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px">
            <div style="background:#FFF0E6;border-radius:10px;padding:14px;border-top:3px solid #FF6600;text-align:center">
              <div style="font-size:22px;margin-bottom:6px">📱</div>
              <div style="font-size:11px;font-weight:700;color:#FF6600;text-transform:uppercase">Digitalisation</div>
              <p style="font-size:12px;color:#455A64;margin-top:4px">Onboarding 100% digital</p>
            </div>
            <div style="background:#FFF0E6;border-radius:10px;padding:14px;border-top:3px solid #FF6600;text-align:center">
              <div style="font-size:22px;margin-bottom:6px">✨</div>
              <div style="font-size:11px;font-weight:700;color:#FF6600;text-transform:uppercase">Simplicité</div>
              <p style="font-size:12px;color:#455A64;margin-top:4px">Parcours intuitifs</p>
            </div>
            <div style="background:#FFF0E6;border-radius:10px;padding:14px;border-top:3px solid #FF6600;text-align:center">
              <div style="font-size:22px;margin-bottom:6px">🔒</div>
              <div style="font-size:11px;font-weight:700;color:#FF6600;text-transform:uppercase">Sécurité</div>
              <p style="font-size:12px;color:#455A64;margin-top:4px">Traçabilité totale</p>
            </div>
          </div>
          <div class="info-box teal">
            <div class="info-box-title">Objectifs stratégiques</div>
            <ul>
              <li>Uniformiser et démocratiser l'offre business</li>
              <li>Accroître la proposition de valeur marchande</li>
              <li>Centraliser tous les besoins sur une plateforme unique accessible sans SIM</li>
            </ul>
          </div>
        </div>
        <div style="text-align:center">
          <div class="phone-frame" style="width:130px;margin:0 auto">
            <img src="{IMG}/fonctions_interface.jpg" alt="Interface OM Business" style="width:100%;display:block;border-radius:20px">
          </div>
          <p style="font-size:11px;color:#888;margin-top:8px;text-align:center">Interface OM Business</p>
        </div>
      </div>
    </div>

    <!-- 3 Profils -->
    <div class="card">
      <div class="card-title">👥 Les 3 Profils OM Business</div>
      <p style="font-size:13px;color:#455A64;margin-bottom:20px;line-height:1.7">
        OM Business cible tous les commerçants en Côte d'Ivoire, formels ou informels, clients Orange Money ou non.
      </p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px">

        <div style="border:2px solid #FF6600;border-radius:14px;overflow:hidden">
          <div style="background:linear-gradient(135deg,#FF6600,#FF8C00);padding:16px 20px;color:white">
            <div style="font-size:10px;font-weight:700;opacity:.8;margin-bottom:4px">PROFIL 1</div>
            <div style="font-size:17px;font-weight:800">OM Business Essentiel</div>
            <div style="font-size:12px;opacity:.85;margin-top:4px">Commerces informels / Micro-entreprises</div>
          </div>
          <div style="padding:14px 18px;background:white">
            <p style="font-size:12px;color:#455A64;line-height:1.6;margin-bottom:10px">Épiciers, vendeurs ambulants, artisans, auto-entrepreneurs, VTC, boutiquiers</p>
            <div style="font-size:11px;font-weight:700;color:#FF6600">TAILLE</div>
            <p style="font-size:12px;color:#455A64;margin-bottom:8px">CA &lt; 150 000 FCFA/an · 1 à 5 employés</p>
            <div style="font-size:11px;font-weight:700;color:#FF6600">BESOINS</div>
            <ul style="list-style:none;margin-top:4px">
              <li style="font-size:12px;padding:2px 0;display:flex;gap:6px"><span style="color:#FF6600">→</span> Encaisser avec un QR code mobile</li>
              <li style="font-size:12px;padding:2px 0;display:flex;gap:6px"><span style="color:#FF6600">→</span> Lien de paiement à distance</li>
              <li style="font-size:12px;padding:2px 0;display:flex;gap:6px"><span style="color:#FF6600">→</span> Retrait sans frais</li>
            </ul>
            <div style="background:#FFF0E6;border-radius:8px;padding:8px 10px;margin-top:8px;font-size:11px;color:#584B26">
              <strong>Lite</strong> : plafond 200K FCFA/j &nbsp;|&nbsp; <strong>Full</strong> : 2M FCFA/j
            </div>
          </div>
        </div>

        <div style="border:2px solid #8D0C23;border-radius:14px;overflow:hidden">
          <div style="background:linear-gradient(135deg,#8D0C23,#B5112C);padding:16px 20px;color:white">
            <div style="font-size:10px;font-weight:700;opacity:.8;margin-bottom:4px">PROFIL 2</div>
            <div style="font-size:17px;font-weight:800">OM Business Classique</div>
            <div style="font-size:12px;opacity:.85;margin-top:4px">Petits commerces formels</div>
          </div>
          <div style="padding:14px 18px;background:white">
            <p style="font-size:12px;color:#455A64;line-height:1.6;margin-bottom:10px">Détaillants, supérettes, maquis, bars, quincailleries, boulangeries</p>
            <div style="font-size:11px;font-weight:700;color:#8D0C23">TAILLE</div>
            <p style="font-size:12px;color:#455A64;margin-bottom:8px">CA entre 150K et 400M FCFA/an · 2 à 10 employés</p>
            <div style="font-size:11px;font-weight:700;color:#8D0C23">BESOINS</div>
            <ul style="list-style:none;margin-top:4px">
              <li style="font-size:12px;padding:2px 0;display:flex;gap:6px"><span style="color:#8D0C23">→</span> Multi QR codes imprimés</li>
              <li style="font-size:12px;padding:2px 0;display:flex;gap:6px"><span style="color:#8D0C23">→</span> Traçabilité des transactions</li>
              <li style="font-size:12px;padding:2px 0;display:flex;gap:6px"><span style="color:#8D0C23">→</span> Retrait sans frais</li>
            </ul>
            <div style="background:#F9E8EC;border-radius:8px;padding:8px 10px;margin-top:8px;font-size:11px;color:#8D0C23">
              Solde max : 15M FCFA · Trx/mois : 30M FCFA
            </div>
          </div>
        </div>

        <div style="border:2px solid #584B26;border-radius:14px;overflow:hidden">
          <div style="background:linear-gradient(135deg,#584B26,#CF9E41);padding:16px 20px;color:white">
            <div style="font-size:10px;font-weight:700;opacity:.8;margin-bottom:4px">PROFIL 3</div>
            <div style="font-size:17px;font-weight:800">OM Business Premium</div>
            <div style="font-size:12px;opacity:.85;margin-top:4px">Moyens &amp; Grands commerces</div>
          </div>
          <div style="padding:14px 18px;background:white">
            <p style="font-size:12px;color:#455A64;line-height:1.6;margin-bottom:10px">Stations-services, supermarchés, pharmacies, hôtels, restaurants, organismes publics</p>
            <div style="font-size:11px;font-weight:700;color:#584B26">TAILLE</div>
            <p style="font-size:12px;color:#455A64;margin-bottom:8px">CA &gt; 400M FCFA/an · +10 employés</p>
            <div style="font-size:11px;font-weight:700;color:#584B26">BESOINS</div>
            <ul style="list-style:none;margin-top:4px">
              <li style="font-size:12px;padding:2px 0;display:flex;gap:6px"><span style="color:#584B26">→</span> Gestion des rôles du personnel</li>
              <li style="font-size:12px;padding:2px 0;display:flex;gap:6px"><span style="color:#584B26">→</span> Analyse des performances</li>
              <li style="font-size:12px;padding:2px 0;display:flex;gap:6px"><span style="color:#584B26">→</span> Facilité de reversement</li>
            </ul>
            <div style="background:#F3EDD8;border-radius:8px;padding:8px 10px;margin-top:8px;font-size:11px;color:#584B26">
              Plafonds illimités (9 999 999 999 FCFA)
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Tarification -->
    <div class="card">
      <div class="card-title">💰 Grille Tarifaire</div>
      <div class="tbl-wrap">
        <table class="tbl-orange">
          <thead><tr><th>Opération</th><th>Tarif</th><th>Profil(s)</th></tr></thead>
          <tbody>
            <tr><td>📲 Encaissement QR Code</td><td><strong>0%</strong> jusqu'à 50 000 FCFA/j (cap 500K/mois) · 1% au-delà</td><td>Essentiel</td></tr>
            <tr><td>📲 Encaissement QR Code</td><td><strong>1%</strong> par encaissement</td><td>Premium</td></tr>
            <tr><td>🏧 Retrait en PDV</td><td><strong>0 FCFA</strong></td><td>Essentiel · Classique</td></tr>
            <tr><td>💸 Transfert (soi-même / tiers)</td><td><strong>0 FCFA</strong></td><td>Essentiel · Classique · Premium</td></tr>
          </tbody>
        </table>
      </div>
      <div style="margin-top:18px">
        <div style="font-size:12px;font-weight:700;color:#455A64;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px">Plafonds par profil (FCFA)</div>
        <div class="tbl-wrap">
          <table class="tbl-orange">
            <thead><tr><th>Profil</th><th>Variante</th><th>Solde</th><th>Trx/Jour</th><th>Trx/Semaine</th><th>Trx/Mois</th></tr></thead>
            <tbody>
              <tr><td rowspan="2">Essentiel</td><td>Lite</td><td>200 000</td><td>200 000</td><td>200 000</td><td>200 000</td></tr>
              <tr><td>Full</td><td>2 000 000</td><td>7 500 000</td><td>10 000 000</td><td>10 000 000</td></tr>
              <tr><td>Classique</td><td>—</td><td>15 000 000</td><td>15 000 000</td><td>N/A</td><td>30 000 000</td></tr>
              <tr><td>Premium</td><td>—</td><td colspan="4" style="text-align:center">9 999 999 999 (illimité)</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Parcours avec captures -->
    <div class="card">
      <div class="card-title">🗺️ Parcours — Création de compte</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">

        <div>
          <div style="font-size:13px;font-weight:700;color:#FF6600;margin-bottom:12px">👤 Client OM (déjà Orange Money)</div>
          <div style="display:flex;gap:12px;align-items:flex-start">
            <div style="flex:1">
              <ol style="padding-left:16px;font-size:13px;color:#2d3748;line-height:2">
                <li>Saisie du numéro</li>
                <li>Catégorisation du commerce</li>
                <li>Accès à la localisation</li>
                <li>Validation des CGU</li>
                <li>Génération du QR code marchand</li>
                <li>Activation notifications</li>
                <li>Accès à l'interface</li>
              </ol>
              <div style="background:#FFF0E6;border-radius:8px;padding:8px 12px;margin-top:8px;font-size:11px;color:#584B26;line-height:1.7">
                Migration O'calm → Essentiel Full<br>
                Migration SMB → Classique<br>
                Migration Classique → Premium
              </div>
            </div>
            <div style="display:flex;flex-direction:column;gap:8px;flex-shrink:0">
              <div class="phone-frame"><img src="{IMG}/creation_om_etape1.jpg" alt="Étape 1" style="width:100%;display:block"></div>
              <div class="phone-frame"><img src="{IMG}/creation_om_etape2.jpg" alt="Étape 2" style="width:100%;display:block"></div>
            </div>
          </div>
        </div>

        <div>
          <div style="font-size:13px;font-weight:700;color:#8D0C23;margin-bottom:12px">🆕 Client Non-OM</div>
          <div style="display:flex;gap:12px;align-items:flex-start">
            <div style="flex:1">
              <ol style="padding-left:16px;font-size:13px;color:#2d3748;line-height:2">
                <li>Saisie du numéro</li>
                <li>Demande de création de compte</li>
                <li>KYC : nom, prénom, date naissance, n° pièce, photo</li>
                <li>Validation Back-Office</li>
                <li>Notification : compte activé ✅</li>
              </ol>
              <div style="background:#FFF0E6;border-radius:8px;padding:8px 12px;margin-top:8px;font-size:11px;color:#584B26">
                Valable aussi pour les clients non-Orange telco (sans SIM / OTT)
              </div>
            </div>
            <div style="display:flex;flex-direction:column;gap:8px;flex-shrink:0">
              <div class="phone-frame"><img src="{IMG}/creation_nonom_etape1.jpg" alt="Non-OM étape 1" style="width:100%;display:block"></div>
              <div class="phone-frame"><img src="{IMG}/creation_nonom_etape2.jpg" alt="Non-OM étape 2" style="width:100%;display:block"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📲 Parcours — Encaissement par QR Code</div>
      <div style="display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap">
        <div style="flex:1;min-width:200px">
          <div style="display:flex;flex-direction:column;gap:12px">
            <div style="display:flex;gap:12px;align-items:center;background:#FFF0E6;border-radius:10px;padding:12px 16px">
              <span style="background:#FF6600;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">1</span>
              <p style="font-size:13px;color:#2d3748">Exposer son QR Code au client</p>
            </div>
            <div style="display:flex;gap:12px;align-items:center;background:#FFF0E6;border-radius:10px;padding:12px 16px">
              <span style="background:#FF6600;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">2</span>
              <p style="font-size:13px;color:#2d3748">Le client scanne le QR Code, saisit le montant et confirme son paiement</p>
            </div>
            <div style="display:flex;gap:12px;align-items:center;background:#F9E8EC;border-radius:10px;padding:12px 16px">
              <span style="background:#8D0C23;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">3</span>
              <p style="font-size:13px;color:#2d3748">Réception de la confirmation de paiement ✅</p>
            </div>
          </div>
        </div>
        <div style="display:flex;gap:8px;flex-shrink:0">
          <div class="phone-frame"><img src="{IMG}/encaissement_qr1.jpg" alt="QR étape 1" style="width:100%;display:block"></div>
          <div class="phone-frame"><img src="{IMG}/encaissement_qr2.jpg" alt="QR étape 2" style="width:100%;display:block"></div>
          <div class="phone-frame"><img src="{IMG}/encaissement_qr3.jpg" alt="QR étape 3" style="width:100%;display:block"></div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🔗 Parcours — Envoi de lien de paiement à distance</div>
      <div style="display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap">
        <div style="flex:1;min-width:200px">
          <div style="display:flex;flex-direction:column;gap:12px">
            <div style="display:flex;gap:12px;align-items:center;background:#FFF0E6;border-radius:10px;padding:12px 16px">
              <span style="background:#FF6600;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">1</span>
              <p style="font-size:13px;color:#2d3748">Cliquer sur le bouton « Envoi de lien »</p>
            </div>
            <div style="display:flex;gap:12px;align-items:center;background:#FFF0E6;border-radius:10px;padding:12px 16px">
              <span style="background:#FF6600;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">2</span>
              <p style="font-size:13px;color:#2d3748">Saisir le montant à encaisser (optionnel)</p>
            </div>
            <div style="display:flex;gap:12px;align-items:center;background:#FFF0E6;border-radius:10px;padding:12px 16px">
              <span style="background:#FF6600;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">3</span>
              <p style="font-size:13px;color:#2d3748">Choisir le canal de communication (SMS, WhatsApp...)</p>
            </div>
            <div style="display:flex;gap:12px;align-items:center;background:#F9E8EC;border-radius:10px;padding:12px 16px">
              <span style="background:#8D0C23;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">4</span>
              <p style="font-size:13px;color:#2d3748">Valider le partage du lien ✅</p>
            </div>
          </div>
        </div>
        <div style="display:flex;gap:8px;flex-shrink:0">
          <div class="phone-frame"><img src="{IMG}/lien_etape1.jpg" alt="Lien étape 1" style="width:100%;display:block"></div>
          <div class="phone-frame"><img src="{IMG}/lien_etape2.jpg" alt="Lien étape 2" style="width:100%;display:block"></div>
          <div class="phone-frame"><img src="{IMG}/lien_etape3.jpg" alt="Lien étape 3" style="width:100%;display:block"></div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">💸 Parcours — Transfert (Gratuit)</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
        <div>
          <div style="font-size:13px;font-weight:700;color:#584B26;margin-bottom:12px">Transfert à soi-même</div>
          <div style="display:flex;gap:12px;align-items:flex-start">
            <ol style="padding-left:16px;font-size:13px;color:#2d3748;line-height:2.1;flex:1">
              <li>Cliquer « Transfert »</li>
              <li>Choisir « à moi-même »</li>
              <li>Saisir le montant</li>
              <li>Confirmer avec son code secret</li>
            </ol>
            <div class="phone-frame"><img src="{IMG}/transfert_soi1.jpg" alt="Transfert soi" style="width:100%;display:block"></div>
          </div>
        </div>
        <div>
          <div style="font-size:13px;font-weight:700;color:#584B26;margin-bottom:12px">Transfert à un tiers</div>
          <div style="display:flex;gap:12px;align-items:flex-start">
            <ol style="padding-left:16px;font-size:13px;color:#2d3748;line-height:2.1;flex:1">
              <li>Cliquer « Transfert »</li>
              <li>Choisir « Autre transfert »</li>
              <li>Sélectionner le contact + montant</li>
              <li>Confirmer avec son code secret</li>
            </ol>
            <div class="phone-frame"><img src="{IMG}/transfert_tiers1.jpg" alt="Transfert tiers" style="width:100%;display:block"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🏧 Parcours — Retrait en PDV (Gratuit)</div>
      <div style="display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap">
        <div style="flex:1;min-width:200px">
          <div style="display:flex;flex-direction:column;gap:12px">
            <div style="display:flex;gap:12px;align-items:center;background:#F3EDD8;border-radius:10px;padding:12px 16px">
              <span style="background:#584B26;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">1</span>
              <p style="font-size:13px;color:#2d3748">Cliquer sur le bouton « Retrait »</p>
            </div>
            <div style="display:flex;gap:12px;align-items:center;background:#F3EDD8;border-radius:10px;padding:12px 16px">
              <span style="background:#584B26;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">2</span>
              <p style="font-size:13px;color:#2d3748">Exposer son QR code au PDV et dire oralement le montant</p>
            </div>
            <div style="display:flex;gap:12px;align-items:center;background:#F3EDD8;border-radius:10px;padding:12px 16px">
              <span style="background:#584B26;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">3</span>
              <p style="font-size:13px;color:#2d3748">Confirmer le retrait sur la liste d'attente dans le menu « Retrait »</p>
            </div>
            <div style="display:flex;gap:12px;align-items:center;background:#F9E8EC;border-radius:10px;padding:12px 16px">
              <span style="background:#8D0C23;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;flex-shrink:0">4</span>
              <p style="font-size:13px;color:#2d3748">Vérifier la transaction dans l'historique ✅</p>
            </div>
          </div>
          <div style="background:#f8fafc;border-radius:8px;padding:8px 12px;margin-top:10px;font-size:12px;color:#455A64">
            Alternative USSD : <strong>#145*2#</strong>
          </div>
        </div>
        <div style="display:flex;gap:8px;flex-shrink:0">
          <div class="phone-frame"><img src="{IMG}/retrait_etape1.jpg" alt="Retrait 1" style="width:100%;display:block"></div>
          <div class="phone-frame"><img src="{IMG}/retrait_etape2.jpg" alt="Retrait 2" style="width:100%;display:block"></div>
          <div class="phone-frame"><img src="{IMG}/retrait_etape3.jpg" alt="Retrait 3" style="width:100%;display:block"></div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📋 Historique &amp; Remboursement</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
        <div>
          <div style="font-size:13px;font-weight:700;color:#1565C0;margin-bottom:12px">Historique des transactions</div>
          <p style="font-size:13px;color:#455A64;line-height:1.7;margin-bottom:12px">Accès en temps réel à toutes les transactions. Vue miniature dans la liste + vue détaillée au clic.</p>
          <div style="display:flex;gap:8px">
            <div class="phone-frame"><img src="{IMG}/historique_liste.jpg" alt="Historique liste" style="width:100%;display:block"></div>
            <div class="phone-frame"><img src="{IMG}/historique_detail.jpg" alt="Historique détail" style="width:100%;display:block"></div>
          </div>
        </div>
        <div>
          <div style="font-size:13px;font-weight:700;color:#1565C0;margin-bottom:12px">Remboursement</div>
          <p style="font-size:13px;color:#455A64;line-height:1.7;margin-bottom:12px">Remboursement d'une transaction directement depuis l'historique sans quitter l'application.</p>
          <div style="display:flex;gap:8px">
            <div class="phone-frame"><img src="{IMG}/remboursement1.jpg" alt="Remboursement 1" style="width:100%;display:block"></div>
            <div class="phone-frame"><img src="{IMG}/remboursement2.jpg" alt="Remboursement 2" style="width:100%;display:block"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📈 Déplafonnement</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
        <div style="background:#E3F2FD;border-radius:10px;padding:16px">
          <div style="font-size:13px;font-weight:700;color:#1565C0;margin-bottom:10px">Vers Profil Classique</div>
          <ol style="padding-left:16px;font-size:13px;color:#2d3748;line-height:1.9">
            <li>Menu options → « Demander déplafonnement »</li>
            <li>Sélectionner « Profil Classique »</li>
            <li>Fournir les pièces (annexe 1)</li>
            <li>Retour client sous 24H</li>
          </ol>
        </div>
        <div style="background:#E3F2FD;border-radius:10px;padding:16px">
          <div style="font-size:13px;font-weight:700;color:#1565C0;margin-bottom:10px">Vers Profil Premium</div>
          <ol style="padding-left:16px;font-size:13px;color:#2d3748;line-height:1.9">
            <li>Menu options → « Demander déplafonnement »</li>
            <li>Sélectionner « Profil Premium »</li>
            <li>Sélectionner la forme juridique</li>
            <li>Fournir la documentation (annexe 2)</li>
            <li>Retour client sous 24H</li>
          </ol>
        </div>
      </div>
      <div class="tbl-wrap" style="margin-top:16px">
        <table class="tbl-orange">
          <thead><tr><th>Profil</th><th>Variante</th><th>Solde</th><th>Trx/Jour</th><th>Trx/Mois</th></tr></thead>
          <tbody>
            <tr><td rowspan="2">Essentiel</td><td>Lite</td><td>200 000</td><td>200 000</td><td>200 000</td></tr>
            <tr><td>Full</td><td>2 000 000</td><td>7 500 000</td><td>10 000 000</td></tr>
            <tr><td>Classique</td><td>—</td><td>15 000 000</td><td>15 000 000</td><td>30 000 000</td></tr>
            <tr><td>Premium</td><td>—</td><td colspan="3" style="text-align:center">Illimité</td></tr>
          </tbody>
        </table>
      </div>
    </div>

  </div><!-- fin tab-m4-cours -->

  <!-- ══ EXERCICES ══ -->
  <div class="tab-section" id="tab-m4-exo" style="display:none">
    <div class="card">
      <div class="card-title">✏️ Exercice 1 — Qualifier le bon profil marchand</div>
      <div class="exercise-box">
        <div class="exercise-title">📋 Mise en situation</div>
        <p>Pour chacun des commerçants ci-dessous, identifiez le profil OM Business approprié et justifiez votre choix.</p>
      </div>
      <div style="display:flex;flex-direction:column;gap:14px;margin-top:16px">
        <div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px">
          <div style="font-size:12px;font-weight:700;color:#455A64;margin-bottom:8px">CAS A — Mireille, vendeuse ambulante</div>
          <p style="font-size:13px;color:#2d3748">Vend des fruits au marché. Travaille seule. Recettes mensuelles &lt; 80 000 FCFA. Veut encaisser avec un QR code mobile.</p>
          <div style="margin-top:10px;background:#f8fafc;border-radius:8px;padding:10px;font-size:12px;color:#455A64">
            ✅ <strong>Essentiel Lite</strong> — CA &lt; 150K/an, besoin simple d'encaissement mobile, plafond 200K FCFA/j suffisant.
          </div>
        </div>
        <div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px">
          <div style="font-size:12px;font-weight:700;color:#455A64;margin-bottom:8px">CAS B — M. Kouamé, propriétaire d'une supérette</div>
          <p style="font-size:13px;color:#2d3748">5 employés. CA mensuel ~8M FCFA. Veut tracer toutes ses transactions, imprimer plusieurs QR codes, retirer sans frais.</p>
          <div style="margin-top:10px;background:#f8fafc;border-radius:8px;padding:10px;font-size:12px;color:#455A64">
            ✅ <strong>Classique</strong> — Besoin de traçabilité et multi-QR codes. CA entre 150K et 400M FCFA/an.
          </div>
        </div>
        <div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px">
          <div style="font-size:12px;font-weight:700;color:#455A64;margin-bottom:8px">CAS C — Hôtel Ôasis, 30 employés</div>
          <p style="font-size:13px;color:#2d3748">CA annuel 2 milliards FCFA. Besoin de gestion des rôles du personnel, d'analyse des performances et de reversements.</p>
          <div style="margin-top:10px;background:#f8fafc;border-radius:8px;padding:10px;font-size:12px;color:#455A64">
            ✅ <strong>Premium</strong> — CA &gt; 400M/an, gestion multi-utilisateurs et plafonds illimités nécessaires.
          </div>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-title">✏️ Exercice 2 — Parcours création de compte Non-OM</div>
      <div class="exercise-box">
        <div class="exercise-title">📋 Mise en situation</div>
        <p>Un commerçant sans compte Orange Money veut ouvrir un compte OM Business Essentiel. Reconstituez le parcours étape par étape en vous aidant des captures ci-dessous.</p>
      </div>
      <div style="display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap;margin-top:16px">
        <div style="flex:1;min-width:200px">
          <div style="display:flex;flex-direction:column;gap:8px">
            <div style="display:flex;gap:12px;align-items:flex-start;background:#f8fafc;border-radius:8px;padding:10px 14px">
              <span style="background:#8D0C23;color:white;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0">1</span>
              <p style="font-size:13px;color:#2d3748">Saisir le numéro du commerçant</p>
            </div>
            <div style="display:flex;gap:12px;align-items:flex-start;background:#f8fafc;border-radius:8px;padding:10px 14px">
              <span style="background:#8D0C23;color:white;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0">2</span>
              <p style="font-size:13px;color:#2d3748">Lancer la demande de création de compte marchand</p>
            </div>
            <div style="display:flex;gap:12px;align-items:flex-start;background:#f8fafc;border-radius:8px;padding:10px 14px">
              <span style="background:#8D0C23;color:white;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0">3</span>
              <p style="font-size:13px;color:#2d3748">Renseigner : Nom, Prénom, Date naissance, N° pièce, Photo recto/verso</p>
            </div>
            <div style="display:flex;gap:12px;align-items:flex-start;background:#f8fafc;border-radius:8px;padding:10px 14px">
              <span style="background:#8D0C23;color:white;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0">4</span>
              <p style="font-size:13px;color:#2d3748">Le dossier passe en corbeille de validation Back-Office</p>
            </div>
            <div style="display:flex;gap:12px;align-items:flex-start;background:#F9E8EC;border-radius:8px;padding:10px 14px">
              <span style="background:#8D0C23;color:white;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0">5</span>
              <p style="font-size:13px;color:#2d3748">Notification : compte activé ✅</p>
            </div>
          </div>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;align-items:center;flex-shrink:0">
          <div class="phone-frame"><img src="{IMG}/creation_nonom_etape1.jpg" alt="Non-OM 1" style="width:100%;display:block"></div>
          <div class="phone-frame"><img src="{IMG}/creation_nonom_etape2.jpg" alt="Non-OM 2" style="width:100%;display:block"></div>
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
            <div class="quiz-option" onclick="answerM4(this,'m4-q1',false,'Le profil Classique cible les petits commerces formels avec CA entre 150K et 400M FCFA/an.')"><span class="option-letter">A</span> OM Business Classique</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q1',true,'Correct ! L\'Essentiel cible les commerces informels / micro-entreprises avec CA &lt; 150K FCFA/an.')"><span class="option-letter">B</span> OM Business Essentiel</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q1',false,'Le Premium est réservé aux grandes entreprises avec CA &gt; 400M FCFA/an et plus de 10 employés.')"><span class="option-letter">C</span> OM Business Premium</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q1',false,'Ce profil n\'existe pas dans la gamme OM Business.')"><span class="option-letter">D</span> OM Business Pro</div>
          </div>
          <div class="quiz-feedback" id="fb-m4-q1"></div>
        </div>
        <div class="quiz-question-block" id="m4-q2">
          <div class="quiz-q-num">Question 02 / 05</div>
          <div class="quiz-q-text">Quel est le tarif d'encaissement QR Code pour un marchand Essentiel jusqu'à 50 000 FCFA/jour ?</div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="answerM4(this,'m4-q2',false,'1% s\'applique au-delà de 50 000 FCFA/jour ou pour le profil Premium.')"><span class="option-letter">A</span> 1% de la transaction</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q2',false,'500 FCFA n\'est pas un tarif OM Business.')"><span class="option-letter">B</span> 500 FCFA forfait</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q2',true,'Correct ! 0% jusqu\'à 50 000 FCFA/jour, plafonné à 500 000 FCFA/mois cumulés pour le profil Essentiel.')"><span class="option-letter">C</span> 0% jusqu'à 50 000 FCFA/jour</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q2',false,'0,5% n\'est pas le tarif appliqué.')"><span class="option-letter">D</span> 0,5%</div>
          </div>
          <div class="quiz-feedback" id="fb-m4-q2"></div>
        </div>
        <div class="quiz-question-block" id="m4-q3">
          <div class="quiz-q-num">Question 03 / 05</div>
          <div class="quiz-q-text">Après le parcours KYC d'un client Non-OM, quelle est l'étape suivante ?</div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="answerM4(this,'m4-q3',false,'Le QR code n\'est généré qu\'après validation du compte.')"><span class="option-letter">A</span> Génération immédiate du QR code marchand</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q3',true,'Correct ! Après le parcours KYC, le dossier passe en corbeille de validation Back-Office avant l\'activation.')"><span class="option-letter">B</span> Validation en corbeille Back-Office</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q3',false,'L\'accès à l\'interface n\'est accordé qu\'après la validation du compte.')"><span class="option-letter">C</span> Accès immédiat à l'interface OM Business</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q3',false,'Aucun frais d\'inscription n\'est requis.')"><span class="option-letter">D</span> Paiement de frais d'inscription</div>
          </div>
          <div class="quiz-feedback" id="fb-m4-q3"></div>
        </div>
        <div class="quiz-question-block" id="m4-q4">
          <div class="quiz-q-num">Question 04 / 05</div>
          <div class="quiz-q-text">Comment un marchand Essentiel Full peut-il augmenter ses plafonds vers le profil Classique ?</div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="answerM4(this,'m4-q4',false,'Appeler le 0808 n\'est pas la procédure de déplafonnement.')"><span class="option-letter">A</span> Appeler le service client 0808</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q4',false,'Créer un nouveau compte n\'est pas la procédure requise.')"><span class="option-letter">B</span> Créer un nouveau compte OM Business</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q4',true,'Correct ! Menu options → Demander déplafonnement → Profil Classique → fournir les pièces. Retour sous 24H.')"><span class="option-letter">C</span> Menu options → "Demander déplafonnement" → fournir les pièces requises</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q4',false,'Le déplafonnement se fait entièrement depuis l\'application.')"><span class="option-letter">D</span> Se rendre en agence Orange avec un dossier physique</div>
          </div>
          <div class="quiz-feedback" id="fb-m4-q4"></div>
        </div>
        <div class="quiz-question-block" id="m4-q5">
          <div class="quiz-q-num">Question 05 / 05</div>
          <div class="quiz-q-text">Quel est le coût d'un retrait en PDV pour un marchand Essentiel ou Classique ?</div>
          <div class="quiz-options">
            <div class="quiz-option" onclick="answerM4(this,'m4-q5',false,'1% n\'est pas le tarif pour les profils Essentiel et Classique.')"><span class="option-letter">A</span> 1% du montant</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q5',false,'500 FCFA n\'est pas le tarif de retrait.')"><span class="option-letter">B</span> 500 FCFA forfait</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q5',true,'Correct ! Le retrait en PDV est gratuit (0 FCFA) pour les profils Essentiel et Classique.')"><span class="option-letter">C</span> 0 FCFA — Gratuit</div>
            <div class="quiz-option" onclick="answerM4(this,'m4-q5',false,'Le retrait en PDV est disponible et gratuit pour ces profils.')"><span class="option-letter">D</span> Non disponible pour ces profils</div>
          </div>
          <div class="quiz-feedback" id="fb-m4-q5"></div>
        </div>
        <div style="margin-top:24px;padding-top:20px;border-top:1px solid #e2e8f0;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-size:24px;font-weight:800;color:#FF6600" id="m4-score-display">0 <span style="font-size:16px;color:#888">/ 5</span></div>
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
      <h3 style="margin-bottom:8px;color:#FF6600">Résultats du quiz — OM Business</h3>
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

# CSS pour les phone frames
PHONE_CSS = """
/* ── PHONE FRAMES ── */
.phone-frame {
  width: 120px;
  border-radius: 20px;
  border: 3px solid #222;
  overflow: hidden;
  box-shadow: 0 6px 20px rgba(0,0,0,0.25);
  flex-shrink: 0;
  background: #000;
}
.phone-frame img {
  width: 100%;
  display: block;
  border-radius: 17px;
}
"""

with open(IDX, "r", encoding="utf-8") as f:
    txt = f.read()

# Injecter CSS phone-frame
txt = txt.replace('/* ── OVERLAY PLEIN ÉCRAN ── */', PHONE_CSS + '\n/* ── OVERLAY PLEIN ÉCRAN ── */')

# Remplacer overlay-m4
start = txt.find('<div class="module-overlay" id="overlay-m4">')
end   = txt.find('<div class="module-overlay" id="overlay-m5">')
if start == -1 or end == -1:
    print("ERREUR: marqueurs non trouvés!")
    exit(1)

txt = txt[:start] + NEW_M4 + '\n\n' + txt[end:]

# Mettre à jour answerM4 pour les deux affichages score
old_score = 'document.getElementById(\'m4-score-display\').innerHTML = total + \' <span>/ 5</span>\';'
new_score = '''const scoreHtml4 = total + ' <span style="font-size:16px;color:#888">/ 5</span>';
  if (document.getElementById('m4-score-display')) document.getElementById('m4-score-display').innerHTML = scoreHtml4;
  if (document.getElementById('m4-score-display-r')) document.getElementById('m4-score-display-r').innerHTML = scoreHtml4;'''
txt = txt.replace(old_score, new_score)

old_label = "document.getElementById('m4-prog-label').textContent = answered + ' / 5';"
new_label = """if (document.getElementById('m4-prog-label')) document.getElementById('m4-prog-label').textContent = answered + ' / 5';
  if (document.getElementById('m4-prog-label-r')) document.getElementById('m4-prog-label-r').textContent = answered + ' / 5';
  if (document.getElementById('m4-prog-fill')) document.getElementById('m4-prog-fill').style.width = (answered / 5 * 100) + '%';"""
old_fill = "document.getElementById('m4-prog-fill').style.width = (answered / 5 * 100) + '%';"
txt = txt.replace(old_fill, '')  # remove old fill line first
txt = txt.replace(old_label, new_label)

with open(IDX, "w", encoding="utf-8") as f:
    f.write(txt)

print(f"index.html: {len(txt)//1024} KB")
print("M4 avec images: OK!")
