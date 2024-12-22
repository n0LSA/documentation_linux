---
title: auditctl-gpt
date: 2024-10-23
date de modification: 2024-10-23
timestamp: 14:13
tags:
  - ressource
status:
  - En cours
type de note:
  - ressource
référence:
  - "[[auditd-gpt]]"
source: 
auteur: aGrellard
---
# Guide complet pour la gestion des fichiers sensibles

## Introduction

La sécurité des fichiers sensibles est cruciale pour la protection de votre système Linux. Des fichiers tels que `/etc/passwd`, `/etc/shadow`, et d'autres contiennent des informations vitales pour le fonctionnement du système et la sécurité des utilisateurs. La surveillance de ces fichiers et la garantie de leurs permissions correctes sont essentielles pour prévenir les accès non autorisés et les modifications malveillantes.

Ce guide vous expliquera comment surveiller les fichiers critiques à l'aide de **auditctl** et comment assurer les bonnes propriétés de possession et de permissions des fichiers sensibles. Chaque commande sera décomposée et expliquée en détail pour une compréhension complète.

---

## 1. Surveillance des fichiers critiques avec auditctl

### Introduction à auditctl

**auditctl** est un outil fourni par le paquet **auditd** qui permet de gérer dynamiquement les règles d'audit du noyau Linux. En utilisant **auditctl**, vous pouvez définir des règles pour surveiller l'accès, la modification ou la suppression de fichiers spécifiques, ce qui est essentiel pour la sécurité du système.

### Vérification de l'installation d'auditd

Avant d'utiliser **auditctl**, assurez-vous que le paquet **auditd** est installé sur votre système.

```bash
sudo apt-get install auditd
```

- **sudo apt-get install auditd** : Installe le démon d'audit **auditd** et les outils associés, y compris **auditctl**.

### Utilisation d'auditctl pour surveiller les fichiers critiques

#### Commande pour surveiller le fichier `/etc/passwd`

```bash
sudo auditctl -w /etc/passwd -p war -k audit_passwd
```

- **sudo auditctl** : Exécute la commande **auditctl** avec les privilèges superutilisateur nécessaires pour modifier les règles d'audit du noyau.
  
- **-w /etc/passwd** : Spécifie le fichier à surveiller. Ici, **-w** signifie "watch" (surveiller), et **/etc/passwd** est le fichier cible.
  
- **-p war** : Définit les permissions à surveiller sur le fichier. Les options sont :
  - **w** : write (écriture)
  - **a** : attribute change (changement d'attribut)
  - **r** : read (lecture)
  
  En combinant **war**, on surveille les opérations d'écriture, de modification d'attribut et de lecture sur le fichier.
  
- **-k audit_passwd** : Associe une clé nommée **audit_passwd** à cette règle, facilitant la recherche dans les logs d'audit.

#### Explication détaillée

- **Pourquoi surveiller `/etc/passwd` ?**
  
  Le fichier **/etc/passwd** contient les informations des comptes utilisateurs du système. Bien qu'il ne contienne pas les mots de passe (stockés dans **/etc/shadow**), toute modification non autorisée de ce fichier peut compromettre la sécurité du système.

- **Surveillance des permissions :**
  
  - **w (write)** : Capture les tentatives d'écriture ou de modification du fichier.
  - **a (attribute change)** : Surveille les changements d'attributs du fichier, tels que les permissions, le propriétaire, ou les dates.
  - **r (read)** : Enregistre les tentatives de lecture du fichier. Surveiller la lecture peut générer beaucoup de logs; assurez-vous que c'est nécessaire pour votre cas d'utilisation.

### Ajout de règles pour d'autres fichiers critiques

Vous pouvez ajouter des règles similaires pour surveiller d'autres fichiers sensibles. Par exemple :

#### Surveiller `/etc/shadow`

```bash
sudo auditctl -w /etc/shadow -p war -k audit_shadow
```

- **/etc/shadow** : Contient les mots de passe chiffrés des utilisateurs. La protection de ce fichier est essentielle.

#### Surveiller `/etc/sudoers`

```bash
sudo auditctl -w /etc/sudoers -p war -k audit_sudoers
```

- **/etc/sudoers** : Contrôle les permissions Sudo des utilisateurs. Toute modification non autorisée peut accorder des privilèges root à des utilisateurs malveillants.

### Vérification des règles d'audit en place

Pour voir les règles d'audit actuellement actives :

```bash
sudo auditctl -l
```

- **sudo auditctl -l** : Liste toutes les règles d'audit actuellement chargées dans le noyau.

### Recherche dans les logs d'audit

Pour consulter les événements enregistrés par les règles d'audit :

```bash
sudo ausearch -k audit_passwd
```

- **sudo ausearch** : Outil pour rechercher dans les logs d'audit.
- **-k audit_passwd** : Filtre les événements associés à la clé **audit_passwd**.

### Exemple de scénario

#### Étape 1 : Modifier le fichier `/etc/passwd`

```bash
sudo echo "test:x:1001:1001::/home/test:/bin/bash" >> /etc/passwd
```

- Cette commande ajoute une ligne au fichier **/etc/passwd**. **Attention** : Ne pas exécuter cette commande sur un système de production, car elle peut causer des problèmes de sécurité.

#### Étape 2 : Vérifier les logs d'audit

```bash
sudo ausearch -k audit_passwd
```

- Vous devriez voir un enregistrement de l'événement, incluant l'utilisateur qui a effectué la modification, le temps, et d'autres détails pertinents.

---

## 2. Assurer les propriétés des fichiers sensibles

Les fichiers sensibles doivent avoir les bonnes permissions et appartenir aux utilisateurs et groupes appropriés pour prévenir tout accès non autorisé.

### Vérification des propriétés actuelles

#### Vérifier le propriétaire et le groupe du fichier `/etc/shadow`

```bash
ls -l /etc/shadow
```

- **ls -l /etc/shadow** : Affiche les détails du fichier, y compris le propriétaire et le groupe.

#### Exemple de sortie attendue

```bash
-rw-r----- 1 root shadow 1525 oct.  23 10:00 /etc/shadow
```

- **root shadow** : Indique que le propriétaire est **root** et le groupe est **shadow**.

### Modification des propriétés si nécessaire

#### Changer le propriétaire du fichier

```bash
sudo chown root /etc/shadow
```

- **sudo chown root /etc/shadow** : Définit le propriétaire du fichier **/etc/shadow** à **root**.
- **chown** : Commande pour changer le propriétaire d'un fichier ou d'un répertoire.

#### Changer le groupe du fichier

```bash
sudo chgrp root /etc/shadow
```

- **sudo chgrp root /etc/shadow** : Définit le groupe du fichier **/etc/shadow** à **root**.
- **chgrp** : Commande pour changer le groupe d'un fichier ou d'un répertoire.

### Définition des permissions correctes

#### Définir les permissions pour `/etc/shadow`

```bash
sudo chmod 640 /etc/shadow
```

- **sudo chmod 640 /etc/shadow** : Définit les permissions du fichier à **rw-r-----**.
  - **6 (rw-)** : Le propriétaire peut lire et écrire.
  - **4 (r--)** : Les membres du groupe peuvent lire.
  - **0 (---)** : Aucun accès pour les autres utilisateurs.

#### Explication des permissions

- **Propriétaire (root)** : Lecture et écriture.
- **Groupe (root)** : Lecture seule.
- **Autres utilisateurs** : Aucun accès.

### Répéter pour d'autres fichiers sensibles

Assurez-vous que les fichiers suivants ont les bonnes propriétés :

- **/etc/passwd**
- **/etc/group**
- **/etc/gshadow**
- **/etc/sudoers**

#### Exemple pour `/etc/sudoers`

```bash
sudo chown root /etc/sudoers
sudo chgrp root /etc/sudoers
sudo chmod 440 /etc/sudoers
```

- **chmod 440** : Permissions **r--r-----**. Seul le propriétaire et le groupe peuvent lire; personne ne peut écrire ou exécuter.

---

## 3. Gestion des permissions avec umask

Le **umask** détermine les permissions par défaut des nouveaux fichiers et répertoires créés. Pour renforcer la sécurité, vous pouvez définir un umask restrictif.

### Vérification du umask actuel

```bash
umask
```

- La valeur par défaut est généralement **022**, ce qui donne des permissions **755** pour les répertoires et **644** pour les fichiers.

### Modification du umask

Pour définir un umask plus restrictif, ajoutez la ligne suivante au fichier **/etc/profile** ou **~/.bashrc** :

```bash
umask 027
```

- **umask 027** : Donne des permissions par défaut de **750** pour les répertoires et **640** pour les fichiers.
  - **Propriétaire** : Lecture, écriture, exécution.
  - **Groupe** : Lecture, exécution.
  - **Autres utilisateurs** : Aucun accès.

---

## 4. Surveillance des changements de permissions

Pour surveiller les modifications des permissions ou des propriétés des fichiers sensibles, vous pouvez utiliser des règles d'audit supplémentaires.

### Exemple de règle pour surveiller les changements d'attributs sur `/etc/shadow`

```bash
sudo auditctl -w /etc/shadow -p a -k audit_shadow_attr
```

- **-p a** : Surveille les changements d'attributs (permissions, propriétaire, groupe).
- **-k audit_shadow_attr** : Clé associée pour faciliter la recherche dans les logs.

### Vérification des règles

```bash
sudo auditctl -l
```

- Assurez-vous que la nouvelle règle est listée.

### Test de la surveillance

#### Étape 1 : Modifier les permissions du fichier

```bash
sudo chmod 600 /etc/shadow
```

- Modifie les permissions du fichier.

#### Étape 2 : Vérifier les logs d'audit

```bash
sudo ausearch -k audit_shadow_attr
```

- Vous devriez voir un enregistrement de la modification des attributs du fichier.

---

## 5. Mise en place d'alertes en temps réel (Optionnel)

Pour être immédiatement informé des modifications sur les fichiers critiques, vous pouvez configurer des alertes en temps réel.

### Utilisation de audispd et plugins

**audispd** est un démon qui peut être utilisé avec des plugins pour traiter les événements d'audit en temps réel.

#### Installation du plugin audispd-syslog

```bash
sudo apt-get install audispd-plugins
```

- Installe les plugins pour **audispd**, y compris **audispd-syslog**.

#### Configuration du plugin

Éditez le fichier de configuration du plugin :

```bash
sudo nano /etc/audisp/plugins.d/syslog.conf
```

Assurez-vous que les lignes suivantes sont présentes :

```bash
active = yes
direction = out
path = builtin_syslog
type = builtin
args = LOG_INFO
format = string
```

- **active = yes** : Active le plugin.
- **path = builtin_syslog** : Utilise le plugin intégré pour envoyer les événements au syslog.

#### Redémarrage des services

```bash
sudo systemctl restart auditd
sudo systemctl restart rsyslog
```

- Redémarre les services pour appliquer les modifications.

### Configuration de rsyslog pour envoyer des alertes

Vous pouvez configurer **rsyslog** pour envoyer des alertes par e-mail ou vers un système de gestion des événements de sécurité.

---

## 6. Bonnes pratiques supplémentaires

- **Sauvegardes régulières** : Effectuez des sauvegardes régulières des fichiers de configuration sensibles.
- **Contrôle d'intégrité** : Utilisez des outils comme **AIDE** (Advanced Intrusion Detection Environment) pour vérifier l'intégrité des fichiers critiques.
- **Journalisation centralisée** : Envisagez de centraliser les logs sur un serveur distant pour éviter la manipulation des logs locaux par un attaquant.
- **Mises à jour régulières** : Maintenez votre système à jour avec les derniers correctifs de sécurité.

---

## Conclusion

La gestion proactive des fichiers sensibles est une composante essentielle de la sécurité système. En surveillant les fichiers critiques avec **auditctl** et en assurant les bonnes propriétés de possession et de permissions, vous renforcez la protection de votre système contre les accès non autorisés et les modifications malveillantes.

N'oubliez pas de revoir régulièrement vos configurations de surveillance et de permissions pour vous assurer qu'elles restent adaptées à l'évolution de votre environnement et des menaces potentielles.

---

## Ressources supplémentaires

- **Page de manuel d'auditctl** : `man auditctl`
- **Documentation de Linux Audit** : [Linux Audit Documentation](https://linux-audit.com/)
- **Sécurisation des fichiers sensibles** : Recherchez des guides et des articles sur les meilleures pratiques pour sécuriser les fichiers système critiques.
- **Advanced Intrusion Detection Environment (AIDE)** : Un outil pour surveiller l'intégrité des fichiers.

---

**Remarque** : Les commandes et configurations présentées dans ce guide doivent être testées dans un environnement sécurisé avant d'être déployées en production. Assurez-vous de comprendre pleinement les implications de chaque commande pour éviter les perturbations involontaires du système.