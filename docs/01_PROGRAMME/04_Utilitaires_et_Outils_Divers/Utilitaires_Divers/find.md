---
title: find
date: 2024-07-12
tags:
  - ressource
  - bash
  - linux
  - programmation
  - scripts
  - programmes
status:
  - En cours
type de note:
  - ressource
référence:
  - "[[redirections]]"
  - "[[Substitution-de-commandes]]"
---

# Documentation de Base de `find`# [¶](https://agrellard.github.io/documentations_linux/commandes-de-base/utilitaires_divers/find/#documentation-de-base-de-find "Permanent link")

## 1. Syntaxe Générale : 
   ```bash
   find [chemin...] [option...] [expression de recherche...]
   ```
  - **chemin...** : Dossiers où commencer la recherche.
  - **expression** : Critères de recherche et actions.

### Paramètres

- **chemin...** : Spécifie le(s) répertoire(s) de départ pour la recherche. Si aucun chemin n'est donné, `find` utilise le répertoire courant par défaut.

### Options Principales d'Expression de Recherche

#### -name pattern
- Recherche des fichiers dont le nom correspond exactement au motif spécifié. Les caractères jokers comme `*` (remplace n'importe quelle chaîne de caractères) et `?` (remplace un seul caractère) peuvent être utilisés.
- Exemple : `find . -name "*.txt"` trouve tous les fichiers `.txt` dans le répertoire courant et ses sous-dossiers.

#### -iname pattern
- Comme `-name`, mais la recherche est insensible à la casse.
- Exemple : `find . -iname "readme.*"` trouvera "README.txt", "readme.md", "ReadMe.TXT", etc.

#### -type c
- Recherche des fichiers d'un type spécifié par `c`. Les valeurs courantes incluent `f` pour les fichiers réguliers, `d` pour les dossiers, et `l` pour les liens symboliques.
- Exemple : `find . -type d` liste tous les dossiers.

#### -size n[сwbkMG]
- Recherche des fichiers par taille. `n` peut être suivi par :
  - `c` pour les octets,
  - `w` pour les mots de deux octets,
  - `b` pour les blocs de 512 octets,
  - `k` pour les kilo-octets,
  - `M` pour les méga-octets,
  - `G` pour les giga-octets.
- Exemple : `find . -size +1M` trouve les fichiers de plus de 1 méga-octet.

#### -mtime n
- Recherche des fichiers modifiés il y a `n` * 24 heures. `+n` pour plus que `n` jours, `-n` pour moins.
- Exemple : `find . -mtime -7` trouve les fichiers modifiés dans les derniers 7 jours.

#### -user nomUtilisateur
- Recherche des fichiers appartenant à l'utilisateur spécifié.
- Exemple : `find . -user adrien` trouve tous les fichiers appartenant à "adrien".

#### -group nomGroupe
- Recherche des fichiers appartenant au groupe spécifié.
- Exemple : `find . -group adrien` trouve tous les fichiers appartenant au groupe "adrien".

#### -perm mode
- Recherche des fichiers avec les permissions spécifiées. Le mode peut être spécifié symboliquement ou en octal.
- Exemple : `find . -perm 644` trouve les fichiers avec des permissions `644`.

#### -exec commande {} \;
- Exécute une commande sur chaque fichier trouvé. `{}` est remplacé par le chemin du fichier trouvé.
- Exemple : `find . -type f -exec chmod 644 {} \;` change les permissions de tous les fichiers en `644`.
- `commande` est la commande que vous souhaitez exécuter sur chaque fichier ou dossier trouvé.
- `{}` est remplacé par le chemin du fichier ou du dossier trouvé par `find`.
- `\;` termine la commande que vous souhaitez exécuter avec `-exec`. Le backslash `\` est utilisé pour échapper le caractère `;`, car sans le backslash, le shell interpréterait `;` comme la fin de la commande `find` elle-même, et non comme une partie de l'argument pour `-exec`.

   En d'autres termes, `\;` est nécessaire pour faire comprendre au shell et à la commande `find` que la fin de la commande spécifiée avec `-exec` a été atteinte, et que ce n'est pas la fin de la commande `find` principale.


#### -ok commande {} \;
- Identique à `-exec`, mais demande une confirmation avant d'exécuter chaque commande.
- Exemple : `find . -type f -ok rm {} \;` demande avant de supprimer chaque fichier trouvé.

#### -prune
- Empêche `find` de descendre dans les sous-dossiers du dossier actuel s'il correspond au motif de recherche.
- Exemple : `find . -type d -name ".git" -prune -o -print` liste tous les fichiers et dossiers, en excluant les dossiers `.git` et leur contenu.

#### -delete
- Supprime les fichiers ou dossiers trouvés (avec prudence).
- Exemple : `find . -type f -name "*.bak" -delete` supprime tous les fichiers avec l'extension `.bak`.

### Autres Options Utiles

#### -ctime n
- Recherche des fichiers par leur "ctime" (le temps de changement du statut du fichier) les derniers `n` jours.
- Exemple : `find . -ctime -5` trouve les fichiers dont le statut a changé dans les 5 derniers jours.

#### -atime n
- Recherche des fichiers accédés dans les derniers `n` jours.
- Exemple : `find . -atime -2` trouve les fichiers qui ont été accédés dans les 2 derniers jours.

#### -depth
- Indique à `find` de traiter chaque répertoire après ses sous-dossiers. Utile pour les actions qui modifient la structure du dossier, comme supprimer.
- Exemple : `find . -depth -type d -empty -delete` supprime les dossiers vides.

#### -maxdepth levels
- Limite la recherche à une certaine profondeur de répertoires.
- Exemple : `find . -maxdepth 2 -name "*.txt"` cherche les fichiers `.txt` seulement jusqu'à 2 niveaux de profondeur.

#### -mindepth levels
- Ignore les niveaux de répertoires spécifiés au début de la recherche.
- Exemple : `find . -mindepth 2 -name "*.txt"` cherche les fichiers `.txt` en ignorant le répertoire courant et ses sous-dossiers immédiats.


### Combinaison d'Expressions

- **expression1 -a expression2** : Opérateur logique "ET", souvent omis car c'est le comportement par défaut.
- **expression1 -o expression2** : Opérateur logique "OU".
- **! expression** : Opérateur logique "NON".
- **\( expression \)** : Groupe des expressions pour contrôler l'ordre d'évaluation (les backslashes sont nécessaires pour échapper les parenthèses au shell).
### Utiliser la négation
L'argument `!` dans la commande `find` sous Linux est utilisé pour négationner une condition. En d'autres termes, il permet de trouver des fichiers ou des répertoires qui ne correspondent pas à un critère spécifique.

Voici quelques exemples concrets pour illustrer comment utiliser cet argument :

#### Exemple 1 : Trouver tous les fichiers sauf ceux avec une extension spécifique

Si vous voulez trouver tous les fichiers dans un répertoire sauf ceux avec l'extension `.txt`, vous pouvez utiliser la commande suivante :

```sh
find /path/to/directory ! -name "*.txt"
```

Dans cet exemple, `! -name "*.txt"` signifie que vous cherchez tous les fichiers dont le nom **ne correspond pas** au motif `*.txt`.

#### Exemple 2 : Trouver tous les fichiers sauf ceux d'une taille spécifique

Si vous voulez trouver tous les fichiers qui ne font pas exactement 1 Mo, vous pouvez utiliser la commande suivante :

```sh
find /path/to/directory ! -size 1M
```

Ici, `! -size 1M` signifie que vous cherchez tous les fichiers dont la taille **n'est pas** de 1 Mo.

#### Exemple 3 : Trouver tous les fichiers sauf ceux appartenant à un utilisateur spécifique

Si vous voulez trouver tous les fichiers qui n'appartiennent pas à l'utilisateur `john`, vous pouvez utiliser la commande suivante :

```sh
find /path/to/directory ! -user john
```

Dans ce cas, `! -user john` signifie que vous cherchez tous les fichiers qui **n'appartiennent pas** à l'utilisateur `john`.

#### Exemple 4 : Combiner plusieurs critères avec la négation

Vous pouvez également combiner plusieurs critères, y compris des négations. Par exemple, si vous voulez trouver tous les fichiers sauf ceux qui sont des fichiers vides et qui n'ont pas l'extension `.log`, vous pouvez utiliser :

```sh
find /path/to/directory ! -empty ! -name "*.log"
```

Ici, `! -empty` signifie que vous cherchez tous les fichiers qui **ne sont pas** vides, et `! -name "*.log"` signifie que vous cherchez tous les fichiers dont le nom **ne correspond pas** au motif `*.log`.


## 2. grouper des conditions ou des expressions : 

Les symboles `\( ... \)` dans une commande `find` sous Linux sont utilisés pour grouper des conditions ou des expressions. Le but est de contrôler l'ordre d'évaluation des expressions et de s'assurer que certaines opérations logiques sont effectuées ensemble, un peu comme les parenthèses sont utilisées en mathématiques pour grouper des nombres et des opérations.

Dans le contexte des commandes shell comme `find`, les parenthèses ont une signification spéciale et peuvent être interprétées par le shell avant que `find` ne les reçoive. Pour éviter cette interprétation précoce par le shell et s'assurer que les parenthèses sont passées à `find` comme partie de son expression de recherche, on les échappe avec un backslash `\`, d'où `\( ... \)`.

Par exemple, considérez la commande suivante :

```bash
find /chemin/ -type d \( -iname "*gsdata*" -o -iname "*tuto*" \) -prune -o -iname "*apprentissage*" -print
```

Ici, `\( ... \)` est utilisé pour grouper `-iname "*gsdata*" -o -iname "*tuto*"` comme une seule condition logique. Cela signifie que `find` évaluera cette condition en tant qu'unité, appliquant `-prune` aux dossiers qui correspondent soit à `*gsdata*`, soit à `*tuto*`. Sans ces parenthèses, l'ordre des opérations pourrait ne pas être celui que vous attendez, ce qui pourrait conduire à des résultats différents de ceux désirés.

En résumé, `\( ... \)` sert à :
- Grouper des conditions ou des expressions pour contrôler l'ordre d'évaluation.
- Assurer que les expressions groupées sont traitées comme une seule unité logique par la commande `find`.
- Éviter l'interprétation des parenthèses par le shell, en les échappant avec `\`.

## 3. Exclure par -iname ou -name
### version avec ((... -o ...)) -prune -o
```bash
find /media/adrien/data/programmation_code/_REVISIONS/ -type d \( -iname "*gsdata*" \) -prune -o -iname "*apprentissage*" -print
```
```bash
find /media/adrien/data/programmation_code/_REVISIONS/ -type d \( -iname "*gsdata*" -o -iname "*tuto*" \) -prune -o -iname "*apprentissage*" -print
```

Cette commande fonctionne comme suit :
- Elle commence par chercher dans le répertoire `/media/adrien/data/programmation_code/_REVISIONS/`.
- Elle utilise `-type d` pour limiter la recherche aux dossiers.
- La partie `\(... -o ... \) -prune` spécifie que si un dossier correspond soit au motif "*gsdata*" soit au motif "*tuto*", il sera exclu de la recherche (ne descend pas dans ces dossiers).
- L'option `-o` (qui signifie "ou") est ensuite utilisée pour séparer les conditions d'exclusion de la condition de recherche principale.
- La condition `-iname "*apprentissage*"` spécifie le motif de recherche pour les dossiers à inclure.
- `-print` s'assure que seuls les chemins correspondant à la condition "apprentissage*" sont affichés.

Cette commande va donc lister tous les dossiers qui contiennent "apprentissage" dans leur nom, tout en excluant ceux qui contiennent "gsdata" ou "tuto" dans leur nom, sans descendre dans ces derniers.
### version avec  grep
```bash
find /media/adrien/data/programmation_code/_REVISIONS/ -type d -iname "*apprentissage*" | grep -v gsdata
```
### version avec  !
```bash
find /media/adrien/data/programmation_code/_REVISIONS/ -type d ! -iname "*gsdata*" -a -iname "*apprentissage*" -print
```

# Exemples d'Utilisation de Base

## 1. **Trouver des Fichiers par Nom** :
   ```
   find /chemin -name 'nom_fichier'
   ```
## 2. **Recherche de Dossiers** :
   ```
   find /chemin -type d -name 'nom_dossier'
   ```
## 3. **Recherche par Taille de Fichier** :
   ```
   find /chemin -size +50M
   ```
## 4. **Recherche par Date de Modification** :
   ```
   find /chemin -mtime -7
   ```

# Utilisation avec Pipe pour Afficher la Taille

## 1. **Taille des Fichiers Trouvés** :
   ```
   find /chemin -type f -exec du -h {} +
   ```
## 2. **Taille des Dossiers Trouvés** :
   ```
   find /chemin -type d -exec du -sh {} +
   ```

# Autres Exemples Courants

## 1. **Trouver et Supprimer** :
   ```
   find /chemin -type f -name 'nom_fichier' -exec rm {} +
   ```
## 2. **Trouver et Compresser** :
   ```
   find /chemin -type f -name '*.log' -exec gzip {} +
   ```

### Autres Exemples avec Pipe

## 1. **Lister et Trier par Taille** :
   ```
   find /chemin -type f -exec ls -lh {} + | sort -k 5 -h
   ```
## 2. **Trouver et Afficher le Contenu** :
   ```
   find /chemin -type f -name 'nom_fichier' -exec cat {} \; | less
   ```

# Commandes utiles
   ```bash
   find /path -iname "*.avi"  -type f -size +100M -size -1000M -exec du -sh {} \; | awk -F/ 'tolower($NF) ~ /^/' | sort -nr

   find / -iname "*.avi" -iname "*dri*" -type f -size +100M -size -1000M -exec du -sh {} \; |  awk -F/ 'tolower($NF) ~ /^t/'| awk -F "/" '{print $1"- "$9}'  | sort -nr

   find / -iname "*.avi" -iname "*ToPia*" -type f -size +100M -size -1000M -exec du -sh {} \; | awk -F "/" '{print $1"- "$9}'  | sort -nr 

   find -name "*.js" -not -path "./directory/*"

   du -a -BM --max-depth=1 / |sort -nr | head -20
   
   find /  -type d -iname "*_0_docu*" -iname "*linux" -exec find {} -type f -iname "*md" -mtime -2  \; | sort > result.txt                                                                                                     
   cat result.txt | xargs l -lh | awk -F: '{print $1 $2}'

   find / -type d \( -iname "*gsdata*" -iname "docu" -prune  \) -o \( -iname "*apprentissage*" -print \)