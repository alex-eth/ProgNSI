from tkinter import*
fen=Tk()
fen.title("Distributeur")
texte=Label(fen, text ="Texte", font=(20))
def fonction():
    print("Hello")
nom=StringVar()
bouton=Button(fen , text="Bouton" , font=(20), command = fonction, bg="red")
saisie=Entry(fen, textvariable=nom)
texte.pack(side=LEFT,padx=10,pady=10)
bouton.pack(side=RIGHT,padx=10,pady=10)
saisie.pack(side=BOTTOM)
fen.mainloop()