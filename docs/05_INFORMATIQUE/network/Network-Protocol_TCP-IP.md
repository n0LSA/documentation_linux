# la suite des protocoles TCP/IP

## Couche 7 (Application)

| Protocol | Port(s)                   | Acronyme                                       | Description                                                                                                                | couche          |
| -------- | ------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------- |
| HTTP     | 80                        | Hype Text Transfer Protocol                    |                                                                                                                            | 7 - Application |
| HTTPS    | 443                       | HyperText Transfer Protocol Secure             | Encapsulation du protocol HTTP via le protocole TLS                                                                        | 7 - Application |
| FTP      | 21(commandes) 20 (donnés) | File Transfer Protocol                         |                                                                                                                            | 7 - Application |
| SFTP     | 22                        | SSH File Transfer Protocol                     | Transfert de fichiers sécurisé utilisant SSH pour le chiffrement                                                           | 7 - Application |
| SSH      | 22                        | Secure Shell                                   | Accès sécurisé à distance des systèmes informatiques via une interface en ligne de commande (CLI - Command Line Interface) | 7 - Application |
| Telnet   | 23                        | Telnet                                         | Accès à distance non sécurisé à des systèmes informatiques.                                                                | 7 - Application |
| SMTP     | 25                        | Simple Mail Transfer Protocol                  | Envoi de mail entre serveurs de messagerie                                                                                 | 7 - Application |
| POP3     | 110                       | Post Office Protocol                           | Récupération de mail sur un serveur                                                                                        | 7 - Application |
| IMAP     | 143                       | Internet Message Access Protocol               | Acces et gestion de mails directement sur le serveur de messagerie                                                         | 7 - Application |
| DNS      | 53                        | Domain Name Server                             | Résolution des noms de domaine en adresse IP                                                                               | 7 - Application |
| DHCP     | 67(serveur) 68(client)    | Dynamic Host Configuration Protocol            | Attributions automatiques des adresses IP et autre paramètres réseaux                                                      | 7 - Application |
| SNMP     | 161(requêtes) 162(trap)   | Simple Network Management Protocol             | Gestion et surveillance des équipement réseau.                                                                             | 7 - Application |
| LDAP     | 389                       | Lightweight Directory Protocol Access Protocol | Accès et gestion des services d'annuaire distribué                                                                         | 7 - Application |
| RDP      | 3389                      | Remote Desktop Protocol                        | Accès a distance aux environnement de bureau Windows                                                                       | 7 - Application |
| SMB      | 445                       | Server Message Block                           | Partage de fichiers et d'imprimantes sur un réseau local                                                                   | 7 - Application |
| NTP      | 123                       | Netwok Time Protocol                           | Synchronisation des horloges des systèmes informatique sur un réseau                                                       | 7 - Application |
| TFTP     | 69                        | Trivial Transfer Protocol                      | Transfert de fichier simple et leger, souvent utilisé pour le démarrage réseau des dispositif                              | 7 - Application |
| SIP      | 5060                      | Session Initial Protocol                       | Établissement et gestion des sessions multimédias, comme les appels VoIP.                                                  | 7 - Application |
| RTP      | 5004                      | Real-Time Transport Protocol                   | VoIP                                                                                                                       | 7 - Application |
| MQTT     | 1883                      | Message Queing Telemetry Transpor              | Messagerie pour application IoT                                                                                            | 7 - Application |

## Couche 3 (Réseau)

| Protocol | Port(s) | Acronyme                          | Description                                                                          | couche                 |
| -------- | ------- | --------------------------------- | ------------------------------------------------------------------------------------ | ---------------------- |
| ICMP     |         | Internet Control Message Protocol | Envoi de message d'erreur t d'information concernant les opération réseau (ex: ping) | 3 - Réseau             |
| ARP      |         | Adress Resolution Protocol        | Association des adresses IP aux adresses MAC sur un réseau local                     | 2 - Liaison de données |
| IGMP     |         | Internet Group Message Protocol   | Gestion des groupes multicast su un réseau IP                                        | 3 - Réseau             |
| OSPF     | 89      | Open Shortest Path First          | Routage dynamique pour déterminer le meilleur chemin des paquets dans un réseaux     | 3 - Réseau             |
| BGP      | 179     | Border Gateway Protocol           | échange des information de routage entre système autonomes sur internet              | 3 - Réseau             |

---



