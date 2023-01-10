from tkinter import *

sommevoulu=0
c=50
d=10
def cinquante() :
    global sommevoulu, c, d
    label_ci["text"] = "50€"
    sommevoulu=sommevoulu+c
    label_retirer["text"] = "Voulez vous retirer cette somme" + str(sommevoulu) + "€"

def dix() :
    global sommevoulu, c, d
    label_dix["text"] = "10€"
    sommevoulu=sommevoulu+d
    label_retirer["text"] = "Voulez vous retirer cette somme" + str(sommevoulu) + "€"

def retirer():
    global sommevoulu, c, d
    sommevoulu=0
    label_retirer["text"] = "Voulez vous retirer cette somme" + str(sommevoulu) + "€"


fenetre = Tk()
fenetre.title("Distributeur de billet")

label_fenetre = Label(fenetre,text="Distributeur ",fg='green', bg="blue",font="Arial 15 italic")
label_fenetre.pack()

label_ci = Label(fenetre, text="50€ ", font="Arial 15 italic")
label_dix= Label(fenetre, text="10€ ", font="Arial 15 italic")
label_retirer= Label(fenetre, text="Voulez vous retirer cette somme" + str(sommevoulu) + "€", font="Arial 15 italic")

bouton_ci = Button(fenetre,text = " 50€",bg='yellow',command = cinquante )
bouton_ci.pack(padx=5,pady=10)
bouton_dix = Button(fenetre,text = " 10 ",bg='red',command = dix )
bouton_dix.pack(padx=5,pady=10)
bouton_retirer = Button(fenetre,text = "Voulez vous retirer cette somme : " + str(sommevoulu) + "€",bg='green',command = retirer )
bouton_retirer.pack(padx=5,pady=10)

bouton_quitter = Button(fenetre,text = " Quitter ",bg='grey' ,command = fenetre.destroy )
bouton_quitter.pack(side=RIGHT,padx=10,pady=10)
fenetre.mainloop()








