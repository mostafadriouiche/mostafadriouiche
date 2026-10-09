# Séquence texte simple avec vidéo (sans animation)

```
Format : texte brut, aucune image, aucune animation
Vidéo : un seul lien, jamais dans l'email 1
Envoi : lemlist (ou votre boîte Namecheap), 10–15 emails par jour au départ
Sortie : toute réponse arrête la séquence
Variables : {{prenom}} {{cabinet}} {{accroche}} {{lien_video}}
```

`{{lien_video}}` = le lien de votre vidéo (YouTube non répertoriée, Vimeo, ou une page de thinkactionn.com). Mettez la vidéo sur une page, jamais en pièce jointe.

**Signature (tous les emails) :**
```
Mostafa Driouiche
ThinkAction · Owl
[Adresse postale de la société]
Si ce n'est pas un sujet pour vous, répondez « non » et je ne vous relancerai pas.
```

---

## Email 1 : Jour 0 (aucun lien)

**Objet :** `tva {{cabinet}}`

```
Bonjour {{prenom}},

{{accroche}}

Dans beaucoup de cabinets, chaque échéance de TVA veut encore dire des heures de ressaisie, avec un régime différent à vérifier pour chaque dossier.

Owl part de l'activité et du régime de TVA de chaque client pour générer les écritures comptables et préparer la déclaration. Vos collaborateurs n'ont plus qu'à contrôler et valider.

Est-ce que c'est un sujet chez {{cabinet}} en ce moment ?

Mostafa
```

Si `{{prenom}}` est vide : « Bonjour, ». Si `{{accroche}}` est vide : supprimez la ligne.

---

## Email 2 : Jour 3 (on propose la vidéo, sans lien)

**Objet :** `erreur de régime`

```
Bonjour {{prenom}},

Une erreur fréquente en saisie : un dossier change de régime de TVA en cours d'année, et le paramétrage ne suit pas. L'écart se découvre au moment de la déclaration, ou lors d'un contrôle.

Owl relit le régime et l'activité de chaque client avant de générer les écritures.

J'ai une vidéo de 2 minutes qui montre un dossier traité de bout en bout, des factures à la déclaration de TVA. Je vous l'envoie ?

Mostafa
```

---

## Réponse « oui » : à envoyer à la main, dans l'heure

**Objet :** garder `RE:` (c'est une vraie réponse)

```
Bonjour {{prenom}},

Avec plaisir, voici la vidéo (2 minutes) :
{{lien_video}}

On y voit un dossier réel : Owl lit l'activité et le régime de TVA, génère les écritures et prépare la déclaration.

Si vous voulez voir le résultat sur un de vos propres dossiers, je vous propose 20 minutes cette semaine : mardi à 10 h ou jeudi à 15 h ?

Mostafa
```

---

## Email 3 : Jour 8 (pour ceux qui n'ont pas répondu : le lien vidéo, une seule fois)

**Objet :** `2 minutes sur un dossier`

```
Bonjour {{prenom}},

Plutôt qu'une longue explication, voici une vidéo de 2 minutes : un dossier client traité dans Owl, des factures jusqu'à la déclaration de TVA.

{{lien_video}}

Si vous la regardez, j'aimerais savoir si ce fonctionnement correspond à la façon dont {{cabinet}} travaille.

Mostafa
```

---

## Email 4 : Jour 15 (essai sur un vrai dossier, aucun lien)

**Objet :** `un dossier test`

```
Bonjour {{prenom}},

Une proposition concrète : vous choisissez un dossier client (anonymisé si vous préférez), on le passe dans Owl, et vous comparez les écritures et la préparation de TVA avec ce que votre équipe a produit.

20 minutes de votre côté, et vous jugez sur votre propre dossier.

Ça vous tente ?

Mostafa
```

---

## Email 5 : Jour 22 (dernier email)

**Objet :** `je clôture`

```
Bonjour {{prenom}},

Sans retour de votre part, je suppose que ce n'est pas le bon moment, et je m'arrête là.

Répondez juste par un chiffre :
1 : intéressé, parlons-en
2 : pas maintenant, revenez vers moi dans 3 mois
3 : pas intéressé, merci de ne plus m'écrire

Bonne fin d'échéance,
Mostafa
```

---

## Comment chaque email est personnalisé

Le seul champ qui change vraiment d'un cabinet à l'autre est `{{accroche}}` : une phrase vraie, tirée du site du cabinet, qui mène au sujet de la TVA. Elle est déjà remplie dans `../prospects/cabinets-maroc-tous.csv` pour les cabinets où le site donne un détail concret. Exemple pour KAP Conseil (Marrakech) :

```
Bonjour,

J'ai vu que KAP Conseil propose la déclaration de TVA à partir de 500 MAD par mois. À ce prix, chaque heure de saisie gagnée compte.

Dans beaucoup de cabinets, chaque échéance de TVA veut encore dire des heures de ressaisie, avec un régime différent à vérifier pour chaque dossier.

Owl part de l'activité et du régime de TVA de chaque client pour générer les écritures comptables et préparer la déclaration. Vos collaborateurs n'ont plus qu'à contrôler et valider.

Est-ce que c'est un sujet chez KAP Conseil en ce moment ?

Mostafa
```
