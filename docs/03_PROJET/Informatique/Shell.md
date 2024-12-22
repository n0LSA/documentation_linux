---
title: les shells dans les systèmes d'exploitation
date: 2024-07-23
date de modification: 2024-07-23
timestamp: 09:13
tags:
  - projet
status:
  - En cours
type de note:
  - projet
référence:
  - "[[emulateur-terminal]]"
  - "[[prompt]]"
auteur: aGrellard
---

# Shells

les shells dans les systèmes d'exploitation.

## Introduction

**Terminal** : Un terminal, ou ***émulateur de terminal***, est une application qui émule un terminal matériel et permet à l'utilisateur de communiquer avec un système d'exploitation via une interface en ligne de commande (CLI) sur un ordinateur moderne. 

L'émulateur de terminal lance un **shell** qui inclut un ***interpréteur de commandes***, analyse les commandes texte, les *interprète* et les *exécute*. 

## Un shell

Le shell fournit une **interface utilisateur** qui permet d'interagir avec le système d'exploitation. Cette interface est distincte de l'émulateur de terminal.

- **Rôle d'un shell** :
	- **Prompt** : Demande à l'utilisateur de saisir une commande et l'envoie.
	- **Interpréter** : Analyse les commandes de l'utilisateur.
	- **Transmettre** : Envoie les instructions au système d'exploitation pour exécution.
	- **Recevoir** : Récupère les résultats de l'exécution du système d'exploitation.
	- **Acheminer** : Transfère ces résultats vers l'émulateur de terminal pour affichage.
	- **Prompt** : Affiche un nouveau prompt après avoir affiché les résultats.

Dans le contexte de systèmes comme Unix et Linux, un **shell** est particulièrement important car il permet à l'utilisateur d'**interagir** avec le système d'exploitation via des commandes texte.

- Il existe plusieurs ***types de shells***, ayant chacun leurs propres caractéristiques et fonctionnalités :
	- **Bourne Shell (sh)** : Le shell original créé par Stephen Bourne.
	- **Bourne Again Shell (bash)** : Une amélioration de ***sh***, couramment utilisée par les systèmes GNU/Linux. 
	- **C Shell (csh)** : Utilise une syntaxe similaire au langage de programmation C.
	- **Korn Shell (ksh)** : Combine les fonctionnalités de ***sh*** et ***csh***.
	- **Z Shell (zsh)** : Offre de nombreuses améliorations et fonctionnalités supplémentaires par rapport à ***bash***.

En plus d’**interpréter** les commandes, le **shell** exécute des scripts, gère les variables d'environnement et offre des fonctionnalités comme : l'historique des commandes, l'auto-complétion, la création d'alias, etc.







