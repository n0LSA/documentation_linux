---
title: les expression régulière
date: 2024-07-28
date de modification: 2024-07-28
timestamp: 12:49
tags:
  - projet
  - linux
  - programmation
  - bash
status:
  - En cours
type de note:
  - projet
référence:
  - "[regex](../../../langages/awk/regex.md)"
auteur: aGrellard
source:
  - https://www.arthurperret.fr/cours/expressions-regulieres.html
  - https://www.pierre-giraud.com/javascript-apprendre-coder-cours/regex-point-alternative-ancre-quantificateur/
---
## Introduction

Les expressions régulières, ou "*regex*", sont des outils puissants utilisés pour trouver des **motifs** spécifiques dans des textes. Imaginez une expression régulière comme un **modèle** que vous donnez à un moteur de recherche pour qu'il trouve des correspondances dans un texte.

Contrairement à une simple recherche de mots ou de phrases, les expressions régulières utilisent des *caractères spéciaux* pour définir des *motifs*. Ces caractères spéciaux ont des rôles spécifiques et constituent la syntaxe des regex. Cette syntaxe permet de créer des motifs de recherche précis, sans se soucier de la signification des mots.

Les moteurs d'expressions régulières interprètent ces motifs et les utilisent pour chercher des correspondances dans des textes. On peut utiliser ces moteurs via des logiciels avec une interface graphique (comme une fenêtre de recherche) ou via une interface en ligne de commande (comme des langages de programmation, des scripts ou des commandes shell).

En résumé, les expressions régulières sont des outils flexibles pour trouver des motifs dans des textes, basés sur une syntaxe de caractères spéciaux, et peuvent être utilisées aussi bien avec des interfaces graphiques qu'en ligne de commande.

Il existe **plusieurs [interpreteurs](interpreteurs.md)** capable d'utiliser les expression régulière, ceux-ci utilisent leur propre *type d'expression* (souvent basé sur **PCRE**, **ERE**, ...)  

Plusieurs types d'expression existe (ERE, PCRE, ..) 

---

Chaque **caractère** et une *expression régulière.* `ad` est une correspondance pour `adrien` . n'importe quel caractères a l'exception de caractères spéciaux : les **Métacaractères**.

`*` `.` `+` `^` `[]` `?` `()` `|` `\` `{}`

## Memo

- **[[grep]]**
	- `-o` affiche uniquement les correspondances trouvées, plutôt que les lignes entières contenant les correspondances.
	- `-P` utilise les expression régulière Perl (Perl-Compatible Regular Expressions, **PCRE**)
	- `-E` utilise les expression régulière (Extend Regular Expression, **ERE**)
	- `-i` insensible a la casse

- Cheat-Sheet
	- [nikiongstone](https://github.com/niklongstone/regular-expression-cheat-sheet)

## le point `.`

`.` permet de rechercher n'importe qu'elle caractères, sauf une nouvelle ligne. pour rechercher le littéral `.` il faudra l'échapper : `\.`

### exemples
```bash
chaine='Bonjour, je suis ^Pierre^. Mon no. est le [06-36-65-65-65]'
```

```
echo "$chaine" | grep -oP "o."
```

```bash
╭─adrien@adrien-MS-7917 /tmp 
╰─$ echo "$chaine" | grep -oP "o."                                                                                             
on
ou
on
o.

```

## Le ou logique `|`

`|` va permettre de créer des masques qui vont pouvoir chercher une séquence de caractères ou une autre.

### exemples
```bash
chaine='Bonjour, je suis ^Pierre^. Mon /numéro/ est le [06-36-65-65-65]'
```


```bash
╭─adrien@adrien-MS-7917 /tmp 
╰─$ echo "$chaine" | grep -ioP "pierre|mathilde"                                                     1 ↵
Pierre

╭─adrien@adrien-MS-7917 /tmp 
╰─$ echo "$chaine" | grep -ioP "o|j"            
o
j
o
j
o
o
```


## Les ancres

### Ancre `^` (Début de ligne). 

l'orsqu `^` est utilisé en dehors d'une classe il indique que l'on va rechercher le caractère suivant en début de ligne
#### Fonctionnement

- **Position** : L'ancre `^` correspond au début d'une ligne.
- **Procédure** :
  1. La regex commence à analyser la chaîne à la position initiale (début de la chaîne).
  2. Si le premier caractère de la chaîne satisfait le reste de l'expression régulière après `^`, il y a une correspondance.
  3. Sinon, il n'y a pas de correspondance, car `^` ne peut correspondre qu'au début de la ligne.

#### Exemple

Expression : `^abc`

Chaîne : "abc def abc"

- Correspondance : "abc" au début de la chaîne.

```bash
echo "abc def abc" | grep -E "^abc"
```

### Ancre `$` (Fin de ligne)

a l'inverse `$` va pouvoir rechercher la présence du caractère précédent en fin de ligne

#### Fonctionnement

- **Position** : L'ancre `$` correspond à la fin d'une ligne.
- **Procédure** :
  1. La regex commence à analyser la chaîne à partir de la fin.
  2. Si les caractères précédant la fin de la chaîne satisfont le reste de l'expression régulière avant `$`, il y a une correspondance.
  3. Sinon, il n'y a pas de correspondance, car `$` ne peut correspondre qu'à la fin de la ligne.

#### Exemple

Expression : `abc$`

Chaîne : "def abc abc"

- Correspondance : "abc" à la fin de la chaîne.

```bash
echo "def abc abc" | grep -E "abc$"
```

### Ancre `\b` (Frontière de mot)

**`\b`** Frontière de mots, correspond à une positon d'un caractère de mot (`\w` `[a-zA-Z0-9_]`) et à un non-caractère de mot (\W), on utilise `\b` pour trouver des mot entier. 

la procédure de détection de `\b` consiste a vérifier chaque position dans la chaîne pour identifier une frontière de mot, en fonction des transitions entre les caractères de mot et non-mots.

#### Fonctionnement

- **Position** : L'ancre `\b` correspond à une frontière de mot, où il y a un changement entre un caractère de mot (lettres, chiffres, underscore) et un caractère non-mot (tout le reste).
- **Procédure** :
  1. La regex commence à analyser la chaîne depuis le début.
  2. À chaque position, elle vérifie s'il y a une transition entre un caractère de mot et un caractère non-mot.
  3. Si une telle transition est détectée, et si le reste de l'expression régulière correspond à cette position, il y a une correspondance.

- Chaîne : "abc 123 a1b2c3 z0y1x2"
- Expression : `\b[a-z-A-Z]`
1. **Position initiale (avant `a` dans "abc")** :
    - Caractère actuel : `a`
    - Caractère précédent : début de chaîne (considéré comme un caractère non-mot)
    - Frontière de mot détectée : Oui (début de chaîne)
    - Appliquez `[a-zA-Z]` : correspond à `a`
2. **Position entre `a` et `b`** :
    - Caractère actuel : `b`
    - Caractère précédent : `a`
    - Frontière de mot détectée : Non (deux caractères de mot adjacents)
    - Déplacez le curseur
3. **Position entre `b` et `c`** :
    - Caractère actuel : `c`
    - Caractère précédent : `b`
    - Frontière de mot détectée : Non (deux caractères de mot adjacents)
    - Déplacez le curseur
4. **Position après `c` et avant l'espace** :
    - Caractère actuel : espace
    - Caractère précédent : `c`
    - Frontière de mot détectée : Oui (changement de caractère de mot à caractère non-mot)
    - Appliquez `[a-zA-Z]` : ne correspond pas (l'espace n'est pas `[a-zA-Z]`)

#### Exemple

Expression : `\babc\b`

Chaîne : "abc def abc"

- Correspondance : "abc" et "abc" comme mots individuels.

```bash
echo "abc def abc" | grep -E "\babc\b"
```

### Ancre `\B` (Non-frontière de mot)

**`\B`** Non-Frontière de mots, correspond à une position ou il n'y a pas de frontière de mot. Utilisé pour recherché des mots isolé, des correspondance qui ne sont pas des mots entiers.

#### Fonctionnement

- **Position** : L'ancre `\B` correspond à une position qui n'est pas une frontière de mot.
- **Procédure** :
  1. La regex commence à analyser la chaîne depuis le début.
  2. À chaque position, elle vérifie qu'il n'y a pas de transition entre un caractère de mot et un caractère non-mot.
  3. Si cette condition est satisfaite, et si le reste de l'expression régulière correspond à cette position, il y a une correspondance.

#### Exemple

Expression : `\Babc\B`

Chaîne : "xabcx"

- Correspondance : "abc" à l'intérieur de "xabcx".

```bash
echo "xabcx" | grep -E "\Babc\B"
```
### Exemples ancres

```bash
chaine='Bonjour, je suis Pierre a^$b. Mon no. est le [06-36-65-65-65]'
```

#### L'ancre carre (`^`)

N'import quel caractère en début de chaîne sauf `\n`

```bash
echo "$chaine" | grep -ioP "^."
```

```
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "$chaine" | grep -ioP "^."
B
```

Une lettre majuscule en début de chaîne

```bash
echo "$chaine" | grep -oP "^[A-Z]"
```

```
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "$chaine" | grep -oP "^[A-Z]" 
B
```

#### L'ancre Dollar (`$`)

```bash
echo "hello world" | grep -oE "world$"
```

```
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "hello world" | grep -oE "world$"
world
```

```bash
echo "worldwide" | grep -oE "world$"
```

```
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "worldwide" | grep -oE "world$"

```

#### `^` et `$`

```bash
chaine='Bonjour, je suis Pierre a^$b. \nMon no. est le [06-36-65-65-65]'  
```

Traiter chaque ligne spéarément

```bash
echo "$chaine" | grep -oE "^.*$" 
```

```bash
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "$chaine" | grep -oE "^.*$"                           
Bonjour, je suis Pierre a^$b. 
Mon no. est le [06-36-65-65-65]
```

avec `awk`

```bash
echo "$chaine" | grep -oE "^.*$" | awk '{print "ligne N°"NR" = "$0}' 
```

```
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "$chaine" | grep -oE "^.*$" | awk '{print "ligne N°"NR" = "$0}'                
ligne N°1 = Bonjour, je suis Pierre a^$b. 
ligne N°2 = Mon no. est le [06-36-65-65-65]
```

avec `read`

```bash
echo "$chaine" | grep -oE "^.*$" | while IFS= read -r line; do echo "$line"
```

```
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "$chaine" | grep -oE "^.*$" | while IFS= read -r line; do echo "$line"; done   130 ↵
Bonjour, je suis Pierre a^$b. 
Mon no. est le [06-36-65-65-65]
```

```bash
echo "$chaine" | grep -oE "^.*$" | while IFS= read -r line; do echo "$line" | wc -m; done
```

```
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "$chaine" | grep -oE "^.*$" | while IFS= read -r line; do echo "$line" | wc -m; done
31
32
```

#### L'ancre frontière de mots (`\b`)

```bash
echo "amant" | grep -E "\ba"
```

```bash
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "amant" | grep -E "\ba"                                                        
amant
^||||
```

```bash
echo category | grep -E "\bcat\b"
```

```bash
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "category" | grep -E "\bcat\b"

╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "cat-egory" | grep -E "\bcat\b"                                               
cat-egory
^^^||||||
```

```bash
echo "amouranth" | grep -E "\bamour"
```

```bash
╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "amouranth" | grep -E "\bamour"
amouranth
^^^^^||||

╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "amouranth" | grep -oE "\bamour"
amour

╭─adrien@adrien-MS-7917 ~/Documents/_I0_DOCU_EXT/mk-docs 
╰─$ echo "amouranth destroy the twitch game" | grep -oE "\bamour\w*\b"
amouranth
```

#### L'ancre non-frontière de mots (`\B`)


## Quantitificateurs

- `*` zero ou plusieurs occurrences 
- `+` une ou plusieurs occurrences 
- `?` Zero ou une occurrences
- `{}` Permet de spécifier un nombre précis d’occurrences du motif précédent
	- `{n}` Exactement `n` occurrences
	- `{n,}` Au moins `n` occurrences
	- `{n,m}` Entre `n` occurrences et `m` occurrences


## Exemples Quantitificateurs

## Le Quantitificateur `*`

```bash
chaine='Bonjour, je suis Pierre123 du abepierreBai a^$b. \nMon no. est le [06-36-65-65-65]'
```

```bash
echo "$chaine" | grep -P "\b[[:alpha:]]*er[[:alpha:]]*\b[^-]"
```

- `\b` commence et termine par une frontière de mot, pour s'assurer que l'occurrence est un mot complet
- `[[:alpha:]]*`
	- `[[:alpha:]]` classe **POSIX** (`[a-zA-Z]`)
	- `*` zéro ou plusieurs occurrences du caractère précédent
	- `[[:alpha:]]*` Recherche zéro ou plusieurs lettres alphabétiques.
- `er` recherche la séquence er
- `[^-]` : le caractère suivant (juste après le mot) ne doit pas être un tiret '-'.

Sortie :

```bash
Bonjour, je suis Pierre123 du abepierreBai a^$b.
                              ^^^^^^^^^^^^
```

```bash
chaine='Bonjour, je suis Pierre123 du abepierre-Bai a^$b. \nMon no. est le [06-36-65-65-65]'
```

```bash
echo "$chaine" | grep -P "\b[[:alpha:]]*er[[:alpha:]]*\b[^-]"
```

Sortie :

```bash
NULL
```
### Exemple `{n}`

```sh
echo "aaa ab aab aaab" | grep -Po "a{3}"
```

**Explication** : Cherche exactement trois `a` consécutifs.

**Résultat** : 
```
aaa
aaa
```

### Exemple 2 `{n,}`

```sh
echo "aaa ab aab aaab" | grep -Po "a{2,}"
```

**Explication** : Cherche au moins deux `a` consécutifs.

**Résultat** : 
```
aaa
aa
aaa
```

### Exemple 3 `{n,m}`

```sh
echo "aaa ab aab aaab" | grep -Po "a{2,3}"
```

**Explication** : Cherche au moins deux mais pas plus de trois `a` consécutifs.

**Résultat** : 
```
aaa
aa
aaa
```

## classes

- `[]`
- `\`
- `()`

- `\`

