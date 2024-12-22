---
title: clear-cmos
date: 2024-08-27
tags:
  - ressource
status:
  - En cours
type de note:
  - ressource
référence:
  - "[[bios]]"
  - "[[02_RESSOURCES/informatique/ordinateur/bios/firmware]]"
---

Sur les systèmes modernes utilisant **UEFI** où les paramètres de configuration sont stockés directement dans la puce de mémoire non volatile (comme la Flash ROM), le processus de réinitialisation des paramètres (équivalent à l'ancien "clear CMOS") est légèrement différent mais suit des principes similaires. Voici comment cela fonctionne :


## V1

### 1. **Option de Réinitialisation via l'Interface UEFI**

La méthode la plus courante pour réinitialiser les paramètres sur un système UEFI consiste à utiliser l'interface UEFI elle-même :

- **Accès à l'UEFI** : Lors du démarrage de l'ordinateur, appuyez sur la touche qui permet d'accéder à l'interface UEFI (généralement **DEL**, **F2**, **ESC**, ou **F10**).
- **Réinitialisation aux valeurs par défaut** : Dans l'interface UEFI, il y a souvent une option intitulée quelque chose comme "Load Default Settings", "Restore Factory Defaults", ou "Load Optimized Defaults". En sélectionnant cette option, vous réinitialisez les paramètres UEFI à leurs valeurs par défaut d'usine, c'est-à-dire les paramètres initialement définis par le fabricant de la carte mère.

### 2. **Bouton ou Jumper de Réinitialisation (Clear CMOS)**

Même sur les cartes mères modernes avec UEFI, beaucoup incluent encore un bouton physique ou un jumper pour réinitialiser les paramètres :

- **Bouton de réinitialisation CMOS** : Certaines cartes mères récentes disposent d'un bouton physique sur la carte mère, souvent appelé "Clear CMOS" ou "Reset". Ce bouton permet de réinitialiser tous les paramètres UEFI aux valeurs par défaut. Le bouton peut être situé directement sur la carte mère ou sur le panneau arrière des ports.
- **Jumper de réinitialisation** : Comme sur les systèmes plus anciens, certaines cartes mères UEFI conservent un jumper de réinitialisation du CMOS. Déplacer ce jumper en position de réinitialisation (souvent en le plaçant sur deux broches spécifiques pendant quelques secondes) réinitialise les paramètres UEFI aux valeurs par défaut.

### 3. **Retrait de la Batterie CMOS**

Sur certains systèmes, le retrait de la batterie CMOS peut toujours fonctionner comme une méthode de réinitialisation des paramètres :

- **Retirer la batterie** : Débranchez l'ordinateur, puis retirez la batterie CMOS de la carte mère pendant environ 5 à 10 minutes. Ensuite, réinsérez la batterie et redémarrez le système.
- **Effet** : Cela peut provoquer une réinitialisation des paramètres UEFI aux valeurs par défaut. Cette méthode fonctionne principalement sur les systèmes où la batterie CMOS joue encore un rôle dans la sauvegarde des paramètres.

### 4. **Réinitialisation via un utilitaire logiciel**

Certains systèmes d'exploitation ou utilitaires fournis par le fabricant de la carte mère permettent également de réinitialiser les paramètres UEFI depuis l'interface du système d'exploitation :

- **Utilitaires spécifiques** : Par exemple, certaines cartes mères offrent des utilitaires Windows ou Linux qui permettent de réinitialiser les paramètres UEFI directement depuis le système d'exploitation, ce qui est utile pour les serveurs ou les systèmes distants.

### Conclusion

Sur les systèmes UEFI modernes, la réinitialisation des paramètres peut être effectuée de plusieurs façons, souvent via l'interface UEFI elle-même ou en utilisant des méthodes physiques comme un bouton ou un jumper. Même si le CMOS n'est plus utilisé de la même manière qu'auparavant, la plupart des cartes mères conservent une méthode matérielle pour forcer la réinitialisation des paramètres, ce qui est essentiel pour résoudre les problèmes de configuration ou restaurer le système à un état connu.

## V2

Si vous avez perdu le mot de passe d'un BIOS UEFI, il existe plusieurs méthodes pour réinitialiser le BIOS, mais la méthode spécifique dépend de la carte mère et du fabricant. Voici les options généralement disponibles :

### 1. **Utilisation du Jumper de Réinitialisation (Clear CMOS)**
   - **Localisation du Jumper** : La plupart des cartes mères ont un jumper de réinitialisation du CMOS, souvent étiqueté "CLR_CMOS", "CLEAR", "JCMOS1", ou quelque chose de similaire. Consultez le manuel de la carte mère pour localiser ce jumper.
   - **Procédure** :
     1. Éteignez l'ordinateur et débranchez-le de l'alimentation.
     2. Localisez le jumper sur la carte mère.
     3. Déplacez le jumper sur les broches de réinitialisation (généralement, cela signifie déplacer le jumper de sa position par défaut vers les deux broches de réinitialisation) pendant environ 5 à 10 secondes.
     4. Remettez le jumper dans sa position d'origine.
     5. Rebranchez l'ordinateur et redémarrez. Le mot de passe BIOS/UEFI devrait être réinitialisé, ainsi que tous les autres paramètres.

### 2. **Retirer la Batterie CMOS**
   - **Procédure** :
     1. Éteignez l'ordinateur et débranchez-le de l'alimentation.
     2. Ouvrez le boîtier et localisez la batterie CMOS, qui est une petite pile ronde (généralement de type CR2032) sur la carte mère.
     3. Retirez délicatement la batterie de son support.
     4. Attendez environ 5 à 10 minutes pour s'assurer que la mémoire CMOS est complètement déchargée.
     5. Réinsérez la batterie et remettez l'ordinateur sous tension.
     6. Redémarrez l'ordinateur. Le mot de passe BIOS/UEFI et les autres paramètres devraient être réinitialisés.

### 3. **Utilisation d'un Bouton de Réinitialisation (Clear CMOS)**
   - **Procédure** :
     1. Éteignez l'ordinateur et débranchez-le de l'alimentation.
     2. Localisez le bouton de réinitialisation CMOS sur la carte mère ou à l'arrière du boîtier (si présent).
     3. Appuyez sur ce bouton pendant 5 à 10 secondes.
     4. Rebranchez l'ordinateur et redémarrez. Les paramètres UEFI, y compris le mot de passe, devraient être réinitialisés.

### 4. **Réinitialisation via l'UEFI ou Utilitaires du Fabricant**
   - **Utilitaire de réinitialisation** : Certains fabricants de cartes mères fournissent des utilitaires spécifiques qui peuvent être utilisés pour réinitialiser les paramètres UEFI, y compris le mot de passe, mais cela nécessite généralement d'avoir accès au système d'exploitation.
   - **Mot de passe maître** : Certains BIOS/UEFI ont des mots de passe maîtres ou des fonctions de récupération accessibles via le support technique du fabricant. Cela implique souvent de contacter le support avec des informations spécifiques sur la carte mère pour obtenir un mot de passe de réinitialisation.

### 5. **Flashage du BIOS/UEFI**
   - **Procédure de Flashage** : Si les méthodes physiques ne fonctionnent pas et que vous avez les connaissances nécessaires, vous pouvez tenter de flasher le BIOS/UEFI avec une version mise à jour ou la même version. Ce processus peut parfois réinitialiser le BIOS à ses paramètres d'usine, y compris le mot de passe. Cependant, c'est une méthode risquée et complexe qui peut endommager la carte mère si elle est mal exécutée.

### 6. **Contact avec le Support Technique**
   - **Assistance Professionnelle** : Si aucune des méthodes ci-dessus ne fonctionne, contacter le support technique du fabricant de la carte mère peut être nécessaire. Ils peuvent fournir des instructions spécifiques ou, dans certains cas, demander l'envoi de la carte mère pour une réinitialisation.

### Conclusion

Réinitialiser un mot de passe BIOS/UEFI perdu nécessite souvent une intervention physique sur la carte mère, que ce soit via un jumper, en retirant la batterie CMOS, ou en utilisant un bouton de réinitialisation. Si ces méthodes échouent ou si vous n'êtes pas à l'aise de les effectuer vous-même, il est recommandé de contacter le support technique du fabricant pour obtenir de l'aide.