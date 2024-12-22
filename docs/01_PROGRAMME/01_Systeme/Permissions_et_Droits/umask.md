---
title: umask
date: 2024-10-23
date de modification: 2024-10-23
timestamp: 14:20
tags:
  - ressource
status:
  - En cours
type de note:
  - ressource
référence:
  - "[[umask-0077]]"
  - "[[umask_login-profil]]"
source:
  - chatgpt
auteur: aGrellard
---
# Guide sur le umask par défaut pour sécuriser un serveur Debian

## Introduction

La sécurisation d'un serveur Debian passe par plusieurs étapes, dont la configuration appropriée des permissions des fichiers et des répertoires. Le **umask** (User file creation MASK) est un paramètre important qui détermine les permissions par défaut des nouveaux fichiers et répertoires créés par les utilisateurs. En définissant correctement le umask par défaut, vous pouvez améliorer la sécurité globale de votre système en limitant l'accès non autorisé aux fichiers.

Ce guide vous expliquera :

- Ce qu'est le umask et comment il fonctionne.
- Les valeurs de umask recommandées pour différents scénarios.
- Comment configurer le umask par défaut pour les utilisateurs.
- Les implications de la modification du umask sur la sécurité.

---

## 1. Comprendre le umask

### 1.1 Qu'est-ce que le umask ?

Le **umask** est un masque de permission qui contrôle les permissions par défaut des nouveaux fichiers et répertoires créés par un utilisateur. Il définit quelles permissions doivent être **retirées** des permissions par défaut.

- **Fichiers** : Par défaut, les fichiers sont créés avec des permissions **666** (lecture et écriture pour tous).
- **Répertoires** : Par défaut, les répertoires sont créés avec des permissions **777** (lecture, écriture et exécution pour tous).

Le umask soustrait des permissions à ces valeurs par défaut.

### 1.2 Comment fonctionne le umask ?

Le umask est une valeur octale à trois chiffres, similaire aux permissions Unix. Chaque chiffre représente les permissions pour :

- **Premier chiffre** : L'utilisateur propriétaire (u)
- **Deuxième chiffre** : Le groupe propriétaire (g)
- **Troisième chiffre** : Les autres utilisateurs (o)

Les permissions possibles sont :

- **4** : Lecture (r)
- **2** : Écriture (w)
- **1** : Exécution (x)

Pour déterminer les permissions finales, on soustrait le umask des permissions par défaut.

**Formule** :

```
Permissions finales = Permissions par défaut - umask
```

---

## 2. Valeurs de umask recommandées

### 2.1 Umask courant par défaut

Sur de nombreuses distributions, y compris Debian, le umask par défaut est **0022**. Cela signifie que :

- **Fichiers** : Permissions finales de **644** (rw-r--r--)
- **Répertoires** : Permissions finales de **755** (rwxr-xr-x)

### 2.2 Umask pour une sécurité renforcée

Pour améliorer la sécurité, il est recommandé d'utiliser un umask plus restrictif, tel que **0027** ou **0077**.

#### Umask 0027

- **Fichiers** : Permissions finales de **640** (rw-r-----)
- **Répertoires** : Permissions finales de **750** (rwxr-x---)

#### Umask 0077

- **Fichiers** : Permissions finales de **600** (rw-------)
- **Répertoires** : Permissions finales de **700** (rwx------)

### 2.3 Comparaison des umask

| Umask | Fichiers (Permissions finales) | Répertoires (Permissions finales) | Usage recommandé                         |
|-------|-------------------------------|------------------------------------|------------------------------------------|
| 0022  | 644 (rw-r--r--)               | 755 (rwxr-xr-x)                    | Par défaut, usage général                |
| 0027  | 640 (rw-r-----)               | 750 (rwxr-x---)                    | Environnements multi-utilisateurs        |
| 0077  | 600 (rw-------)               | 700 (rwx------)                    | Sécurité maximale, données sensibles     |

---

## 3. Configurer le umask par défaut

### 3.1 Pour tous les utilisateurs

Pour définir le umask par défaut pour tous les utilisateurs du système, vous pouvez modifier le fichier **/etc/profile** ou **/etc/login.defs**.

#### Méthode 1 : Modifier /etc/profile

1. **Éditer le fichier** :

   ```bash
   sudo nano /etc/profile
   ```

2. **Ajouter ou modifier la ligne suivante** :

   ```bash
   umask 027
   ```

3. **Enregistrer et quitter**.

4. **Appliquer les changements** :

   Les nouveaux paramètres seront appliqués lors de la prochaine connexion. Pour les appliquer immédiatement :

   ```bash
   source /etc/profile
   ```

#### Méthode 2 : Modifier /etc/login.defs

1. **Éditer le fichier** :

   ```bash
   sudo nano /etc/login.defs
   ```

2. **Trouver la ligne commençant par UMASK** et modifier la valeur :

   ```plaintext
   UMASK 027
   ```

3. **Enregistrer et quitter**.

### 3.2 Pour un utilisateur spécifique

Vous pouvez définir le umask pour un utilisateur en modifiant ses fichiers de configuration personnels, tels que **~/.bashrc** ou **~/.profile**.

1. **Éditer le fichier** :

   ```bash
   nano ~/.bashrc
   ```

2. **Ajouter la ligne** :

   ```bash
   umask 027
   ```

3. **Enregistrer et quitter**.

4. **Appliquer les changements** :

   ```bash
   source ~/.bashrc
   ```

### 3.3 Pour des services spécifiques

Certains services ou applications peuvent avoir besoin de définir un umask particulier. Vous pouvez configurer le umask dans les fichiers de configuration du service ou dans les scripts de démarrage.

**Exemple pour Apache** :

1. **Éditer le fichier de configuration** :

   ```bash
   sudo nano /etc/apache2/envvars
   ```

2. **Ajouter la ligne** :

   ```bash
   umask 027
   ```

3. **Redémarrer le service** :

   ```bash
   sudo systemctl restart apache2
   ```

---

## 4. Implications de la modification du umask

### 4.1 Impact sur les permissions

- **Umask plus restrictif** : Limite l'accès aux fichiers et répertoires nouvellement créés.
- **Umask trop restrictif** : Peut causer des problèmes si les fichiers doivent être accessibles par d'autres utilisateurs ou services.

### 4.2 Considérations pour les environnements multi-utilisateurs

- **Umask 0027** : Bon compromis pour les environnements où les utilisateurs travaillent en groupe. Les autres utilisateurs n'auront pas accès aux fichiers.
- **Umask 0077** : Convient pour des comptes administratifs ou des utilisateurs manipulant des données sensibles.

### 4.3 Applications spécifiques

- Certains programmes créent des fichiers qui doivent être accessibles par d'autres utilisateurs ou services. Vérifiez la compatibilité avant de modifier le umask.

---

## 5. Vérifier le umask actuel

Pour connaître le umask actuel de votre session, exécutez :

```bash
umask
```

La sortie sera sous forme octale, par exemple **0022**.

---

## 6. Exemples pratiques

### 6.1 Définir un umask de 0027 pour tous les utilisateurs

1. **Modifier /etc/profile** :

   ```bash
   sudo nano /etc/profile
   ```

2. **Ajouter ou modifier la ligne** :

   ```bash
   umask 027
   ```

3. **Enregistrer, quitter et appliquer** :

   ```bash
   source /etc/profile
   ```

### 6.2 Définir un umask de 0077 pour l'utilisateur root

1. **Éditer le fichier ~/.bashrc de root** :

   ```bash
   sudo nano /root/.bashrc
   ```

2. **Ajouter la ligne** :

   ```bash
   umask 077
   ```

3. **Enregistrer, quitter et appliquer** :

   ```bash
   source /root/.bashrc
   ```

---

## 7. Bonnes pratiques

- **Tester avant de déployer** : Avant de définir un umask global, testez-le avec un utilisateur pour vous assurer qu'il n'y a pas d'effets indésirables.
- **Documenter les changements** : Notez les modifications apportées pour faciliter la maintenance future.
- **Considérer les besoins des applications** : Certains logiciels peuvent nécessiter des permissions spécifiques. Assurez-vous que le umask choisi ne perturbe pas leur fonctionnement.

---

## 8. Conclusion

Le choix du umask par défaut est une étape importante dans la sécurisation d'un serveur Debian. En définissant un umask plus restrictif, vous réduisez le risque d'accès non autorisé aux fichiers créés par les utilisateurs. Cependant, il est essentiel de trouver un équilibre entre la sécurité et la fonctionnalité, en tenant compte des besoins spécifiques de votre environnement et des applications utilisées.

---

## Ressources supplémentaires

- **Page de manuel du umask** : `man umask`
- **Documentation Debian sur la sécurité** : [Securing Debian Manual](https://www.debian.org/doc/manuals/securing-debian-howto/)
- **Guide sur les permissions Unix** : Recherchez des articles détaillés sur la gestion des permissions sous Unix/Linux.

---

**Remarque** : Les commandes et les fichiers mentionnés peuvent varier en fonction de la version de Debian utilisée. Assurez-vous d'adapter les instructions à votre environnement spécifique.

---