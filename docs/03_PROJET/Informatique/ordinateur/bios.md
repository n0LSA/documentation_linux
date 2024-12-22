---
title: Le Bios
date: 2024-08-26
tags:
  - projet
status:
  - En cours
type de note:
  - projet
auteur: aGrellard
référence:
  - "[[02_RESSOURCES/informatique/ordinateur/bios/firmware]]"
  - "[[volatile-memory]]"
  - "[[02_RESSOURCES/informatique/ordinateur/bios/boot-devices]]"
source:
  - chatgpt
---
# Le BIOS

Le BIOS (**Basic Input/Output Stream**)

>C'est un composant logiciel qui réside sur un puce de mémoire non volatile sur la carte mère. Son rôle principale et de fournir les instruction nécessaire pour amorcer le système d'exploitation lors du démarrage de l'ordinateur.

>plus précisément il s'agit d'un **programme** ([[02_RESSOURCES/informatique/ordinateur/bios/firmware]]) qu est stocké sur une **puce de mémoire non volatile** ([[volatile-memory]]), telle q'une **EEPROM** (Electrically Erasable Programable Read-Only Memory) ou une Flash ROM, cette puce contient le firmware du BIOS, qui est le programme utilisé pour initialiser le matériel et démarrer le système d'exploitation. L’exécution du bios se fait via un processus qui implique le processeur principal de l'ordinateur.

>le bios travail en tandem avec une puce de mémoire volatil Le **[[cmos]]** qui a l'aides d'une pile permet de garder en mémoire les paramètres utilisateur de configuration du bios. Avec l'évolution des BIOS UEFI (Unified Extensible Firmware Interface) la puce mémoire permet le stockage dynamique des paramètres de configurations directement dans la mémoire flash en se passant d'une puce CMOS.

- **le BIOS UEFI**
	- prend en charge les **table de partition GPT** (GUID Partition Table) qui permet de gérer des disques dur de plus de **2TO**, contrairement au MBR  (Master Boot Record) utilisé par les bios traditionnel.
	- prend en charge une **interface graphique** contrairement au bios qui à une interface texte.
	- peut amorcer plus **rapidement** les systèmes d’exploitation.
	- inclut une mode **CSM** (Compatibility Support Module) qui permet de démarrer des système d’exploitation conçu pour des bios traditionnel.
	- intègre le **Secure Boot** et peut aussi intégrer un gestion avancée des énergies.
	- peut intégrer des mise a jour sans besoin de remplacer le [[02_RESSOURCES/informatique/ordinateur/bios/firmware]]

- **UEFI et Legacy** :
	- **Mode Legacy :** c'est un mode de démarrage qui émule le comportement d'un bios traditionnel. Ce mode est souvent utilisé pour des raisons de compatibilités avec des systèmes plus ancien ou des disque utilisant un table de partition MBR. Toutefois le mode Legacy seul ne peut pas tirer des fonctionnalités du bios UEFI.
	- **Mode UEFI :** mode de fonctionnement utilise toutes les fonctionnalités de l'UEFI y compris le support GPT.
	- **Mode Legacy+UEFI**

- **Le bios remplis plusieurs fonction cruciales** :
	 - **Initialisation du matériel :** Au démarrage le BIOS effectue un POST (Power-On Self Test) pour vérifier que le matériel de base (processeur, mémoire, périphériques, etc..) fonctionne correctement.
	- **Configuration de matérielle :** Le BIOS permet de configurer certains matériels, comme l'ordre de démarrage, les vitesses d'horloge ou de fréquences, ou encore les paramètres de la mémoire.
	- **Gestion du bootloader :** Il charge le bootloader du système d'exploitation installé sur le disque dur ou tout autre périphérique de stockage amorçable ([[02_RESSOURCES/informatique/ordinateur/bios/boot-devices]]).
	- **Abstraction matérielle :** ([[material-abstraction]]) 
		- Le bios offre une couche d'abstraction entre le système et le matériel. Il permet au système d'exploitation et au logiciels de base de fonctionner sans avoir besoin de connaître les spécificités du matériel sous-jacent.
		- Le bios fournit des services de base, comme la gestions des périphériques d'entrée (clavier, souris) et des  périphériques de sortie (écran), pour le fonctionnement correct de l'ordinateur.

- [**BIOS PHASE**](https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/windows-boot-issues-troubleshooting)
	- **Mise sous tension (Power-On)**
		- reset du CPU
	- **Exécution des premières instruction de BIOS**
		- Adresse de démararage
		- Lecture de BIOS
	- **Power-On-Self-Test (POST)**
		- Initialisation de matériel
		- Diagnostic et messages d'erreur
	- **Initialisation des périphériques**
		- Contrôleurs matériels
		- Tableau de routage des interruptions (Interrupt Vector Table)
	- **Configurations des paramètres de démarrage**
		- Configuration des périphériques de démarrage
		- Chargement du Bootloader
	- **Transfert du Bootloader**
		- Chargement en mémoire
		- Exécution du bootloader
	- **Chargement du noyau du système d'exploitation**
		- Sélection du système d'exploitation
		- Chargement du noyau
	- **Initialisation du système d'exploitation**
		- Initialisation du noyeau
		- Démarrage des services
		- Chargement de l'interface utilisateur