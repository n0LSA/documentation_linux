## Introduction

Lorsque l'ordinateur démarre, le processeur exécute une série d'instructions qui permettent d'initialiser le matériel et de charger le système d'exploitation. Voici un aperçu des étapes et des instructions clés que le processeur suit lors de ce processus, du moment où l'alimentation est allumée jusqu'à ce que le système d'exploitation prenne le relais :

## ressources

- https://wentzwu.com/2024/01/30/how-computers-boot-up/
- https://www.msnoob.com/windows-computer-boot-sequence.html
- https://subscription.packtpub.com/book/security/9781838827793/9/ch09lvl1sec77/windows-boot-sequence
- https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/windows-boot-issues-troubleshooting
- https://baptiste-wicht.developpez.com/tutoriels/hardware/demarrage/
- https://www.malekal.com/quel-est-le-processus-et-sequence-de-demarrage-dun-pc-post-bios-os/

## V1

### 1. **Mise sous tension (Power-On)**
   - **Reset du CPU** : Lorsque l'alimentation est activée, le processeur est réinitialisé. Il commence à exécuter des instructions à partir d'une adresse prédéfinie en mémoire. Cette adresse est spécifiée par le fabricant du processeur et correspond généralement à l'endroit où se trouve le BIOS sur la puce EEPROM ou Flash ROM.

### 2. **Exécution des premières instructions du BIOS**
   - **Adresse de démarrage** : Le processeur commence à exécuter les instructions situées à une adresse fixe. Sur les systèmes x86, cette adresse est généralement 0xFFFFFFF0 (pour les anciens systèmes BIOS) ou une adresse similaire en fonction de l'architecture.
   - **Lecture du BIOS** : Le processeur lit les instructions du BIOS/UEFI stockées dans la puce EEPROM/Flash ROM et commence à les exécuter. Ces instructions incluent la configuration de base du processeur et de la mémoire pour préparer l'initialisation du matériel.

### 3. **Power-On Self Test (POST)**
   - **Initialisation du matériel** : Le BIOS exécute une série de tests pour vérifier que les composants matériels de base sont opérationnels (mémoire RAM, processeur, carte graphique, etc.). C'est le POST (Power-On Self Test).
   - **Diagnostic et messages d'erreur** : Si des erreurs sont détectées, le BIOS peut afficher des messages d'erreur à l'écran ou émettre des bips via le haut-parleur interne pour indiquer un problème (par exemple, un échec de la RAM ou un problème de carte graphique).

### 4. **Initialisation des périphériques**
   - **Contrôleurs matériels** : Le BIOS initialise les contrôleurs de périphériques intégrés, comme les contrôleurs de disque (SATA, NVMe), les ports USB, les interfaces réseau, etc.
   - **Tableau de routage des interruptions (Interrupt Vector Table)** : Le BIOS initialise également le tableau de routage des interruptions, qui permet au processeur de gérer les interruptions matérielles correctement.

### 5. **Configuration des paramètres de démarrage**
   - **Configuration des périphériques de démarrage** : Le BIOS détermine l'ordre des périphériques de démarrage en fonction des paramètres configurés (par exemple, disque dur, lecteur optique, clé USB).
   - **Chargement du bootloader** : Le BIOS localise le secteur de démarrage du premier périphérique de démarrage valide. Le secteur de démarrage contient un petit programme appelé **bootloader**, qui est le prochain élément exécuté par le processeur.

### 6. **Transfert au Bootloader**
   - **Chargement en mémoire** : Le BIOS charge le bootloader (généralement situé dans le Master Boot Record, ou MBR, pour les systèmes utilisant le MBR, ou dans une partition spécifique pour les systèmes GPT) en mémoire vive (RAM).
   - **Exécution du Bootloader** : Le processeur commence à exécuter les instructions du bootloader. Le rôle du bootloader est de charger le noyau du système d'exploitation dans la mémoire et de préparer l'environnement pour qu'il puisse fonctionner.

### 7. **Chargement du noyau du système d'exploitation**
   - **Sélection du système d'exploitation** : Si plusieurs systèmes d'exploitation sont installés, le bootloader peut présenter un menu permettant de choisir lequel démarrer (par exemple, via GRUB pour Linux).
   - **Chargement du noyau** : Le bootloader charge le noyau du système d'exploitation sélectionné en mémoire vive. Le noyau est le cœur du système d'exploitation, responsable de la gestion du matériel et de la coordination des processus.
   - **Passage de contrôle** : Une fois le noyau chargé, le bootloader transfère le contrôle au noyau du système d'exploitation, qui commence à s'exécuter.

### 8. **Initialisation du système d'exploitation**
   - **Initialisation du noyau** : Le noyau initialise les structures internes, configure les pilotes matériels, et démarre les processus de base nécessaires au fonctionnement du système.
   - **Démarrage des services** : Le système d'exploitation commence à démarrer les services et les démons (processus en arrière-plan) nécessaires, comme la gestion des réseaux, la gestion des fichiers, etc.
   - **Chargement de l'interface utilisateur** : Enfin, le système d'exploitation charge l'interface utilisateur (par exemple, l'écran de connexion ou le bureau), permettant à l'utilisateur de commencer à utiliser l'ordinateur.

### Conclusion

Le processus de démarrage d'un ordinateur implique une série complexe d'étapes, où le processeur exécute successivement des instructions du BIOS/UEFI, du bootloader, puis du noyau du système d'exploitation. La puce EEPROM/Flash ROM où est stocké le BIOS/UEFI joue un rôle crucial en fournissant les premières instructions qui permettent au système de s'initialiser et de charger le système d'exploitation.


## V2

Si vous souhaitez configurer le BIOS, cela se produit entre les étapes **2** et **5** de la séquence de démarrage que vous avez listée. Voici plus de détails sur le processus et comment le chargement des paramètres sauvegardés se passe :

### Étape 2. Exécution des premières instructions du BIOS

- **Accès à l'interface de configuration du BIOS** : Immédiatement après la mise sous tension et le début de l'exécution des premières instructions du BIOS, vous pouvez accéder à l'interface de configuration du BIOS. Cela se fait généralement en appuyant sur une touche spécifique (comme **F2**, **DEL**, **ESC**, ou **F10**) pendant le démarrage, avant que l'ordinateur ne commence à charger le système d'exploitation.
  
- **Interface utilisateur** : Une fois que vous avez appuyé sur la touche appropriée, le BIOS interrompt le processus de démarrage normal et charge l'interface utilisateur du BIOS/UEFI, qui est souvent une interface textuelle (pour les BIOS traditionnels) ou graphique (pour les systèmes UEFI).

### Étape 3. Power-On Self Test (POST)

- **Exécution des tests matériels** : Si vous n'intervenez pas pour accéder au BIOS, le BIOS poursuit son exécution en effectuant le POST. Cependant, si vous avez accédé au BIOS, le POST peut être retardé ou certaines de ses fonctions limitées, car vous êtes maintenant en mode configuration.
  
- **Modification des paramètres** : Dans l'interface de configuration du BIOS, vous pouvez modifier une variété de paramètres, tels que l'ordre de démarrage, les réglages de la mémoire RAM, les paramètres du processeur, les options de sécurité comme les mots de passe, etc.

### Étape 5. Configuration des paramètres de démarrage

- **Chargement des paramètres sauvegardés** : Lorsque vous modifiez les paramètres dans le BIOS, ceux-ci sont sauvegardés dans la mémoire non volatile (généralement le **CMOS**) lorsque vous choisissez de "sauvegarder et quitter" l'interface de configuration. Ces paramètres sont ensuite utilisés lors des étapes suivantes du démarrage.
  
- **Application des paramètres** : Si vous avez modifié des paramètres critiques (comme l'ordre de démarrage), ces paramètres sont immédiatement appliqués par le BIOS lorsque vous quittez l'interface. Le BIOS va alors utiliser ces nouveaux paramètres pour configurer les périphériques et préparer le transfert du contrôle au bootloader.

### Chargement des paramètres sauvegardés

- **Accès aux paramètres au démarrage** : Lors de chaque démarrage, le BIOS lit les paramètres stockés dans la mémoire CMOS. Ces paramètres incluent les configurations que vous avez éventuellement modifiées lors d'une session précédente dans le BIOS.
  
- **Interprétation des paramètres** : Le BIOS utilise ces paramètres pour déterminer comment initialiser les périphériques, quel ordre de démarrage utiliser, et comment gérer diverses autres options matérielles.
  
- **Réinitialisation des paramètres par défaut** : Si les paramètres stockés sont corrompus ou si vous souhaitez revenir aux paramètres d'usine, vous pouvez réinitialiser le BIOS à ses valeurs par défaut depuis l'interface de configuration.

### Conclusion

La configuration du BIOS se passe juste après l'exécution des premières instructions du BIOS, mais avant que le système ne commence le processus POST et la configuration des paramètres de démarrage. Lorsque vous accédez à l'interface de configuration du BIOS, vous pouvez modifier les paramètres qui sont ensuite sauvegardés dans la mémoire CMOS. Ces paramètres sont ensuite chargés et utilisés à chaque démarrage pour déterminer comment le système doit être initialisé.