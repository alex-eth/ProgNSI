
from PIL import Image
from random import *
image_ini = Image.open("xey.jpg")

largeur, hauteur = image_ini.size
print(largeur,hauteur)

image_retaille_1 = image_ini.resize((500, 500), Image.ANTIALIAS)


image_new = Image.new("RGB", (500, 500))
def points_colorees ():


    for x in range(450) :
        x=x+50
        for y in range(450) :
            pixel = image_retaille_1.getpixel((x, y))
            y=y+50

            p_rouge = pixel[0]
            p_vert =  pixel[1]
            p_bleu =  pixel[2]

            if x % 5 ==0 and y%5==0:
                image_new.putpixel((x, y),(randint(1,255), randint(1,255), randint(1,255)))
            else :
                image_new.putpixel((x, y),(p_rouge, p_vert, p_bleu))



    image_new.show()