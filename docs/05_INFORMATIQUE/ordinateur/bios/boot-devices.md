---
title: périphériques d'amorçage
date: 2024-08-26
tags:
  - ressource
status:
  - En cours
type de note:
  - ressource
source:
  - chatgpt
  - https://www.lenovo.com/fr/fr/glossary/what-is-boot-device/
auteur: aGrellard
---


```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# périphériques d'amorçage

## GPT

Un périphérique d'amorçage, ou "boot device" en anglais, est un dispositif à partir duquel un ordinateur charge son système d'exploitation au moment de son démarrage. En d'autres termes, c'est le périphérique contenant les fichiers nécessaires pour initialiser le système d'exploitation et permettre à l'ordinateur de fonctionner.

### Types de périphériques d'amorçage
Il existe plusieurs types de périphériques d'amorçage, chacun avec ses propres caractéristiques :

1. **Disque dur (HDD/SSD)** : 
   - C'est le périphérique d'amorçage le plus courant. Le disque dur ou le SSD contient généralement le système d'exploitation installé, que l'ordinateur charge lors de son démarrage.

2. **Lecteur de CD/DVD/Blu-ray** :
   - Dans certains cas, notamment lors de l'installation d'un système d'exploitation, un ordinateur peut amorcer à partir d'un disque optique contenant les fichiers d'installation.

3. **Clé USB** :
   - De plus en plus courante, la clé USB est souvent utilisée pour l'installation de systèmes d'exploitation ou pour amorcer un environnement de secours. Elle est très pratique car elle est portable et peut être facilement reconfigurée.

4. **Disquette** :
   - Historiquement, les disquettes étaient couramment utilisées comme périphériques d'amorçage, mais elles sont aujourd'hui obsolètes.

5. **Réseau (PXE - Preboot Execution Environment)** :
   - Le démarrage sur réseau permet à un ordinateur de charger un système d'exploitation ou un programme d'amorçage à partir d'un serveur distant via une connexion réseau. Cette méthode est souvent utilisée dans des environnements de gestion d'infrastructure pour des installations automatisées.

6. **Périphériques externes** :
   - Il peut s'agir de disques durs externes ou de SSD connectés via USB, Thunderbolt, ou eSATA, qui peuvent être configurés comme des périphériques d'amorçage.

### Comment fonctionne un périphérique d'amorçage ?

Lorsqu'un ordinateur est mis sous tension, le BIOS (Basic Input/Output System) ou l'UEFI (Unified Extensible Firmware Interface) prend le contrôle et effectue une série de tests matériels (POST - Power-On Self Test). Ensuite, il cherche un périphérique d'amorçage dans un ordre prédéfini dans ses paramètres. Cet ordre peut être configuré dans le BIOS/UEFI et peut inclure plusieurs périphériques.

- **Exemple d'ordre de démarrage** : 
  1. Clé USB
  2. Disque dur interne
  3. Lecteur de CD/DVD
  4. Réseau (PXE)

Si le BIOS/UEFI trouve un périphérique d'amorçage avec les fichiers nécessaires, il charge le programme de démarrage (bootloader) situé sur ce périphérique. Le bootloader a pour tâche de charger le système d'exploitation en mémoire pour que l'ordinateur puisse fonctionner.

### Importance des périphériques d'amorçage
Les périphériques d'amorçage sont essentiels car sans eux, l'ordinateur ne pourrait pas démarrer correctement. Ils sont aussi utilisés pour des tâches spécifiques comme :
- **Réinstaller ou réparer un système d'exploitation**.
- **Tester un nouveau système d'exploitation sans l'installer** (ex : distributions Linux Live).
- **Exécuter des outils de diagnostic ou de récupération**.

En résumé, un périphérique d'amorçage est indispensable pour le démarrage et le bon fonctionnement d'un ordinateur. Il peut prendre différentes formes, chacune adaptée à des besoins spécifiques, allant du simple démarrage d'un système d'exploitation installé, à la récupération de données, ou à l'installation d'un nouveau système.

## Lenovo

### Qu`est-ce qu`un périphérique d`amorçage ?

Un périphérique d'amorçage est un support de stockage à partir duquel un ordinateur ou un autre appareil électronique charge son système d'exploitation ou son microprogramme lors du démarrage ou du redémarrage. Il peut s'agir d'un disque dur, d'un disque SSD (solid state drive), d'un lecteur USB (universal serial bus), d'un disque compact/disque numérique polyvalent (CD/DVD) ou d'un emplacement réseau.

### Pourquoi le périphérique de démarrage est-il important ?

Le périphérique d'amorçage est crucial car il contient les fichiers et les instructions nécessaires au démarrage de l'ordinateur. Il permet à l'ordinateur d'accéder au système d'exploitation et de lancer les processus nécessaires à son fonctionnement normal.

### Que se passe-t-il si l'ordinateur ne trouve pas de périphérique de démarrage ?

Si l'ordinateur ne trouve pas de périphérique d'amorçage, il affiche généralement un message d'erreur tel que « Aucun périphérique d'amorçage trouvé » ou « Système d'exploitation introuvable ». Cela indique généralement que l'ordinateur ne parvient pas à localiser un système d'exploitation ou un support de démarrage, ce qui peut être dû à diverses raisons telles qu'un disque dur déconnecté ou un périphérique défectueux.

### Quelle est la différence entre un disque dur (HDD) et un disque dur à état solide (SSD) en tant que périphériques de démarrage ?

Un disque dur et un disque SSD sont tous deux des dispositifs de stockage, mais leurs technologies sous-jacentes sont différentes. Les disques durs utilisent des disques magnétiques en rotation pour stocker les données, tandis que les disques SSD utilisent des puces de mémoire flash. Les disques SSD sont généralement plus rapides, plus fiables et plus silencieux que les disques durs, ce qui en fait des choix populaires pour les périphériques de démarrage.

### Puis-je utiliser un lecteur USB (Universal Serial Bus) comme périphérique de démarrage ?

Oui, vous pouvez utiliser un lecteur USB comme périphérique de démarrage. C'est généralement le cas lors de l'installation ou de la réparation d'un système d'exploitation. Vous pouvez créer un lecteur USB amorçable en utilisant des outils tels que Rufus ou Windows Media Creation Tool pour copier les fichiers nécessaires sur le lecteur USB.

### Qu'est-ce qu'un disque compact/disque numérique polyvalent (CD/DVD) amorçable ?

Un CD ou DVD amorçable est un disque qui contient un système d'exploitation amorçable ou un autre logiciel. Ces disques peuvent être utilisés comme périphériques de démarrage en les insérant dans le lecteur optique de l'ordinateur et en configurant le logiciel d'entrée/sortie de base (BIOS) ou l'interface micrologicielle extensible unifiée (UEFI) pour donner la priorité au démarrage à partir du lecteur optique.

### Puis-je démarrer à partir d'un emplacement réseau ?

Oui, il est possible de démarrer un ordinateur à partir d'un emplacement réseau en utilisant des technologies telles que l'environnement d'exécution pré-amorçage (PXE) ou l'amorçage réseau. Cela permet à l'ordinateur de charger le système d'exploitation ou d'autres logiciels sur le réseau au lieu de s'appuyer sur des périphériques de stockage locaux.

### À quoi servent le master boot record (MBR) et la table de partition GUID (GPT) ?

Le MBR et le GPT sont deux schémas de partitionnement différents utilisés sur les périphériques d'amorçage. Le MBR est le schéma de partitionnement traditionnel utilisé par les anciens systèmes, tandis que le GPT est le schéma le plus récent et le plus avancé. Ils définissent la structure du périphérique d'amorçage, y compris la disposition des partitions et les informations relatives à l'amorçage.

### Puis-je avoir plusieurs périphériques de démarrage sur mon ordinateur ?

Oui, vous pouvez avoir plusieurs périphériques de démarrage sur votre ordinateur. Cela est souvent utile dans les situations où plusieurs systèmes d'exploitation sont installés, comme dans une configuration à double démarrage avec Windows et Linux. L'ordre de démarrage détermine le périphérique à partir duquel l'ordinateur tentera de démarrer en premier.

### Qu'est-ce que le chargeur de démarrage ?

Le chargeur de démarrage est un petit programme qui réside dans le périphérique de démarrage et qui est chargé de charger le système d'exploitation dans la mémoire. Il est généralement stocké dans un emplacement spécifique du périphérique d'amorçage, tel que l'enregistrement d'amorçage principal (MBR) ou la partition système EFI (ESP), et contient des instructions sur la manière de démarrer le système d'exploitation.

### Quel est le rôle du système d'entrée/sortie de base (BIOS) ou de l'interface micrologicielle extensible unifiée (UEFI) dans le processus d'amorçage ?

Le BIOS ou le micrologiciel UEFI joue un rôle crucial dans le processus de démarrage. Il initialise les composants matériels, effectue un autotest à la mise sous tension (POST) pour vérifier l'absence d'erreurs, puis localise et charge le chargeur d'amorçage à partir du périphérique d'amorçage désigné. Il est responsable de la transition de l'ordinateur d'un état hors tension à un état où le système d'exploitation peut prendre le relais.

### Puis-je démarrer à partir d'un disque dur externe connecté via le bus série universel (USB) ?

Oui, vous pouvez démarrer à partir d'un disque dur externe connecté via USB. De nombreux ordinateurs prennent en charge le démarrage par USB, ce qui vous permet de connecter un disque dur externe et de configurer l'ordre de démarrage pour donner la priorité aux périphériques USB. Cela peut s'avérer utile pour le dépannage, la récupération de données ou l'exécution de systèmes d'exploitation portables.

### Qu'est-ce qu'un démarrage en réseau ?

Un démarrage en réseau, également connu sous le nom d'environnement d'exécution pré-amorçage (PXE), permet à un ordinateur de démarrer à partir d'un emplacement réseau au lieu de s'appuyer sur des périphériques de stockage locaux. Lors d'un démarrage en réseau, l'ordinateur contacte un serveur réseau qui héberge les fichiers de démarrage et les images du système d'exploitation nécessaires. Cette méthode est couramment utilisée dans les environnements d'entreprise pour le déploiement, les mises à jour et la récupération à distance.

### Puis-je changer temporairement le périphérique de démarrage sans modifier les paramètres du système d'entrée/sortie de base (BIOS) ?

Oui, vous pouvez changer temporairement le périphérique de démarrage sans modifier les paramètres du BIOS. La plupart des ordinateurs modernes disposent d'une touche ou d'une combinaison de touches qui vous permet d'accéder à un menu d'amorçage pendant le démarrage. En appuyant sur cette touche, vous pouvez sélectionner un périphérique d'amorçage différent pour cette session de démarrage particulière sans modifier de façon permanente l'ordre d'amorçage.

### Qu'est-ce qu'une clé USB amorçable ?

Une clé USB amorçable est une clé USB qui contient un système d'exploitation ou un logiciel amorçable. Elle vous permet de démarrer votre ordinateur à partir de la clé USB plutôt qu'à partir des périphériques de stockage internes. Les clés USB amorçables sont couramment utilisées pour des tâches telles que l'installation ou la réparation de systèmes d'exploitation, l'exécution de diagnostics ou la création d'environnements portables.

### Puis-je démarrer mon ordinateur à partir d'une carte SD (Secure Digital) ?

Dans certains cas, il est possible de démarrer un ordinateur à partir d'une carte SD. Cependant, tous les ordinateurs ne prennent pas en charge le démarrage à partir d'une carte SD par défaut. Vous devez disposer d'un ordinateur doté d'un système d'entrée/sortie de base (BIOS) ou d'un micrologiciel UEFI (Unified Extensible Firmware Interface) qui autorise le démarrage à partir de cartes SD, et vous devrez peut-être configurer l'ordre de démarrage en conséquence. Il convient de noter que le démarrage à partir d'une carte SD est moins courant que le démarrage à partir d'autres périphériques tels que les disques durs ou les lecteurs USB (Universal Serial Bus).

### Qu'est-ce qu'un secteur d'amorçage ?

Un secteur d'amorçage est une petite section d'un périphérique de stockage, tel qu'un disque dur (HD) ou un disque dur à état solide (SSD), qui contient le code nécessaire pour lancer le processus d'amorçage. Dans les systèmes d'entrée/sortie de base (BIOS) traditionnels, le secteur d'amorçage se trouve dans l'enregistrement d'amorçage principal (MBR). Dans les systèmes UEFI (Unified Extensible Firmware Interface), il se trouve généralement dans la partition système EFI (ESP). Le code du secteur d'amorçage est responsable du chargement du chargeur d'amorçage et du démarrage du système d'exploitation.

### Qu'est-ce qu'une image de disque amorçable ?

Une image de disque amorçable est un fichier qui contient une copie complète et amorçable d'un système d'exploitation ou d'un environnement logiciel. Elle est souvent utilisée pour créer des supports amorçables, tels que des lecteurs USB (Universal Serial Bus) ou des disques optiques amorçables. L'image disque contient tous les fichiers et configurations nécessaires au démarrage du système d'exploitation ou du logiciel lorsqu'il est démarré à partir du support concerné.

### Puis-je démarrer mon ordinateur à partir d'un système d'exploitation basé sur l'informatique dématérialisée ?

Oui, il est possible de démarrer votre ordinateur à partir d'un système d'exploitation en nuage. Les systèmes d'exploitation basés sur l'informatique dématérialisée, également connus sous le nom de bureaux dématérialisés ou d'infrastructure de bureau virtuel (VDI), vous permettent d'accéder à un système d'exploitation et de l'exécuter à distance par le biais d'une connexion internet. Vous pouvez démarrer votre ordinateur et vous connecter au système d'exploitation en nuage à l'aide d'un client ou d'un navigateur web pris en charge.