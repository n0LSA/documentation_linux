---
title: cmos
date: 2024-08-27
tags:
  - ressource
status:
  - En cours
type de note:
  - ressource
référence:
  - "[[02_RESSOURCES/informatique/ordinateur/bios/clear-cmos]]"
  - "[[bios]]"
  - "[[volatile-memory]]"
---
# La puce CMOS

## Introduction

La raison pour laquelle les paramètres de configuration du BIOS sont stockés dans une puce **CMOS** distincte, alors que le BIOS lui-même est stocké sur une puce de mémoire non volatile (comme une EEPROM ou Flash ROM), réside principalement dans des considérations historiques et techniques liées à la flexibilité et à l'efficacité des systèmes informatiques.

### Explications historiques et techniques

1. **Mémoire non volatile pour le firmware BIOS :**
   - Le BIOS est un programme (firmware) qui doit être conservé même lorsque l'ordinateur est éteint. Par conséquent, il est stocké dans une mémoire non volatile comme une EEPROM ou une puce Flash ROM. Cette mémoire est parfaite pour stocker le firmware car elle conserve les données sans alimentation électrique.

2. **Pourquoi une mémoire CMOS séparée ?**
   - **Stockage dynamique et modifiable** : Le CMOS a été historiquement utilisé pour stocker les paramètres de configuration du BIOS (comme l'ordre de démarrage, les paramètres de mémoire, les réglages de l'horloge, etc.) car il permettait une modification rapide et fréquente des données. Contrairement à la ROM, qui était plus lente à écrire et nécessitait un processus spécifique pour être mise à jour (par exemple, lors du "flashage"), le CMOS était facile à modifier par le BIOS chaque fois que l'utilisateur changeait un paramètre.
   - **Alimentation par batterie** : Le CMOS est alimenté par une petite batterie sur la carte mère, ce qui lui permet de conserver les paramètres même lorsque l'ordinateur est éteint. C'était une solution pratique et peu coûteuse pour les anciens systèmes où la mémoire non volatile réinscriptible (comme Flash ROM) était soit inexistante, soit coûteuse et complexe à utiliser pour des écritures fréquentes.

3. **Évolution vers l'UEFI :**
   - **Fusion des rôles** : Avec l'introduction de l'UEFI (Unified Extensible Firmware Interface), beaucoup de systèmes modernes utilisent maintenant la même puce de mémoire non volatile (Flash) pour stocker à la fois le firmware et les paramètres de configuration. Les puces de mémoire Flash modernes sont suffisamment rapides et fiables pour permettre le stockage dynamique des paramètres de configuration directement dans la mémoire Flash, éliminant ainsi le besoin d'une puce CMOS séparée.
   - **Redondance et sauvegarde** : Cependant, certains systèmes continuent d'utiliser une petite portion de CMOS pour des raisons de compatibilité et de redondance, ou simplement par convention.

### Avantages d'utiliser le CMOS historiquement

- **Rapidité d'accès** : Les anciens systèmes utilisaient le CMOS pour stocker les paramètres du BIOS en raison de la rapidité d'accès et de la capacité à modifier facilement les données sans nécessiter de réécrire toute la puce de mémoire.
- **Séparation des fonctions** : Le fait de séparer les paramètres de configuration du BIOS du code du BIOS lui-même permettait de protéger le firmware contre les modifications accidentelles ou les pannes liées à une mise à jour défectueuse.

### Conclusion

Historiquement, le CMOS a été utilisé pour stocker les paramètres de configuration du BIOS parce qu'il était plus pratique et flexible pour des mises à jour fréquentes des paramètres par rapport aux technologies de mémoire non volatile disponibles à l'époque. Aujourd'hui, avec les systèmes UEFI modernes, cette distinction tend à disparaître, et de nombreux systèmes stockent désormais les paramètres directement dans la même mémoire Flash que le firmware. Cependant, la conception traditionnelle basée sur le CMOS reste encore en place dans certains systèmes, principalement pour des raisons de compatibilité et de convention.