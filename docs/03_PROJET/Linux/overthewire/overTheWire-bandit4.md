---
title: overTheWire
date: 2024-07-27
date de modification: 2024-07-27
timestamp: 16:54
tags:
  - projet
  - linux
  - bash
  - programmation
  - informatique
status:
  - En cours
type de note:
  - projet
référence:
  - "[[find]]"
auteur: aGrellard
---
# overTheWire

## overTheWire - bandit4 - find passwd

Pour trouver le flag contenant la clé SSH pour le prochain niveau, voici la clé du niveau actuel : `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`.

### Commandes initiales

```bash
bandit4@bandit:~$ ls -lshaR
.:
total 24K
4.0K drwxr-xr-x  3 root root 4.0K Jul 17 15:57 .
4.0K drwxr-xr-x 70 root root 4.0K Jul 17 15:58 ..
4.0K -rw-r--r--  1 root root  220 Mar 31 08:41 .bash_logout
4.0K -rw-r--r--  1 root root 3.7K Mar 31 08:41 .bashrc
4.0K drwxr-xr-x  2 root root 4.0K Jul 17 15:57 inhere
4.0K -rw-r--r--  1 root root  807 Mar 31 08:41 .profile

./inhere:
total 48K
4.0K drwxr-xr-x 2 root    root    4.0K Jul 17 15:57 .
4.0K drwxr-xr-x 3 root    root    4.0K Jul 17 15:57 ..
4.0K -rw-r----- 1 bandit5 bandit4   33 Jul 17 15:57 -file00
4.0K -rw-r----- 1 bandit5 bandit4   33 Jul 17 15:57 -file01
4.0K -rw-r----- 1 bandit5 bandit4   33 Jul 17 15:57 -file02
4.0K -rw-r----- 1 bandit5 bandit4   33 Jul 17 15:57 -file03
4.0K -rw-r----- 1 bandit5 bandit4   33 Jul 17 15:57 -file04
4.0K -rw-r----- 1 bandit5 bandit4   33 Jul 17 15:57 -file05
4.0K -rw-r----- 1 bandit5 bandit4   33 Jul 17 15:57 -file06
4.0K -rw-r----- 1 bandit5 bandit4   33 Jul 17 15:57 -file07
4.0K -rw-r----- 1 bandit5 bandit4   33 Jul 17 15:57 -file08
4.0K -rw-r----- 1 bandit5 bandit4   33 Jul 17 15:57 -file09
```

### Recherche des fichiers

Pour rechercher de manière récursive tous les fichiers dont le nom contient le motif `-file`, utilisez la commande suivante :

```bash
find . -type f -iname "*-file*" -exec cat {} +
```

```bash
bandit4@bandit:~$ find . -type f -iname "*-file*" -exec cat {} +
��,��▒����Yq��f�L���j▒�0�����x�4F�����n�Qy��y�{+R�bZ�k�F�*      ʧh?+>����R0\��q�c��(|�^��9�������F��p�������tk���%��
N�.��4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw5K���p�    X
�QĹ�M���p4�-�8��=��!#g�����pӻT9�F�����3ˤ�����)
��$}P�cL���s��@�2%Y�

```
### Explications des options

- `-type` spécifie le type d'élément à rechercher :
  - `-type f` ne recherche que des fichiers.
  - `-type d` ne recherche que des dossiers.
- `-iname` spécifie le nom de l'élément à rechercher, insensible à la casse :
  - `"*motif*"` correspond à zéro ou plusieurs caractères avant et après le motif.
    - Par exemple, `-iname "*log*"` peut correspondre à : `"logfile"`, `"mylog.txt"`, `"catalog"`, `"dialog"`, etc.
- `-exec` ([[find-exec_sh]]) est une option de **[[find]]** qui permet d'exécuter une commande spécifiée pour chaque fichier trouvé :
  - `cat` est la commande à exécuter sur le fichier.
  - `{}` est remplacé par le chemin du fichier trouvé par **find**.
  - `+` indique que **cat** sera exécuté une seule fois pour tous les fichiers trouvés, regroupant les chemins des fichiers dans une seule commande.

### Améliorations

Pour **affiner les résultats** nous pouvons afficher un saut de ligne après chaque lecture d'un fichier, pour ce faire nous exécuterons plusieurs commandes avec `-exec`
### Exécution de plusieurs commandes

Pour exécuter plusieurs commandes sur chaque fichier trouvé, nous pouvons utiliser `sh` (l'interpréteur de commandes) avec l'option `-c`. Cela permet de créer un nouveau shell pour exécuter les commandes. Nous avons besoin de l'option `-c` qui indique que ce qui suit est une chaîne de commandes à exécuter.

Ensuite, nous devons spécifier les arguments à passer au shell. Dans une commande shell ou un script, `$0` représente le nom du script. Pour éviter tout problème et passer les bons arguments à notre commande, nous utiliserons un placeholder `_` pour `$0`, et ensuite `{}` qui remplace le chemin du fichier.

Voici un exemple de commande qui affiche le contenu de chaque fichier et ajoute une ligne vide après chaque fichier :

```bash
find . -type f -iname "*-file*" -exec sh -c 'cat "$1" && echo ""' _ {} \;
```

### Explication des arguments de `sh`

- `sh -c` lance un nouveau shell et exécute les commandes spécifiées.
- `'cat "$1" && echo ""'` est la chaîne de commandes à exécuter. `"$1"` représente le chemin du fichier trouvé.
- `_` est un placeholder pour `$0`, qui est requis par `sh -c`.
- `{}` est remplacé par le chemin du fichier trouvé par **find**.
- `\;` indique la fin de la commande `-exec`.

### Résultat de la commande

Voici la sortie de la commande :

```bash
bandit4@bandit:~$ find . -type f -iname "*-file*" -exec sh -c 'cat $1 && echo ""' _ {} \;
��,��▒����Yq��f�L���j▒�0�����x�4F
�����n�Qy��y�{+R�bZ�k�F�*
ʧh?+>����R0\��q�c��(|�^��
��9�������F��p�������tk���%��

l�����]�a-@gQ�÷�wz�P��ߠy�
N�.��>�3k�v�5K���p�     X
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

�QĹ�M���p4�-�8��=��!#g����
�pӻT9�F�����3ˤ�����)
T�՜F�ǭ�
��$}P�cL���s��@�2%Y�
                    ы�Ϣ��

```

Ce résultat montre que le contenu des fichiers contient des données binaires ou non lisibles. 

### Améliorations

**Trouver le password utilisateur**

a voir : [[clé ssh]]

### Caractères Autorisés pour les Mots de Passe

#### Linux

Sur les systèmes Linux, les caractères autorisés pour les mots de passe utilisateurs sont généralement très flexibles. En pratique, presque tous les caractères peuvent être utilisés, y compris :

- Lettres minuscules (`a-z`)
- Lettres majuscules (`A-Z`)
- Chiffres (`0-9`)
- Caractères spéciaux et de ponctuation (par exemple : `!@#$%^&*()-_=+[]{}|;:'",.<>?/`~`)
- Espaces

#### Tableau des Caractères

| Caractère | Code ASCII | Description              |
|-----------|-------------|--------------------------|
| !         | 33          | Point d'exclamation      |
| @         | 64          | A commercial             |
| #         | 35          | Dièse                    |
| $         | 36          | Signe dollar             |
| %         | 37          | Pourcentage              |
| ^         | 94          | Accent circonflexe       |
| &         | 38          | Esperluette              |
| *         | 42          | Astérisque               |
| (         | 40          | Parenthèse ouvrante      |
| )         | 41          | Parenthèse fermante      |
| -         | 45          | Tiret                    |
| _         | 95          | Soulignement             |
| =         | 61          | Égal                     |
| +         | 43          | Plus                     |
| [         | 91          | Crochet ouvrant          |
| ]         | 93          | Crochet fermant          |
| {         | 123         | Accolade ouvrante        |
| }         | 125         | Accolade fermante        |
| |         | 124         | Barre verticale          |
| ;         | 59          | Point-virgule            |
| :         | 58          | Deux-points              |
| '         | 39          | Apostrophe               |
| "         | 34          | Guillemets               |
| ,         | 44          | Virgule                  |
| .         | 46          | Point                    |
| <         | 60          | Inférieur                |
| >         | 62          | Supérieur                |
| ?         | 63          | Point d'interrogation    |
| /         | 47          | Barre oblique            |
| ~         | 126         | Tilde                    |
| `         | 96          | Accent grave             |
| )         | 41          | Parenthèse fermante (répétée) |

### Expression

Sachant cela nous pourrions utiliser un **expression régulière** qui dirait que la chaîne de caractères doit commencer et se terminer par un ou plusieurs caractères imprimable.

- `^` **ancrage** qui représente le **début** d'une ligne
- `[]` définit une **classe de caractères**, une classe de caractères correspond à n'importe quel caractères parmi ceux spécifiés a l'intérieur des crochets. Les classes de caractères peuvent inclure des caractères individuels, des plages de caractères, des classes POSIX, et peuvent être négatives pour exclure certains caractères.
- `[:print:]` classe POSIX qui correspond a n'importe quel caractères (y compris l'éspace)
- `+` **quantificateur** qui indique 1 ou plusieurs occurrences du motif précédent
- `*` **quantificateur** 0, 1 ou plusieurs occurrences du motif précédent
- `$` **ancrage** qui représente la **fin** d'une ligne

Nous pourrions utiliser `grep` avec l'option `-E` qui permet d'utiliser les expressions régulières.

```bash
grep -E "^[[:print:]]+$" file.txt
```

### Commande pour trouver un passwd en clair

```bash
find . -type f -iname "*-file*" -exec sh -c 'grep -E "^[[:print:]]+$" $1' _ {} \;
```

```bash
bandit4@bandit:~$ find . -type f -iname "*-file*" -exec sh -c 'grep -E "^[[:print:]]+$" "$0" && echo "";' {} \;
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

```

## overTheWire - bandit5 - find passwd

Améliorons notre commande : 

```bash
find . -type f -exec sh -c 'grep -E "^[[:print:]]{10,64}$" $1 2>/dev/null | grep -v " " && echo ""' _ {} \;

```

`{10,64}` Les **quantificateurs** `{min,max}` permettent de spécifier une nombre de caractères **minimum** et **maximum** pour le motif précédent.
`2>/dev/null` **Redirige** la **sortie d’erreurs** ver le fichier spécial **/dev/null**
`|` pipe de la sortie de  `grep -E "^[[:print:]]{10,64}$" $1 2>/dev/null`
`grep -v " "` l'option `-v` indique a *grep* de renvoyer les lignes **ne** correspondent **pas** au motif suivant .
`&&` **chainer** la commande si la commande de l'opérande de gauche réussi 
`echo ""` ajoute un ligne vide

Sortie :

```bash
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

HISTCONTROL=ignoreboth
HISTSIZE=1000
HISTFILESIZE=2000
#force_color_prompt=yes
xterm*|rxvt*)

```