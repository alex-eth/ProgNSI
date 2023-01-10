from tkinter import *


def Euro() :
    sommevoulu=var_resultat.get()
    resultat=sommevoulu*0.89
    label_euro["text"] = "€" + str(resultat)



def Dollard() :
    sommevoulu=var_resultat.get()
    resultat=sommevoulu*1.13
    label_dollard["text"] = "$" + str(resultat)



fenetre = Tk()
fenetre.title("Convertisseur Euro en Dollard")

var_resultat = IntVar()
saisie_resultat = Entry(fenetre,textvariable = var_resultat , width =10)
saisie_resultat.pack(padx=5,pady=5)

label_fenetre = Label(fenetre,text="Convertisseur ",fg='green', bg="blue",font="Arial 15 italic")
label_fenetre.pack()

label_euro = Label(fenetre, text="€ ", font="Arial 15 italic")
label_euro.pack(padx=100, pady=10)
label_dollard = Label(fenetre, text="$ ", font="Arial 15 italic")
label_dollard.pack(padx=100, pady=10)

# Les boutons
bouton_euro = Button(fenetre,text = " € ",bg = 'yellow',command = Euro)
bouton_euro.pack(side = LEFT,padx = 100,pady = 10)
bouton_dollard = Button(fenetre,text = "$",bg = 'green',command = Dollard)
bouton_dollard.pack(side = RIGHT,padx = 100,pady = 10)



fenetre.mainloop()





