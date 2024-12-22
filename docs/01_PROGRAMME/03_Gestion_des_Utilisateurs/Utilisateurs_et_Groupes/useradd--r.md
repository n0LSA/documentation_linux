L'option `-r` de la commande `useradd` est utilisée pour créer un utilisateur système. Voici ce qu'elle fait en détail :

1. **Création d'un utilisateur système** : Contrairement aux utilisateurs normaux, un utilisateur système est destiné à des processus système ou des services (comme les démons). Il ne s'agit pas d'un compte destiné à être utilisé par une personne réelle pour se connecter.

2. **UID (User ID)** : Lorsqu'un utilisateur est créé avec l'option `-r`, l'UID (identifiant de l'utilisateur) est attribué automatiquement dans une plage spéciale réservée aux utilisateurs système. Sur de nombreuses distributions, cette plage est souvent comprise entre 1 et 999 ou 1 et 499, selon les configurations.

3. **Pas de répertoire personnel** : Par défaut, `useradd -r` ne crée pas de répertoire personnel pour l'utilisateur. Cela fait sens puisque les utilisateurs système n'ont pas besoin d'un environnement de travail complet comme un utilisateur humain.

4. **Pas de shell de connexion** : L'utilisateur créé avec `-r` a généralement un shell de connexion limité, tel que `/usr/sbin/nologin` ou `/bin/false`, car cet utilisateur n'est pas censé se connecter de manière interactive.

5. **Utilisation typique** : L'option `-r` est utilisée pour créer des comptes système pour des services ou des applications. Par exemple, lors de l'installation de certains logiciels comme `nginx` ou `mysql`, un utilisateur système est souvent créé avec cette option pour exécuter le service de manière isolée.

### Exemple de commande :
```bash
sudo useradd -r my_service_user
```
Cette commande crée un utilisateur système nommé `my_service_user` sans répertoire personnel ni possibilité de connexion interactive.

Si tu as besoin de gérer des services ou des démons spécifiques sur tes systèmes, cette option est particulièrement utile pour isoler les processus et éviter les conflits avec des utilisateurs standards.