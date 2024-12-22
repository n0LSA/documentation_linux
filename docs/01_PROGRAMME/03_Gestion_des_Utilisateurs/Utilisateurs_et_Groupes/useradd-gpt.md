---
title: Guide Complet sur la Commande `useradd` sous Linux
date: 2024-10-27
date de modification: 2024-10-27
timestamp: 13:25
tags:
  - ressource
status:
  - En cours
type de note:
  - ressource
référence: 
source:
  - chatgpt
  - https://chatgpt.com/c/6718312f-1544-8003-acdb-556b1e46d04c
auteur: aGrellard
---
# Guide Complet sur la Commande `useradd` sous Linux

## Introduction

La gestion des utilisateurs est une tâche essentielle pour tout administrateur système sous Linux. La commande **`useradd`** est un outil puissant et flexible utilisé pour créer de nouveaux comptes utilisateurs. Elle permet de définir divers paramètres lors de la création d’un utilisateur, tels que le répertoire personnel, le shell par défaut, les groupes d’appartenance, et bien plus encore.

Ce guide détaillé vous expliquera :

- **Qu'est-ce que `useradd` ?**
- **Syntaxe et options principales de `useradd`**
- **Exemples pratiques d'utilisation de `useradd`**
- **Différences entre `useradd` et `adduser`**
- **Bonnes pratiques et considérations de sécurité**
- **Gestion avancée des utilisateurs**
- **Ressources supplémentaires**

---

## 1. Qu'est-ce que `useradd` ?

### 1.1 Définition

- **`useradd`** est une commande de bas niveau utilisée pour créer de nouveaux comptes utilisateurs sur un système Linux.
- Elle configure divers aspects du compte utilisateur, tels que le répertoire personnel, le shell par défaut, les groupes d'appartenance, et d'autres paramètres.
- Contrairement à **`adduser`**, qui est souvent un script plus convivial et interactif (surtout sous Debian/Ubuntu), **`useradd`** offre une interface plus directe et nécessite souvent l'utilisation d'options pour configurer correctement un utilisateur.

### 1.2 Pourquoi utiliser `useradd` ?

- **Flexibilité** : Permet une personnalisation fine lors de la création des utilisateurs.
- **Automatisation** : Idéal pour les scripts et les tâches automatisées où une interaction utilisateur n'est pas souhaitée.
- **Compatibilité** : Disponible sur la plupart des distributions Linux, offrant une méthode standardisée pour la gestion des utilisateurs.

---

## 2. Syntaxe et Options Principales de `useradd`

### 2.1 Syntaxe Générale

```bash
useradd [OPTIONS] NOM_UTILISATEUR
```

- **NOM_UTILISATEUR** : Le nom du nouvel utilisateur à créer.

### 2.2 Options Courantes

Voici les options les plus couramment utilisées avec **`useradd`** :

| Option        | Description                                                                                                                                                     |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-c COMMENT`  | Ajoute un commentaire pour l'utilisateur, souvent utilisé pour le nom complet ou d'autres informations descriptives.                                           |
| `-d CHEMIN`   | Définit le répertoire personnel de l'utilisateur. Si utilisé avec `-m`, le répertoire sera créé s'il n'existe pas.                                             |
| `-e DATE`     | Spécifie la date d'expiration du compte au format **YYYY-MM-DD**.                                                                                            |
| `-f JOURS`    | Définit le nombre de jours après l'expiration du mot de passe avant que le compte ne soit désactivé.                                                         |
| `-g GROUPE`   | Définit le groupe principal de l'utilisateur.                                                                                                                 |
| `-G GROUPES`  | Spécifie une liste de groupes supplémentaires auxquels l'utilisateur sera ajouté. Les groupes doivent être séparés par des virgules.                             |
| `-m`          | Crée le répertoire personnel de l'utilisateur s'il n'existe pas déjà.                                                                                        |
| `-M`          | Ne crée pas de répertoire personnel, même si l'option par défaut le fait.                                                                                      |
| `-s SHELL`    | Définit le shell par défaut de l'utilisateur.                                                                                                                  |
| `-p MOT_DE_PASSE` | Définit le mot de passe crypté de l'utilisateur. **Attention** : Passer le mot de passe directement via la ligne de commande peut être un risque de sécurité. |
| `-u UID`      | Attribue un UID spécifique à l'utilisateur.                                                                                                                    |
| `-r`          | Crée un compte système avec un UID inférieur à 1000 (selon la configuration), généralement utilisé pour des services ou démons système.                           |

### 2.3 Paramètres par Défaut

Les paramètres par défaut de **`useradd`** peuvent varier selon la distribution, mais généralement :

- **Shell par défaut** : `/bin/bash`
- **Répertoire personnel** : `/home/NOM_UTILISATEUR`
- **Groupes** : Un groupe principal avec le même nom que l'utilisateur
- **Mot de passe** : Aucun mot de passe initial (l'utilisateur doit le définir ultérieurement)
- **Expiration du compte** : Aucun (le compte ne s'expire pas par défaut)

---

## 3. Exemples Pratiques d'Utilisation de `useradd`

### 3.1 Création d'un Utilisateur Simple

```bash
sudo useradd johndoe
```

- **Résultat** :
  - Création de l'utilisateur **johndoe**.
  - Répertoire personnel par défaut : `/home/johndoe` (si `-m` est utilisé par défaut).
  - Groupe principal : `johndoe`.
  - Shell par défaut : `/bin/bash`.

**Remarque** : Cette commande seule ne crée pas le répertoire personnel. Pour cela, utilisez l'option `-m` ou assurez-vous que votre configuration par défaut inclut la création du répertoire personnel.

### 3.2 Création d'un Utilisateur avec un Répertoire Personnel

```bash
sudo useradd -m -d /home/johndoe -s /bin/bash -c "John Doe" johndoe
```

- **Options Utilisées** :
  - `-m` : Crée le répertoire personnel.
  - `-d /home/johndoe` : Spécifie le chemin du répertoire personnel.
  - `-s /bin/bash` : Définit le shell par défaut.
  - `-c "John Doe"` : Ajoute un commentaire descriptif.

- **Résultat** :
  - Création de l'utilisateur **johndoe** avec un répertoire personnel à `/home/johndoe`.
  - Shell par défaut : `/bin/bash`.
  - Commentaire : "John Doe".

### 3.3 Création d'un Utilisateur avec des Groupes Supplémentaires

```bash
sudo useradd -m -G sudo,developers -s /bin/bash -c "Jane Smith" janesmith
```

- **Options Utilisées** :
  - `-m` : Crée le répertoire personnel.
  - `-G sudo,developers` : Ajoute l'utilisateur aux groupes **sudo** et **developers**.
  - `-s /bin/bash` : Définit le shell par défaut.
  - `-c "Jane Smith"` : Ajoute un commentaire descriptif.

- **Résultat** :
  - Création de l'utilisateur **janesmith**.
  - Ajout aux groupes **sudo** (pour les privilèges administratifs) et **developers** (pour les permissions spécifiques aux développeurs).

### 3.4 Création d'un Compte Système

```bash
sudo useradd -r -s /usr/sbin/nologin -c "Service SSH" sshd
```

- **Options Utilisées** :
  - `-r` : Crée un compte système avec un UID inférieur à 1000.
  - `-s /usr/sbin/nologin` : Définit un shell qui empêche la connexion interactive.
  - `-c "Service SSH"` : Ajoute un commentaire descriptif.

- **Résultat** :
  - Création du compte **sshd** utilisé par le démon SSH.
  - Aucun accès interactif possible pour cet utilisateur.

### 3.5 Spécifier un UID lors de la Création

```bash
sudo useradd -m -u 1500 -s /bin/bash user1500
```

- **Options Utilisées** :
  - `-m` : Crée le répertoire personnel.
  - `-u 1500` : Attribue l'UID 1500 à l'utilisateur.
  - `-s /bin/bash` : Définit le shell par défaut.

- **Résultat** :
  - Création de l'utilisateur **user1500** avec un UID spécifique de 1500.

### 3.6 Création d'un Utilisateur avec un Mot de Passe Crypté

**Attention** : Passer le mot de passe directement via la ligne de commande peut être un risque de sécurité, car il peut être visible dans l'historique des commandes. Il est recommandé d'utiliser `passwd` après la création de l'utilisateur.

```bash
sudo useradd -m -p $(openssl passwd -1 MonMotDePasseSecurise) secureuser
```

- **Options Utilisées** :
  - `-m` : Crée le répertoire personnel.
  - `-p` : Définit le mot de passe crypté.

- **Résultat** :
  - Création de l'utilisateur **secureuser** avec le mot de passe défini.

**Note** : Pour des raisons de sécurité, préférez définir le mot de passe après la création avec la commande `passwd` :

```bash
sudo passwd secureuser
```

---

## 4. Différences entre `useradd` et `adduser`

### 4.1 `useradd`

- **Type** : Commande de bas niveau.
- **Utilisation** : Plus flexible et offre un contrôle granulaire, mais nécessite l'utilisation d'options pour configurer correctement les utilisateurs.
- **Interface** : Non interactive, nécessite la spécification explicite des paramètres via des options.

### 4.2 `adduser`

- **Type** : Script de haut niveau (souvent basé sur `useradd`).
- **Utilisation** : Plus convivial et interactif, facilite la création d'utilisateurs avec des invites pour définir les paramètres.
- **Interface** : Interactive, guide l'utilisateur à travers le processus de création.

### 4.3 Choisir entre `useradd` et `adduser`

- **Scripts et Automatisation** : Utilisez **`useradd`** pour les scripts automatisés où l'interaction humaine n'est pas souhaitée.
- **Gestion Manuelle** : Utilisez **`adduser`** pour une gestion manuelle et plus conviviale des utilisateurs, surtout si vous préférez une interface interactive.

**Exemple d'utilisation interactive avec `adduser`** :

```bash
sudo adduser johndoe
```

Cette commande vous guidera à travers plusieurs invites pour définir le mot de passe, le nom complet, etc.

---

## 5. Bonnes Pratiques et Considérations de Sécurité

### 5.1 Utiliser des Options Appropriées

- **Créer le Répertoire Personnel** : Toujours utiliser l'option `-m` pour créer le répertoire personnel lors de la création d'un nouvel utilisateur.
  
  ```bash
  sudo useradd -m -s /bin/bash newuser
  ```

- **Définir le Shell par Défaut** : Utilisez l'option `-s` pour spécifier le shell, évitant ainsi les shells non sécurisés.
  
  ```bash
  sudo useradd -m -s /bin/bash newuser
  ```

### 5.2 Gestion des Groupes

- **Groupes Secondaires** : Ajoutez les utilisateurs aux groupes secondaires nécessaires pour accorder des permissions spécifiques sans leur donner des privilèges excessifs.
  
  ```bash
  sudo useradd -m -G sudo,developers newuser
  ```

- **Créer des Groupes Personnalisés** : Pour les rôles spécifiques (par exemple, **comptabilite**, **devops**, **webdev**), créez des groupes personnalisés et attribuez les utilisateurs en conséquence.
  
  ```bash
  sudo groupadd comptabilite
  sudo useradd -m -G comptabilite newuser
  ```

### 5.3 Sécurité des Comptes

- **Définir des Mots de Passe Sécurisés** : Après la création d’un utilisateur, définissez un mot de passe fort avec la commande `passwd`.
  
  ```bash
  sudo passwd newuser
  ```

- **Limiter les Privilèges** : N'accordez des privilèges administratifs qu'aux utilisateurs qui en ont besoin. Utilisez des groupes comme **sudo** pour gérer les accès privilégiés.

### 5.4 Configuration de UMASK

- **UMASK 0077** : Comme discuté précédemment, configurez un UMASK restrictif pour assurer que les nouveaux fichiers et répertoires sont privés par défaut.
  
  ```bash
  sudo sed -i 's/^UMASK.*/UMASK   0077/g' /etc/login.defs
  ```

- **Permissions des Répertoires /home** : Appliquez des permissions strictes sur les répertoires personnels pour empêcher l'accès non autorisé.
  
  ```bash
  sudo chmod 770 /home/*
  ```

### 5.5 Documentation et Audit

- **Documenter les Comptes Utilisateurs** : Tenez un registre des utilisateurs créés, de leurs rôles et de leurs groupes d'appartenance.
- **Auditer Régulièrement les Comptes** : Vérifiez périodiquement les comptes utilisateurs pour identifier et supprimer les comptes inactifs ou non nécessaires.

---

## 6. Gestion Avancée des Utilisateurs

### 6.1 Modifier un Utilisateur Existants

Pour modifier les paramètres d'un utilisateur existant, utilisez la commande **`usermod`**.

**Exemple** : Ajouter un utilisateur au groupe **sudo**.

```bash
sudo usermod -aG sudo johndoe
```

- **Options** :
  - `-aG` : Ajoute l'utilisateur à un groupe sans retirer l'appartenance à d'autres groupes.

### 6.2 Supprimer un Utilisateur

Pour supprimer un utilisateur, utilisez la commande **`userdel`**.

**Exemple** : Supprimer un utilisateur et son répertoire personnel.

```bash
sudo userdel -r johndoe
```

- **Options** :
  - `-r` : Supprime le répertoire personnel de l'utilisateur et son mail spool.

### 6.3 Verrouiller ou Déverrouiller un Compte Utilisateur

**Verrouiller un compte** :

```bash
sudo usermod -L johndoe
```

- **Option** :
  - `-L` : Verrouille le mot de passe de l'utilisateur, empêchant toute connexion.

**Déverrouiller un compte** :

```bash
sudo usermod -U johndoe
```

- **Option** :
  - `-U` : Déverrouille le mot de passe de l'utilisateur.

### 6.4 Définir des Politiques de Mot de Passe

Utilisez la commande **`chage`** pour gérer les politiques de mot de passe d’un utilisateur.

**Exemple** : Forcer un utilisateur à changer son mot de passe lors de sa prochaine connexion.

```bash
sudo chage -d 0 johndoe
```

- **Options** :
  - `-d 0` : Définit la date du dernier changement de mot de passe à 0, forçant un changement au prochain login.

**Autres options** :

- **Définir la durée maximale d'un mot de passe** :
  
  ```bash
  sudo chage -M 90 johndoe
  ```

- **Définir la durée minimale avant qu’un mot de passe puisse être changé** :
  
  ```bash
  sudo chage -m 7 johndoe
  ```

- **Définir une alerte avant l'expiration du mot de passe** :
  
  ```bash
  sudo chage -W 14 johndoe
  ```

---

## 7. Différences Clés entre `useradd` et `adduser`

### 7.1 `useradd`

- **Type** : Commande de bas niveau.
- **Flexibilité** : Offre une personnalisation fine via de nombreuses options.
- **Interface** : Non interactive, nécessite l'utilisation d'options pour définir les paramètres.

### 7.2 `adduser`

- **Type** : Script de haut niveau, souvent basé sur `useradd`.
- **Facilité d'utilisation** : Interactive, guide l'utilisateur à travers le processus de création.
- **Configuration par Défaut** : Configure automatiquement le répertoire personnel, définit le mot de passe, etc.

### 7.3 Choisir entre `useradd` et `adduser`

- **Automatisation** : Utilisez **`useradd`** dans les scripts automatisés où une interaction utilisateur n'est pas souhaitée.
- **Gestion Manuelle** : Utilisez **`adduser`** pour une gestion manuelle et plus conviviale des utilisateurs.

**Exemple d'utilisation de `adduser`** :

```bash
sudo adduser johndoe
```

Cette commande vous invitera à fournir des informations supplémentaires comme le mot de passe, le nom complet, etc.

---

## 8. Bonnes Pratiques et Considérations de Sécurité

### 8.1 Principe du Moindre Privilège

- **Attribuer des Permissions Minimales** : N’accordez aux utilisateurs que les permissions nécessaires pour accomplir leurs tâches.
- **Utiliser des Groupes** : Gérez les permissions via des groupes plutôt que d'attribuer des permissions directement aux utilisateurs.

### 8.2 Sécuriser les Répertoires Personnels

- **Permissions Restrictives** : Configurez un **umask** restrictif (comme **0077**) pour assurer que les nouveaux fichiers et répertoires sont privés.
  
  ```bash
  sudo sed -i 's/^UMASK.*/UMASK   0077/g' /etc/login.defs
  sudo chmod 770 /home/*
  ```

- **Isoler les Groupes** : Assurez-vous que chaque utilisateur a un groupe unique pour éviter les accès non autorisés par le biais des groupes.

### 8.3 Gestion des Mots de Passe

- **Forcer le Changement de Mot de Passe** : Lors de la création d'un nouvel utilisateur, forcez le changement du mot de passe à la première connexion.
  
  ```bash
  sudo useradd -m -s /bin/bash newuser
  sudo passwd newuser
  sudo chage -d 0 newuser
  ```

- **Politiques de Complexité** : Implémentez des politiques de complexité et d'expiration des mots de passe pour renforcer la sécurité.

### 8.4 Surveillance et Audit

- **Logs** : Surveillez les logs pour détecter toute activité suspecte liée aux comptes utilisateurs.
  
  ```bash
  sudo tail -f /var/log/auth.log
  ```

- **Audits Réguliers** : Effectuez des audits réguliers des comptes utilisateurs pour identifier et supprimer les comptes inactifs ou non nécessaires.

### 8.5 Sécuriser les Composants Système

- **Éviter l'Utilisation de `root`** : N'utilisez pas le compte **root** pour les tâches quotidiennes. Créez des utilisateurs avec des privilèges appropriés via des groupes comme **sudo**.
  
  ```bash
  sudo useradd -m -G sudo adminuser
  sudo passwd adminuser
  sudo chage -d 0 adminuser
  ```

- **Limiter l'Accès SSH** : Configurez SSH pour limiter l'accès aux utilisateurs autorisés uniquement.
  
  - Éditez le fichier **`/etc/ssh/sshd_config`** :
    
    ```plaintext
    AllowUsers adminuser johndoe
    ```
  
  - Redémarrez le service SSH :
    
    ```bash
    sudo systemctl restart sshd
    ```

### 8.6 Utiliser des Scripts d'Automatisation

- **Scripts Shell** : Utilisez des scripts shell pour automatiser la création et la gestion des utilisateurs, surtout dans des environnements à grande échelle.
  
  **Exemple** : Script pour créer un utilisateur avec des paramètres spécifiques.

  ```bash
  #!/bin/bash

  if [ "$#" -ne 2 ]; then
      echo "Usage: $0 NOM_UTILISATEUR MOT_DE_PASSE"
      exit 1
  fi

  NOM_UTILISATEUR=$1
  MOT_DE_PASSE=$2

  sudo useradd -m -s /bin/bash -G sudo,developers -c "Nouvel Utilisateur" "$NOM_UTILISATEUR"
  echo "$NOM_UTILISATEUR:$MOT_DE_PASSE" | sudo chpasswd
  sudo chage -d 0 "$NOM_UTILISATEUR"

  echo "Utilisateur $NOM_UTILISATEUR créé avec succès."
  ```

---

## 9. Conclusion

La commande **`useradd`** est un outil essentiel pour la gestion des utilisateurs sous Linux, offrant une flexibilité et un contrôle granulaire sur les paramètres des comptes utilisateurs. En maîtrisant **`useradd`**, vous pouvez créer et gérer efficacement des comptes utilisateurs adaptés aux besoins spécifiques de votre environnement tout en assurant la sécurité et la conformité de votre système.

**Rappel** :

- **Utilisez les options appropriées** pour configurer les comptes utilisateurs de manière sécurisée.
- **Suivez les bonnes pratiques** en matière de gestion des utilisateurs et des permissions pour renforcer la sécurité de votre système.
- **Automatisez** la gestion des utilisateurs dans les environnements à grande échelle pour gagner du temps et réduire les erreurs.

---

## Ressources Supplémentaires

- **Pages de Manuel** :
  - `man useradd`
  - `man usermod`
  - `man userdel`
  - `man passwd`
  - `man chage`
  
- **Documentation Officielle** :
  - [Documentation Debian sur la Gestion des Utilisateurs](https://www.debian.org/doc/manuals/debian-reference/ch04.en.html)
  - [Ubuntu Community Help Wiki - /etc/login.defs](https://help.ubuntu.com/community/login.defs)
  
- **Livres** :
  - *Linux System Administration* par Tom Adelstein et Bill Lubanovic
  - *The Linux Command Line* par William Shotts
  
- **Tutoriels en Ligne** :
  - [DigitalOcean - How To Add and Delete Users on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-ubuntu-20-04)
  - [Linode - How to Create a New User on Ubuntu 20.04](https://www.linode.com/docs/guides/add-a-user-to-ubuntu-20-04/)

---

**Remarque** : Les commandes et les configurations mentionnées peuvent varier légèrement en fonction de la distribution Linux utilisée et de sa version. Assurez-vous d'adapter les instructions à votre environnement spécifique et de tester les commandes dans un environnement contrôlé avant de les appliquer en production.