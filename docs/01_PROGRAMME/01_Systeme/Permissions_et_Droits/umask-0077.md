---
title: umask-0077
date: 2024-10-23
date de modification: 2024-10-23
timestamp: 14:19
tags:
  - ressource
  - templates
status:
  - En cours
type de note:
  - ressource
référence:
  - "[[umask_login-profil]]"
  - "[[umask]]"
source:
  - chatgpt
auteur: aGrellard
---
# Explication du résultat attendu pour la modification de l'UMASK et des droits des répertoires /home

## Introduction

Le durcissement d'un serveur est essentiel pour assurer la sécurité des données et la confidentialité des utilisateurs. En particulier, la configuration appropriée des permissions sur les répertoires personnels des utilisateurs et la définition d'un **UMASK** restrictif sont des mesures importantes pour empêcher l'accès non autorisé aux fichiers et répertoires des autres utilisateurs.

Le **niveau de durcissement : R** indique un niveau recommandé ou renforcé de sécurité.

Dans ce contexte, deux commandes sont utilisées :

1. **`chmod 770 /home/*`**
2. **`sed -i 's/^UMASK.*/UMASK   0077/g' /etc/login.defs`**

Nous allons expliquer le résultat attendu de ces commandes et leur impact sur la sécurité du serveur.

---

## 1. Modification des droits des répertoires /home avec `chmod 770 /home/*`

### Explication de la commande

- **`chmod`** : Commande utilisée pour changer les permissions (mode) des fichiers ou répertoires.
- **`770`** : Représente les nouvelles permissions à appliquer.
    - **7** (propriétaire) : Lecture, écriture et exécution (rwx).
    - **7** (groupe) : Lecture, écriture et exécution (rwx).
    - **0** (autres) : Aucune permission.
- **`/home/*`** : Sélectionne tous les répertoires (ou fichiers) dans le répertoire **/home**.

### Résultat attendu

- **Permissions des répertoires dans /home** :
    - Les répertoires personnels de chaque utilisateur dans **/home** auront les permissions **770**.
    - Cela signifie que seuls le propriétaire du répertoire et les membres du groupe propriétaire peuvent accéder au contenu du répertoire.
    - Les "autres" utilisateurs n'ont **aucune permission** sur ces répertoires.

### Impact sur la sécurité

- **Confidentialité renforcée** :
    - Empêche les utilisateurs non autorisés de parcourir ou d'accéder aux fichiers des autres utilisateurs.
- **Contrôle d'accès** :
    - Les membres du même groupe que le propriétaire peuvent toujours accéder au répertoire si nécessaire.
- **Réduction des risques** :
    - Limite la possibilité pour un utilisateur malveillant ou une application compromise d'accéder à des données sensibles.

---

## 2. Modification de l'UMASK dans `/etc/login.defs` avec `sed -i 's/^UMASK.*/UMASK   0077/g' /etc/login.defs`

### Explication de la commande

- **`sed`** : Éditeur de flux (stream editor) utilisé pour effectuer des transformations sur des fichiers.
- **`-i`** : Modifie le fichier en place (édition "inline").
- **`'s/^UMASK.*/UMASK   0077/g'`** : Expression sed qui remplace la ligne commençant par **UMASK** par **UMASK   0077**.
    - **`s/.../.../g`** : Syntaxe de substitution (substitution globale).
    - **`^UMASK.*`** : Correspond à toute ligne commençant par **UMASK** et suivie de n'importe quels caractères.
- **`/etc/login.defs`** : Fichier de configuration qui définit les paramètres de création des comptes utilisateurs.

### Résultat attendu

- **Modification du fichier `/etc/login.defs`** :
    - Le paramètre **UMASK** est modifié pour être **0077**.
- **Impact sur la création de nouveaux utilisateurs** :
    - À partir de maintenant, lorsque de nouveaux utilisateurs sont créés, leur umask par défaut sera **0077**.

### Comprendre l'UMASK 0077

- **UMASK** : Définit les permissions par défaut des nouveaux fichiers et répertoires créés.
- **UMASK 0077** :
    - Permissions par défaut pour les nouveaux fichiers : **600** (rw-------)
    - Permissions par défaut pour les nouveaux répertoires : **700** (rwx------)
- **Interprétation** :
    - Les nouveaux fichiers et répertoires créés par les utilisateurs ne seront accessibles que par le propriétaire. Ni le groupe, ni les autres utilisateurs n'auront de permissions sur ces fichiers.

### Impact sur la sécurité

- **Sécurité renforcée des nouveaux fichiers** :
    - Empêche par défaut que d'autres utilisateurs aient accès aux nouveaux fichiers et répertoires créés.
- **Protection des données sensibles** :
    - Réduit le risque de fuite d'informations via des fichiers mal configurés.
- **Consistance** :
    - Assure que tous les nouveaux utilisateurs auront des permissions par défaut sécurisées, sans nécessiter de configuration manuelle supplémentaire.

---

## 3. Résumé de l'action globale

En combinant ces deux commandes, vous effectuez les actions suivantes :

1. **Sécurisation des répertoires existants** :
    - En modifiant les permissions des répertoires déjà présents dans **/home**, vous assurez que les données actuelles des utilisateurs sont protégées contre l'accès non autorisé.

2. **Définition de permissions sécurisées pour les futurs utilisateurs** :
    - En modifiant le fichier **/etc/login.defs**, vous garantissez que les nouveaux utilisateurs créés auront un umask par défaut de **0077**, ce qui protège leurs futurs fichiers et répertoires.

---

## 4. Considérations supplémentaires

### 4.1 Vérification des groupes des utilisateurs

- **Groupes principaux** :
    - Par défaut, chaque utilisateur a son propre groupe principal (généralement du même nom que l'utilisateur).
- **Impact du chmod 770** :
    - Si les utilisateurs partagent un groupe commun, les membres du groupe pourraient accéder aux répertoires des autres utilisateurs.
    - Pour une isolation complète, assurez-vous que chaque utilisateur a un groupe unique.

### 4.2 Applications nécessitant un partage de fichiers

- **Collaborations** :
    - Si des utilisateurs doivent collaborer et partager des fichiers, des configurations supplémentaires seront nécessaires.
    - Vous pouvez créer des groupes spécifiques pour ces collaborations et ajuster les permissions en conséquence.

### 4.3 Attention aux services système

- **Services tels que `cron`, `at`, `mail`** :
    - Certains services système peuvent nécessiter l'accès à des répertoires utilisateurs.
    - Assurez-vous que ces services fonctionnent correctement après les modifications.

### 4.4 Tester les modifications

- **Tester avec un compte utilisateur** :
    - Connectez-vous avec un compte utilisateur et vérifiez que les permissions fonctionnent comme prévu.
- **Vérifier l'accès pour les autres utilisateurs** :
    - Essayez d'accéder aux répertoires d'autres utilisateurs pour confirmer que l'accès est refusé.

---

## 5. Conclusion

La modification du **UMASK** et des permissions des répertoires **/home** est une étape importante pour renforcer la sécurité d'un serveur Debian. En appliquant ces changements :

- **Vous empêchez les utilisateurs d'accéder aux fichiers des autres**, protégeant ainsi la confidentialité des données personnelles et sensibles.
- **Vous établissez une politique de sécurité cohérente** pour les utilisateurs existants et futurs.
- **Vous réduisez les risques associés aux permissions par défaut trop permissives**, qui pourraient être exploitées par des utilisateurs malveillants ou des applications compromises.

Il est essentiel de toujours considérer les besoins spécifiques de votre environnement et de vos utilisateurs. Si certains utilisateurs ont besoin de partager des fichiers, des configurations supplémentaires seront nécessaires pour permettre cette collaboration tout en maintenant un niveau de sécurité approprié.

---

