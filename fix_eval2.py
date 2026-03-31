# -*- coding: utf-8 -*-
"""
fix_eval2.py — Applique toutes les corrections au fichier evaluation.html
"""

import sys

IN  = r"C:\Users\MAFA HOLDING\CREATIONS FOF\Formation\evaluation.html"
OUT = IN  # on écrit dans le même fichier

# ── Lire le fichier ──────────────────────────────────────────────────────────
with open(IN, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"[OK] Fichier lu : {len(content)} caractères")

# ============================================================
# CORRECTION — QUESTIONS_BY_POSTE (bloc complet)
# ============================================================

DELIM_START = 'const QUESTIONS_BY_POSTE = {'
DELIM_END   = '}; // fin QUESTIONS_BY_POSTE'

idx_start = content.find(DELIM_START)
idx_end   = content.find(DELIM_END)

assert idx_start != -1, "ERREUR: délimiteur START introuvable"
assert idx_end   != -1, "ERREUR: délimiteur END introuvable"
assert idx_end > idx_start, "ERREUR: ordre des délimiteurs incorrect"

print(f"[OK] QUESTIONS_BY_POSTE trouve : chars {idx_start} -> {idx_end + len(DELIM_END)}")

NEW_QUESTIONS_BLOCK = r"""const QUESTIONS_BY_POSTE = {
'call-center': [
  { type:'qcm', text:"Un agent Call Center ouvre un dossier dans Connectel. L'entrepreneur répond mais dit ne pas être disponible cette semaine. Quelle est la procédure correcte ?", options:["Classer le dossier comme 'Refus ferme'","Planifier un rappel dans 7 jours et noter la disponibilité","Proposer immédiatement 3 créneaux alternatifs et noter le plus proche","Transmettre au superviseur pour décision"], correct:2, points:1 },
  { type:'qcm', text:"Connectel affiche pour un dossier le statut 'Doublon détecté'. Que fait l'agent ?", options:["Supprimer le dossier le plus ancien","Valider les deux et laisser le Back Office décider","Ne traiter qu'un seul des deux dossiers et signaler l'autre au superviseur","Ignorer et continuer le traitement normalement"], correct:2, points:1 },
  { type:'qcm', text:"L'entrepreneur dit avoir reçu sa Carte Entreprenant il y a 6 mois mais n'a jamais eu de rendez-vous de mise à jour. Comment l'agent traite-t-il ce cas ?", options:["Clôturer le dossier comme 'Déjà traité'","Vérifier dans Connectel si la mise à jour est bien enregistrée, sinon planifier un nouveau RDV","Ignorer car la carte a déjà été émise","Transférer au Back Office sans note"], correct:1, points:1 },
  { type:'qcm', text:"Lors d'un appel, l'entrepreneur fournit une adresse différente de celle enregistrée dans Connectel. Quelle action s'impose ?", options:["Mettre à jour l'adresse directement dans Connectel","Ignorer car l'adresse est secondaire","Noter la nouvelle adresse dans le commentaire du dossier et signaler pour mise à jour Back Office","Annuler le RDV et clôturer le dossier"], correct:2, points:1 },
  { type:'qcm', text:"Après 3 tentatives infructueuses sur un dossier (numéro valide mais pas de réponse), quel statut l'agent doit-il appliquer dans Connectel ?", options:["Refus ferme","Injoignable — à relancer selon planning","Dossier clôturé définitivement","Numéro invalide"], correct:1, points:1 },
  { type:'qcm', text:"Un entrepreneur accepte un RDV mais précise qu'il ne sera disponible que le dimanche. L'équipe terrain ne travaille pas le dimanche. Que fait l'agent ?", options:["Confirmer le RDV au dimanche quand même","Proposer le lundi matin comme alternative la plus proche et noter la contrainte","Classer comme 'Refus ferme' car dimanche impossible","Transférer au superviseur sans proposer d'alternative"], correct:1, points:1 },
  { type:'qcm', text:"L'agent Call Center constate dans Connectel qu'un dossier a été marqué 'Validé' par le Back Office mais que l'entrepreneur appelle pour signaler qu'il n'a jamais reçu sa carte. Que fait l'agent ?", options:["Dire à l'entrepreneur qu'il a tort et clôturer l'appel","Ouvrir un ticket d'anomalie et escalader au superviseur","Renvoyer l'entrepreneur directement au Back Office","Créer un nouveau dossier de zéro"], correct:1, points:1 },
  { type:'qcm', text:"Pendant un appel, l'entrepreneur demande à l'agent de lui préciser le contenu exact de sa Carte Entreprenant (données imprimées). Quelle réponse est correcte ?", options:["L'agent lit toutes les données personnelles du dossier","L'agent explique les informations générales imprimées sur la carte sans lire les données sensibles","L'agent refuse toute information et raccroche","L'agent donne uniquement le numéro de dossier"], correct:1, points:1 },
  { type:'qcm', text:"Quel est l'impact d'un taux d'appels 'Refus ferme' élevé dans une équipe Call Center ?", options:["Aucun impact, c'est inévitable","Signal d'alerte sur la qualité du discours ou le ciblage des dossiers","Cela améliore la productivité car les dossiers sont clôturés plus vite","Preuve que le projet ID30 n'intéresse pas les entrepreneurs"], correct:1, points:1 },
  { type:'qcm', text:"Lors d'un appel, le correspondant qui répond n'est pas l'entrepreneur inscrit mais son épouse. L'épouse accepte le RDV. L'agent doit :", options:["Confirmer le RDV avec l'épouse et noter que le RDV doit être confirmé avec l'entrepreneur directement","Refuser et raccrocher car l'entrepreneur n'est pas disponible","Valider le RDV sans mention particulière","Classer comme 'Refus ferme' car l'entrepreneur n'a pas répondu"], correct:0, points:1 },
  { type:'qcm', text:"La DMT (Durée Moyenne de Traitement) d'un agent est de 18 minutes par appel, alors que la norme est 10 minutes. Quelle est la cause la plus probable ?", options:["L'agent travaille trop lentement, il faut le sanctionner","L'agent ne maîtrise pas les raccourcis Connectel ou le script d'appel","Les entrepreneurs du secteur sont naturellement plus bavards","Le réseau téléphonique est mauvais dans la zone"], correct:1, points:1 },
  { type:'qcm', text:"Un entrepreneur en état d'énervement accuse MAFA Holding d'être une arnaque. Comment l'agent réagit-il ?", options:["Raccrocher poliment pour éviter l'escalade","Rester calme, présenter les références officielles (Ministère du Commerce), proposer un rappel ultérieur","Mettre l'entrepreneur en attente indéfiniment","Contester les accusations et défendre MAFA Holding fermement"], correct:1, points:1 },
  { type:'qcm', text:"Quel est le KPI principal utilisé pour évaluer la performance individuelle d'un agent Call Center ID30 ?", options:["Le nombre total d'appels passés","Le nombre de fiches validées par jour (cible : 15 minimum)","Le temps moyen passé en pause","Le nombre d'entrepreneurs ayant raccroché"], correct:1, points:1 },
  { type:'qcm', text:"L'agent remarque que 5 dossiers consécutifs dans sa file ont le même numéro de téléphone. Que doit-il faire ?", options:["Appeler le numéro 5 fois","Appeler une seule fois, noter l'anomalie et la signaler au superviseur","Supprimer les 4 doublons","Valider les 5 dossiers avec le même RDV"], correct:1, points:1 },
  { type:'qcm', text:"Dans le protocole Call Center ID30, que se passe-t-il après la confirmation d'un RDV par l'entrepreneur ?", options:["L'agent clôture immédiatement le dossier","L'agent envoie les informations au Back Office pour préparation de l'équipe terrain","L'agent attend que le terrain valide avant toute action","L'agent rappelle le lendemain pour reconfirmer"], correct:1, points:1 },
  { type:'vf', text:"Un agent Call Center peut modifier directement le numéro de téléphone d'un entrepreneur dans Connectel sans validation Back Office.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Si l'entrepreneur n'a pas répondu après 3 tentatives réparties sur 3 jours différents, le dossier peut être classé 'Injoignable définitif'.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'vf', text:"Le Call Center peut confirmer un RDV terrain même si l'équipe terrain n'a pas encore confirmé la disponibilité de l'agent pour ce créneau.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Un agent Call Center qui dépasse systématiquement 15 fiches par jour peut réduire la qualité de sa vérification des informations.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'qcm', text:"Lors d'un appel de relance, l'entrepreneur dit : 'J'ai déjà un RDV prévu pour dans 3 jours'. Comment l'agent vérifie-t-il cette information ?", options:["Il croit l'entrepreneur sur parole","Il vérifie dans Connectel si un RDV est bien enregistré avec cette date","Il annule l'ancien RDV et en crée un nouveau","Il transfère au superviseur"], correct:1, points:1 },
  { type:'qcm', text:"Un agent Call Center reçoit un message de son superviseur lui demandant de valider 30 fiches ce jour au lieu de 15 pour rattraper un retard. Que doit faire l'agent ?", options:["Accepter et valider 30 fiches sans se soucier de la qualité","Accepter mais maintenir le protocole qualité, quitte à ne pas atteindre 30","Refuser catégoriquement de travailler plus","Valider des dossiers sans appeler pour gagner du temps"], correct:1, points:1 },
  { type:'qcm', text:"Quelle information l'agent doit-il impérativement noter dans Connectel à la fin de chaque appel, qu'il soit fructueux ou non ?", options:["Uniquement si l'appel a abouti à un RDV","Le résumé de l'appel, le statut appliqué et l'heure du prochain contact","Le nom de l'opérateur téléphonique de l'entrepreneur","La météo du jour pour contexte"], correct:1, points:1 },
  { type:'qcm', text:"L'entrepreneur accepte le RDV mais demande que l'agent terrain arrive avant 7h du matin. L'heure standard de démarrage terrain est 8h. Que fait l'agent ?", options:["Confirmer le RDV à 7h pour satisfaire l'entrepreneur","Expliquer les horaires standards et proposer le créneau le plus tôt possible (8h-9h)","Classer comme refus car horaire impossible","Ignorer la demande et confirmer à l'heure standard sans le mentionner"], correct:1, points:1 },
  { type:'qcm', text:"Pourquoi est-il interdit à un agent Call Center de promettre des avantages financiers à l'entrepreneur pour accepter le RDV ?", options:["Car cela crée de fausses attentes et nuit à la crédibilité du projet ID30","Car l'agent n'a pas de budget pour cela","Car les avantages sont réservés aux superviseurs","Ce n'est pas interdit, c'est une technique de persuasion valable"], correct:0, points:1 },
  { type:'qcm', text:"Un entrepreneur enregistré à Abidjan Cocody appelle pour signaler qu'il a déménagé à Bouaké. Quelle est la procédure correcte ?", options:["Mettre à jour l'adresse dans Connectel et transférer le dossier à l'équipe Bouaké","Clôturer le dossier car hors zone","Ignorer le déménagement et maintenir le RDV à Abidjan","Créer un nouveau dossier à Bouaké en gardant l'ancien ouvert"], correct:0, points:1 },
  { type:'qcm', text:"Combien de jours maximum une fiche peut-elle rester au statut 'En attente de reconfirmation' avant d'être relancée ?", options:["1 jour","3 jours","7 jours","14 jours"], correct:1, points:1 },
  { type:'qcm', text:"L'agent constate que son taux de conversion RDV est de 30% alors que la moyenne équipe est 65%. Quelle est la première action à mener ?", options:["Accuser la qualité des dossiers fournis","Analyser les enregistrements d'appels avec le superviseur pour identifier les points d'amélioration","Augmenter la vitesse des appels","Passer à un autre projet"], correct:1, points:1 },
  { type:'vf', text:"Un agent Call Center peut décider seul de clôturer définitivement un dossier sans validation de son superviseur.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Le script d'appel est un guide — l'agent peut l'adapter selon le profil de l'entrepreneur, tout en respectant les informations obligatoires.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'open', text:"Un entrepreneur accepte le RDV mais après la conversation, vous réalisez que l'adresse qu'il a donnée est différente de celle dans Connectel, et le numéro alternatif qu'il a mentionné n'est pas enregistré. Décrivez précisément toutes les actions que vous effectuez dans Connectel et vis-à-vis de votre superviseur.", options:[], correct:0, points:3 }
],

'back-office': [
  { type:'qcm', text:"Le Back Office reçoit un dossier où le score Proof of Life est de 63 et les photos sont nettes. La CNI est valide. Quelle décision est correcte ?", options:["Rejeter car le score recommandé est 70","Valider car le score dépasse le minimum de 60 et les autres éléments sont conformes","Mettre en attente en demandant une nouvelle capture biométrique","Transférer au superviseur pour décision"], correct:1, points:1 },
  { type:'qcm', text:"Un dossier présente une CNI avec une date d'expiration dépassée de 2 mois mais le préfet de l'époque a signé une attestation de renouvellement. Le Back Office doit :", options:["Valider avec l'attestation comme pièce complémentaire","Rejeter car la CNI est expirée","Valider sans condition car l'attestation suffit","Ignorer l'expiration si la photo correspond"], correct:0, points:1 },
  { type:'qcm', text:"Le Back Office constate que les coordonnées GPS d'un dossier pointent vers la mer (erreur évidente). Quelle est la bonne procédure ?", options:["Corriger manuellement les coordonnées en estimant l'emplacement probable","Valider en notant l'erreur GPS dans les commentaires","Rejeter le dossier — retour terrain obligatoire pour recapturer le GPS","Supprimer les coordonnées et valider sans GPS"], correct:2, points:1 },
  { type:'qcm', text:"Deux photos de portrait d'un même dossier montrent deux personnes différentes. Le Back Office doit :", options:["Conserver la meilleure photo et valider","Contacter le Call Center pour clarification","Rejeter immédiatement — incohérence d'identité grave nécessitant une nouvelle visite","Demander à l'agent terrain de choisir laquelle est correcte"], correct:2, points:1 },
  { type:'qcm', text:"Le Back Office reçoit 40 dossiers le lundi matin. Le délai maximum de traitement est 48h. Il est 9h lundi. À quelle heure au plus tard tous les dossiers doivent-ils être traités ?", options:["Lundi 17h","Mardi 9h","Mercredi 9h","Mardi 23h59"], correct:2, points:1 },
  { type:'qcm', text:"Un dossier arrive avec les 3 photos requises mais l'une d'elles montre le marchand portant des lunettes de soleil. Le Proof of Life est à 72. Que fait le Back Office ?", options:["Valider car le Proof of Life dépasse 70","Rejeter — la photo avec lunettes de soleil ne permet pas la vérification biométrique correcte","Valider en notant la réserve dans les commentaires","Demander uniquement une nouvelle photo sans retour terrain"], correct:1, points:1 },
  { type:'qcm', text:"Le Back Office identifie que le même entrepreneur est enregistré dans deux communes différentes avec deux agents différents. Les données KYC sont identiques. Quelle procédure s'applique ?", options:["Valider les deux dossiers pour ne pas perdre de données","Conserver le dossier le plus complet, rejeter l'autre et signaler les deux agents concernés","Supprimer les deux et demander un nouvel enrôlement","Laisser le système gérer automatiquement"], correct:1, points:1 },
  { type:'qcm', text:"Un dossier présente un secteur d'activité KYB = 'Commerce général' mais les photos montrent clairement un salon de coiffure. Le Back Office :", options:["Valide car 'Commerce général' englobe tout","Corrige lui-même le secteur d'activité","Rejette pour incohérence KYB et demande une correction terrain","Ignore l'incohérence si les autres données sont correctes"], correct:2, points:1 },
  { type:'qcm', text:"Quelle est la conséquence directe d'un taux de rejet Back Office supérieur à 25% sur une période donnée ?", options:["Aucune, c'est normal pour un projet de formalisation","Coût supplémentaire terrain, retards et nécessité d'analyser les causes racines avec les équipes","Cela prouve que les agents terrain sont incompétents","Le projet ID30 doit être arrêté"], correct:1, points:1 },
  { type:'qcm', text:"La photo de la CNI d'un dossier est lisible mais présente un reflet lumineux qui cache partiellement le numéro de CNI. Le Back Office :", options:["Valide car la majorité des informations sont lisibles","Rejette — le numéro de CNI doit être entièrement lisible pour la vérification légale","Essaie de deviner les chiffres manquants","Contacte le Ministère pour vérification"], correct:1, points:1 },
  { type:'qcm', text:"Un agent terrain a oublié de capturer la photo du lieu d'activité mais toutes les autres données sont parfaites. Le Back Office :", options:["Valide par exception car les autres données sont excellentes","Rejette — la photo du lieu d'activité est une pièce obligatoire irremplaçable","Demande uniquement la photo manquante par email à l'agent","Note la manque et valide quand même en attente"], correct:1, points:1 },
  { type:'qcm', text:"Le KYB d'un dossier indique 5 employés mais l'entrepreneur a déclaré au Call Center n'avoir aucun employé. Cette contradiction :", options:["Est ignorée car KYC prime sur les déclarations téléphoniques","Doit entraîner un rejet pour vérification et clarification terrain","Est normale car les déclarations téléphoniques et terrain peuvent différer","Ne concerne pas le Back Office"], correct:1, points:1 },
  { type:'qcm', text:"Un dossier est envoyé en Back Office avec un score Proof of Life de 58. L'agent terrain a noté : 'lumière faible, meilleure condition impossible sur le terrain'. Le Back Office :", options:["Valide par compréhension des conditions difficiles","Rejette systématiquement car 58 est sous le seuil minimum de 60","Valide uniquement si le superviseur terrain confirme les conditions","Demande une deuxième tentative dans de meilleures conditions (retour terrain)"], correct:3, points:1 },
  { type:'qcm', text:"La date de naissance sur la CNI indique 1985 mais le formulaire KYC indique 1958. Même prénom et nom. Le Back Office :", options:["Valide en prenant la date de la CNI comme référence","Rejette pour incohérence — l'écart de 27 ans sur l'âge est une erreur critique","Valide en notant les deux dates","Corrige manuellement en alignant sur la CNI"], correct:1, points:1 },
  { type:'qcm', text:"Quel document permet au Back Office de contester une validation déjà faite par un superviseur terrain ?", options:["Une demande verbale","Un rapport d'anomalie documenté avec preuves (photos, données) soumis à la hiérarchie","Aucun, la décision du superviseur terrain est définitive","Un email informel"], correct:1, points:1 },
  { type:'vf', text:"Un score Proof of Life de 60 est suffisant pour valider un dossier si toutes les autres pièces sont conformes.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'vf', text:"Le Back Office peut valider un dossier dont la CNI expire dans 30 jours sans mention particulière.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Si l'adresse GPS est incorrecte mais l'adresse déclarée est cohérente, le Back Office peut valider en conservant l'adresse déclarée uniquement.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Le Back Office peut décider de valider un dossier en attente depuis plus de 72h sans retour terrain, pour éviter le blocage.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'qcm', text:"Un dossier rejeté revient avec corrections après 8 jours ouvrés (au lieu de 5). Le Back Office :", options:["Refuse de le traiter car hors délai","Traite le dossier normalement et note le retard dans le rapport de suivi","Demande une pénalité à l'agent terrain","Archive le dossier sans traitement"], correct:1, points:1 },
  { type:'qcm', text:"Un dossier arrive complet et conforme. Mais le Back Office reconnaît la photo de l'entrepreneur comme étant un de ses proches. Que doit faire l'agent Back Office ?", options:["Valider car les données sont conformes","Signaler le conflit d'intérêt à son superviseur et demander qu'un autre agent traite ce dossier","Rejeter le dossier","Valider rapidement avant que quelqu'un ne remarque"], correct:1, points:1 },
  { type:'qcm', text:"Le Back Office traite en moyenne 25 dossiers par jour. Un lot urgent de 60 dossiers arrive avec délai de 24h. La priorité correcte est :", options:["Traiter les 60 en urgence en sautant certaines vérifications","Traiter les 25 normaux d'abord, puis les 60","Alerter le superviseur, définir des priorités et traiter méthodiquement en respectant les standards","Refuser les 60 car c'est au-delà de la capacité"], correct:2, points:1 },
  { type:'qcm', text:"Quel est l'indicateur clé qui différencie un Back Office performant d'un Back Office rapide mais peu fiable ?", options:["Le nombre de dossiers traités par heure","Le taux de validation croisé avec le taux d'anomalies détectées après validation","Le nombre d'heures supplémentaires effectuées","La taille des fichiers traités"], correct:1, points:1 },
  { type:'qcm', text:"Un agent Back Office découvre qu'un lot de 15 dossiers envoyés par le même agent terrain contient des photos identiques copiées-collées sur des formulaires différents. Il doit :", options:["Valider car les formulaires ont des noms différents","Rejeter tous les 15 dossiers et signaler immédiatement comme fraude potentielle au superviseur et à la direction","Rejeter uniquement les dossiers avec doublons évidents","Appeler l'agent terrain pour clarification avant toute action"], correct:1, points:1 },
  { type:'qcm', text:"La différence entre KYC et KYB dans le dossier ID30 est :", options:["KYC = données financières, KYB = données personnelles","KYC = identité personnelle de l'entrepreneur, KYB = données sur l'activité commerciale","KYC et KYB désignent la même chose dans ce contexte","KYC = données Back Office, KYB = données terrain"], correct:1, points:1 },
  { type:'qcm', text:"Le Back Office reçoit un dossier avec une note de l'agent terrain : 'Entrepreneur nerveux, a refusé de sourire pour la photo'. Le Proof of Life est à 64. Le Back Office :", options:["Rejette car le score est trop bas","Valide car 64 dépasse le minimum de 60 et le contexte explique le score bas","Demande une nouvelle visite pour avoir un score de 70","Ignore la note de l'agent"], correct:1, points:1 },
  { type:'vf', text:"Un dossier pour lequel le Back Office ne peut pas vérifier les coordonnées GPS (zone hors couverture cartographique) doit systématiquement être rejeté.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Le Back Office est autorisé à valider provisoirement un dossier incomplet pour ne pas bloquer l'émission de la Carte Entreprenant.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Un entrepreneur ayant deux activités commerciales différentes peut légalement avoir deux dossiers ID30 distincts.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'qcm', text:"Lors du contrôle d'un dossier, le Back Office constate que le FAMOCO utilisé avait une version firmware obsolète lors de la capture. Cela impacte :", options:["Uniquement la qualité des photos","La fiabilité du Proof of Life et potentiellement la précision GPS — le dossier doit être signalé","Rien, le firmware n'affecte pas les données","Uniquement la date de capture"], correct:1, points:1 },
  { type:'open', text:"Vous recevez un dossier avec ces caractéristiques : Proof of Life = 61, CNI expirée depuis 3 semaines, coordonnées GPS à 800m de l'adresse déclarée, photos nettes mais secteur d'activité KYB vide. Détaillez votre décision pour chaque point et justifiez votre décision finale : validation, mise en attente ou rejet.", options:[], correct:0, points:3 }
],

'inspecteur': [
  { type:'qcm', text:"Lors d'une visite, l'inspecteur scanne le QR Code mais l'application indique 'Enregistrement non trouvé'. L'entrepreneur présente sa Carte Entreprenant physique. L'inspecteur doit :", options:["Valider visuellement sur la base de la carte physique","Signaler l'anomalie dans l'application, photographier la carte et escalader au superviseur","Demander à l'entrepreneur de contacter le Back Office lui-même","Ignorer et passer au point de vente suivant"], correct:1, points:1 },
  { type:'qcm', text:"L'inspecteur arrive chez un entrepreneur. Le lieu d'activité déclaré est un kiosque de 2m² mais la carte indique une superficie de 25m². Que fait l'inspecteur ?", options:["Valider car les superficies sont approximatives","Signaler l'écart comme non-conformité KYB et documenter avec photos","Corriger lui-même la superficie dans l'application","Ignorer car la superficie n'est pas un critère de conformité"], correct:1, points:1 },
  { type:'qcm', text:"L'inspecteur découvre qu'un entrepreneur utilise sa Carte Entreprenant pour une activité totalement différente de celle déclarée (ex : déclaré coiffeur, exerce comme mécanicien). Quelle est la gravité de cette situation ?", options:["Mineure — l'activité importe peu tant que la carte est valide","Majeure — fraude sur l'identité commerciale, escalader immédiatement au superviseur et documentation complète","Normale — les activités peuvent évoluer","Mineure — noter dans le rapport sans signalement urgent"], correct:1, points:1 },
  { type:'qcm', text:"La précision GPS lors d'une visite d'inspection affiche 12 mètres. L'inspecteur :", options:["Continue normalement, 12 mètres est excellent","Attend que la précision atteigne 5 mètres ou moins avant de capturer","Note la précision 'Acceptable' (≤15m), documente et continue","Reporte la visite car la précision est insuffisante"], correct:2, points:1 },
  { type:'qcm', text:"L'entrepreneur refuse catégoriquement de laisser l'inspecteur prendre des photos de son commerce, invoquant des raisons de sécurité. L'inspecteur :", options:["Prend quand même les photos discrètement","Abandonne la visite sans rapport","Documente le refus dans l'application avec date/heure, note les observations visuelles et signale au superviseur","Accepte et valide quand même sans photos"], correct:2, points:1 },
  { type:'qcm', text:"Lors d'une visite, l'inspecteur constate que la Carte Entreprenant présentée est une photocopie et non l'original. L'entrepreneur dit avoir perdu l'original. L'inspecteur :", options:["Accepte la photocopie et valide","Demande à l'entrepreneur de se rendre au bureau MAFA pour duplicata, documente et marque 'Carte manquante'","Valide provisoirement en attendant le duplicata","Confisque la photocopie"], correct:1, points:1 },
  { type:'qcm', text:"L'inspecteur visite un point de vente. L'entrepreneur est présent mais refuse de montrer sa Carte Entreprenant en disant qu'elle est 'à la maison'. L'inspecteur :", options:["Valide quand même sur la base de l'identité verbale","Programme une re-visite dans 48h et documente le motif","Clôture définitivement le dossier comme non-conforme","Appelle le Call Center pour signalement"], correct:1, points:1 },
  { type:'qcm', text:"Sur la carte de l'application Inspector, un point ROUGE signifie :", options:["Un entrepreneur enrôlé récemment en attente de visite","Un entrepreneur déjà visité et marqué non-conforme nécessitant suivi urgent","Un inspecteur en déplacement dans ce secteur","Une zone sans couverture réseau"], correct:1, points:1 },
  { type:'qcm', text:"L'inspecteur réalise sa 11ème visite de la journée mais il est 17h30 et le dernier entrepreneur sur sa liste ferme à 18h. La distance est de 35 minutes. Que fait l'inspecteur ?", options:["Abandonne la visite et la reporte au lendemain","Tente de se dépêcher quitte à bâcler la documentation","Appelle le superviseur pour décider : effectuer la visite ou la reprogrammer intelligemment","Marque la visite comme 'Effectuée' sans y aller pour atteindre son quota"], correct:2, points:1 },
  { type:'qcm', text:"L'inspecteur constate que 3 entrepreneurs voisins (marché adjacent) ont exactement les mêmes coordonnées GPS dans leurs dossiers. Cela indique :", options:["Une erreur systématique de capture GPS lors de l'enrôlement — à signaler comme anomalie groupe","Que les 3 entrepreneurs partagent le même emplacement légalement","Une coïncidence normale dans les marchés denses","Que l'application GPS est défectueuse"], correct:0, points:1 },
  { type:'qcm', text:"Lors d'une visite, l'entrepreneur montre une Carte Entreprenant au nom de sa femme mais c'est l'homme qui gère l'activité au quotidien. L'inspecteur :", options:["Valide car l'activité est bien présente","Documente la situation : titulaire absent, activité gérée par tiers — signaler pour vérification de conformité légale","Invalide immédiatement","Ignore et passe à la prochaine visite"], correct:1, points:1 },
  { type:'qcm', text:"Qu'est-ce qu'une visite 'fantôme' dans le contexte de l'inspection ID30 ?", options:["Une visite effectuée la nuit","Une visite enregistrée dans l'application sans avoir été réellement effectuée sur le terrain — fraude grave","Une visite sans GPS activé","Une visite d'un entrepreneur difficile à trouver"], correct:1, points:1 },
  { type:'qcm', text:"L'inspecteur remarque que son application affiche 'Synchronisation en échec depuis 6h'. Il a 4 rapports de visite non synchronisés. Il doit :", options:["Recommencer les 4 visites une fois le réseau rétabli","Sauvegarder les données localement et synchroniser dès que le réseau est disponible — ne pas effacer les données","Contacter le superviseur pour saisir manuellement les données","Abandonner les rapports et refaire les visites"], correct:1, points:1 },
  { type:'qcm', text:"La Fiche de Visite Inspector comporte 8 étapes. L'étape 5 (Actions) permet de :", options:["Photographier le lieu d'activité","Saisir le statut de conformité et les actions correctives recommandées","Enregistrer la signature de l'entrepreneur","Soumettre le rapport final"], correct:1, points:1 },
  { type:'qcm', text:"Un entrepreneur conforme il y a 3 mois est re-visité et son activité a complètement cessé (local vide). L'inspecteur :", options:["Valide car le dossier était conforme précédemment","Marque 'Non-conforme — Activité cessée' avec photos du local vide et remonte au superviseur","Supprime la Carte Entreprenant de la base de données","Ignore et maintient le statut conforme"], correct:1, points:1 },
  { type:'vf', text:"Un inspecteur peut fermer une visite comme 'Conforme' si le QR Code est valide même sans avoir vérifié la concordance activité/réalité terrain.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"L'application Inspector permet à l'inspecteur de contester une validation Back Office directement depuis son interface.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Un inspecteur peut effectuer une visite de contrôle sans que l'entrepreneur soit présent, si le lieu d'activité est accessible et l'activité observable.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Le rapport d'inspection doit contenir au minimum 2 photos géolocalisées pour être accepté par le système.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'qcm', text:"L'inspecteur constate une erreur dans son propre rapport après soumission. Quelle est la procédure ?", options:["Supprimer le rapport et en créer un nouveau","Contacter le superviseur pour demander une correction officielle du rapport soumis","Soumettre un second rapport en contradiction avec le premier","Ignorer l'erreur si elle est mineure"], correct:1, points:1 },
  { type:'qcm', text:"Un inspecteur est sollicité par un entrepreneur pour 'accélérer' la conformité de son dossier en échange d'un service. L'inspecteur doit :", options:["Accepter si le dossier mérite vraiment d'être validé","Refuser fermement, documenter la tentative de corruption et la signaler immédiatement à son superviseur","Accepter mais noter la conformité objective","Ignorer et traiter le dossier normalement"], correct:1, points:1 },
  { type:'qcm', text:"Lors d'une visite groupée dans un marché, l'inspecteur peut-il utiliser une seule photo de la devanture du marché pour plusieurs dossiers d'entrepreneurs différents ?", options:["Oui, si les entrepreneurs sont dans le même marché","Non — chaque dossier exige des photos individuelles spécifiques à l'emplacement et l'activité de l'entrepreneur","Oui, si les entrepreneurs sont côte à côte","Non, sauf autorisation superviseur"], correct:1, points:1 },
  { type:'qcm', text:"La Fiche de Visite étape 2 correspond à :", options:["GPS","QR Code","Photos","Signature"], correct:1, points:1 },
  { type:'qcm', text:"Comment l'inspecteur distingue un point ORANGE d'un point JAUNE sur la carte Inspector ?", options:["Orange = attente validation, Jaune = problème GPS détecté","Orange = enrôlé par agent en attente de première inspection, Jaune = re-visite programmée","Orange = conforme, Jaune = non-conforme","Il n'y a pas de points jaunes dans Inspector"], correct:1, points:1 },
  { type:'qcm', text:"L'inspecteur a effectué 12 visites aujourd'hui dont 4 marquées 'Non-conformes'. Son superviseur lui demande de 'réajuster' ces 4 dossiers en conformes pour améliorer les statistiques. L'inspecteur :", options:["Obéit au superviseur car c'est sa hiérarchie","Refuse et signale la pression hiérarchique inappropriée à l'échelon supérieur","Modifie 2 sur 4 comme compromis","Obéit mais garde une copie de ses rapports originaux"], correct:1, points:1 },
  { type:'vf', text:"L'inspecteur peut décider de ne pas visiter un entrepreneur déjà conforme lors de la dernière inspection si aucun signalement n'a été fait sur ce dossier.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Un inspecteur dont le taux de conformité dépasse 95% sur un mois peut être suspecté de ne pas effectuer des contrôles rigoureux.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'open', text:"Lors d'une visite d'inspection, vous découvrez : (1) QR Code valide et correspondent au dossier, (2) l'activité est présente mais différente de celle déclarée, (3) l'entrepreneur dit avoir changé d'activité il y a 2 mois sans en informer MAFA. Détaillez chaque étape de votre rapport et vos recommandations.", options:[], correct:0, points:3 }
],

'superviseur': [
  { type:'qcm', text:"Un agent de votre équipe a un taux de déploiement de 35% (objectif : 85%) depuis 2 semaines. Les autres agents sont à 80%+. Quelle est votre première action ?", options:["Le sanctionner immédiatement","Organiser un accompagnement terrain d'une journée pour identifier les blocages opérationnels","Lui attribuer une zone plus facile sans discussion","Ignorer en espérant que ça s'améliore"], correct:1, points:1 },
  { type:'qcm', text:"L'application Superviseur affiche 3 déploiements 'En attente de validation' depuis plus de 2 heures. Vous êtes en réunion. Que faites-vous ?", options:["Attendre la fin de la réunion","Valider rapidement sur mobile entre deux points de la réunion ou déléguer à un superviseur adjoint si disponible","Demander aux agents d'annuler et de recommencer demain","Ignorer — les agents peuvent attendre"], correct:1, points:1 },
  { type:'qcm', text:"Un marchand contacte directement le superviseur (numéro transmis par erreur par un agent) pour se plaindre que son QR Code ne fonctionne pas. Le superviseur :", options:["Donne le numéro du 0808 uniquement","Vérifie dans l'application Superviseur le statut du déploiement, identifie l'agent concerné et coordonne la solution","Demande au marchand de rappeler l'agent directement","Dit au marchand que ce n'est pas son rôle"], correct:1, points:1 },
  { type:'qcm', text:"Votre équipe de 6 agents doit déployer 300 QR Codes en 5 jours. Comment répartissez-vous les objectifs ?", options:["60 par agent sur 5 jours sans distinction","Analyser les performances passées de chaque agent et attribuer des objectifs différenciés selon les capacités","Donner 300 à l'agent le plus performant","Demander à chaque agent de s'auto-attribuer son objectif"], correct:1, points:1 },
  { type:'qcm', text:"L'application Superviseur indique qu'un agent a synchronisé 15 déploiements en 2 heures (hors du commun). Vous devez :", options:["Féliciter l'agent publiquement sans vérification","Vérifier la géolocalisation et les détails de chaque déploiement pour confirmer leur authenticité","Ignorer car c'est une bonne performance","Demander à l'agent une explication écrite"], correct:1, points:1 },
  { type:'qcm', text:"Un agent signale que lors de 3 enrôlements consécutifs dans un même marché, les QR Codes à blanc ont été refusés par le système (déjà utilisés). Que fait le superviseur ?", options:["Demander à l'agent de continuer avec d'autres kits","Investiguer si les kits ont été compromis, bloquer les QR Codes suspects et signaler à la direction technique","Fournir de nouveaux kits sans investigation","Suspendre l'agent jusqu'à clarification"], correct:1, points:1 },
  { type:'qcm', text:"Le taux de déploiement de votre équipe est 75% (objectif 85%). Il reste 5 jours. Quelle stratégie adoptez-vous ?", options:["Accepter 75% car c'est proche de l'objectif","Analyser les zones non couvertes, réaffecter les agents vers les marchés à forte densité et intensifier le suivi quotidien","Demander une extension de délai","Travailler uniquement les marchés faciles pour gonfler les chiffres"], correct:1, points:1 },
  { type:'qcm', text:"Lors d'un test de transaction post-déploiement, le QR Code affiche 'Marchand non trouvé'. L'agent a déjà quitté le point de vente. Le superviseur :", options:["Demande à l'agent de revenir immédiatement chez le marchand pour réenrôler","Appelle le 0808 pour signalement technique pendant que l'agent retourne chez le marchand","Invalide le déploiement et demande à l'agent de le refaire le lendemain","Marque le déploiement comme réussi malgré l'erreur"], correct:1, points:1 },
  { type:'qcm', text:"Votre équipe utilise l'application Agent version 2.1 mais une mise à jour vers 2.3 est disponible. La 2.3 corrige des bugs GPS. Que faites-vous ?", options:["Laisser chaque agent décider de mettre à jour","Planifier une mise à jour coordonnée de toute l'équipe lors d'une pause pour éviter les incohérences de version","Mettre à jour uniquement votre propre application en premier","Attendre que la direction impose la mise à jour"], correct:1, points:1 },
  { type:'qcm', text:"Un marchand Premium refuse de montrer ses documents financiers à l'agent lors du déplafonnement. L'agent vous appelle. Que conseillez-vous ?", options:["Forcer le marchand à montrer les documents","Expliquer que les documents sont obligatoires pour le déplafonnement Premium — sans eux, seul le profil Classique est possible","Valider le déplafonnement Premium sans les documents pour ne pas perdre le marchand","Demander au marchand d'envoyer les documents par WhatsApp"], correct:1, points:1 },
  { type:'qcm', text:"Le tableau de bord Superviseur indique que votre zone a un taux de 'Doublons détectés' de 12% (moyenne nationale : 3%). Que faire en priorité ?", options:["Ignorer car votre taux de déploiement est bon","Analyser les dossiers doublons pour identifier si c'est une erreur de kits, de procédure ou de fraude potentielle","Accuser les agents de fraude sans investigation","Signaler à la direction et attendre leurs instructions"], correct:1, points:1 },
  { type:'qcm', text:"Un agent vous demande comment gérer un marchand OM Essentiel qui veut encaisser 120 000 FCFA en une seule transaction. Que répondez-vous ?", options:["La transaction sera refusée","La transaction est acceptée avec des frais sur les 70 000 FCFA au-delà du plafond gratuit de 50 000 FCFA/jour","La transaction nécessite une validation superviseur","Le marchand doit passer au profil Classique avant d'encaisser"], correct:1, points:1 },
  { type:'qcm', text:"Quelle est la différence opérationnelle entre un déploiement 'QR Code à blanc' et un 'QR Code actif' dans l'application Agent ?", options:["Le QR Code à blanc est en noir et blanc, l'actif est en couleur","Le QR Code à blanc est scanné lors de l'enrôlement O'calm pour initialiser le compte, le QR Code actif est le code final fonctionnel après validation","Le QR Code à blanc est temporaire, valable 24h seulement","Il n'y a aucune différence fonctionnelle"], correct:1, points:1 },
  { type:'qcm', text:"Vous constatez qu'un agent enregistre systématiquement des tests de transaction réussis mais les marchands signalent que leurs QR Codes ne fonctionnent pas. Que soupçonnez-vous ?", options:["Un problème réseau localisé dans la zone de l'agent","L'agent falsifie les tests de transaction dans l'application sans les effectuer réellement","Un bug de l'application que vous devez signaler","Une formation insuffisante des marchands"], correct:1, points:1 },
  { type:'qcm', text:"Le superviseur reçoit une demande d'un agent pour changer de zone de déploiement car 'les marchands dans sa zone sont hostiles'. Que fait le superviseur ?", options:["Refuse catégoriquement, la zone est fixe","Accompagne l'agent dans la zone pour observer les interactions, propose des techniques de persuasion et réévalue si nécessaire","Accepte immédiatement le changement de zone","Signale l'agent à la direction pour manque de professionnalisme"], correct:1, points:1 },
  { type:'vf', text:"Le superviseur peut valider un déploiement QR Code sans avoir vérifié si le test de transaction a été effectué.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"Si un agent O'calm enregistre plus de 8 déploiements par jour pendant 3 jours consécutifs, le superviseur doit le signaler à la direction comme performance exceptionnelle à analyser.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'vf', text:"Un superviseur peut accéder aux données de performance de toutes les équipes du projet, pas seulement la sienne.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'vf', text:"L'application Superviseur permet de bloquer temporairement un agent soupçonné de fraude en attendant l'investigation.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'qcm', text:"Lors d'une réunion d'équipe hebdomadaire, un agent partage publiquement les difficultés d'un collègue. Vous en tant que superviseur :", options:["Laissez le débat s'installer, c'est constructif","Recadrez immédiatement : les performances individuelles se traitent en entretien privé, pas en réunion collective","Encouragez la comparaison entre agents pour stimuler la compétition","Ignorez l'incident"], correct:1, points:1 },
  { type:'qcm', text:"Le RCCM d'un marchand demandant le profil Premium indique une date de création d'entreprise postérieure à la date d'inscription ID30. Cela signifie :", options:["Le marchand est éligible au Premium car il a maintenant un RCCM","Anomalie chronologique — l'entreprise légale n'existait pas au moment de l'enrôlement ID30, à signaler et analyser","Aucun problème — les dates peuvent différer légalement","Le dossier ID30 doit être mis à jour avec la nouvelle date"], correct:1, points:1 },
  { type:'qcm', text:"L'application Superviseur indique que 4 agents ont synchronisé leurs données dans la même plage horaire (8h01 à 8h04) avec des localisations différentes de plus de 15 km chacune. Que peut cela indiquer ?", options:["Un réseau très rapide ce matin-là","Une synchronisation différée de données collectées la veille, ou une anomalie de données à vérifier","Une performance exceptionnelle de l'équipe","Une mise à jour automatique de l'application"], correct:1, points:1 },
  { type:'qcm', text:"Un marchand Essentiel demande à un agent comment passer au profil Classique. L'agent ne sait pas répondre et appelle le superviseur. La réponse correcte est :", options:["Appeler le 0808","Menu options de l'application OM Business → Demander déplafonnement → Profil Classique → Fournir les pièces requises — réponse sous 24h","Se rendre en agence Orange","Attendre 6 mois d'utilisation active avant de pouvoir déplafonner"], correct:1, points:1 },
  { type:'qcm', text:"Quel critère différencie le profil OM Business Classique du profil Essentiel en termes de plafond mensuel d'encaissement ?", options:["Classique : 500 000 FCFA, Essentiel : 250 000 FCFA","Classique : plafond supérieur négocié avec Orange CI (plusieurs millions FCFA), Essentiel : 500 000 FCFA/mois gratuit","Classique : illimité, Essentiel : 100 000 FCFA","Classique : 1 000 000 FCFA, Essentiel : 500 000 FCFA"], correct:1, points:1 },
  { type:'qcm', text:"Un superviseur constate que son équipe atteint l'objectif en quantité mais que le taux d'anomalies signalées post-déploiement est de 18% (tolérance : 5%). Quelle est la cause la plus probable ?", options:["L'objectif quantitatif est trop élevé","Les agents privilégient la vitesse de déploiement au détriment de la qualité de vérification","Les marchands sont mal formés","Le réseau est instable dans la zone"], correct:1, points:1 },
  { type:'vf', text:"Le superviseur est co-responsable de la qualité des déploiements de ses agents, pas seulement de leur volume.", options:["Vrai","Faux"], correct:0, points:1 },
  { type:'vf', text:"Un superviseur peut approuver un déploiement pour un marchand dont le QR Code à blanc a déjà été utilisé par un autre agent.", options:["Vrai","Faux"], correct:1, points:1 },
  { type:'open', text:"Vous supervisez une équipe de 5 agents sur une zone de 3 marchés. Après 2 semaines, vous constatez : agent A = 90% d'objectif, B = 85%, C = 45%, D = 78%, E = 30%. Le délai de fin de mission est dans 8 jours. Décrivez votre plan d'action complet pour les 8 jours restants, agent par agent.", options:[], correct:0, points:3 }
]
}; // fin QUESTIONS_BY_POSTE"""

# Reconstruire le contenu avec le nouveau bloc
content = (
    content[:idx_start]
    + NEW_QUESTIONS_BLOCK
    + content[idx_end + len(DELIM_END):]
)

print("[OK] Bloc QUESTIONS_BY_POSTE remplacé")

# ============================================================
# CORRECTION A — Sauvegarder liste complète dans localStorage (finalizeExam)
# ============================================================

OLD_A = """  state.results.push(result);

  // Sauvegarder dans localStorage sous le code personnel
  try {
    localStorage.setItem('mafa_result_' + resultCode, JSON.stringify(result));
  } catch(e) {}"""

NEW_A = """  state.results.push(result);

  // Sauvegarder dans localStorage sous le code personnel
  try {
    localStorage.setItem('mafa_result_' + resultCode, JSON.stringify(result));
  } catch(e) {}
  // Sauvegarder liste complete dans localStorage
  try { localStorage.setItem('mafa_all_results', JSON.stringify(state.results)); } catch(e) {}"""

assert OLD_A in content, "ERREUR A: pattern introuvable"
content = content.replace(OLD_A, NEW_A, 1)
print("[OK] Correction A appliquée (mafa_all_results save)")

# ============================================================
# CORRECTION B — Restaurer résultats au démarrage (INIT)
# ============================================================

OLD_B = "state.examActive = true;\n</script>"

NEW_B = """state.examActive = true;
// Restaurer les resultats depuis localStorage
try {
  const stored = localStorage.getItem('mafa_all_results');
  if(stored) state.results = JSON.parse(stored);
} catch(e) {}
</script>"""

assert OLD_B in content, "ERREUR B: pattern introuvable"
content = content.replace(OLD_B, NEW_B, 1)
print("[OK] Correction B appliquée (restauration localStorage)")

# ============================================================
# CORRECTION C — Colonne "Poste" dans renderResults()
# ============================================================

OLD_C_TH = """            <th>Rang</th>
            <th>Candidat</th>
            <th>Contact</th>
            <th>Score</th>
            <th>Durée</th>
            <th>Date</th>"""

NEW_C_TH = """            <th>Rang</th>
            <th>Candidat</th>
            <th>Poste</th>
            <th>Contact</th>
            <th>Score</th>
            <th>Durée</th>
            <th>Date</th>"""

assert OLD_C_TH in content, "ERREUR C (th): pattern introuvable"
content = content.replace(OLD_C_TH, NEW_C_TH, 1)
print("[OK] Correction C <th> appliquée")

OLD_C_TD = """              <td><strong>${r.firstname} ${r.lastname}</strong></td>
              <td style="font-size:0.8rem;color:var(--text-muted)">${r.email}<br>${r.phone||''}</td>"""

NEW_C_TD = """              <td><strong>${r.firstname} ${r.lastname}</strong></td>
              <td style="font-size:0.78rem;color:var(--accent);font-weight:600">${r.posteLabel||'—'}</td>
              <td style="font-size:0.8rem;color:var(--text-muted)">${r.email}<br>${r.phone||''}</td>"""

assert OLD_C_TD in content, "ERREUR C (td): pattern introuvable"
content = content.replace(OLD_C_TD, NEW_C_TD, 1)
print("[OK] Correction C <td> appliquée")

# ============================================================
# CORRECTION D — resetExam() supprime aussi localStorage
# ============================================================

OLD_D = "    state.results = [];\n    state.examActive = false;"
NEW_D = "    state.results = [];\n    try { localStorage.removeItem('mafa_all_results'); } catch(e) {}\n    state.examActive = false;"

assert OLD_D in content, "ERREUR D: pattern introuvable"
content = content.replace(OLD_D, NEW_D, 1)
print("[OK] Correction D appliquée (resetExam localStorage)")

# ============================================================
# CORRECTION E — Bouton "Effacer tout" dans renderResults()
# ============================================================

OLD_E = "      <button class=\"btn btn-orange btn-sm\" onclick=\"exportResults()\">📥 Exporter CSV</button>\n    </div>`;\n}"

NEW_E = "      <button class=\"btn btn-orange btn-sm\" onclick=\"exportResults()\">📥 Exporter CSV</button>\n      <button class=\"btn btn-secondary btn-sm\" onclick=\"if(confirm('Effacer tous les resultats ?')){state.results=[];try{localStorage.removeItem('mafa_all_results');}catch(e){}renderResults();}\" style=\"border-color:var(--danger);color:var(--danger)\">🗑 Effacer tout</button>\n    </div>`;\n}"

assert OLD_E in content, "ERREUR E: pattern introuvable"
content = content.replace(OLD_E, NEW_E, 1)
print("[OK] Correction E appliquée (bouton Effacer tout)")

# ── Écrire le fichier modifié ────────────────────────────────────────────────
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n[SUCCES] Fichier écrit : {OUT}")
print(f"         Taille finale : {len(content)} caractères")
