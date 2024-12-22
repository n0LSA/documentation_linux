---
title: umask_login-profil
date: 2024-10-23
date de modification: 2024-10-23
timestamp: 14:18
tags:
  - ressource
status:
  - En cours
type de note:
  - ressource
référence:
  - "[[umask]]"
  - "[[umask-0077]]"
source:
  - chatgpt
auteur: aGrellard
---
## `/etc/profile` et `/etc/login.defs`

La configuration de la **umask** (ou "User Mask") dans Linux permet de définir les permissions par défaut lors de la création de fichiers et de répertoires. Le choix entre les fichiers `/etc/profile` et `/etc/login.defs` pour définir la **umask** dépend du contexte et de l'impact que tu souhaites donner à cette configuration.

Voici les différences entre ces deux fichiers dans le cadre de la modification de la **umask** :


### 1. **/etc/profile**

- **Contexte** : Ce fichier est utilisé pour configurer l'environnement de tous les utilisateurs lors de l'ouverture d'une session interactive (shell de connexion).
- **Fonctionnement** : Lorsqu'un utilisateur se connecte à un système (localement ou via SSH), le fichier `/etc/profile` est exécuté par le shell de connexion (par exemple `bash` ou `zsh`). Ce fichier définit diverses variables d'environnement et peut également inclure la configuration de la **umask**.
- **Utilisation pour umask** : Si tu définis la **umask** dans `/etc/profile`, elle sera appliquée uniquement aux utilisateurs qui lancent un shell de connexion. Cela signifie que la configuration ne s'appliquera qu'aux sessions interactives.
  
  Exemple de modification dans `/etc/profile` :
  ```bash
  umask 022
  ```

  **Impact** : La **umask** définie dans `/etc/profile** s'applique uniquement aux utilisateurs qui ouvrent une session shell interactive.

- **Limitation** : Ce fichier n'affecte pas les processus qui ne démarrent pas une session interactive, comme les services ou les processus démarrés au démarrage du système.

### 2. **/etc/login.defs**

- **Contexte** : Ce fichier contient des paramètres de configuration utilisés par les programmes relatifs à la gestion des utilisateurs et des connexions, comme `login`, `useradd`, etc. Il permet de définir des valeurs par défaut pour diverses opérations du système, y compris la **umask**.
- **Fonctionnement** : Lorsque le système gère une connexion utilisateur via un programme de connexion comme `login`, `su`, ou d'autres services de gestion d'utilisateur, il consulte le fichier `/etc/login.defs` pour appliquer certaines configurations globales, y compris la **umask**.
  
  Exemple de modification dans `/etc/login.defs` :
  ```bash
  UMASK 022
  ```

  **Impact** : La **umask** définie dans `/etc/login.defs** s'applique globalement à tous les utilisateurs lors de la création de nouveaux fichiers, même en dehors des sessions interactives. Cela inclut les processus lancés en arrière-plan, les services, les démons, ou les connexions via des services comme `SSH` qui passent par un programme de gestion de connexions.

- **Utilisation pour umask** : Utiliser `/etc/login.defs` est plus adapté si tu veux appliquer la **umask** de manière plus large, y compris pour les processus non interactifs.

### Principales différences :

| Caractéristique                  | `/etc/profile`                                 | `/etc/login.defs`                            |
| -------------------------------- | ---------------------------------------------- | -------------------------------------------- |
| **Type d'utilisateurs affectés** | Sessions shell interactives uniquement         | Toutes les connexions gérées par `login`     |
| **Moment de l'exécution**        | Lors du démarrage d'une session interactive    | Lors de la gestion des connexions            |
| **Type de fichiers affectés**    | Fichiers créés par l'utilisateur dans le shell | Fichiers créés globalement par l'utilisateur |
| **Processus non interactifs**    | Non (n'affecte pas les services, démons, etc.) | Oui (affecte tous les processus)             |

### Quel fichier choisir pour la **umask** ?
- Si tu souhaites que la **umask** s'applique uniquement aux **sessions utilisateur interactives** (lorsqu'un utilisateur ouvre un shell), alors `/etc/profile` est le fichier à modifier.
- Si tu veux que la **umask** soit appliquée à tous les processus, y compris ceux lancés par des **services systèmes** ou lors de connexions gérées par `login`, utilise plutôt `/etc/login.defs`.

Pour une configuration plus générale, affectant à la fois les connexions interactives et non interactives, il est souvent plus efficace de définir la **umask** dans `/etc/login.defs`. Toutefois, pour les environnements spécifiques comme un shell interactif, `/etc/profile` est plus approprié.

##  `/etc/profile` et `/etc/login.defs` - partie 2

Dans les contextes que tu mentionnes, l'application de la **umask** varie selon l'environnement dans lequel les scripts ou les services sont exécutés. Chaque environnement peut avoir ses propres règles ou mécanismes pour définir la **umask** utilisée lors de la création de fichiers et de répertoires.

### 1. **Les scripts exécutés dans un shell interactif**
Si tu exécutes des **scripts** manuellement dans un shell (zsh, bash), la **umask** utilisée sera la même que celle configurée pour ta session shell interactive. Cela signifie que la umask est héritée du fichier de configuration du shell comme `/etc/profile`, `~/.bashrc`, ou `~/.zshrc`.

- **Par exemple**, si tu as défini `umask 022` dans ton fichier `~/.zshrc`, alors **lorsque tu exécutes un script dans un terminal**, toutes les actions du script qui créent des fichiers ou des répertoires respecteront cette **umask**.
  
  Exemple :
  - Si tu exécutes ce script dans un shell interactif :
    ```bash
    #!/bin/bash
    mkdir testdir
    touch testfile
    ```
    Le répertoire **testdir** aura des permissions de `755` et le fichier **testfile** aura des permissions de `644`, car c’est la umask `022` (par défaut ou définie dans le shell) qui s'applique.

### 2. **Les scripts placés dans `/usr/local/bin` (ou exécutés via cron, etc.)**
Les scripts placés dans des répertoires comme `/usr/local/bin` ou exécutés automatiquement via un planificateur comme **cron** n’héritent pas forcément de la umask de l’utilisateur courant. Leur comportement dépend souvent de la manière dont ces scripts sont invoqués.

#### **a. Scripts dans `/usr/local/bin` exécutés manuellement**
- Si tu exécutes manuellement un script qui se trouve dans `/usr/local/bin` via un shell (zsh, bash), alors la **umask** appliquée sera celle de ta session shell, comme mentionné dans le point précédent. Cela dépend de ce qui est défini dans `/etc/profile`, `~/.bashrc`, `~/.zshrc`, ou équivalent.

#### **b. Scripts exécutés automatiquement (ex. via cron ou at)**
- **cron** et d’autres mécanismes d’automatisation ont leur propre contexte d’exécution, et ils peuvent ne pas hériter de la umask définie dans les fichiers de configuration du shell interactif.
- Par défaut, **cron** n'utilise pas le fichier `/etc/profile`, donc la umask par défaut pourrait être différente de celle utilisée dans un shell interactif. Si tu veux définir une **umask** spécifique dans un script exécuté par cron, il est conseillé de définir explicitement la **umask** au début du script.

  Exemple d’un script cron avec une umask définie :
  ```bash
  #!/bin/bash
  umask 022  # Définit la umask à 022 pour ce script
  mkdir /path/to/directory
  ```

### 3. **Les services dans `/etc/systemd/system/`**
Les services définis dans **systemd** (fichiers dans `/etc/systemd/system/`) ne suivent pas les règles de **umask** de l'environnement utilisateur. Leur comportement est contrôlé par **systemd** lui-même. Si tu veux définir une umask spécifique pour un service, tu peux le faire dans le fichier d’unité **systemd** correspondant.

#### **a. Configurer la umask pour un service systemd**
Pour un service **systemd**, tu peux spécifier explicitement la **umask** dans le fichier d’unité de service en utilisant la directive `UMask`.

- Exemple d'un fichier d’unité systemd (`/etc/systemd/system/monservice.service`) avec une **umask** définie :
```ini
[Unit]
Description=Mon Service Exemple

[Service]
ExecStart=/usr/local/bin/mon_script.sh
UMask=027  # Définit la umask à 027 pour ce service

[Install]
WantedBy=multi-user.target
```

  Dans cet exemple :
  - La ligne `UMask=027` définit la **umask** pour ce service spécifique. Cela signifie que tous les fichiers ou répertoires créés par ce service auront des permissions basées sur cette **umask**.
  - Les fichiers créés par ce service auront des permissions de `750` pour les répertoires et `640` pour les fichiers (en fonction de la umask `027`).

#### **b. Sans UMask spécifié dans systemd**
- Si aucune **umask** n'est spécifiée dans le fichier d’unité systemd, la umask par défaut de **systemd** sera utilisée. Cela pourrait être la umask par défaut du système (souvent `022`), ou bien la umask configurée pour l’utilisateur système sous lequel le service est exécuté.

### Récapitulatif :

| **Contexte**                | **Quelle umask est utilisée ?**                                              |
|-----------------------------|------------------------------------------------------------------------------|
| **Shell interactif (zsh, bash)** | La umask définie dans `/etc/profile`, `~/.bashrc`, `~/.zshrc`, ou équivalent. |
| **Scripts dans `/usr/local/bin` exécutés manuellement** | La umask de la session shell de l'utilisateur (définie dans `~/.bashrc`, `~/.zshrc`). |
| **Scripts automatisés (via cron, etc.)** | Utilise la umask par défaut du système, sauf si spécifié dans le script. |
| **Services systemd** | La umask définie dans le fichier d’unité systemd avec la directive `UMask`. |

### Conclusion :
- **Pour les scripts** : Si tu exécutes des scripts dans un shell interactif, la umask utilisée est celle définie dans tes fichiers de configuration de shell (comme `~/.zshrc`, `~/.bashrc`, ou `/etc/profile`). Si le script est automatisé via cron ou autre, il est conseillé de définir la **umask** dans le script lui-même.
- **Pour les services systemd** : Tu peux définir une **umask** spécifique pour chaque service dans son fichier d’unité systemd à l'aide de la directive `UMask`. Si non spécifié, c'est la umask par défaut du système qui sera utilisée.

##  `/etc/profile` et `/etc/login.defs` - partie 3

Le fichier **`/etc/login.defs`** est principalement utilisé pour définir des paramètres de configuration globaux qui s'appliquent aux comptes utilisateurs lors de leur création ou pour certains aspects de leur gestion. En ce qui concerne la **umask** définie dans ce fichier, elle est utilisée dans des cas bien spécifiques, notamment par des outils liés à la gestion des utilisateurs et des connexions.

Voici dans quels cas la **umask** définie dans **`/etc/login.defs`** est utilisée :

### 1. **Création de nouveaux comptes utilisateurs**
Lorsque tu utilises des commandes comme **`useradd`** ou **`adduser`** pour créer un nouvel utilisateur, la **umask** définie dans `/etc/login.defs` est appliquée pour déterminer les permissions par défaut des fichiers et répertoires créés pour l'utilisateur, notamment le **répertoire personnel** (`home`).

- **UMASK** : Ce paramètre dans `/etc/login.defs` définit les permissions par défaut pour les fichiers et répertoires créés lorsque de nouveaux utilisateurs sont ajoutés au système. Cela affecte les répertoires et fichiers initiaux créés dans le répertoire personnel de l'utilisateur (`/home/username`).

  Par exemple :
  ```bash
  # Dans /etc/login.defs
  UMASK 077
  ```

  Cela signifie que lors de la création d'un nouvel utilisateur avec `useradd`, les répertoires et fichiers créés dans `/home/username` auront des permissions restreintes :
  - Répertoires : `700` (lecture, écriture, exécution seulement pour le propriétaire).
  - Fichiers : `600` (lecture, écriture seulement pour le propriétaire).

### 2. **Programmes de connexion système comme `login`**
Lorsqu'un utilisateur se connecte via des mécanismes de gestion des connexions tels que **`login`**, **`su`**, ou **`sshd`** (pour les connexions SSH), la **umask** peut être influencée par le paramètre défini dans `/etc/login.defs`. Toutefois, cela dépend du service de connexion utilisé, car certains services (comme `sshd`) peuvent avoir leurs propres mécanismes pour gérer la **umask** (par exemple via `/etc/ssh/sshd_config`).

- **Exemple avec `login`** : 
  Lorsqu'un utilisateur se connecte via une interface d'authentification basée sur **`login`** (comme pour une connexion physique ou en console), la **umask** définie dans `/etc/login.defs` peut s'appliquer. Si la **umask** n'est pas spécifiée ailleurs (comme dans les fichiers de profil utilisateur), c'est celle de **`/etc/login.defs`** qui sera utilisée pour définir les permissions par défaut des fichiers créés pendant cette session.

### 3. **Commande `su` (changer d'utilisateur)**
Lorsque tu utilises la commande **`su`** pour te connecter à un autre compte utilisateur sans ouvrir un shell interactif complet, la **umask** définie dans **`/etc/login.defs`** peut être utilisée pour définir les permissions des fichiers créés dans cette session.

- **Exemple** : 
  Si tu exécutes la commande suivante :
  ```bash
  su - username
  ```
  et que la **umask** est définie dans `/etc/login.defs`, cette **umask** peut être appliquée à la nouvelle session de l'utilisateur.

### 4. **Autres programmes systèmes liés à la gestion des utilisateurs**
Certains autres outils et démons liés à la gestion des utilisateurs, comme **`sshd`** (serveur SSH), peuvent se référer à la **umask** dans **`/etc/login.defs`** si aucun autre fichier de configuration ne la spécifie. Cependant, il est important de noter que de nombreux services modernes (comme `sshd`) permettent de configurer la **umask** directement dans leurs propres fichiers de configuration, comme **`/etc/ssh/sshd_config`**.

### Exemple de configuration dans `/etc/login.defs` :

```bash
# /etc/login.defs

# Définit la umask pour les nouveaux utilisateurs
UMASK 077
```

Cela signifie que :
- Lors de la création d'un nouvel utilisateur avec `useradd` ou `adduser`, tous les répertoires et fichiers créés initialement dans le répertoire personnel de l'utilisateur auront des permissions limitées.
- Si l'utilisateur se connecte via un programme utilisant directement les paramètres de `login.defs` (comme `login` ou `su`), cette umask peut également être appliquée.

### 5. **Limites de l'usage de `/etc/login.defs`**
Il est important de noter que la **umask** définie dans **`/etc/login.defs`** ne s'applique pas de manière générale à tous les contextes ou services. Par exemple :
- Elle ne s'applique pas aux shells interactifs (comme **zsh** ou **bash**), où la **umask** est plutôt définie dans des fichiers comme `/etc/profile`, `~/.bashrc`, `~/.zshrc`, etc.
- Elle ne s'applique pas non plus aux processus ou services **systemd**, qui peuvent définir leur propre **umask** via leurs fichiers d'unité.

### Récapitulatif :

| **Contexte**                               | **UMASK dans `/etc/login.defs` est utilisée ?**                               |
|--------------------------------------------|------------------------------------------------------------------------------|
| **Création de nouveaux utilisateurs**      | Oui, pour définir les permissions par défaut des fichiers et répertoires créés. |
| **Connexion via `login`**                  | Oui, dans certaines configurations de gestion de connexion (console, etc.).  |
| **Utilisation de `su` pour changer d'utilisateur** | Oui, peut être appliquée lors d'une connexion avec `su`.                         |
| **Services et démons (`systemd`, etc.)**   | Non, ceux-ci utilisent généralement leurs propres configurations (comme `UMask`). |
| **Shell interactif (zsh, bash)**           | Non, la umask est définie dans `/etc/profile` ou `~/.bashrc`, `~/.zshrc`.    |

### Conclusion :
Le fichier **`/etc/login.defs`** est principalement utilisé pour définir des paramètres globaux relatifs à la gestion des utilisateurs, comme la **umask** pour la création de nouveaux comptes ou pour les connexions via des outils comme **`login`** et **`su`**. Cependant, il n'affecte pas directement les sessions interactives ni les services système gérés par **systemd**, où d'autres mécanismes de configuration de la **umask** sont utilisés.