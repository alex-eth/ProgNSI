from PIL import Image, ImageTk
from tkinter import *

def Plus ():
    global nb, operation
    operation="+"
    nb=var_resultat.get()

def Moins ():
    global nb, operation
    operation="-"
    nb=var_resultat.get()

def Fois ():
    global nb, operation
    operation="*"
    nb=var_resultat.get()

def Diviser ():
    global nb, operation
    operation="/"
    nb=var_resultat.get()

def Egal ():
    global nb, operation
    if operation == "+" :
        rep=nb+var_resultat
    if operation == "-" :
        rep=nb-var_resultat
    if operation == "*" :
        rep=nb*var_resultat
    if operation == "/" :
        rep=nb/var_resultat


#-----------------------------------------------------
# Les constantes
#-----------------------------------------------------
LARG=300       # Taille du canevas
HAUT=300
TAILLE = 10    # Taille des objets

#-----------------------------------------------------
# Les fenetres
#-----------------------------------------------------
# On crée la fenêtre principale
fenetre = Tk()
fenetre.title("Calculatrice Graphique")

label_1 = Label(fenetre,text = "Calculatrice",fg = 'blue', bg = "yellow",font = "Arial 15 italic")
label_1.pack(padx = 5,pady = 5)

# Fenetre qui contient le choix des couleurs
frame_1 = Frame(fenetre,width = 350,height = 100,bg = "grey",bd = 4,relief = RAISED)
frame_1.pack(padx = 5,pady = 5)
# Les boutons
bouton_plus = Button(fenetre,text = " + ",bg = 'yellow',command = Plus)
bouton_moins = Button(fenetre,text = "-",bg = 'green',command = Moins)
bouton_fois = Button(fenetre,text = "*",bg = 'red' ,command = Fois)
bouton_diviser = Button(fenetre,text = "/",bg = 'pink',command = Diviser)
bouton_egal = Button(fenetre,text = "=",bg = 'purple',command = Egal)

var_resultat = IntVar()
saisie_resultat = Entry(fenetre,textvariable = var_resultat , width =10)
saisie_resultat.pack(padx=5,pady=5)

label_resultat = Label(fenetre, text="La reponse est :" ,fg='white',bg="magenta", font="Arial 15 italic")
label_resultat.pack(padx=5,pady=5)

bouton_plus.pack(side = LEFT,padx = 10,pady = 10)
bouton_moins.pack(side = LEFT,padx = 20,pady = 20)
bouton_fois.pack(side = RIGHT,padx = 30,pady = 30)
bouton_diviser.pack(side = RIGHT,padx = 40,pady = 40)
bouton_egal.pack(side = RIGHT,padx = 50,pady = 50)

fenetre.mainloop()
