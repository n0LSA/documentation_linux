---
title: " Les Périphériques d'Entrée et de Sortie"
date: 2024-09-23
date de modification: 2024-09-23
timestamp: 12:39
tags:
  - projet
status:
  - En cours
type de note:
  - projet
référence: 
auteur: aGrellard
source:
  - https://chatgpt.com/c/66f017f5-a8f8-8003-8d11-8f61d5873134
---
#  Les Périphériques d'Entrée et de Sortie

## A faire

- [ ] Finir le chapitre sécuritée : [[IT-IO-Devices-secu]] 
- [ ] Conclusion :  [[IT-IO-Devices-end]]
- [ ] Rubber Ducky : [[Rubber-Ducky]]

## Introduction 

Les périphériques d'entrée et de sortie sont les éléments qui permettent l'interaction entre l'utilisateur et le système informatique. Il constituent les points physique ou logique par lesquels les données et les commandes sont transmises a l'ordinateur, et par lesquels les résultats du traitement sont restitués à l'utilisateur.

Ces dispositifs jouent un rôle fondamental dans le cycle du traitement de l'information, qui repose sur le modèle [[IT-Process|Entrée -> Traitement-> Sortie]]. Dans ce modèle les **périphériques d'entrée** servent à introduire des données but dans le système. Ces données sont ensuite traitée par les composant internes de l'ordinateur comme le processeur, la mémoire. Puis les **périphérique de sortie** présentant les informations traitées sous une forme exploitable par l'utilisateur, qu'il s'agisse d'un affiche visuel, d'un son ou toute autre forme de restitution.

Pourquoi utiliser des périphériques : 

- **Faciliter la communication homme-machine** : ils traduisent les actions de l'utilisateur en signaux compréhensible par l'ordinateur et vice versa .
- **Permette l'exécution de tâches complexes** : Grâce a ces dispositifs l'utilisateur peut interagir avec des logiciel sophistiqués pour accomplir un variété de tâches, de la création de documents à a la conception graphique en passant par la gestion de base de données.
- **Améliorer l'accessibilité et l'efficacité**  : Des périphériques bien conçu rendent les systèmes informatique plus accessible, en tenant compte des besoins variés des utilisateurs, y compris ceux en situation de handicap.

## Table des matoéres

```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

## Classification des périphériques

Les périphériques d'entrée et de sortie peuvent être classé en trois catégories : 

1. **Périphérique d'entrée** : Dispositifs permettent de fournir des données au système.
2. **Périphérique de  sortie** : Dispositifs permettent de restituer les informations traitées à l'utilisateur.
3. **Périphérique mixte** **(entré/sortie)** : Dispositifs pouvant à la fois entrée et sortir des données.

### Périphérique d'entrée

Les périphériques d'entrée sont des dispositifs que l'utilisateur utilise pour introduire des données ou des commandes dans le système informatique. il sont le premier point de contacte dans le modèle [[IT-Process|Entrée -> Traitement-> Sortie]]

#### Exemples courants :

- **Clavier** : Permet la saisie de texte, de chiffres et de commandes. C'est l'un des périphériques d'entrée les plus fondamentaux.
- **Souris** : Dispositif de pointage qui permet de naviguer dans l'interface graphique, de sélectionner des objets et d'exécuter des commandes.
- **Microphone** : Capture des signaux audio, utilisé pour la communication vocale, l'enregistrement audio ou la reconnaissance vocale.
- **Scanner** : Numérise des documents physiques pour créer des images ou des fichiers numériques.
- **Appareil photo numérique/Webcam** : Capture des images ou des vidéos, utilisé pour la vidéoconférence, la photographie ou l'enregistrement vidéo.
- **Joystick/Manette de jeu** : Utilisé principalement dans les jeux vidéo pour contrôler les actions dans l'environnement virtuel.
- **Tablette graphique** : Permet aux artistes et designers de dessiner directement dans un environnement numérique avec un stylet.
- **Capteurs** : Dans les contextes industriels ou scientifiques, des capteurs peuvent mesurer des variables environnementales comme la température, la pression, ou le mouvement, et transmettre ces données au système.

### Périphérique de  sortie

Les périphériques de sortie dont des dispositifs qui restituent les informations traitées par le système informatique à l'utilisateur. Il matérialise le résulta du traitement sous une forme perceptible pour l'utilisateur.

#### Exemples courants :

- **Moniteur/Écran** : Affiche des images, du texte, des vidéos et des interfaces utilisateur graphiques.
- **Imprimante** : Produit des copies physiques de documents numériques sur papier ou autres supports.
- **Haut-parleurs/Casque audio** : Restitue le son, qu'il s'agisse de musique, de voix ou d'effets sonores.
- **Projecteur** : Affiche des images ou des vidéos sur une surface plus grande, utilisé dans les présentations ou le cinéma à domicile.
- **Traceur** : Utilisé principalement pour imprimer des dessins techniques et des plans en grand format.
- **Afficheur braille** : Permet aux personnes malvoyantes de lire le texte affiché à l'écran en braille.

### Périphérique mixte (entré/sortie) 

Les **périphériques mixte** ou périphériques d'**entrée/sortie**, sont des dispositifs qui peuvent a la fois **entrée des données** dans le système et **sortir des informations** vers l'utilisateur. Ils combinent les fonctions des périphériques d'entrée et de sortie.

#### Exemples courants :

- **Écran tactile** : Sert à la fois d'affichage (sortie) et de dispositif d'entrée par le toucher. L'utilisateur peut interagir directement avec ce qui est affiché à l'écran.
- **Modem/Routeur** : Permet l'échange de données entre l'ordinateur et le réseau Internet, envoyant et recevant des informations.
- **Imprimante multifonction** : Combine les fonctions d'imprimante (sortie), de scanner (entrée), et parfois de photocopieur ou de fax.
- **Casque de réalité virtuelle (VR)** : Affiche un environnement virtuel immersif (sortie) et capture les mouvements de la tête ou du corps de l'utilisateur (entrée) pour interagir avec cet environnement.
- **Disque dur externe/Clé USB** : Permet de stocker des données (sortie lorsqu'on y enregistre des données, entrée lorsqu'on les lit).
- **Tablette et smartphone** : Dispositifs polyvalents qui intègrent des écrans tactiles, des caméras, des microphones, des haut-parleurs, et peuvent entrer et sortir des données de multiples façons.

## Interactions avec le système informatique

Les périphérique d'entrée et de sortie ne fonctionne pas isolément, ils interagissent étroitement avec le système informatique par l'utilisation de matériel et de logiciels qui assurent la communication.

### La communication avec le matériel

#### Rôle des bus de données et des Interfaces matériel.

- **Bus de données** : ces sont des circuits électronique qui permettent le transfert de données entre les différents composants de l'ordinateur, y compris les périphériques. Ils assurent la communication entre entre composant et périphériques.
	- **Bus interne** : Relient les composant interne du système, comme le bus PCI Express pour les cartes d'extension.
	- **Bus externe** : Interfaces pour les périphériques externes, comme USB, HDMI, etc.
- **Interfaces matérielles**  : Ce sont les connecteurs et les protocoles qui permettent physiquement de brancher les périphériques à l'ordinateur.
	- **USB (Universal Serial Bus)** : Interfaces couramment utilisées pour les clavier, souris, disque dur externes, etc.
	- **Bluetooth** : Technologie sans fils pour connecter des périphériques comme des casques audio, enceintes, etc.
	- **HDMI/DisplayPort** : Interfaces pour les moniteurs et projecteurs.
	- **Ethernet/Wi-Fi** : Pour les périphériques réseaux

Ces bus et interfaces assurent que les données circulent correctement entre le périphérique et le système, en respectant des protocoles établi pour garantir la compatibilité et la performance.

### Rôles des pilotes (drivers)

Les **pilotes** ou **drivers** sont des logiciels spécifiques qui permettent au système d'exploitation de communiquer avec les périphériques matériels. Il joue un rôle crucial dans l'interaction entre le matériel et le logiciel.

- **Fonction des pilotes**
	- **Abstraction du matériel** : les pilotes cachent les informations matériel aux applications, offrant une interface standardisée pour accéder aux fonctionnalité du périphérique
	- **Gestion de communications** : ils interprètent les signaux du périphériques et les traduisent en instructions compréhensible pour le système d'exploitation, et vice versa.
	- **Optimisation matériel** : Ils peuvent inclure des optimisations matériel pour tirer le meilleur parti du logiciel
- **Installation de mise a jour**
	- **Fournis par le fabricant** : Les pilotes sont souvent développer par les fabricant du périphérique pour garantir une compatibilité optimale.
	- **Mises a jour régulières** : Les mises a jour de pilote corrige des bugs, améliorent les performances, et ajoute de nouvelles fonctionnalités.

Sans les pilotes le système d'exploitation ne pourrait pas reconnaitre ni utiliser correctement les périphériques connectés. 

### Gestion par le système d'exploitation

le système d'exploitation (OS) est responsable de la gestion global des ressources du système, y compris les périphériques d'entrée et de sortie.

- **Attribution des ressources**
	- **Gestion des interruptions (IRQ)** : les périphériques utilisent des lignes d'interruption pour signaler au processeur qu'il ont besoin d'attention. L'OS gère ces interruption pour prioriser les taches.
	- **Allocation de mémoire** : Les périphériques peuvent nécessiter de la mémoire pour fonctionner, L'OS alloue l'espace en mémoire vive
	- **Gestion des ports E/S** : L'OS contrôle les ports d'entrée et de sortie pour permettre la communication avec les périphériques.

L'OS va aussi effectuer la **Gestion des conflits entre périphériques**, des **Mise a jour** (notamment pour: la compatibilité avec de nouveaux ou d'ancien périphériques, mettre a jour les pilotes)

## Sécurité et périphériques

Les périphériques d'entrée et de sortie, en tant que points d'interaction avec le système, peuvent présenter des vulnérabilités qui doivent être prise en compte pour assurer la sécurité global du système informatique.

### Risque associés

#### Keylogges : Menaces liées aux claviers

- **Keyloggers matériels** : Dispositifs physiques installer entre le clavier et l'ordinateur pour enregistrer les frappes.
- **Keyloggers logiciels** : Programmes malveillant qui capture les entrée du clavier.
- **Risques** :
	- Vol de mot de passe, informations personnelles, données sensibles.
	- Surveillance non autorisée des activités de l'utilisateur.

#### Périphériques USB malveillants

- **Introduction de logiciels malveillants** : Les clés USB peuvent contenir des virus, des chevaux de Troie ou des ransomwares.
- **Attaques USB HID (Human Interface Device)** : Un périphérique USB peut se faire passer pour un clavier ou une souris et exécuter des commandes malveillantes.
- **Risques** :
    - Compromission du système.
    - Perte de données.
    - Accès non autorisé au réseau.


