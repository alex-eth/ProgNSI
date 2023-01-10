# -*- coding: utf-8 *-*
#
#-----------------------------------------------------
# Projet Hackathon
#-----------------------------------------------------
#
from PIL import Image
from random import *
# ouvrir une image dans le dossier du programme Python
image_ini = Image.open("xey.jpg")


# taille de l'image
largeur, hauteur = image_ini.size
print(largeur,hauteur)

# Modification de la taille de l'image
image_retaille_1 = image_ini.resize((500, 500), Image.ANTIALIAS)
image_retaille_1.show()
### ou
#facteur=2
#largeur_2 = int(largeur*facteur)
#hauteur_2 = int(hauteur*facteur)
#image_retaille_2 = image_ini.resize((largeur_2, hauteur_2), Image.ANTIALIAS)
#image_retaille_2.show()

# créer une nouvelle image vide
image_new = Image.new("RGB", (500, 500))
a=5
b=5
# valeurs du pixel de coordonnées x, y --> (l'origine (0, 0) est en haut à gauche)
for x in range(450) :
    x=x+50
    for y in range(450) :
        pixel = image_retaille_1.getpixel((x, y))
        y=y+50

# valeurs des couleurs rouge, vert, bleu
        p_rouge = pixel[0]
        p_vert =  pixel[1]
        p_bleu =  pixel[2]

# modification du pixel de coordonnées x, y
        if y % 5 ==0 and y%5==0:
            image_new.putpixel((x, y),(randint(1,255), randint(1, 255), randint(1, 255)))
        else :
            image_new.putpixel((x, y),(p_rouge, p_vert, p_bleu))


# affichage de l'image finale
image_new.save('sortie.png')
image_new.show()
