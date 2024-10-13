---
title: expressions régulières - les interpréteurs
date: 2024-08-02
tags:
  - ressource
status:
  - En cours
type de note:
  - ressource
source:
  - chatgpt
---
# Les interpréteurs des expressions régulières

De nombreux moteurs et langages de programmation sont capables d’interpréter les expressions régulière.

Chaque langage peut avoir son propre interpréteur d'expressions régulières, avec des variation pour la syntaxe et fonctionnalités.



### Outils et Utilitaires

1. **grep** :
    
    - **Types d'expressions** :
        - **POSIX Basic Regular Expressions (BRE)** : Par défaut.
        - **POSIX Extended Regular Expressions (ERE)** : Avec l'option `-E` ou `--extended-regexp`.
        - **Perl Compatible Regular Expressions (PCRE)** : Avec l'option `-P` ou `--perl-regexp`.
    - **Exemples** :
        - BRE : `grep 'pattern' file.txt`
        - ERE : `grep -E 'pattern' file.txt`
        - PCRE : `grep -P 'pattern' file.txt`
2. **sed** :
    
    - **Types d'expressions** :
        - **POSIX Basic Regular Expressions (BRE)** : Par défaut.
        - **POSIX Extended Regular Expressions (ERE)** : Avec l'option `-E` ou `-r` (selon les versions).
    - **Exemples** :
        - BRE : `sed 's/pattern/replacement/' file.txt`
        - ERE : `sed -E 's/pattern/replacement/' file.txt`
3. **awk** :
    
    - **Types d'expressions** :
        - **POSIX Basic Regular Expressions (BRE)** : Par défaut.
        - **POSIX Extended Regular Expressions (ERE)** : Utilisation implicite, ou via des options spécifiques dans certaines versions (`--re-interval`).
    - **Exemple** :
        - `awk '/pattern/ { print $0 }' file.txt`
4. **vim** :
    
    - **Types d'expressions** :
        - **Expressions régulières de Vim** : Basées sur POSIX, avec des extensions spécifiques à Vim.
    - **Exemples** :
        - Recherche : `/pattern`
        - Remplacement : `:%s/pattern/replacement/g`
5. **Notepad++** :
    
    - **Types d'expressions** :
        - **Scintilla Regular Expressions** : Basées sur PCRE (Perl Compatible Regular Expressions).
    - **Exemple** :
        - Recherche : `Ctrl + F`, puis onglet "Expression régulière"
6. **Visual Studio Code** :
    
    - **Types d'expressions** :
        - **JavaScript Regular Expressions** : Basées sur ECMAScript (JavaScript).
    - **Exemple** :
        - Recherche : `Ctrl + F`, puis cocher "Use Regular Expression"

### Bases de Données

1. **PostgreSQL** :
    
    - **Types d'expressions** :
        - **POSIX Regular Expressions** : Support pour les expressions régulières case-sensitive et case-insensitive.
    - **Exemples** :
        - Case-sensitive : `SELECT * FROM table WHERE column ~ 'pattern';`
        - Case-insensitive : `SELECT * FROM table WHERE column ~* 'pattern';`
2. **MySQL** :
    
    - **Types d'expressions** :
        - **Henry Spencer Regular Expressions** : Similaires aux expressions régulières POSIX étendues (ERE).
    - **Exemple** :
        - `SELECT * FROM table WHERE column REGEXP 'pattern';`
3. **SQLite** :
    
    - **Types d'expressions** :
        - **Custom Regular Expressions** : Utilisation de fonctions personnalisées avec des bibliothèques externes comme PCRE.
    - **Exemple (avec extension PCRE)** :
        - `SELECT * FROM table WHERE column REGEXP 'pattern';`



### Utilisation

- **POSIX Basic Regular Expressions (BRE)** : Utilisées par défaut dans `grep`, `sed`, et `awk`.
- **POSIX Extended Regular Expressions (ERE)** : Utilisées avec des options spécifiques dans `grep`, `sed`, et `awk`.
- **Perl Compatible Regular Expressions (PCRE)** : Disponibles dans `grep` (avec l'option `-P`), `Notepad++`, et par extension dans `SQLite`.
- **JavaScript Regular Expressions** : Utilisées dans Visual Studio Code.
- **Scintilla Regular Expressions** : Utilisées dans Notepad++.
- **Expressions régulières spécifiques** : Utilisées par Vim et basées sur des extensions POSIX.

### Langages et Leurs Interpréteurs d'Expressions Régulières

1. **Python** :
   - **Module `re`** : Implémente les expressions régulières de base compatibles avec Perl, mais sans certaines fonctionnalités avancées de PCRE.
   - **Module `regex`** (bibliothèque tierce) : Une alternative plus puissante au module `re`, avec un support pour certaines fonctionnalités avancées de PCRE comme les captures nommées, les lookbehind variables, et plus encore.

2. **JavaScript** :
   - Utilise son propre moteur d'expressions régulières intégré, compatible avec la majorité des fonctionnalités courantes de Perl, mais limité par rapport à PCRE.
   - Supporte les lookahead/lookbehind, les groupes de capture, mais ne supporte pas les conditionals ou les subroutines.

3. **Java** :
   - **Package `java.util.regex`** : Basé sur une implémentation compatible avec Perl, avec certaines limitations. Il ne supporte pas les lookbehind variables et les captures non-gourmandes.
   - Fournit des classes comme `Pattern` et `Matcher` pour travailler avec les regex.

4. **C# (.NET)** :
   - **Namespace `System.Text.RegularExpressions`** : Implémente des expressions régulières compatibles avec Perl avec quelques extensions spécifiques à .NET, comme les captures nommées.
   - Utilise des classes comme `Regex` pour la manipulation des motifs.

5. **PHP** :
   - Utilise **PCRE (Perl Compatible Regular Expressions)** via les fonctions `preg_*` (comme `preg_match`, `preg_replace`).
   - Offre une compatibilité étendue avec les fonctionnalités de PCRE.

6. **Perl** :
   - Le langage qui a popularisé les expressions régulières et offre une des implémentations les plus puissantes et flexibles.
   - Supporte une large gamme de fonctionnalités avancées, y compris les assertions lookbehind variables, les conditionals, les captures nommées et bien plus encore.

7. **Ruby** :
   - Classe `Regexp` : Fournit un support riche pour les expressions régulières, compatible avec de nombreuses fonctionnalités de PCRE.
   - Supporte les lookahead/lookbehind, les captures nommées, et les subroutines.

8. **Go** :
   - **Package `regexp`** : Implémente les expressions régulières basées sur la syntaxe RE2, qui est conçue pour être sûre et éviter les backtracking exponentiels.
   - Limité par rapport à PCRE, ne supporte pas les lookbehind.

9. **Rust** :
   - **Crate `regex`** : Implémente les expressions régulières basées sur la syntaxe RE2, avec une sécurité et des performances optimisées.
   - Ne supporte pas les lookbehind ou les captures non-gourmandes.

10. **C/C++** :
    - En C++, **bibliothèque `<regex>`** depuis C++11 offre un support pour les expressions régulières similaires à celles de la norme ECMAScript.
    - Peut utiliser des bibliothèques tierces comme **PCRE** pour des fonctionnalités plus avancées.

### Différences Clés et Exemples

1. **Lookbehind Variable** :
   - **Python (`re`)** : Non supporté
   - **Python (`regex`)** : Supporté
   - **Java** : Non supporté
   - **JavaScript** : Supporté (depuis ECMAScript 2018)

2. **Captures Nomées** :
   - **Python (`re`)** : Supporté
   - **JavaScript** : Supporté (depuis ECMAScript 2018)
   - **Java** : Supporté
   - **C#** : Supporté

3. **Conditionals** :
   - **Perl** : Supporté
   - **PHP** : Supporté
   - **JavaScript** : Non supporté
