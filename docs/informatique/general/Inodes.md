---
title: Inodes
date: 2024-07-22
tags:
  - ressource
  - informatique
status:
  - En cours
type de note:
  - ressource
auteur: aGrellard
source:
  - chatgpt
référence: [[metadta]]
---

# Inodes

Un inode (index node) est une structure de données utilisée par les systèmes de fichiers Unix/Linux pour décrire un fichier ou un répertoire. Chaque fichier ou répertoire a un inode unique qui contient toutes les informations sur le fichier à l'exception de son nom et de ses données.

**Contenu d'un Inode** :
1. **Numéro d'inode** : Un identifiant unique pour l'inode dans le système de fichiers.
2. **Métadonnées du fichier** :
   - **Mode** : Type de fichier (fichier, répertoire, lien symbolique, etc.) et permissions d'accès.
   - **Nombre de liens** : Le nombre de noms de fichiers faisant référence à cet inode.
   - **UID (User ID)** : Identifiant de l'utilisateur propriétaire du fichier.
   - **GID (Group ID)** : Identifiant du groupe propriétaire du fichier.
   - **Timestamps** :
     - **Dernier accès** : Heure de la dernière lecture du fichier.
     - **Dernière modification** : Heure de la dernière écriture dans le fichier.
     - **Dernier changement** : Heure du dernier changement de l'inode lui-même (par exemple, modification des permissions).
3. **Pointeurs vers les blocs de données** :
   - **Pointeurs directs** : Liens directs vers les blocs de données contenant le contenu du fichier.
   - **Pointeurs indirects** : Liens vers des blocs de pointeurs, utilisés pour les fichiers très grands.

**Fonctionnement des Inodes** :
- Les inodes ne contiennent pas le nom du fichier. Le nom est stocké dans les entrées de répertoire qui associent un nom de fichier à un numéro d'inode.
- Quand un fichier est ouvert, le système de fichiers utilise l'inode pour accéder aux métadonnées et localiser les données du fichier sur le disque.

**Exemple d'utilisation des Inodes** :
- Lorsqu'un fichier est créé, un inode est alloué et rempli avec les informations du fichier.
- Lorsqu'un fichier est supprimé, l'inode est libéré et peut être réutilisé pour un nouveau fichier.
