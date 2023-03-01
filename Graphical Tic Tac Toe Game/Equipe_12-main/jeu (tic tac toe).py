from tkinter import *
from PIL import Image, ImageTk
from random import *
import time
from datetime import datetime

####################################################################################################
####################################################################################################

fenetre = Tk()
fenetre.title("TTT")


fenetre.geometry("1000x800")


v_start = False

# crétion des variables qui comptent les scores

highscore=0
nb_perdu=0
nb_gagner=0

# algorithme de verification
def verification ():
    global l
    j_gagner=False
    j_perdu=False

    #############################################################
    #verification si le joueur a completer une ligne horizontale
    if l[0] + l[1] + l[2] == 3 or l[3] + l[4] + l[5] == 3 or l[6] + l[7] + l[8] == 3:
        gagner()
        j_gagner = True

    # verification si le joueur a completer une ligne verticale
    if l[0] + l[3] + l[6] == 3 or l[1] + l[4] + l[7] == 3 or l[2] + l[5] + l[8] == 3 :
        gagner()
        j_gagner = True

    # verification si le joueur a completer une ligne diagonale
    if l[0] + l[4] + l[8] == 3 or l[6] + l[4] + l[2] == 3 :
        gagner()
        j_gagner = True
    #############################################################

    #############################################################
    # verification si l'ordi a completer une ligne horizontale
    if l[0] + l[1] + l[2] == 30 or l[3] + l[4] + l[5] == 30 or l[6] + l[7] + l[8] == 30:
        perdu()
        j_perdu = True

    # verification si l'ordi a completer une ligne verticale
    if l[0] + l[3] + l[6] == 30 or l[1] + l[4] + l[7] == 30 or l[2] + l[5] + l[8] == 30:
        perdu()
        j_perdu = True

    # verification si l'ordi a completer une ligne diagonale
    if l[0] + l[4] + l[8] == 30 or l[6] + l[4] + l[2] == 30:
        perdu()
        j_perdu = True
    ##############################################################

    #verifiction d'une potentielle égalité
    if 0 not in l and j_perdu == False and j_gagner == False :
        egalite()





def gagner ():
    global highscore, nb_gagner
    #afficher WIN sur tout le jeu
    canevas.create_image(0,0,anchor = NW, image = win)
    #score augmente
    highscore+=0.5
    nb_gagner+=0.5


def perdu ():
    global highscore, nb_perdu
    #afficher Lose sur tout le jeu
    canevas.create_image(0,0,anchor = NW, image = lose)
    highscore=0
    nb_perdu+=1




def egalite () :
    #afficher Egalite sur l'écran
    canevas.create_image(0,0,anchor = NW, image = img_egalite)


def AI ():
    global l

    # L'ordi choisit une place disponible sur le jeu

    a=randint(0,8)
    if l[a] == 0 :
        l[a]=10
        print("oui",a,l)

    elif 0 not in l :
        return "egalite"

    else :
        while l[a] != 0 :
            a=randint(0,8)
            print("non",a,l)

    # ajout de 10 à la position de la case (permet de verifier si qqun à gagner)
    l[a]=10

    # placement de rond par l'ordi
    if a == 0 :
        #placer x= 0 250 et y= 0 250
        canevas.create_image(0,0,anchor = NW, image = rond)
    if a == 1 :
        #placer x= 254 504 et y= 0 250
        canevas.create_image(254,0,anchor = NW, image = rond)
    if a == 2 :
        #placer x= 504 754 et y= 0 250
        canevas.create_image(504,0,anchor = NW, image = rond)
    if a == 3:
        #placer x= 0 250 et y= 254 504
        canevas.create_image(0,254,anchor = NW, image = rond)
    if a == 4:
        #placer x= 254 504 et y= 254 504
        canevas.create_image(254,254,anchor = NW, image = rond)
    if a == 5:
        #placer x= 504 754 et y= 254 504
        canevas.create_image(504,254,anchor = NW, image = rond)
    if a == 6:
        #placer x= 0 250  et y= 504 754
        canevas.create_image(0,504,anchor = NW, image = rond)
    if a == 7:
        #placer x= 254 504 et y= 504 754
        canevas.create_image(254,504,anchor = NW, image = rond)
    if a == 8:
        #placer x= 504 754 et y= 504 754
        canevas.create_image(504,504,anchor = NW, image = rond)

#algorithme qui permet d'efffacer les images afin de recommencer une partie
def effacer(canevas):
    canevas.delete(ALL)
    for i in range(3):
        for j in range(3):
            x = 8 + 246 * i
            y = 8 + 246 * j
            canevas.create_rectangle(x, y, x + 246, y + 246, width=4)



def start ():
    global l, v_start
    v_start = True

    # suprimer les croix et ronds et suprimer l'affichage win lose ou egalite
    effacer(canevas)
    #remise à zero de la liste permetant de verifier si qqun à gagner
    l=[0,0,0,
       0,0,0,
       0,0,0]
    #actualisation du score
    score()
    score_gagner()
    score_perdu()



####################################################################################################
####################################################################################################



larg_tic=246
long_tic=246




# On retaille à 200x200 Pixels
image_croix = Image.open("red-cross.png").resize((200,200), Image.ANTIALIAS)
image_croix = ImageTk.PhotoImage(image_croix)

#le joueur qui place les ronds

def Clic(event):
    global v_start
    if v_start:
        global l
        X=event.x
        Y=event.y
        if 0<X/long_tic<1 and 0<Y/larg_tic<1:
            l[0]=1
            canevas.create_image(0,0,anchor = NW, image =image_croix )
        if 1<X/long_tic<2 and 0<Y/larg_tic<1:
            l[1]=1
            canevas.create_image(250,0,anchor = NW, image = image_croix)
        if 2<X/long_tic<3 and 0<Y/larg_tic<1:
            l[2]=1
            canevas.create_image(504,0,anchor = NW, image =image_croix)
        if 0<X/long_tic<1 and 1<Y/larg_tic<2:
            l[3]=1
            canevas.create_image(0,250,anchor = NW, image = image_croix)
        if 1<X/long_tic<2 and 1<Y/larg_tic<2:
            l[4]=1
            canevas.create_image(250,250,anchor = NW, image = image_croix)
        if 2<X/long_tic<3 and 1<Y/larg_tic<2:
            l[5]=1
            canevas.create_image(504,250,anchor = NW, image = image_croix)
        if 0<X/long_tic<1 and 2<Y/larg_tic<3:
            l[6]=1
            canevas.create_image(0,504,anchor = NW, image = image_croix)
        if 1<X/long_tic<2 and 2<Y/larg_tic<3:
            l[7]=1
            canevas.create_image(250,504,anchor = NW, image = image_croix)
        if 2<X/long_tic<3 and 2<Y/larg_tic<3:
            l[8]=1
            canevas.create_image(504,504,anchor = NW, image = image_croix)

        #une fois que le joueur à placer son rond, on verifie si qqun à gagner puis c'est au tour de l'ordi
        verification()
        AI()
        verification()

#grille du jeu
canevas = Canvas(fenetre, width=750, height=750, bg="lightgrey")
canevas.pack(padx=5,pady=5)
canevas.place(x=249, y=25)
canevas.bind('<Button-1>', Clic)

#définition des images utilisées
rond = Image.open("rond.png").resize((246,246), Image.ANTIALIAS)
rond = ImageTk.PhotoImage(rond)

win = Image.open("win.gif").resize((750, 750), Image.ANTIALIAS)
win = ImageTk.PhotoImage(win)

lose = Image.open("lose.gif").resize((750, 750), Image.ANTIALIAS)
lose = ImageTk.PhotoImage(lose)

img_egalite = Image.open("Egalite.png").resize((750, 750), Image.ANTIALIAS)
img_egalite = ImageTk.PhotoImage(img_egalite)

tic = Label(fenetre,text = "Tic",fg = 'black',font = "Arial 15 italic")
tic.place(x=350, y=-3)
tac = Label(fenetre,text = "Tac",fg = 'black',font = "Arial 15 italic")
tac.place(x=600, y=-3)
toe = Label(fenetre,text = "Toe",fg = 'black',font = "Arial 15 italic")
toe.place(x=850, y=-3)


#bouttons
bouton_start = Button(fenetre,text = " Start ",bg = 'green', command = start)
bouton_start.configure(height=5, width=30)
bouton_start.place(x=10,y=600)
bouton_quit = Button(fenetre,text = " Quit ",bg = 'red',command = fenetre.destroy)
bouton_quit.configure(height=5, width=30)
bouton_quit.place(x=10,y=700)

#Affichage des scores
def score ():
    l_best_score= Label(fenetre,text = highscore,fg = 'green',font = "Arial 15 italic")
    l_best_score.place(x=0,y=100)
    l_best_score_2=Label(fenetre,text = "Bestscore (série de victoire)",fg = 'green',font = "Arial 15 italic")
    l_best_score_2.place(x=0,y=70)

def score_gagner ():
    global nb_gagner
    l_best_score= Label(fenetre,text = nb_gagner,fg = 'cyan',font = "Arial 15 italic")
    l_best_score.place(x=0,y=160)
    l_best_score_2=Label(fenetre,text = "Nombre de victoires total",fg = 'cyan',font = "Arial 15 italic")
    l_best_score_2.place(x=0,y=130)

def score_perdu ():
    global nb_perdu
    l_best_score= Label(fenetre,text = nb_perdu,fg = 'purple',font = "Arial 15 italic")
    l_best_score.place(x=0,y=220)
    l_best_score_2=Label(fenetre,text = "Nombre de défaites total",fg = 'purple',font = "Arial 15 italic")
    l_best_score_2.place(x=0,y=190)




#grille
for i in range(3):
    for j in range(3):
        x=8+246*i
        y=8+246*j
        canevas.create_rectangle(x,y,x+246,y+246 ,width=4)



fenetre.mainloop()


















