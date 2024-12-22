# Comprendre `cron` et `crontab` sous Linux

## Introduction

**Cron** est un utilitaire de planification de tâches sous Unix/Linux qui permet d'exécuter automatiquement des scripts ou des commandes à des intervalles de temps spécifiés. **Crontab** (abréviation de "cron table") est le fichier de configuration qui spécifie les tâches à exécuter et leur programmation.

Ce guide vous expliquera en détail :

- Ce qu'est **cron** et comment il fonctionne.
- Comment utiliser **crontab** pour planifier des tâches.
- La syntaxe des fichiers crontab.
- Des exemples pratiques pour créer et gérer des tâches cron.
- Les commandes associées et les bonnes pratiques.

---

## 1. Qu'est-ce que `cron` ?

### 1.1 Description générale

- **Cron** est un démon (service en arrière-plan) qui exécute des tâches planifiées à des moments précis.
- Il est idéal pour automatiser les tâches répétitives, comme les sauvegardes, les mises à jour, l'envoi de rapports, etc.
- Cron vérifie chaque minute si une tâche doit être exécutée en fonction des horaires définis dans les fichiers crontab.

### 1.2 Le service `cron`

- Sur la plupart des systèmes Linux, le service cron est activé par défaut.
- Vous pouvez vérifier son statut avec :

  ```bash
  sudo systemctl status cron
  ```

- Pour démarrer, arrêter ou redémarrer le service :

  ```bash
  sudo systemctl start cron
  sudo systemctl stop cron
  sudo systemctl restart cron
  ```

---

## 2. Qu'est-ce que `crontab` ?

### 2.1 Définition

- **Crontab** est le fichier de configuration utilisé par cron pour savoir quelles tâches exécuter et quand.
- Chaque utilisateur peut avoir son propre fichier crontab, permettant de planifier des tâches spécifiques à cet utilisateur.
- Les fichiers crontab sont généralement stockés dans `/var/spool/cron/crontabs/`, mais ils ne doivent pas être modifiés directement. Utilisez les commandes fournies pour les gérer.

### 2.2 Commandes de base `crontab`

- **Lister les tâches cron de l'utilisateur courant** :

  ```bash
  crontab -l
  ```

- **Éditer le crontab de l'utilisateur courant** :

  ```bash
  crontab -e
  ```

- **Supprimer le crontab de l'utilisateur courant** :

  ```bash
  crontab -r
  ```

- **Utiliser le crontab d'un autre utilisateur (nécessite des privilèges sudo)** :

  - Lister :

    ```bash
    sudo crontab -u nom_utilisateur -l
    ```

  - Éditer :

    ```bash
    sudo crontab -u nom_utilisateur -e
    ```

---

## 3. Syntaxe d'une entrée crontab

Chaque ligne dans un fichier crontab représente une tâche planifiée et suit la syntaxe suivante :

```plaintext
* * * * * commande à exécuter
```

Les cinq premiers champs spécifient quand exécuter la commande :

1. **Minute** (0-59)
2. **Heure** (0-23)
3. **Jour du mois** (1-31)
4. **Mois** (1-12)
5. **Jour de la semaine** (0-7) (0 ou 7 = dimanche)

### 3.1 Signification des caractères spéciaux

- **`*`** : Tous les valeurs possibles pour ce champ.
- **`,`** : Séparation des valeurs multiples.
- **`-`** : Intervalle de valeurs.
- **`/`** : Pas d'incrémentation.

### 3.2 Exemples

- **Exécuter une commande tous les jours à 2h30 du matin** :

  ```plaintext
  30 2 * * * /chemin/vers/commande
  ```

- **Exécuter toutes les 15 minutes** :

  ```plaintext
  */15 * * * * /chemin/vers/commande
  ```

- **Exécuter tous les lundis à 8h00** :

  ```plaintext
  0 8 * * 1 /chemin/vers/commande
  ```

- **Exécuter du lundi au vendredi à 17h30** :

  ```plaintext
  30 17 * * 1-5 /chemin/vers/commande
  ```

---

## 4. Planification de tâches avec `crontab`

### 4.1 Éditer le crontab

Pour ajouter ou modifier des tâches, utilisez :

```bash
crontab -e
```

Cela ouvrira votre crontab dans l'éditeur de texte par défaut (souvent `nano` ou `vi`).

### 4.2 Ajouter une tâche

Par exemple, pour exécuter un script de sauvegarde tous les jours à minuit :

```plaintext
0 0 * * * /home/utilisateur/scripts/sauvegarde.sh
```

### 4.3 Enregistrer et quitter

- Dans **nano** :
  - **Ctrl + O** : Enregistrer.
  - **Entrée** : Confirmer le nom du fichier.
  - **Ctrl + X** : Quitter.
- Dans **vi** :
  - **`Esc`** : Passer en mode commande.
  - **`:wq`** : Enregistrer et quitter.

---

## 5. Variables d'environnement dans `crontab`

### 5.1 Variables courantes

- **SHELL** : Le shell à utiliser pour exécuter les commandes (par défaut `/bin/sh`).
- **PATH** : Chemins où chercher les exécutables (par défaut souvent limité).
- **MAILTO** : Adresse e-mail où envoyer les sorties (stdout et stderr) des tâches cron.

### 5.2 Exemple

Pour définir le PATH et désactiver les e-mails :

```plaintext
SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
MAILTO=""

# Tâches planifiées
* * * * * /chemin/vers/commande
```

---

## 6. Redirection de la sortie des tâches cron

### 6.1 Capturer la sortie dans un fichier

Pour enregistrer la sortie standard et les erreurs :

```plaintext
* * * * * /chemin/vers/commande >> /chemin/vers/log.txt 2>&1
```

- **`>>`** : Ajoute la sortie standard au fichier spécifié.
- **`2>&1`** : Redirige la sortie d'erreur standard vers la sortie standard.

### 6.2 Ignorer la sortie

Si vous ne souhaitez pas recevoir d'e-mails ni enregistrer la sortie :

```plaintext
* * * * * /chemin/vers/commande > /dev/null 2>&1
```

---

## 7. Bonnes pratiques

### 7.1 Chemins absolus

Toujours utiliser des chemins absolus pour les commandes et les fichiers, car le PATH dans cron est souvent limité.

### 7.2 Permissions

Assurez-vous que les scripts et les fichiers ont les permissions appropriées et sont exécutables.

### 7.3 Tester les scripts

Testez vos scripts manuellement avant de les planifier avec cron pour vous assurer qu'ils fonctionnent comme prévu.

### 7.4 Surveillance

- Vérifiez régulièrement les logs pour détecter les erreurs.
- Sur certains systèmes, les logs de cron se trouvent dans `/var/log/cron` ou sont intégrés dans `/var/log/syslog`.

---

## 8. Exemples pratiques

### 8.1 Exécuter un script toutes les heures

```plaintext
0 * * * * /home/utilisateur/scripts/mon_script.sh
```

### 8.2 Nettoyer un répertoire temporaire tous les jours à 3h00

```plaintext
0 3 * * * rm -rf /home/utilisateur/tmp/*
```

### 8.3 Synchroniser l'heure du système avec un serveur NTP toutes les semaines

```plaintext
0 0 * * 0 ntpdate pool.ntp.org
```

---

## 9. Gestion des tâches cron système

En plus des crontabs utilisateur, il existe des répertoires système pour planifier des tâches :

- **`/etc/cron.hourly/`** : Tâches exécutées toutes les heures.
- **`/etc/cron.daily/`** : Tâches exécutées quotidiennement.
- **`/etc/cron.weekly/`** : Tâches exécutées chaque semaine.
- **`/etc/cron.monthly/`** : Tâches exécutées chaque mois.

Pour ajouter une tâche, placez simplement un script exécutable dans le répertoire approprié.

---

## 10. Restrictions et autorisations

### 10.1 Fichiers `cron.allow` et `cron.deny`

- **`/etc/cron.allow`** : Liste des utilisateurs autorisés à utiliser `cron`.
- **`/etc/cron.deny`** : Liste des utilisateurs interdits d'utiliser `cron`.

Si **`cron.allow`** existe, seul les utilisateurs listés peuvent utiliser `cron`, et **`cron.deny`** est ignoré.

---

## Conclusion

**Cron** et **crontab** sont des outils puissants pour automatiser les tâches sous Linux. En comprenant leur fonctionnement et en suivant les bonnes pratiques, vous pouvez planifier efficacement des tâches répétitives et gagner du temps.

---

## Ressources supplémentaires

- **Page de manuel de cron** : `man cron`
- **Page de manuel de crontab** : `man crontab`
- **Tutoriels en ligne** : Recherchez des guides et des exemples supplémentaires pour approfondir votre compréhension.
- **Planificateur de crontab en ligne** : [Crontab Guru](https://crontab.guru/) - Outil en ligne pour aider à construire des expressions cron.

---

**Remarque** : Les configurations et les chemins peuvent varier légèrement en fonction de la distribution Linux utilisée. Assurez-vous d'adapter les instructions à votre environnement spécifique.

---