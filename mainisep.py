#Implementation SHA-1 main.py
from fonctions import *
 
def Hash(message):
    """ Fonction prenant en argument une chaîne de caractères de moins de 2^64 bits et qui renvoie la chaîne de
    caracteres correspondant au ha.ché en hexadécimal à ce message obtenue à l'aide la fonction de hachage
    cryptographique SHA-1"""
 
    liste_ascii = Ascii_liste(message)                              # Conversion caractères --> ASCII
    liste_binaire = []
 
    for nombre in liste_ascii:                                      # Conversion ASCII --> Binaire
        liste_binaire.append(Binaire(int(nombre)))
    message_binaire = []

    for binaire in liste_binaire:                                   # Concaténation de toutes les listes de bianires
        message_binaire += binaire
 
    len_bin = len(message_binaire)
 
    message_binaire += [1]
 
    nb_zeros = (512-(len_bin+65))%512                               # Calcul du nombre de zéros à ajouter
    message_binaire += [0 for _ in range(nb_zeros)]                 # Concaténation des zéros à la fin du message
 
    message_binaire += Padded_bits_bin(Binaire(len_bin),64)         # Ajout de la représentation binaire de len_bin
                                                                    # paddé jusqu'à 64 bits
 
 
 
    message_binaire = Regroupe_liste_en_sslistes_nbelements(message_binaire,512)        # Découpage en sous-listes de
                                                                                        # 512 bits (blocks)
 
    message_binaire_final = []
 
    for _ in range(0,len(message_binaire)):                         # Découpage des sous-listes de 512 bits en
                                                                    # sous-listes de 32 bits (chunks)
 
        message_binaire_final.append(Regroupe_liste_en_sslistes_nbelements(message_binaire[_],32))
 
    h1 = 1732584193                                                 # Définition de l'état initial des valeurs
    h2 = 4023233417                                                 # de hachage intermédiaires
    h3 = 2562383102
    h4 = 271733878
    h5 = 3285377520
 
    for block in message_binaire_final:                             # Boucle qui calcule les valeurs de hachage
                                                                    # intermédiaires pour chaque bloc jusqu'à
                                                                    # l'obtention du haché final
 
 
        extended_block = Extend_mot(block)
 
        compresse = Compression(extended_block,h1,h2,h3,h4,h5)
 
        h1,h2,h3,h4,h5 = Decimal(Troncature_liste_n(Binaire(h1 + compresse[0]),32)),\
                         Decimal(Troncature_liste_n(Binaire(h2 + compresse[1]),32)),\
                         Decimal(Troncature_liste_n(Binaire(h3 + compresse[2]),32)),\
                         Decimal(Troncature_liste_n(Binaire(h4 + compresse[3]),32)),\
                         Decimal(Troncature_liste_n(Binaire(h5 + compresse[4]),32))
 
    # Calcul du haché final en héxadécimal
 
    hash = Binaire_hexa(Binaire(h1)) + Binaire_hexa(Binaire(h2))\
           + Binaire_hexa(Binaire(h3)) + Binaire_hexa(Binaire(h4)) + Binaire_hexa(Binaire(h5))
 
    return hash

