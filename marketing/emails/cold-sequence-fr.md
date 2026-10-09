# Séquence de prospection à froid : cabinets comptables (Track A)

```
Séquence : Owl — prospection cabinets comptables
Déclencheur : cabinet ajouté à la liste vérifiée
Objectif : obtenir une réponse (« oui, envoyez la vidéo » / « on peut en parler »)
Longueur : 5 emails sur 22 jours
Format : texte brut, pas d'image, pas de lien dans l'email 1, suivi d'ouverture désactivé
Sortie : toute réponse (positive ou négative) arrête la séquence immédiatement
Envoi : depuis un domaine secondaire, mardi à jeudi, 9 h – 11 h
```

**Variables :** `{{prenom}}`, `{{cabinet}}`, `{{ville}}`, `{{accroche}}` (une phrase personnelle, voir plus bas).

**Signature (tous les emails) :**
```
Mostafa Driouiche
ThinkAction · Owl
[Adresse postale de la société]
Si ce n'est pas un sujet pour vous, répondez « non » et je ne vous relancerai pas.
```

---

## Email 1 : Jour 0 (la personnalisation compte le plus ici)

**Objet :** `tva {{cabinet}}`
*(variantes à tester : `saisie et tva` · `vos fins de mois`)*

```
Bonjour {{prenom}},

{{accroche}}

Dans beaucoup de cabinets, chaque échéance de TVA veut encore dire des heures de ressaisie, avec un régime différent à vérifier pour chaque dossier.

Owl part de l'activité et du régime de TVA de chaque client pour générer les écritures comptables et préparer la déclaration. Vos collaborateurs n'ont plus qu'à contrôler et valider.

Est-ce que c'est un sujet chez {{cabinet}} en ce moment ?

Mostafa
```

**Exemples d'`{{accroche}}`** (doit mener au problème, pas juste flatter) :
- « J'ai vu que vous recrutez un collaborateur comptable à {{ville}} ; j'imagine que les échéances de TVA pèsent sur l'équipe actuelle. »
- « Votre cabinet suit beaucoup de commerçants et de restaurateurs, des dossiers où les taux de TVA se mélangent vite. »
- « J'ai lu votre post sur la dernière échéance de TVA, et le point sur le temps passé en saisie m'a parlé. »

Pas d'accroche réelle ? Supprimez la ligne plutôt que d'écrire une flatterie générique.

---

## Email 2 : Jour 3 (angle : le risque, et le pont vers la vidéo)

**Objet :** `erreur de régime`

```
Bonjour {{prenom}},

Une erreur fréquente en saisie : un dossier passe d'un régime de TVA à un autre en cours d'année, et le paramétrage ne suit pas. L'écart se découvre au moment de la déclaration, ou pire, lors d'un contrôle.

Owl relit le régime et l'activité de chaque client avant de générer les écritures, donc l'écriture suit le bon régime dès le départ.

J'ai une vidéo de 2 minutes qui montre un dossier traité de bout en bout, des factures à la déclaration. Je vous l'envoie ?

Mostafa
```

> Si la réponse est « oui » → envoyer `templates/owl-video-email.html` (Track B).

---

## Email 3 : Jour 8 (angle : preuve)

**Objet :** `un cabinet comme {{cabinet}}`

```
Bonjour {{prenom}},

[Nom du cabinet pilote ou « Un cabinet de 6 personnes à Lyon »] traitait [X] dossiers TVA par mois, avec [Y] heures de saisie par échéance.

Avec Owl, l'équipe est passée à [Z] heures, et les collaborateurs ont repris du temps pour le conseil client.

Est-ce que des chiffres comparables vous intéresseraient pour {{cabinet}} ?

Mostafa
```

> ⚠️ N'envoyez cet email qu'avec des **chiffres réels**. Sans pilote encore, remplacez-le par un email « coût caché » : nombre de dossiers × heures × taux horaire d'un collaborateur.

---

## Email 4 : Jour 15 (angle : essai sur un vrai dossier)

**Objet :** `un dossier test`

```
Bonjour {{prenom}},

Une proposition concrète : vous choisissez un dossier client (anonymisé si vous préférez), on le passe dans Owl, et vous comparez les écritures et la préparation de TVA avec ce que votre équipe a produit.

Ça prend 20 minutes de votre côté et vous jugez sur votre propre dossier.

Ça vous tente ?

Mostafa
```

---

## Email 5 : Jour 22 (rupture, et on respecte la décision)

**Objet :** `je clôture`

```
Bonjour {{prenom}},

Sans retour de votre part, je suppose que ce n'est pas le bon moment, et je m'arrête là.

Pour faire simple, répondez juste par un chiffre :

1 : intéressé, parlons-en
2 : pas maintenant, revenez vers moi dans 3 mois
3 : pas intéressé, merci de ne plus m'écrire

Bonne fin d'échéance,
Mostafa
```

> Après cet email, **plus aucun contact** sauf si le cabinet répond 1 ou 2.

---

## Traiter les réponses (dans l'heure)

| Réponse | Action |
|---|---|
| « Oui, envoyez la vidéo » | Envoyer l'email vidéo HTML et entrer le contact dans la séquence nurture |
| « On peut en parler » | Proposer 2 créneaux précis + lien Calendly |
| « On a déjà un logiciel » | « Lequel ? Owl prépare les écritures et la TVA en amont, et s'exporte vers [logiciel]. Je vous montre sur un dossier ? » |
| « Et la sécurité des données ? » | Réponse courte + email nurture n°3 (sécurité) |
| « Pas maintenant » | Noter une relance à 3 mois, rien avant |
| « Non » / « Stop » | Liste d'exclusion, immédiatement |

## Contrôle qualité avant envoi
- Lire l'email à voix haute : est-ce qu'un expert-comptable l'écrirait à un confrère ?
- Moins de 90 mots, une seule question, aucun lien dans l'email 1.
- « Vous » domine sur « nous ».
- Pas de « J'espère que vous allez bien », pas de « solution innovante », pas de « révolutionner ».
