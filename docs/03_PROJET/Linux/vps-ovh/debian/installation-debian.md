---
title: installation-debian
date: 2024-10-23
date de modification: 2024-10-23
timestamp: 19:03
tags:
  - projet
  - templates
status:
  - En cours
type de note:
  - projet
référence: 
source: 
auteur: aGrellard
---


---

- https://hackmd.io/@Ben-Rahiti-Romain/SkciYWMWj
- https://soursot.lombardandco.fr/2024/06/02/installation-et-securisation-dun-serveur-debian-12/#pam
- https://www.isyweb.com/blog/post/Installer-et-securiser-un-serveur-web-complet-mail-et-ftp-sur-Debian-12-Bookworm-70

---

- https://www.linuxtricks.fr/wiki/differences-sudo-su-et-su
- https://www.cyberciti.biz/faq/linux-hide-processes-from-other-users/

---

- https://chatgpt.com/c/6718312f-1544-8003-acdb-556b1e46d04c
- https://chatgpt.com/c/67171a26-c4d0-8003-a848-398423026b20
- https://chatgpt.com/c/67188190-0bec-8003-9168-d3c2639dd2c4

---

- wireguard
	- [vpn+réseaux local](https://chatgpt.com/c/6710b205-d4e0-8003-b9ba-05a3d9992cb0)
	- [51820](https://chatgpt.com/c/6710bb38-a230-8003-9aae-8edba526ece3)
	- [plage réseaux](https://chatgpt.com/c/6710cd98-9be8-8003-b708-9bfac00c5080)
	- https://chatgpt.com/c/6717bae3-4c20-8003-aef5-cd0d880e7091
	- [clients](https://chatgpt.com/c/6710eafd-2288-8003-bdb0-b1a894680c67)

---

- borg
	- https://chatgpt.com/c/67115419-e270-8003-8d37-9fe864b937c1

---

- [[2024-10-19]]

---

--

```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

# vps

## OVH
### debian 12

## Paramètres de localisation (locales)

les **[[locale]]** définissent les paramètres régionaux, tels que :

- La langue d'affichage dy système
- Le format de date et d'heures
- Les conventions monétaires
- les caractères de collation
- l'encodage des caractères (UTF-8, ISO-8859)

méthodes pour la configuration :

- dpkg-reconfigure locales
- /etc/locale.gen 
	- modifier le fichier
	- `sudo locale-gen` pour actualiser
- /etc/default/locale
	- modifier ou ajouter les variables : `LANG="fr_FR.UTF-8"` `LANGUAGE="fr_FR:fr"` `LC_ALL="fr_FR.UTF-8"`
	- `sudo locale-gen` pour actualiser

### Configuration du fuseaux horaire

- `timedatectl` est un utilitaire inclus avec `systemd` qui permet de gérer les paramètres de date et d'heures du système: fuseaux horaires, horloge système, et la synchronisation du temps. 
- `set-timzone <timezone>` option de `timedatectl` qui permet de définir le fuseau horaire
- `sudo timedatectl set-timezone Europe/Paris`

## Configuration [[apt-sources|sources apt]]

```bash
sudo vi /etc/apt/sources.list
```

```plaintext
# Dépôts officiels Debian 12 (Bookworm)
deb http://deb.debian.org/debian/ bookworm main contrib non-free
deb-src http://deb.debian.org/debian/ bookworm main contrib non-free

# Mises à jour de sécurité
deb http://security.debian.org/debian-security bookworm-security main contrib non-free
deb-src http://security.debian.org/debian-security bookworm-security main contrib non-free

# Mises à jour proposées
deb http://deb.debian.org/debian/ bookworm-updates main contrib non-free
deb-src http://deb.debian.org/debian/ bookworm-updates main contrib non-free
```

## Mise à jour des paquets apt

```bash
sudo apt update
```

## Installation du paquet sudo

```bash
sudo apt install -y sudo
```

## Installation d'[[auditd-gpt|Auditd]]

>Auditd est un démon de suivi d'événements de sécurité sur les systèmes linux. Il permet de surveiller et d'enregistrer les actions des utilisateurs et des processus.

### paquets a installer

- `auditd` :le démon
- `auditspd-plugins` : plugins pour améliorer les cpacités

```bash
sudo apt install -y auditd auditspd-plugins
```

- gestions via systemd
	
	```bash
	sudo systemctl status auditd
	sudo systemctl start auditd
	sudo systemctl stop auditd
	sudo systemctl restart auditd
	```

### configurations des règles d'audit

#### fichier de configuration

```
/etc/audit/rules.d/audit.rules
```

#### ajout des régles d'audit

- https://soursot.lombardandco.fr/2024/06/02/installation-et-securisation-dun-serveur-debian-12/#pam
- [[auditd-gpt#2. Configuration des règles d'audit|Configuration des règles d'audit]]
- [[auditctl-gpt]] : surveillance de dossiers sensible `/etc/passwd`, `/etc/shadow`

## UMASK

>[UMASK et droits des répertoires /home](https://hackmd.io/@Ben-Rahiti-Romain/SkciYWMWj#Modification-de-UMASK-et-des-droits-des-r�pertoires-home)

|                        |                                                                 |
| ---------------------- | --------------------------------------------------------------- |
| [[umask\|UMASK]]       | modificationet droits des répertoires `/home`                    |
| [[umask-0077]]         | appliquer des droits `770` si le dossier home existe déjà.       |
| [[umask_login-profil]] | définition d'un masque par défaut pour les nouveaux utilisateur  |

| Umask | Fichiers (Permissions finales) | Répertoires (Permissions finales) | Usage recommandé                     |
| ----- | ------------------------------ | --------------------------------- | ------------------------------------ |
| 0022  | 644 (rw-r--r--)                | 755 (rwxr-xr-x)                   | Par défaut, usage général            |
| 0027  | 640 (rw-r-----)                | 750 (rwxr-x---)                   | Environnements multi-utilisateurs    |
| 0077  | 600 (rw-------)                | 700 (rwx------)                   | Sécurité maximale, données sensibles |

## Utilisateurs

### supprimer l'user par default

- [[deluser]]

#### Options Principales[¶](https://n0lsa.github.io/documentation_linux/commandes-de-base/gestion_utilisateurs_groupes/deluser.html#options-principales "Permanent link")

- `--remove-home` : Supprime le répertoire personnel de l'utilisateur ainsi que sa boîte aux lettres.
- `--remove-all-files` : Supprime tous les fichiers appartenant à l'utilisateur sur le système.
- `--backup` : Crée une sauvegarde des fichiers de l'utilisateur avant la suppression.
- `--backup-to CHEMIN` : Spécifie le répertoire où sauvegarder les fichiers de l'utilisateur.
- `--group` : Indique que le nom spécifié est celui d'un groupe à supprimer.
- `--system` : Indique que l'utilisateur ou le groupe est un utilisateur ou un groupe système.
- `--quiet` : Mode silencieux, réduit la sortie de la commande.

```bash
deluser --remove-all-files <username>
```

```bash
sudo deluser --remove-home --remove-all-files nom_utilisateur
```

#### Supprimer les fichiers appartenant a l'utilisateur dans d'autre répertoires

```bash
sudo find / -user <nom_user> -exec rm -rf {}\;
```

#### Suppression divers

- [[getent]]
- [[crontab_delByUser|supprimer les tâches cron d'un utilisateur]]

### Créer un utilisateur

- [[useradd-gpt|useradd]]
	- `-m` : crée le répertoire personnel
	- `-M` : ne crée pas de dossier personel
	- `-k` : spécifie un répertoire squelette pour le contenu du répertoire. utilisé avec `-m`
		- par default **useradd** utilise /etc/skel comme répertoire de squelette
		- lors de la création d'un répertoire personnel avec `-m`, les fichiers du répertoire squelette sont copiés dans le nouveau répertoire personnel.
		- `-k` peut être utilisé avec `/dev/null` : empêche la copie des fichiers par défaut en spécifiant un répertoire squelette vide.
	- `-c` : ajoute un description au compte utilisateur
	- `-d` : spécifie l'emplacement du répertoire personnel
	- `-g` : définit le groupe initial de l'utilisateur
		- ``sudo useradd -g développeurs alice``
	- `-G` : assigne des groupes supplémentaires à l'utilisateur
		- `sudo useradd -G sudo,webmasters bob`
	- `-s` : spécifie le shell de connexion de l'utilisateur
		- `sudo useradd -s /bin/zsh adrien`
	- `-r` : [[useradd--r|création d'un utilisateur système]]

	```bash
	useradd -d "administrateur" -m -s /bin/bash -G sudo <username>
	```

- [[groups]] : afficher les groupes de l'utilisateur
	
	```bash
	groups <username>
	```

### Attribution d'un mot de passe utilisateur et root

- [[02_RESSOURCES/Linux/programme/03_Gestion_des_Utilisateurs/Utilisateurs_et_Groupes/passwd|passwd]] : changer le mot de passe du compte utilisateur
	
	```bash
	passwd <user> 
	```

## Installation du serveur ssh

```bash
apt install -y openssh-server
```

- La commande `sshd` permet de lancer le serveur **SSH**
	- `/usr/sbin/sshd [options]`
- sur le plupart des systèmes, `sshd` est géré via **systmd**

## Configuration du serveur SSH

### vérifier les versions par défaut (ovh)

 - répertoire : `/etc/ssh/ssd_confg.d`

### ajouter une configuration personnalisé

- répertoire : `/etc/ssh/ssd_confg.d`
- s'assuré que la ligne `Include /etc/ssh/sshd_config.d/*.conf` et bien présente en haut du fichier `/etc/ssh/sshd_config`

```
/etc/ssh/sshd_config.d/custom-ssh.conf
```

```
Port 
	22, 2222, 49152-65535
PermitRootLogin
PubKeyAuthentification
PasswordAuthentification
```

### Clés d'autorisations

#### le dossier `.ssh`

Le dossier `.ssh` est un répertoire caché situé dans le répertoire personnel d'un utilisateur. Il est utilisé par le protocole **SSh** pour stocker les fichiers de configuration nécessaire a l'établissement de connexion **SSH** entre client et serveur.

#### création du dossier `.ssh`

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
```

- le répertoire par défaut se trouver a la racine du dossier personnel de l'utilisateur `/home/<user>/.ssh` ou `~/.ssh`
- Octroyer les droits 4(lecture)+2(écriture)+1(exécution) au dossier

#### Création de la clé publique

```bash
ssh-keygen -t rsa -b 4096
```

```
ssh-copy-id -i ~/.ssh/id_rsa.pub -p 2222 user@adresse_ip
```

#### Création du fichier `authorized_keys`

```bash
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

- l’enlacement par défaut du fichier se trouve dans le dossier `.ssh`
- assurer des droits uniquement pour l'utilisateur en lecture et en écriture 
- la commande `ssh-copy-id` peut être utilisée pour copier la clé publique d'un machine local sur le **serveur** : `ssh-copy-id nom_utilisateur@adresse_ip_du_serveur`
- on peut aussi l'ajouter manuellement en éditant le fichier `authorized_keys`



## ufw

### ssh 

- `49152 - 65535` : private range

### docker - nginx

- `80/tcp` : webserver
- `443/tcp` : ssl/tsl

## rsyslog

>documentation : [[rsyslog-gpt]]

### Installation de Rsyslog

Sur les systèmes Debian/Ubuntu récents, Rsyslog est généralement installé par défaut. Vous pouvez vérifier s'il est déjà installé :

```bash
rsyslogd -v
```

- **rsyslogd -v** : Affiche la version de Rsyslog installée. Si la commande n'est pas reconnue, cela signifie que Rsyslog n'est pas installé.

Si Rsyslog n'est pas installé, vous pouvez l'installer avec la commande suivante :

```bash
sudo apt-get install rsyslog
```

- **sudo apt-get install rsyslog** : Installe le paquet Rsyslog depuis les dépôts officiels.

### Vérification du statut du service Rsyslog

Une fois installé, vérifiez que le service Rsyslog est actif :

```bash
sudo systemctl status rsyslog
```


### Backup `/etc/rsyslog.conf`


```
###############
#### RULES ####
###############

#
# Log anything besides private authentication messages to a single log file
#
*.*;auth,authpriv.none          -/var/log/syslog

#
# Log commonly used facilities to their own log file
#
auth,authpriv.*                 /var/log/auth.log
cron.*                          -/var/log/cron.log
kern.*                          -/var/log/kern.log
mail.*                          -/var/log/mail.log
user.*                          -/var/log/user.log

```

## fail2ban

### failregex

### ufw

### sshd

### jail

## paquets additionnels

- **`curl`** : Un outil en ligne de commande pour transférer des données avec des URL. Il supporte divers protocoles comme HTTP, FTP, et SFTP.
- **`wget`** : Un outil en ligne de commande utilisé pour télécharger des fichiers depuis le Web. Il supporte le téléchargement récursif et la reprise des téléchargements interrompus.
- **`git`** : Un système de contrôle de version décentralisé, utilisé pour suivre les modifications dans le code source et collaborer avec d'autres développeurs.
- **`unzip`** : Un utilitaire pour extraire les fichiers contenus dans des archives compressées au format ZIP.
- **`hstr`** : Un utilitaire qui améliore la gestion de l'historique de la ligne de commande en rendant les recherches plus rapides et plus intuitives.
- **`exa`** : Une alternative moderne à la commande `ls` qui liste les fichiers et dossiers avec des informations détaillées et des couleurs.
- **`bat`** : Une alternative à `cat` avec mise en évidence syntaxique, numérotation des lignes et bien d'autres fonctionnalités.
- **`tree`** : Affiche la structure des fichiers et des répertoires sous forme d'arborescence, pour une meilleure visualisation des dossiers imbriqués.
- **`btop`** : Un moniteur de ressources interactif avec une interface utilisateur graphique pour surveiller les processus, l'utilisation du CPU, de la mémoire et du réseau.
- **`neofetch`** : Un outil qui affiche des informations système dans le terminal, comme le nom de la distribution, la version du noyau, l'utilisation des ressources, etc., souvent accompagné d'un logo ASCII.
- **`ranger`** : Un gestionnaire de fichiers en mode texte avec une interface en colonnes et la navigation par raccourcis clavier.
- **`pandoc`** : Un convertisseur de documents polyvalent, capable de convertir entre divers formats de fichiers comme Markdown, LaTeX, HTML, PDF, etc.
- **`lynx`** : Un navigateur Web en mode texte qui permet de naviguer sur Internet depuis un terminal.
- **`vim`** : Un éditeur de texte avancé en mode console, extrêmement flexible et personnalisable, utilisé pour l'édition de fichiers de texte brut et de code source.
- **`jq`** : Un outil en ligne de commande pour manipuler et analyser des données au format JSON de manière simple et efficace.
- **`yq`** : Une extension de `jq` qui permet de traiter des fichiers YAML en ligne de commande, facilitant la lecture et la modification de ce format.
- **`rsync`** : Un outil pour synchroniser des fichiers et des répertoires entre différentes machines ou systèmes de fichiers, connu pour son efficacité en termes de bande passante.
- **`rclone`** : Un outil en ligne de commande pour la gestion des fichiers dans des services de stockage cloud. Il permet de synchroniser, copier, monter et chiffrer des fichiers sur différents services cloud comme Google Drive, Backblaze, Amazon S3, et bien d'autres. `rclone` est très flexible et optimisé pour les transferts de fichiers à grande échelle entre environnements locaux et distants.
- **`lsof`** : Un utilitaire qui liste les fichiers ouverts sur le système, souvent utilisé pour diagnostiquer les problèmes liés aux fichiers et processus verrouillés.
- **`iftop`** : Un outil pour surveiller l'utilisation de la bande passante réseau en temps réel, affichant les connexions réseau et leur consommation de bande passante.

- **`ncdu`** : Un analyseur d'utilisation du disque en mode texte, très rapide et interactif, utilisé pour identifier les dossiers prenant le plus d'espace.
- **`tmux`** : Un multiplexeur de terminal qui permet de diviser une session de terminal en plusieurs panneaux et de garder des sessions ouvertes même après la fermeture du terminal.
- **`screen`** : Un multiplexeur de terminal qui permet de créer plusieurs sessions de terminal au sein d'un même terminal, utile pour garder des sessions actives après déconnexion.
- **`zsh`** : Une alternative au shell Bash, connue pour sa personnalisation avancée, sa gestion des complétions intelligentes et sa popularité avec le framework Oh My Zsh.
- **`fzf`** : Un utilitaire de fuzzy searching en ligne de commande qui permet de rechercher de manière interactive dans des fichiers, des historiques de commandes, ou d'autres listes.
- **`fd`** : Un outil de recherche de fichiers simplifié et plus rapide que la commande `find`. Il offre une syntaxe plus moderne et facile à utiliser.
- **`ripgrep`** : Un outil de recherche de texte dans des fichiers, extrêmement rapide et plus performant que `grep`, souvent utilisé pour les grands projets de code.
- **`nmap`** : Un puissant scanner de réseau utilisé pour découvrir des machines et services sur un réseau, ainsi que pour réaliser des audits de sécurité.
- **`ffmpeg`** : Un ensemble d'outils pour manipuler des fichiers multimédia, utilisé pour convertir, streamer et enregistrer de l'audio et de la vidéo.
- **`docker`** : Une plateforme de conteneurisation qui permet de créer, déployer et gérer des applications dans des environnements isolés.
- **`podman`** : Une alternative à Docker, offrant la gestion de conteneurs sans nécessiter de démon, souvent préférée pour des raisons de sécurité.
- **`aria2`** : Un téléchargeur de fichiers multi-protocoles (HTTP, FTP, BitTorrent, Metalink) en ligne de commande, offrant la possibilité de télécharger plusieurs fichiers simultanément.
- **`youtube-dl`** : Un utilitaire en ligne de commande pour télécharger des vidéos depuis YouTube et d'autres plateformes vidéo.
- **`gpg`** : Un outil pour chiffrer, signer et vérifier des données et des communications, utilisé pour garantir la sécurité et l'authenticité.
- **`vagrant`** : Un outil pour la gestion des machines virtuelles, simplifiant la création et la configuration d'environnements de développement reproductibles.
- **`virtualbox`** : Un logiciel de virtualisation permettant de créer et d'exécuter des machines virtuelles sur votre ordinateur.
- **`speedtest-cli`** : Un utilitaire pour tester la vitesse de la connexion Internet directement depuis le terminal, en utilisant les serveurs de Speedtest.net.
- **`netcat`** : Un outil polyvalent pour les opérations réseau, comme le port scanning, la redirection de ports ou l'établissement de connexions réseau simples.

## zsh

## systéme de fichier

### dossier personnel

- `/home/<user>/` **`documents`**

## rclone

### montage permanent

### service système 

## pyrhon virtual env 

### installation

### répertoire

- `/home/<user>/` **`documents`** `/` **`python-venv`** `/`

## reverse proxy

### nginx reverse proxy

### `site-avaible-domaine.fr`

### apache - caddy

## docker

### nextcloud-aio

- [github](https://github.com/nextcloud/all-in-one)

```
sudo docker run \
--init \
--sig-proxy=false \
--name nextcloud-aio-mastercontainer \
--restart always \
--publish 80:80 \
--publish 8080:8080 \
--publish 8443:8443 \
--volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config \
--volume /var/run/docker.sock:/var/run/docker.sock:ro \
nextcloud/all-in-one:latest
```

```
CONTAINER ID   IMAGE                              COMMAND                  CREATED        STATUS                 PORTS                                                                                  NAMES
9c71ef0ed96d   nextcloud/aio-apache:latest        "/start.sh /usr/bin/…"   21 hours ago   Up 4 hours (healthy)   80/tcp, 0.0.0.0:443->443/tcp, 0.0.0.0:443->443/udp, :::443->443/tcp, :::443->443/udp   nextcloud-aio-apache
d668dc23f739   nextcloud/aio-notify-push:latest   "/start.sh"              21 hours ago   Up 4 hours (healthy)                                                                                          nextcloud-aio-notify-push
0e42936f8765   nextcloud/aio-nextcloud:latest     "/start.sh /usr/bin/…"   21 hours ago   Up 3 hours (healthy)   9000/tcp                                                                               nextcloud-aio-nextcloud
0946a972271b   nextcloud/aio-imaginary:latest     "/start.sh"              21 hours ago   Up 4 hours (healthy)                                                                                          nextcloud-aio-imaginary
65bacbbea230   nextcloud/aio-redis:latest         "/start.sh"              21 hours ago   Up 4 hours (healthy)   6379/tcp                                                                               nextcloud-aio-redis
6aed0f3dd0a7   nextcloud/aio-postgresql:latest    "/start.sh"              21 hours ago   Up 4 hours (healthy)   5432/tcp                                                                               nextcloud-aio-database
cf3f18d1dabd   nextcloud/aio-talk:latest          "/start.sh superviso…"   21 hours ago   Up 4 hours (healthy)   0.0.0.0:3478->3478/tcp, 0.0.0.0:3478->3478/udp, :::3478->3478/tcp, :::3478->3478/udp   nextcloud-aio-talk
05187a658d3e   nextcloud/aio-collabora:latest     "/start-collabora-on…"   21 hours ago   Up 4 hours (healthy)   9980/tcp                                                                               nextcloud-aio-collabora

```

**`config.php`**

`sudo docker exec -it nextcloud-aio-nextcloud /bin/bash`


### jellyfin
### komga
### qbittorrent

### tmdb app

## wireguard

### installation (debian)

```
sudo apt install wireguard -y
```

### Fonctionnement

- répertoire de configuration : `/etc/wireguard/` 
- fichier de configuration : `/etc/wireguard/*.conf`

Chaque fichier de configuration représente une interface WireGuard, souvent nommée wg0.conf (ou wg1.conf pour plusieurs interfaces).

### Structure du fichier de configuration

Le fichier de configuration est divisé en deux parties principales : `[interface]` et `[peer]`

- `[interfance]` : représente les paramètres de l'interface WireGuard locale, c'est-à-dire la machine sur laquelle le fichier est configuré (client ou serveur)
- `[peer]` : Représente les informations de chaques pair avec lequel la machine va se connecter
- 

## syncthing




