---
title: Expansion de Paramètre
date: 2024-07-10
tags:
  - ressource
status:
  - Complété
type de note:
  - ressource
source:
  - chatgpt
référence:
  - "[[02_RESSOURCES/Linux/langage/bash/bash-docu/Tableaux]]"
---

# Expansion de Paramètre sous Linux

---

## Introduction

L'expansion de paramètre est une fonctionnalité puissante des shells Unix/Linux qui permet de manipuler et transformer des variables de manière flexible et dynamique. Cette documentation détaillée explique comment l'utiliser, avec des exemples concrets.

---

## Installation

Aucune installation spécifique n'est nécessaire pour utiliser l'expansion de paramètre. Cette fonctionnalité est intégrée dans les shells comme Bash, qui est généralement préinstallé sur les distributions Linux.

---

## Fonctionnement de l'Expansion de Paramètre

### Comment cela fonctionne

L'expansion de paramètre permet de référencer et manipuler des valeurs de variables de manière plus flexible que les simples variables. Elle inclut des fonctionnalités telles que la substitution, la manipulation de chaînes et la fourniture de valeurs par défaut.

### Syntaxe de la Fonction avec des Exemples

#### Référencement de Variables

```sh
variable="Hello"
echo ${variable}
```
Affiche la valeur de la variable `variable`.

#### Longueur d'une Chaîne

```sh
string="Hello, World!"
echo ${#string}
```
Affiche la longueur de la chaîne `string`.

#### Substitution de Chaîne

```sh
filename="document.txt"
echo ${filename%.txt}.pdf
```
Remplace l'extension `.txt` par `.pdf`.

---

## Options de l'Expansion de Paramètre

### Liste des Options et leur Utilisation

#### Valeur par Défaut

- **${variable:-valeur_par_defaut}** : Utilise `valeur_par_defaut` si `variable` n'est pas définie.

```sh
echo ${username:-"Invité"}
```

#### Assignation par Défaut

- **${variable:=valeur_par_defaut}** : Assigne `valeur_par_defaut` à `variable` si elle n'est pas définie.

```sh
echo ${username:="Invité"}
```

#### Substitution Conditionnelle

- **${variable:+valeur}** : Utilise `valeur` si `variable` est définie.

```sh
echo ${username:+ "Utilisateur : $username"}
```

#### Erreur si Non Défini

- **${variable:?message}** : Affiche `message` et arrête le script si `variable` n'est pas définie.

```sh
echo ${username:? "Erreur : nom d'utilisateur non défini"}
```

---

## Exemples Concrets et Explications

### Validation des Arguments

```sh
#!/bin/bash
usage() {
  echo "Usage: $0 filename"
  exit 1
}

if [ $# -ne 1 ]; then
  usage
else
  filename=$1
  echo "Processing file: ${filename}"
fi
```
Cet exemple montre comment utiliser une fonction `usage` pour vérifier le nombre d'arguments fournis au script et affiche un message d'erreur si le nombre d'arguments est incorrect.

### Opérations sur les Chaînes

```sh
#!/bin/bash
text="Hello World"
echo ${text:6:5}  # Affiche "World"
```
Cet exemple extrait une sous-chaîne de `text` à partir du 7e caractère (index 6) et de longueur 5.

### Vérification de Variables

```sh
#!/bin/bash
directory=${1:? "Erreur : aucun répertoire spécifié"}
echo "Changement de répertoire vers : $directory"
cd "$directory"
```
Cette commande utilise `${1:? "message"}` pour s'assurer qu'un argument est fourni, sinon elle affiche un message d'erreur et arrête le script.

---

## Références

Pour plus de détails, vous pouvez consulter les ressources suivantes :
- [Stack Overflow sur l'expansion de paramètre](https://stackoverflow.com/questions/34535587/what-is-usage-in-shell-scripting)
- [Guide débutant Linux sur Ubuntu](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
- [Guide complet pour débutants sur Linux.com](https://www.linux.com/training-tutorials/complete-beginners-guide-linux/)

---

Cette documentation fournit une base solide pour utiliser l'expansion de paramètre dans vos scripts shell sous Linux.