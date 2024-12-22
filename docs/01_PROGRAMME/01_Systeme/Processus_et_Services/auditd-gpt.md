---
title: auditd-gpt
date: 2024-10-23
date de modification: 2024-10-23
timestamp: 14:11
tags:
  - ressource
status:
  - En cours
type de note:
  - ressource
référence:
  - "[[auditctl-gpt]]"
source:
  - https://soursot.lombardandco.fr/2024/06/02/installation-et-securisation-dun-serveur-debian-12/#pam
auteur: aGrellard
---
# Guide complet pour l'installation et la configuration d'Auditd

## Introduction

Auditd est un démon de suivi des événements de sécurité sur les systèmes Linux. Il permet de surveiller et d'enregistrer les actions des utilisateurs et des processus, offrant ainsi une traçabilité complète des activités sur le système. Cela est particulièrement utile pour la conformité aux réglementations, le dépannage et la détection d'intrusions.

Ce guide vous expliquera comment installer et configurer Auditd sur votre système Debian/Ubuntu, en détaillant chaque étape et en expliquant chaque ligne de code.

---

## 1. Installation d'Auditd

### Mise à jour du système

Avant d'installer de nouveaux paquets, il est recommandé de mettre à jour la liste des paquets disponibles et les paquets existants.

```bash
sudo apt-get update
sudo apt-get upgrade
```

- **sudo apt-get update** : Met à jour la liste des paquets disponibles depuis les dépôts configurés.
- **sudo apt-get upgrade** : Met à jour tous les paquets installés vers leurs dernières versions disponibles.

### Installation du paquet Auditd

```bash
sudo apt-get install auditd audispd-plugins
```

- **sudo apt-get install auditd** : Installe le démon d'audit et les outils associés.
- **audispd-plugins** : Ce paquet contient des plugins pour le répartiteur d'événements audit, améliorant les capacités de reporting.

### Activation du service Auditd au démarrage

```bash
sudo systemctl enable auditd
```

- **sudo systemctl enable auditd** : Configure le système pour démarrer le service Auditd automatiquement lors du démarrage du système.

### Démarrage du service Auditd

```bash
sudo systemctl start auditd
```

- **sudo systemctl start auditd** : Démarre le service Auditd immédiatement.

### Vérification du statut du service

```bash
sudo systemctl status auditd
```

- **sudo systemctl status auditd** : Affiche l'état actuel du service Auditd, confirmant qu'il fonctionne correctement.

---

## 2. Configuration des règles d'audit

Les règles d'audit déterminent quels événements sont surveillés et enregistrés par Auditd.

### Édition du fichier de règles

```bash
sudo nano /etc/audit/rules.d/audit.rules
```

- **sudo nano /etc/audit/rules.d/audit.rules** : Ouvre le fichier de règles d'audit avec l'éditeur Nano en mode superutilisateur.

### Ajout des règles spécifiques

Ajoutez les lignes suivantes au fichier pour définir les événements à surveiller :

```bash
-a always,exit -F arch=b64 -S execve
-w /etc/passwd -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/sudoers -p wa -k actions
-w /var/log/faillog -p wa -k auth
-w /var/log/lastlog -p wa -k auth
-a always,exit -F path=/usr/bin/chmod -F perm=x -F auid>=1000 -F auid!=4294967295 -k perm_mod
-a always,exit -F path=/usr/bin/chown -F perm=x -F auid>=1000 -F auid!=4294967295 -k perm_mod
-a always,exit -F arch=b64 -S connect -S accept -k network
```

#### Explication de chaque règle :

1. **Surveillance des appels système `execve` :**

   ```bash
   -a always,exit -F arch=b64 -S execve
   ```

   - **-a always,exit** : Applique la règle à chaque entrée et sortie d'un appel système.
   - **-F arch=b64** : Filtre pour l'architecture 64 bits.
   - **-S execve** : Spécifie l'appel système `execve`, utilisé pour exécuter des programmes.

2. **Surveillance des modifications des fichiers critiques :**

   a. **/etc/passwd, /etc/group, /etc/shadow** (Identité des utilisateurs)

   ```bash
   -w /etc/passwd -p wa -k identity
   -w /etc/group -p wa -k identity
   -w /etc/shadow -p wa -k identity
   ```

   - **-w** : Spécifie le chemin du fichier à surveiller.
   - **-p wa** : Surveille les permissions d'écriture (w) et d'attribut (a).
   - **-k identity** : Attribue un nom de clé pour faciliter la recherche dans les logs.

   b. **/etc/sudoers** (Actions sudo)

   ```bash
   -w /etc/sudoers -p wa -k actions
   ```

   - **-k actions** : La clé `actions` permet de filtrer les logs relatifs aux modifications du fichier sudoers.

3. **Surveillance des logs d'authentification :**

   ```bash
   -w /var/log/faillog -p wa -k auth
   -w /var/log/lastlog -p wa -k auth
   ```

   - **/var/log/faillog** : Enregistre les tentatives de connexion échouées.
   - **/var/log/lastlog** : Contient les informations sur la dernière connexion de chaque utilisateur.

4. **Surveillance des changements de permissions et de propriété :**

   ```bash
   -a always,exit -F path=/usr/bin/chmod -F perm=x -F auid>=1000 -F auid!=4294967295 -k perm_mod
   -a always,exit -F path=/usr/bin/chown -F perm=x -F auid>=1000 -F auid!=4294967295 -k perm_mod
   ```

   - **-F path=/usr/bin/chmod** : Filtre pour le binaire `chmod`.
   - **-F perm=x** : Surveille les exécutions (permission d'exécution).
   - **-F auid>=1000** : Se concentre sur les utilisateurs normaux (UID >= 1000).
   - **-F auid!=4294967295** : Exclut les utilisateurs non définis.
   - **-k perm_mod** : Clé pour les modifications de permissions.

5. **Surveillance des connexions réseau :**

   ```bash
   -a always,exit -F arch=b64 -S connect -S accept -k network
   ```

   - **-S connect -S accept** : Surveille les appels système `connect` et `accept`, utilisés pour les connexions réseau.
   - **-k network** : Clé pour les événements réseau.

### Sauvegarde et fermeture du fichier

Après avoir ajouté les règles, enregistrez les modifications en appuyant sur **Ctrl + O**, puis quittez Nano avec **Ctrl + X**.

---

## 3. Configuration de auditd.conf

Le fichier **auditd.conf** gère les paramètres du démon Auditd, tels que la rotation des logs, la taille maximale des fichiers, etc.

### Édition du fichier de configuration principal

```bash
sudo nano /etc/audit/auditd.conf
```

### Modification des paramètres de rotation des logs

Assurez-vous que les paramètres suivants sont définis :

```bash
max_log_file = 8
num_logs = 5
max_log_file_action = ROTATE
```

#### Explication des paramètres :

- **max_log_file = 8** : Définit la taille maximale d'un fichier log à 8 Mo.
- **num_logs = 5** : Le nombre de fichiers log à conserver après rotation.
- **max_log_file_action = ROTATE** : Action à effectuer lorsque le fichier log atteint sa taille maximale (ici, rotation des logs).

### Sauvegarde et fermeture du fichier

Enregistrez les modifications (**Ctrl + O**) et quittez Nano (**Ctrl + X**).

---

## 4. Application des modifications

### Redémarrage du service Auditd

```bash
sudo systemctl restart auditd
```

- **sudo systemctl restart auditd** : Redémarre le service pour appliquer les nouvelles configurations.

### Vérification du statut du service

```bash
sudo systemctl status auditd
```

- **sudo systemctl status auditd** : Confirme que le service fonctionne correctement après le redémarrage.

---

## 5. Vérification de la configuration

Pour s'assurer que les règles d'audit sont correctement chargées :

```bash
sudo auditctl -l
```

- **sudo auditctl -l** : Liste toutes les règles d'audit actuellement chargées dans le noyau.

Vous devriez voir les règles que vous avez ajoutées listées ici.

---

## 6. Test des règles d'audit

### Exemple : Modification du fichier /etc/passwd

Essayez de modifier le fichier **/etc/passwd** :

```bash
sudo echo "test" >> /etc/passwd
```

Ensuite, vérifiez les logs d'audit :

```bash
sudo ausearch -k identity
```

- **sudo ausearch -k identity** : Recherche dans les logs d'audit tous les événements associés à la clé `identity`.

Vous devriez voir un enregistrement de votre modification, confirmant que la règle fonctionne.

---

## 7. Analyse des logs d'audit

### Outils de base

- **ausearch** : Recherche dans les logs d'audit.
- **aureport** : Génère des rapports à partir des logs d'audit.

### Exemple d'utilisation de ausearch

```bash
sudo ausearch -k network
```

- Recherche tous les événements liés aux connexions réseau.

### Exemple d'utilisation de aureport

```bash
sudo aureport -au
```

- Génère un rapport des événements d'authentification.

---

## 8. Sécurisation supplémentaire

### Protection des fichiers de configuration

Assurez-vous que seuls les utilisateurs autorisés peuvent modifier les fichiers de configuration d'Auditd.

```bash
sudo chown root:root /etc/audit/auditd.conf
sudo chmod 600 /etc/audit/auditd.conf
```

- **sudo chown root:root** : Définit le propriétaire et le groupe à root.
- **sudo chmod 600** : Donne des permissions de lecture et d'écriture uniquement au propriétaire.

---

## Conclusion

Vous avez maintenant configuré Auditd pour surveiller des événements critiques sur votre système. Cette configuration permet de détecter des modifications non autorisées, de suivre les actions des utilisateurs et de renforcer la sécurité globale du système.

N'oubliez pas de surveiller régulièrement les logs d'audit et d'ajuster les règles en fonction des besoins spécifiques de votre environnement.

---

## Ressources supplémentaires

- **Page de manuel d'Auditd** : `man auditd`
- **Documentation officielle** : [Linux Audit Documentation](https://linux.die.net/man/8/auditd)
- **Tutoriels avancés** : Recherche de guides sur l'analyse approfondie des logs d'audit.

---

**Remarque** : La configuration d'Auditd peut varier en fonction de la distribution Linux utilisée. Ce guide est basé sur Debian/Ubuntu, mais les principes généraux s'appliquent à la plupart des systèmes Linux.