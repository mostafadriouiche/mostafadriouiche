# Séquence texte simple avec vidéo (sans animation)

**Message central :** les outils de saisie automatique (OCR) lisent la facture. Owl lit la facture *et* le dossier du client (secteur, activité, régime de TVA), comme le ferait un comptable. Voir `../competitors-ocr.md`.

```
Format : texte brut, aucune image, aucune animation
Vidéo : un seul lien, jamais dans l'email 1
Envoi : lemlist (ou votre boîte Namecheap), 10–15 emails par jour au départ
Sortie : toute réponse arrête la séquence
Variables : {{prenom}} {{cabinet}} {{accroche}} {{lien_video}}
Règle : ne jamais citer un concurrent par son nom
```

`{{lien_video}}` = le lien de votre vidéo (YouTube non répertoriée, Vimeo, ou une page de thinkactionn.com). Jamais en pièce jointe.

**Signature (tous les emails) :**
```
Mostafa Driouiche
ThinkAction · Owl
Rue El Arrar, Bd Lalla El Yacout, 3e étage, Casablanca
Si ce n'est pas un sujet pour vous, répondez « non » et je ne vous relancerai pas.
```

---

## Email 1 : Jour 0 (aucun lien)

**Objet :** `saisie et tva`
*(variante à tester : `tva {{cabinet}}`)*

```
Bonjour {{prenom}},

{{accroche}}

Les outils de saisie automatique lisent une facture : date, fournisseur, montant, TVA. Ils ne savent pas si le client est un restaurant ou une entreprise de BTP, ni sous quel régime de TVA il déclare. Le choix des comptes et le contrôle de la TVA restent donc pour votre équipe.

Owl part du secteur et de l'activité de chaque client pour construire les écritures, et prépare la TVA en concordance avec la déclaration. Votre équipe vérifie, puis exporte vers votre logiciel habituel.

Est-ce que la saisie et la TVA prennent encore beaucoup de temps chez {{cabinet}} ?

Mostafa
```

Si `{{prenom}}` est vide : « Bonjour, ». Si `{{accroche}}` est vide : supprimez la ligne.

---

## Email 2 : Jour 3 (un cas concret, puis on propose la vidéo, sans lien)

**Objet :** `nouveau fournisseur`

```
Bonjour {{prenom}},

Un cas que vos collaborateurs connaissent : une facture d'un fournisseur que le client n'a jamais utilisé, avec deux taux de TVA.

Un outil qui apprend de l'historique n'a rien sur ce fournisseur. Il applique un compte par défaut, et votre équipe corrige à la main.

Owl raisonne à partir du dossier du client (son secteur, son activité, son régime de TVA). La première facture est donc traitée comme la centième.

J'ai une vidéo de 2 minutes qui le montre sur un vrai dossier. Je vous l'envoie ?

Mostafa
```

---

## Réponse « oui » : à envoyer à la main, dans l'heure

**Objet :** garder `RE:` (c'est une vraie réponse)

```
Bonjour {{prenom}},

Avec plaisir, voici la vidéo (2 minutes) :
{{lien_video}}

On y voit un dossier réel : Owl part de l'activité du client, construit les écritures sur tous les journaux et prépare la TVA. Ce qui prenait des heures prend quelques minutes.

Si vous voulez voir le résultat sur un de vos propres dossiers, je vous propose 20 minutes cette semaine : mardi à 10 h ou jeudi à 15 h ?

Mostafa
```

---

## Email 3 : Jour 8 (pour ceux qui n'ont pas répondu : le lien vidéo, une seule fois)

**Objet :** `lire ou comptabiliser`

```
Bonjour {{prenom}},

Pour voir la différence entre lire une facture et la comptabiliser, voici 2 minutes sur un vrai dossier, de la photo de la facture jusqu'à la TVA prête à déclarer :

{{lien_video}}

Une seule question m'intéresse : est-ce que les comptes proposés par Owl correspondent à ce que votre équipe aurait passé ?

Mostafa
```

---

## Email 4 : Jour 15 (le test sur leur facture la plus difficile, aucun lien)

**Objet :** `votre facture la plus difficile`

```
Bonjour {{prenom}},

Une proposition concrète : envoyez-moi, anonymisée, la facture qui pose le plus de problèmes à votre équipe. Un avoir, plusieurs taux de TVA, un fournisseur inconnu.

On la passe dans Owl ensemble en 20 minutes, et vous jugez les écritures vous-même.

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

## Réponses rapides aux questions fréquentes

**« On utilise déjà un outil de saisie automatique. »**
```
Très bien, il vous fait déjà gagner la frappe des montants. Owl va plus loin : il part du dossier client (secteur, activité, régime de TVA) pour proposer les comptes et préparer la TVA. Je vous montre la différence sur une facture d'un nouveau fournisseur ? 20 minutes suffisent.
```

**« Est-ce compatible avec notre logiciel ? »**
```
Oui. Votre équipe vérifie les écritures dans Owl, puis les exporte vers votre logiciel comptable habituel. Vous ne changez pas d'outil de production.
```

**« Peut-on l'essayer ? »**
```
Oui. L'essai démarre après la signature du contrat, et si Owl ne vous convient pas, vous pouvez résilier dans la semaine.
```

**« Et la sécurité des données ? »** → [TODO : hébergement, chiffrement, accès. Réponse à compléter avec des faits exacts.]

**« Quel est le prix ? »** → [TODO]

---

## Exemple complet : KAP Conseil (Marrakech)

```
Bonjour,

J'ai vu que KAP Conseil propose la déclaration de TVA à partir de 500 MAD par mois. À ce prix, chaque heure de saisie gagnée compte.

Les outils de saisie automatique lisent une facture : date, fournisseur, montant, TVA. Ils ne savent pas si le client est un restaurant ou une entreprise de BTP, ni sous quel régime de TVA il déclare. Le choix des comptes et le contrôle de la TVA restent donc pour votre équipe.

Owl part du secteur et de l'activité de chaque client pour construire les écritures, et prépare la TVA en concordance avec la déclaration. Votre équipe vérifie, puis exporte vers votre logiciel habituel.

Est-ce que la saisie et la TVA prennent encore beaucoup de temps chez KAP Conseil ?

Mostafa
ThinkAction · Owl
Rue El Arrar, Bd Lalla El Yacout, 3e étage, Casablanca
Si ce n'est pas un sujet pour vous, répondez « non » et je ne vous relancerai pas.
```
