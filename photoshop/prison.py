from PIL import Image
from random import*
# -*- coding: utf-8 *-*
#
#-----------------------------------------------------
# Projet Hackathon
#-----------------------------------------------------
image_ini = Image.open("xey.jpg")


# taille de l'image
largeur, hauteur = image_ini.size
print(largeur,hauteur)

# Modification de la taille de l'image
image_retaille_1 = image_ini.resize((500, 500), Image.ANTIALIAS)
##image_retaille_1.show()

serrure_ini= Image.open("serrure.png")
img_serrure= serrure_ini.resize((50, 50), Image.ANTIALIAS)

# créer une nouvelle image vide
image_new = Image.new("RGB", (500, 500))


# ouvrir une image dans le dossier du programme Python
def prison ():
##    image_ini = Image.open("xey.jpg")


# taille de l'image
    largeur, hauteur = image_ini.size
    print(largeur,hauteur)

# Modification de la taille de l'image
    image_retaille_1 = image_ini.resize((500, 500), Image.ANTIALIAS)
    image_retaille_1.show()
# Modification de la taille de l'image

### ou
#facteur=2
#largeur_2 = int(largeur*facteur)
#hauteur_2 = int(hauteur*facteur)
#image_retaille_2 = image_ini.resize((largeur_2, hauteur_2), Image.ANTIALIAS)
#image_retaille_2.show()

    serrure_ini= Image.open("serrure.png")
    img_serrure= serrure_ini.resize((50, 50), Image.ANTIALIAS)

# créer une nouvelle image vide
    image_new = Image.new("RGB", (500, 500))

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
            if x % 25 ==0 :
                image_new.putpixel((x, y),(125, 125, 125))
            else :
                image_new.putpixel((x, y),(p_rouge, p_vert, p_bleu))
    for x in range(0,49):
        for y in range (49):
            pi = img_serrure.getpixel((x,y))

            p_rouge = pi[0]
            p_vert =  pi[1]
            p_bleu =  pi[2]

            image_new.putpixel((x+50, y+250),(p_rouge, p_vert, p_bleu))


# affichage de l'image finale

    image_new.show()