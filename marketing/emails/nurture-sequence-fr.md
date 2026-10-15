# Séquence nurture : après une réponse positive (Track B, HTML avec animation et vidéo)

```
Séquence : Owl — démo et pilote
Déclencheur : le cabinet a répondu « oui » / demandé la vidéo / s'est inscrit sur le site
Objectif : démo réservée, puis pilote de 30 jours démarré
Longueur : 5 emails sur 14 jours
Format : HTML (template templates/owl-video-email.html), GIF animé, vignette vidéo, un bouton
Envoi : depuis thinkactionn.com via Brevo (ou Mailchimp)
Sortie : démo réservée → arrêter la séquence et passer au suivi commercial
```

---

## N1 : Immédiatement : la vidéo
**Template :** `templates/owl-video-email.html` (déjà rédigé)
**Objet :** `La vidéo Owl promise (2 min)`
**Pré-en-tête :** `Un dossier client traité de bout en bout, des factures à la déclaration de TVA.`
**CTA :** `▶ Voir la démo` → page vidéo · lien secondaire : `Réserver 20 minutes` → Calendly

---

## N2 : Jour 2 : comment ça marche (GIF `owl-flow.gif`)
**Objet :** `Owl en 3 étapes`
**Pré-en-tête :** `Activité et régime de TVA, écritures, déclaration prête à contrôler.`

```
Bonjour {{prenom}},

Voici ce qui se passe quand un dossier entre dans Owl :

[GIF animé : owl-flow.gif]

1. Owl lit l'activité du client et son régime de TVA.
2. Il génère les écritures comptables avec les bons comptes et les bons taux.
3. Il prépare la déclaration de TVA, que votre collaborateur contrôle et valide.

Votre équipe garde la main sur la validation. Owl prend la saisie.

[Bouton : Voir un dossier réel →  page vidéo]

Mostafa
```

---

## N3 : Jour 5 : sécurité (l'objection n°1 des cabinets)
**Objet :** `Où vont les données de vos clients ?`
**Pré-en-tête :** `Hébergement, chiffrement, accès : les réponses précises.`

```
Bonjour {{prenom}},

C'est la première question que posent les experts-comptables, et c'est normal : vous êtes responsable des données de vos clients.

Concrètement, avec Owl :
- Hébergement : [TODO : pays / hébergeur]
- Chiffrement : [TODO : en transit et au repos]
- Accès : [TODO : comptes par collaborateur, droits par dossier, journal des actions]
- Vos données restent les vôtres : [TODO : export complet, suppression sur demande]

Si votre cabinet a un questionnaire sécurité, envoyez-le-moi et je le remplis.

[Bouton : Poser une question → répondre à l'email]

Mostafa
```

> ⚠️ Remplir chaque TODO avec des faits exacts. Une promesse de sécurité fausse est un vrai risque juridique.

---

## N4 : Jour 9 : le calcul du temps gagné
**Objet :** `Combien coûte une échéance de TVA ?`
**Pré-en-tête :** `Un calcul de 30 secondes avec les chiffres de votre cabinet.`

```
Bonjour {{prenom}},

Un calcul rapide pour {{cabinet}} :

[nombre de dossiers TVA] × [heures de saisie par dossier] × [coût horaire d'un collaborateur]

Exemple : 80 dossiers × 1,5 h × 150 MAD = 18 000 MAD de saisie par échéance mensuelle.

Owl ne supprime pas le contrôle, mais il retire l'essentiel de la saisie. Sur votre propre chiffre, combien de ces heures pourraient aller au conseil ?

[Bouton : Faire le calcul ensemble (20 min) → Calendly]

Mostafa
```

---

## N5 : Jour 14 : l'offre pilote
**Objet :** `Un pilote sur 10 de vos dossiers`
**Pré-en-tête :** `30 jours, mise en place incluse, vous jugez sur une vraie échéance.`

```
Bonjour {{prenom}},

Je vous propose un pilote :

- 10 dossiers de votre choix
- 30 jours, soit une vraie échéance de TVA
- Mise en place faite avec vous
- [TODO : gratuit / prix pilote / déduit de l'abonnement]

À la fin, vous comparez le temps passé et la qualité des écritures. Si ça ne vous convainc pas, on s'arrête là.

[Bouton : Démarrer le pilote → Calendly]

Mostafa
```

---

## Mesures
| Mesure | Cible |
|---|---|
| Clic sur la vidéo (N1) | 40 %+ (ces contacts ont demandé la vidéo) |
| Démo réservée sur la séquence | 25–40 % |
| Désinscription par email | < 0,5 % |

Utilisez le skill `ab-testing` pour tester l'objet de N1 et la vignette vidéo (GIF ou image fixe).
