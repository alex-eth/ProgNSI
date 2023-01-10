# -*- coding: utf-8 *-*
#---------------------------------------------------------------------
# Décryptage image 400 * 300 pixels
#---------------------------------------------------------------------
from PIL import Image # Pour lire et écrire des images dans un fichier

def poids_faible(n):
    ecriture_binaire = [0 for i in range(0,8)] # Initialisation Ecriture binaire
    for i in range(8):
       ecriture_binaire[i] =  n%2
       n=n//2
# Renvoie les 4 bits de poids faible
    return ecriture_binaire[0:4]

longueur = 400
hauteur  = 300

# Image à décrypter
img_ini = Image.open('Indice_3.png')

# Création d'une image vide
img_fin = Image.new('L',(longueur,hauteur),"grey")

# Boucle sur les pixels **** A compléter ***
for x in range (0,longueur):
    for y in range (0,hauteur) :
        pixel=img_ini.getpixel((x, y))
        f=poids_faible(pixel)
        pixel=f[0]*16 + f[1]*32 + f[2]*64 + f[3]*128
        img_fin.putpixel((x, y),pixel)

#
img_fin.show()





