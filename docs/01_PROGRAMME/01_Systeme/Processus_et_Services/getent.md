---
title: getent
date: 2024-10-23
date de modification: 2024-10-23
timestamp: 14:21
tags:
  - ressource
status:
  - En cours
type de note:
  - ressource
référence:
  - "[[deluser]]"
  - "[[groups]]"
  - "[[groupadd]]"
  - "[[groupdel]]"
  - "[[02_RESSOURCES/Linux/programme/03_Gestion_des_Utilisateurs/Utilisateurs_et_Groupes/useradd|useradd]]"
source:
  - chatgpt
auteur: aGrellard
---
# Guide complet sur la commande `getent` sous Linux

## Introduction

La commande **`getent`** est un outil puissant sous Linux qui permet d'accéder aux entrées des bases de données administratives, telles que les comptes utilisateurs, les groupes, les hôtes, les services, etc., en interrogeant les services de noms configurés, comme les fichiers locaux, NIS, DNS ou LDAP. Elle est particulièrement utile pour récupérer des informations de manière standardisée, sans avoir à connaître les détails de la configuration du système de noms.

Ce guide détaillé vous expliquera :

- Ce qu'est la commande `getent` et comment elle fonctionne.
- Les bases de données auxquelles `getent` peut accéder.
- Comment utiliser `getent` avec des exemples pratiques.
- Les avantages de l'utilisation de `getent` par rapport à d'autres commandes.
- Quelques cas d'utilisation courants.

---

## 1. Comprendre la commande `getent`

### 1.1 Qu'est-ce que `getent` ?

- **`getent`** est l'abréviation de **"get entries"**.
- Elle permet de récupérer des entrées depuis les bases de données administratives spécifiées dans le **NSS (Name Service Switch)**, comme défini dans le fichier **`/etc/nsswitch.conf`**.
- Les bases de données accessibles incluent : **passwd**, **group**, **hosts**, **services**, **protocols**, **networks**, **ethers**, etc.

### 1.2 Pourquoi utiliser `getent` ?

- **Uniformité** : Fournit une interface unique pour interroger différentes bases de données.
- **Transparence** : Interroge les services de noms configurés sans avoir à connaître leur implémentation (fichiers locaux, NIS, LDAP, etc.).
- **Facilité d'utilisation** : Simplifie la récupération d'informations système pour les scripts et les administrateurs.

---

## 2. Bases de données prises en charge

Les bases de données que `getent` peut interroger incluent :

- **passwd** : Informations sur les comptes utilisateurs.
- **group** : Informations sur les groupes.
- **hosts** : Noms d'hôtes et adresses IP.
- **services** : Services réseau (ports et protocoles).
- **protocols** : Protocoles réseau.
- **networks** : Réseaux.
- **ethers** : Adresses matérielles Ethernet.
- **shadow** : Informations sur les mots de passe des utilisateurs (nécessite des privilèges).
- **netgroup** : Groupes de réseaux (NIS).

---

## 3. Utilisation de `getent`

### 3.1 Syntaxe générale

```bash
getent base_de_données [clé ...]
```

- **base_de_données** : Le nom de la base de données à interroger (par exemple, `passwd`, `group`, `hosts`).
- **clé** (facultatif) : Une ou plusieurs clés pour filtrer les résultats (par exemple, un nom d'utilisateur, un nom de groupe, un nom d'hôte).

### 3.2 Exemples pratiques

#### 3.2.1 Récupérer toutes les entrées de la base `passwd`

```bash
getent passwd
```

- Affiche toutes les entrées des utilisateurs, similaires au contenu de `/etc/passwd`, mais en incluant les utilisateurs provenant d'autres sources (comme LDAP).

#### 3.2.2 Récupérer les informations pour un utilisateur spécifique

```bash
getent passwd nom_utilisateur
```

- Exemple :

  ```bash
  getent passwd alice
  ```

- Affiche l'entrée de l'utilisateur `alice`.

#### 3.2.3 Récupérer toutes les entrées de la base `group`

```bash
getent group
```

- Liste tous les groupes disponibles sur le système.

#### 3.2.4 Récupérer les informations pour un groupe spécifique

```bash
getent group nom_groupe
```

- Exemple :

  ```bash
  getent group sudo
  ```

- Affiche les informations du groupe `sudo`.

#### 3.2.5 Récupérer les entrées de la base `hosts`

```bash
getent hosts
```

- Affiche les entrées de résolution des noms d'hôtes.

#### 3.2.6 Récupérer l'adresse IP d'un hôte spécifique

```bash
getent hosts nom_domaine_ou_adresse_ip
```

- Exemple :

  ```bash
  getent hosts www.example.com
  ```

- Renvoie l'adresse IP associée à `www.example.com`.

#### 3.2.7 Récupérer les services réseau

```bash
getent services
```

- Liste les services réseau définis.

#### 3.2.8 Récupérer les informations pour un service spécifique

```bash
getent services nom_service
```

- Exemple :

  ```bash
  getent services ssh
  ```

- Affiche le port et le protocole pour le service `ssh`.

---

## 4. Avantages de l'utilisation de `getent`

### 4.1 Indépendance du backend

- **Transparence** : Vous n'avez pas à savoir si les informations proviennent de fichiers locaux, d'un serveur NIS, LDAP ou autre.
- **Compatibilité** : Fonctionne de manière cohérente quelle que soit la configuration du système.

### 4.2 Sécurité

- **Contrôle d'accès** : Les permissions d'accès aux données sont respectées. Par exemple, pour accéder à la base `shadow`, vous devez avoir les privilèges appropriés.

### 4.3 Simplicité pour les scripts

- **Automatisation** : Facile à intégrer dans des scripts shell pour automatiser des tâches d'administration.
- **Format standard** : Les sorties sont dans un format standard, facilitant le traitement avec d'autres outils (comme `awk`, `grep`, `cut`).

---

## 5. Cas d'utilisation courants

### 5.1 Vérifier l'existence d'un utilisateur ou d'un groupe

#### Vérifier si un utilisateur existe

```bash
if getent passwd nom_utilisateur > /dev/null; then
    echo "L'utilisateur existe."
else
    echo "L'utilisateur n'existe pas."
fi
```

#### Vérifier si un groupe existe

```bash
if getent group nom_groupe > /dev/null; then
    echo "Le groupe existe."
else
    echo "Le groupe n'existe pas."
fi
```

### 5.2 Récupérer l'UID ou le GID d'un utilisateur ou d'un groupe

#### Obtenir l'UID d'un utilisateur

```bash
getent passwd nom_utilisateur | cut -d: -f3
```

#### Obtenir le GID d'un groupe

```bash
getent group nom_groupe | cut -d: -f3
```

### 5.3 Résolution de noms d'hôtes

#### Obtenir l'adresse IP d'un hôte

```bash
getent hosts nom_domaine
```

- Alternative à `nslookup` ou `dig`, utilisant les services de noms configurés.

### 5.4 Liste des membres d'un groupe

```bash
getent group nom_groupe | awk -F: '{print $4}'
```

- Affiche les membres du groupe spécifié.

---

## 6. Bases de données supplémentaires

### 6.1 `shadow`

- Contient les informations sensibles sur les mots de passe des utilisateurs.
- **Accès restreint** : Seul l'utilisateur root ou un utilisateur avec les privilèges appropriés peut y accéder.

#### Exemple :

```bash
sudo getent shadow nom_utilisateur
```

### 6.2 `services`, `protocols`, `networks`

- **`services`** : Informations sur les services réseau (ports et protocoles).
- **`protocols`** : Informations sur les protocoles réseau.
- **`networks`** : Informations sur les réseaux.

---

## 7. Configuration du Name Service Switch (NSS)

### 7.1 Fichier `/etc/nsswitch.conf`

- Définit l'ordre des services de noms pour chaque base de données.
- Exemple d'entrée pour la base `passwd` :

  ```plaintext
  passwd:         files ldap
  ```

- Cela signifie que pour la base `passwd`, le système cherchera d'abord dans les fichiers locaux (`/etc/passwd`), puis dans LDAP.

### 7.2 Impact sur `getent`

- `getent` suit l'ordre défini dans `/etc/nsswitch.conf`.
- Si une base de données n'est pas configurée pour utiliser certains services, `getent` ne les interrogera pas.

---

## 8. Limitations et considérations

- **Permissions** : Certaines bases de données comme `shadow` nécessitent des privilèges élevés.
- **Disponibilité** : `getent` dépend des services de noms configurés et disponibles.
- **Performances** : Interroger des services distants (comme LDAP) peut prendre plus de temps.

---

## 9. Conclusion

La commande `getent` est un outil essentiel pour les administrateurs système sous Linux, offrant un moyen uniforme et flexible d'accéder aux informations des bases de données administratives. En utilisant `getent`, vous pouvez interroger diverses sources d'informations sans vous soucier de la manière dont elles sont implémentées ou configurées, ce qui simplifie grandement les tâches d'administration et de scriptage.

---

## Ressources supplémentaires

- **Page de manuel de getent** : `man getent`
- **Documentation sur NSS** : `man nsswitch.conf`
- **Administration système Linux** : Recherchez des guides et des livres pour approfondir vos connaissances en administration système.

---

**Remarque** : Les exemples et commandes fournis sont génériques et peuvent nécessiter des ajustements en fonction de la configuration spécifique de votre système.

---