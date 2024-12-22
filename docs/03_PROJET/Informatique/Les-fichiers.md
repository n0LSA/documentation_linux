---
title: Les fichiers informatiques expliqués
date: 2024-07-22
date de modification: 2024-07-22
timestamp: 21:31
tags:
  - projet
status:
  - En cours
type de note:
  - projet
référence:
  - "[[Chemins-absolus]]"
  - "[[Chemin-absolue-cannonique]]"
  - "[[Inodes]]"
  - "[[Metadata]]"
auteur: aGrellard
source:
  - tvaira
---
# Les fichiers
Les fichiers informatiques expliqués.

## Introduction

Un fichier informatique est une ***collection organisée de données*** stockées sur un support de stockage informatique comme un disque dur, un SSD, une clé USB ou un serveur distant. 

Les fichiers sont utilisés pour conserver et organiser des informations de manière permanente ou temporaire.

>Chaque fichier est une collection organisée de données structurées de manières spécifique selon son type de fichier (texte, binaire)

## Caractéristiques d'un Fichier informatique

- **Nom et chemin d'Accès **:
	- **Nom**: Chaque fichier a un nom unique dans son répertoire qui le distingue des autres fichier.
	- **Chemin d'accès** : le fichier et identifié de manière unique pas son chemin d'accès complet, incluant tous les répertoires intermédiaires jusqu'à la racine du système de fichiers.
- **Types de fichier** :
	- **Fichier Texte** : Contient des données interprétables directement comme du texte (ASCII, UTF-8, etc.)
	- **Fichier Binaire** : Fichier qui ne sont pas interprétables directement comme du texte
- **Structures et Organisation** :
	- Les fichiers sont organisés dans un structure arborescente de répertoires, ou chaque répertoires peut contenir des fichiers ou répertoires.
	- **Inodes** (dans les systèmes Unix/Linux) : Chaque fichiers est associé a un **Indoe**, une structure de données contenant des informations sur le fichier (permissions, propriétaire, timestamps, etc.)
- **Métadonnées** :
	- Les fichiers contiennent des métadonnées, qui incluent des informations comme la taille du fichier, les dates de création et de modification, les permissions d'accès et le propriétaire du fichier.
- **Accès et Manipulation** :
	- Les fichiers peuvent êtres lus, écrits, déplacés, copiés et supprimé a l'aide de commande et outils du système d'exploitation.
	- les fichiers sont manipulé via des application ou scripts, qui peuvent traiter les données contenues dans ces fichiers.
- **Systèmes de fichiers** :
	- Un système gère l'organisation, le stockage, la hiérarchie et la récupération des fichiers. (NTFS, FAT32, ext4, BTRFS)

## Conclusion
Un fichier informatique est une **unité de stockage de données**, unique par son nom dans son répertoire, et identifiable par son chemin d’accès. il peut être de type *texte* ou *bianire*, contient des métadonnées et il est gérée par un système de fichier. 

---

Un fichier informatique est un ensemble de données stockées sur un support de stockage et identifié par un nom unique dans un système de fichiers .
Un fichier informatique est une entité gérée par le système de fichier, avec un nom unique dans son répertoire, identifié par un chemin, et potentiellement associé a un structure de données complexes comme les inodes.