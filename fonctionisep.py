#Implementation SHA-1 fonction.py

hex_table = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],["0","1","2","3","4","5","6","7","8","9","a",\
                                                         "b","c","d","e","f"]]
 
# Table de conversion utilisée pour convertir les nombres binaires en héxadécimal
 
def complement(liste):
    """ Fonction prenant en argument un liste de 0 et de 1 correspondant à un nombre binaire et renvoyant la liste de
    0 et de 1 correspondant au complément binaire du nombre de départ."""
    for i in range(len(liste)):
        if liste[i]==1:
            liste[i]=0
        else:
            liste[i]=1
    return liste
 
def fonction1(a,b,c):                                # Fonction booléenne #1 de SHA-1
    """ Fonction prenant en arguments 3 entier naturel et renvoyant un entier naturel obtenu grâce à des opérations binaires sur ces 
    nombres, elle contribue à la confusion de SHA-1"""
 
    return (a&b)| Decimal(complement(Binaire(a))) & c
 
def fonction2(a,b,c):                                # Fonction booléenne #2 de SHA-1
    """ Fonction prenant en arguments 3 entier naturel et renvoyant un entier naturel obtenu grâce à des opérations binaires sur ces 
    nombres, elle contribue à la confusion de SHA-1"""
 
    return (a & b) | ( a & c) | (b & c)
 
def fonction3(a,b,c):                                # Fonction booléenne #3 de SHA-1
   """ Fonction prenant en arguments 3 entier naturel et renvoyant un entier naturel obtenu grâce à des opérations binaires sur ces 
    nombres, elle contribue à la confusion de SHA-1"""
    return a^b^c
 
def Ascii_liste(liste):
 
    """Fonction admettant en paramètre une liste dont les termes sont des chaînes de caractères et qui renvoie une
     liste contenant le code ASCII + 256 (afin que chaque caractère soit codé sur le même nombre de bits) convertit en chaîne de caractères correspondant au représentant de chaque 
     caractère de la liste"""
 
    liste_ascii = []
 
    for caractere in liste:
        liste_ascii.append(str(ord(caractere)+256))
 
    return liste_ascii
 
def Representant_inverse(liste):
 
    """Fonction admettant en paramètre une liste dont les termes sont les représentants de differents caractères 
    et qui renvoie une liste contenant les caractères en questions"""
 
    liste_caracteres = []
 
    for representant in liste:
        liste_caracteres.append(chr(int(representant)))
 
    return liste_caracteres
 
def Regroupe_liste_en_sslistes_nbelements(objet,nbelements=1):
 
    """Fonction admettant en paramètre une liste dont les termes sont des strings et qui
     renvoie la même liste mais dont les termes sont fusionés (nbterme)s à (nbterme)"""
 
    nbelements -= 1
    liste_regroupee = []
    liste_transfert = []
    compteur = 0
    compteur_nbelements = 0
 
    while compteur<len(objet):
 
        if compteur_nbelements<nbelements:
            liste_transfert.append(objet[compteur])
            compteur_nbelements += 1
        else:
            liste_transfert.append(objet[compteur])
            liste_regroupee.append(liste_transfert)
            liste_transfert = []
            compteur_nbelements = 0
 
        compteur += 1
 
    if liste_transfert!=[]:
        liste_regroupee.append(liste_transfert)
 
    return liste_regroupee
 
def Fusion_termes_liste_str(liste):
 
    """Fonction admettant en paramètre une liste de chaînes de caractères et renvoie une chaine de caractères
     contenant simplement tous les termes de la liste précédentes en un"""
 
    liste_fusionnee = ""
 
    for chaine in liste:
        liste_fusionnee += chaine
 
    return liste_fusionnee
 
def Binaire(nombre):
    """ Fonction prenant en argument un entier naturel nombre et renvoyant le nombre binaire correspondant codé sur
    32 bits sous forme de liste de 0 et de 1."""
 
    if nombre==0:
        return [0]*32
    quotient = nombre
    binaire = []
    while quotient!=0:
        reste = quotient%2
        binaire.append(reste)
        quotient = quotient//2
    binaire.reverse()
    if len(binaire)<32:
        binaire = (32-len(binaire))*[0] + binaire
    return binaire
 
def Padded_bits_bin(bin,desiredlen):
    """ Fonction prenant en argument une liste de 0 et de 1 correspondant à un nombre binaire et un entier naturel 
     correspondant à la longueur en bits voulue, et qui va insérer autant de 0 que nécessaire au millieu de la liste
     afin d'obtenir la longueur désirée. """
 
    length = len(bin)
    for _ in range(desiredlen-length):
        bin.insert(length//2,0)
    return bin
 
def Rotate_left(mot,n_rot):
    """ Fonction prenant en argument une liste de 0 et de 1 correspondant à un nombre binaire et un entier naturel
    n_rot et renvoie la liste obtenue en effectuant l'opération binaire de rotation à gauche de n_rot bits."""
 
    return mot[n_rot:] + mot[:n_rot]
 
def Decimal(nombre_bin):
    """ Fonction prenant en argument une liste de 0 et de 1 correspondant à un nombre binaire et renvoyant l'entier
    naturel correspondant à la conversion en décimal de ce nombre binaire."""
 
    decimal = 0
    nombre_bin.reverse()
    for _ in range(len(nombre_bin)):
        if  nombre_bin[_]==1:
            decimal += 2 ** _
    return decimal
 
def Extend_mot(mot):
    """ Fonction prenant en argument une liste correspondant à un bloc de 16 chunks de 32 bits du message à coder
    et qui renvoie une liste étendue à 80 chunks de 32 bits selon un procédé déféni par l'algorithme de SHA-1."""
 
    liste_extend = mot
    for indice in range(16,80):
        liste_extend.append(Rotate_left(Binaire(Decimal(liste_extend[indice-3])\
        ^Decimal(liste_extend[indice-8])^Decimal(liste_extend[indice-14])^Decimal(liste_extend[indice-16])),1))
    return liste_extend
 
def Binaire_hexa(nombre_bin):
    """ Fonction prenanat en argument une liste de 0 et de 1 correspondant à un nombre binaire et qui renvoie la 
    chaîne de caractères correspondant à la conversion de ce nombre binaire en héxadécimal. """
 
    if len(nombre_bin)%4!=0:
        for _ in range(4 - len(nombre_bin) % 4):
            nombre_bin.insert(0,0)
    nombre_bin_decoupe = Regroupe_liste_en_sslistes_nbelements(nombre_bin,4)
    nb_hexa = ""
    for _ in nombre_bin_decoupe:
        index = hex_table[0].index(Decimal(_))
        nb_hexa += hex_table[1][index]
    return nb_hexa
 
def Troncature_liste_n(liste,n):
    """ Fonction prenant en argument une liste de x éléments et un entier naturel n et renvoyant cette même liste
    tronquée à n éléments."""
 
    liste = liste[:n]
 
    return liste
 
 
 
def Compression(mot,a,b,c,d,e):
    """ Fonction prenant en argument un mot étendu à 80 chunks de 32 bits et les variables, entiers naturels, de hachage
     intermédiaires a, b, c, d et e. Et qui renvoie les nouvelles valeurs de hachage intermédiaires (entiers naturels) 
     conformément à l'algorithme officiel de SHA-1."""
 
    y1 = 1518500249             # Définition de l'état initial de la fonction de chiffrement par bloc
    y2 = 1859775393
    y3 = 2400959708
    y4 = 3395469782
 
    for rang in range(80):
        if 0<= rang <= 19:
            etat = Decimal(Rotate_left(Binaire(a), 5)) + fonction1(b, c, d) + e + Decimal(mot[rang]) + y1
            a, b, c, d, e = Decimal(Troncature_liste_n(Binaire(etat),32)), a, Decimal(Rotate_left(Binaire(b), 30)), c, d
        elif 20 <= rang <= 39:
            etat = Decimal(Rotate_left(Binaire(a),5)) + fonction3(b, c, d) + e + Decimal(mot[rang]) + y2
            a,b,c,d,e = Decimal(Troncature_liste_n(Binaire(etat),32)),a,Decimal(Rotate_left(Binaire(b),30)),c,d
        elif 40 <= rang <= 59:
            etat = Decimal(Rotate_left(Binaire(a), 5)) + fonction2(b, c, d) + e + Decimal(mot[rang]) + y3
            a, b, c, d, e = Decimal(Troncature_liste_n(Binaire(etat),32)), a, Decimal(Rotate_left(Binaire(b), 30)), c, d
        else:
            etat = Decimal(Rotate_left(Binaire(a), 5)) + fonction3(b, c, d) + e + Decimal(mot[rang]) + y4
            a, b, c, d, e = Decimal(Troncature_liste_n(Binaire(etat),32)), a, Decimal(Rotate_left(Binaire(b), 30)), c, d
 
    return [a,b,c,d,e]
