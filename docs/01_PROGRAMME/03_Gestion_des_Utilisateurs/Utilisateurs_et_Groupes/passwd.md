# Documentation de la commande `passwd` sous Linux (Debian)

## Introduction

La commande `passwd` est un utilitaire sous Linux utilisé pour changer les mots de passe des comptes utilisateurs. Elle permet aux utilisateurs de modifier leur propre mot de passe, et aux administrateurs système de gérer les mots de passe et les politiques de sécurité des comptes.

---

## Comment l'installer

Sur les systèmes Debian et ses dérivés, la commande `passwd` est généralement installée par défaut car elle fait partie des utilitaires essentiels du système. Toutefois, si elle n'est pas disponible pour une raison quelconque, vous pouvez l'installer en utilisant les commandes suivantes :

```bash
sudo apt update
sudo apt install passwd
```

**Explication :**

- `sudo apt update` : met à jour la liste des paquets disponibles.
- `sudo apt install passwd` : installe le paquet `passwd`.

---

## Comment fonctionne la commande

La commande `passwd` modifie le mot de passe d'un utilisateur en mettant à jour le fichier `/etc/shadow`, qui stocke les mots de passe chiffrés et les informations relatives aux comptes utilisateurs.

- **Pour un utilisateur standard :** L'exécution de `passwd` sans options permet de changer son propre mot de passe.
- **Pour un administrateur (root) :** L'administrateur peut changer le mot de passe de n'importe quel utilisateur en spécifiant son nom.

Lors du changement de mot de passe, la commande peut également mettre à jour des paramètres comme la date d'expiration du mot de passe, le verrouillage du compte, etc.

---

## Syntaxe de la commande avec des exemples

### Syntaxe générale

```bash
passwd [options] [nom_utilisateur]
```

- **`options`** : paramètres optionnels pour modifier le comportement de la commande.
- **`nom_utilisateur`** : le nom du compte utilisateur concerné. Si omis, la commande s'applique à l'utilisateur courant.

### Exemples

#### Exemple 1 : Changer son propre mot de passe

```bash
passwd
```

**Explication :**

- Exécute la commande en tant qu'utilisateur courant.
- Vous serez invité à entrer votre mot de passe actuel, puis le nouveau mot de passe.

#### Exemple 2 : Changer le mot de passe d'un autre utilisateur (en tant que root)

```bash
sudo passwd alice
```

**Explication :**

- `sudo` élève les privilèges pour exécuter la commande en tant que super-utilisateur.
- Change le mot de passe de l'utilisateur `alice`.

---

## Exemples concrets et détaillés

### Exemple 1 : Forcer un utilisateur à changer son mot de passe à la prochaine connexion

```bash
sudo passwd --expire bob
```

**Décomposition :**

- **`sudo`** : exécute la commande avec des privilèges administratifs.
- **`passwd`** : commande pour gérer les mots de passe.
- **`--expire`** : option pour expirer le mot de passe immédiatement.
- **`bob`** : nom de l'utilisateur ciblé.

**Explication :**

- L'utilisateur `bob` sera obligé de changer son mot de passe lors de sa prochaine connexion, renforçant ainsi la sécurité.

### Exemple 2 : Verrouiller un compte utilisateur

```bash
sudo passwd --lock caroline
```

**Décomposition :**

- **`--lock`** : verrouille le compte en empêchant toute connexion.
- **`caroline`** : nom de l'utilisateur à verrouiller.

**Explication :**

- Empêche l'utilisateur `caroline` de se connecter, sans supprimer son compte ni ses fichiers.

### Exemple 3 : Définir une durée maximale pour la validité d'un mot de passe

```bash
sudo passwd --maxdays=90 david
```

**Décomposition :**

- **`--maxdays=90`** : fixe la validité du mot de passe à 90 jours.
- **`david`** : utilisateur concerné.

**Explication :**

- Oblige l'utilisateur `david` à changer son mot de passe tous les 90 jours, améliorant la sécurité du compte.

---

## Liste complète des options de la commande

### Options et leur utilisation

1. **`-d`, `--delete`** : Supprime le mot de passe de l'utilisateur.

   - **Usage :**

     ```bash
     sudo passwd --delete emma
     ```

   - **Explication :**

     - Permet à l'utilisateur `emma` de se connecter sans mot de passe (non recommandé pour des raisons de sécurité).

2. **`-e`, `--expire`** : Expire immédiatement le mot de passe.

   - **Usage :**

     ```bash
     sudo passwd --expire frank
     ```

   - **Explication :**

     - Force `frank` à changer son mot de passe lors de sa prochaine connexion.

3. **`-i`, `--inactive`** : Définit le nombre de jours après l'expiration du mot de passe avant que le compte ne soit désactivé.

   - **Usage :**

     ```bash
     sudo passwd --inactive 30 grace
     ```

   - **Explication :**

     - Si `grace` ne change pas son mot de passe expiré après 30 jours, son compte sera désactivé.

4. **`-l`, `--lock`** : Verrouille le mot de passe du compte.

   - **Usage :**

     ```bash
     sudo passwd --lock henry
     ```

   - **Explication :**

     - Empêche toute connexion avec le mot de passe actuel de `henry`.

5. **`-n`, `--mindays`** : Définit le nombre minimum de jours entre les changements de mot de passe.

   - **Usage :**

     ```bash
     sudo passwd --mindays 5 isabelle
     ```

   - **Explication :**

     - `isabelle` devra attendre au moins 5 jours avant de pouvoir changer à nouveau son mot de passe.

6. **`-q`, `--quiet`** : Mode silencieux, réduit la sortie de la commande.

   - **Usage :**

     ```bash
     passwd --quiet
     ```

   - **Explication :**

     - Exécute la commande en affichant le moins d'informations possible.

7. **`-r`, `--repository`** : Modifie le mot de passe dans le référentiel spécifié.

   - **Usage :**

     ```bash
     sudo passwd --repository nis julien
     ```

   - **Explication :**

     - Change le mot de passe de `julien` dans le service NIS (Network Information Service).

8. **`-S`, `--status`** : Affiche l'état du mot de passe de l'utilisateur.

   - **Usage :**

     ```bash
     passwd --status karen
     ```

   - **Explication :**

     - Donne des informations sur le statut du mot de passe de `karen` (verrouillé, expiré, etc.).

9. **`-u`, `--unlock`** : Déverrouille le mot de passe du compte.

   - **Usage :**

     ```bash
     sudo passwd --unlock leon
     ```

   - **Explication :**

     - Permet à `leon` de se reconnecter en utilisant son mot de passe.

10. **`-w`, `--warndays`** : Définit le nombre de jours de préavis avant l'expiration du mot de passe.

    - **Usage :**

      ```bash
      sudo passwd --warndays 14 maria
      ```

    - **Explication :**

      - `maria` recevra un avertissement 14 jours avant que son mot de passe n'expire.

11. **`-x`, `--maxdays`** : Définit le nombre maximum de jours pendant lesquels le mot de passe est valide.

    - **Usage :**

      ```bash
      sudo passwd --maxdays 60 nicolas
      ```

    - **Explication :**

      - Le mot de passe de `nicolas` expirera après 60 jours.

### Exemple d'utilisation d'une option

#### Verrouiller et déverrouiller un compte utilisateur

- **Verrouiller :**

  ```bash
  sudo passwd --lock olivia
  ```

  **Explication :**

  - Empêche `olivia` de se connecter en verrouillant son mot de passe.

- **Déverrouiller :**

  ```bash
  sudo passwd --unlock olivia
  ```

  **Explication :**

  - Réautorise `olivia` à se connecter en déverrouillant son mot de passe.

---

## Conclusion

La commande `passwd` est un outil puissant pour la gestion des mots de passe et la sécurité des comptes utilisateurs sous Linux. En comprenant ses différentes options et leur utilisation, les administrateurs et les utilisateurs peuvent assurer une meilleure protection de leurs systèmes et de leurs données.
