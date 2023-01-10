# -*- coding: utf-8 *-*
#-------------------------------------------------------------------------------
# Créer une image avec logo 1°5
# 0 = Noir   255 = Blanc
#-------------------------------------------------------------------------------
#
# Pour lire et écrire des images dans un fichier
from PIL import Image
#
# Création de l'image "mon_image"
# image.mode = RGB ou L pour echelle de gris
#
largeur = 1000
longueur = 500
mon_image = Image.new('RGB',(largeur,longueur),"blue")
#
# Ecriture du premier chiffre
#

for y in range(100,400):
    for x in range(280,320):
        p_rouge= 99 + (x//2)
        p_vert=134 +(x//2)
        p_bleu=156 + (x//4)
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))
#
# Ecriture du second chiffre
#
for y in range(100,140):
    for x in range(600,800):
        p_rouge=76
        p_vert=157
        p_bleu=131
        mon_image.putpixel((x,y),(p_rouge,p_vert,p_bleu))
for y in range(100,250):
    for x in range (600, 650) :
        pixel = 255
        mon_image.putpixel((x,y),pixel)
for y in range(250,280):
    for x in range(600,800):
        pixel = 255
        mon_image.putpixel((x,y),pixel)
for y in range(280,470):
    for x in range (800, 850) :
        pixel = 255
        mon_image.putpixel((x,y),pixel)
for y in range(460,480):
    for x in range(600,800):
        pixel = 255
        mon_image.putpixel((x,y),pixel)

# Ecriture des points
#

#
# Affichage de l'image
#
mon_image.save('sortie.png')
mon_image.show()