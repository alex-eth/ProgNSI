from tkinter import *
from PIL import Image, ImageTk
import sqlite3

connection = sqlite3.connect("BdD.db")
cursor = connection.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, prenom TEXT, nom TXT, numero INT, adresse TXT, email TXT, date TXT)")

fenetre = Tk()
fenetre.title("Répertoire de contact")


fenetre.geometry("1000x800")
fenetre.configure(bg = "SteelBlue3")


def ajout():
    cursor.execute("INSERT INTO contact(prenom, nom, numero) VALUES(?,?,?)", data)


def supprimer (data) :
    cursor.execute('DELETE FROM contact WHERE prenom = ? AND nom = ?', data)


def recherche_num (n):
    cursor.execute('SELECT * FROM contact WHERE prenom = ? AND nom = ?',n)
    liste = cursor.fetchall()
    print(liste)


def recherche_contact (n):
    cursor.execute('SELECT * FROM contact WHERE numero = ?',n)
    liste = cursor.fetchall()
    print(liste)

def afficher () :
    cursor.execute('SELECT * FROM contact')
    liste = cursor.fetchall()
    print("*** ",liste, " ***")


canevas = Canvas(fenetre, width=500, height=600, bg="SteelBlue4")
canevas.pack(padx=5,pady=5)
canevas.place(x=5, y=100)

titre= Label(fenetre,text = "ʀᴇᴘᴇʀᴛᴏɪʀᴇ (*powered by Windows 95)",fg = 'black',font = "Arial 15 italic")
titre.place(x=5, y=5)

bouton_ajout = Button(fenetre,text = " Ajouter un contact ",bg = 'dark khaki', command = ajout)
bouton_ajout.configure(height=5, width=30)
bouton_ajout.place(x=700,y=100)

bouton_sup = Button(fenetre,text = " Suprimmer un contact  ",bg = 'dark khaki', command = ajout)
bouton_sup.configure(height=5, width=30)
bouton_sup.place(x=700,y=225)

bouton_recherche = Button(fenetre,text = " Rechercher un contact ",bg = 'dark khaki', command = ajout)
bouton_recherche.configure(height=5, width=30)
bouton_recherche.place(x=700,y=350)

bouton_r_num = Button(fenetre,text = " Rechercher par numéro ",bg = 'dark khaki', command = ajout)
bouton_r_num.configure(height=5, width=30)
bouton_r_num.place(x=700,y=475)

bouton_quit = Button(fenetre,text = " Quitter ",bg = 'red4', command = fenetre.destroy)
bouton_quit.configure(height=5, width=30)
bouton_quit.place(x=700,y= 600)


fenetre.mainloop()
