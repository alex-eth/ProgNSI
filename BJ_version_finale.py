#  BLACKJACK VERSION FINALE
from random import*
import time
import os

os.system("Color 01")
dico_paquet = {"2♥":2, "2♦":2, "2♣":2, "2♠":2, "3♥":3,"3♦":3,"3♣":3,"3♠":3, "4♥":4,"4♦":4,"4♣":4,"4♠":4,"5♥":5,"5♦":5,"5♣":5,"5♠":5,"6♥":6,"6♦":6,"6♣":6,"6♠":6,"7♥":7,"7♦":7,"7♣":7,"7♠":7,"8♥":8,"8♦":8,"8♣":8,"8♠":8,"9♥":9,"9♦":9,"9♣":9,"9♠":9,"10♥":10,"10♦":10,"10♣":10,"10♠":10,"Valet ♥":10,"Valet ♦":10,"Valet ♣":10,"Valet ♠":10,"Dame ♥":10,"Dame ♦":10,"Dame ♣":10,"Dame ♠":10,"Roi ♥":10,"Roi ♦":10,"Roi ♣":10,"Roi ♠":10,"As ♥":1,"As ♦":1,"As ♣":1,"As ♠":1}

#Classe de la Banque

class Banque(object):
    def __init__ (self):
        self.l_joueur=[]
        self.l=[]
        self.cont=[]

    def inscrit(self,j):
        self.l_joueur.append(j)

    def nom(self):
        for j in self.l_joueur:
            print(j.nom)

# fonction qui distribue nb cartes à tous les joueurs ET qui calcule le score. Il renvoie le nom du joueur avec sa main et son score

    def distribuer(self, nb):

        for j in self.l_joueur:
            for i in range(nb):
                j.main.append(self.l.pop())
            for x in range(len(j.main)):
                for cle,valeur in dico_paquet.items():
                    if j.main[x]==cle:
                        j.score=j.score+valeur
            print("La main de",j.nom,"est", j.main,"et a un score de :", j.score)

# fonction qui demande aux joueurs (qui peuvent) s'ils veulent continuer, donc tirer une nouvelle carte.

    def continuer (self) :
        self.cont=0
        for j in self.l_joueur:
            if j.score < 21 :
                print("*** ",j.nom," : ",j.main," et score : ", j.score," ***")
                question = input("Souhaites tu tirer une nouvelle carte ? o/n :")
                if question == "o" or question == "oui" or question == "Oui" :
                    shuffle(self.l)
                    j.main.append(self.l.pop())

                    for cle,valeur in dico_paquet.items():
                        if j.main[len(j.main)-1]==cle:
                            j.score=j.score+valeur
                    print("*** ",j.nom," : ",j.main, " et score : ",j.score," ***")
                    print(" ")
                else :
                    print("Ok, tu passes ton tour !!!")
                    print(" ")
                    self.cont+=1
            else :
                self.cont+=1

# fonction qui crée le jeu de cartes

    def jeu_de_carte (self):
        l=self.l
        for i in range (1,14):
            if i <= 9 :
                l.append(str(i+1)+"♦")
                l.append(str(i+1)+"♥")
                l.append(str(i+1)+"♠")
                l.append(str(i+1)+"♣")

            if i == 10 :
                l.append("Valet ♦")
                l.append("Valet ♥")
                l.append("Valet ♠")
                l.append("Valet ♣")

            if i == 11 :
                l.append("Dame ♦")
                l.append("Dame ♥")
                l.append("Dame ♠")
                l.append("Dame ♣")

            if i == 12 :
                l.append("Roi ♦")
                l.append("Roi ♥")
                l.append("Roi ♠")
                l.append("Roi ♣")

            if i ==13 :
                l.append("As ♦")
                l.append("As ♥")
                l.append("As ♠")
                l.append("As ♣ ")

        shuffle(l)
        return l

# fonction qui recherche le vainqueur.

    def fin(self):
        a=True
        max=0
        gagnant="Pas de vainqueur"
        while a==True:
            for j in self.l_joueur:
                if j.score<=21:
                    if j.score>max:
                        max=j.score
                        gagnant=j
                    elif j.score==max:
                        return "*** Il y a une égalité entre tous les joueurs qui ont comme score :", max," ***"

            if max==0:
                print("*** ","Il n'y a pas de vainqueur dans cette partie !"," ***")
                a=False

            else:
                print("*** ",gagnant.nom,"a gagné la partie avec un score de :",max," ***")
                a=False

# classe du Joueur

class Joueur(object):
    def __init__ (self, nom):
        self.nom=nom
        self.score=0
        self.main=[]

# Inscritpion des joueurs #

Alexis=Joueur("Alexis")
Tanguy=Joueur("Tanguy")
Prof=Joueur("Mr Dauce")
b=Banque()
b.inscrit(Tanguy)
b.inscrit(Alexis)
b.inscrit(Prof)


def style ():
    print("Loading game : ", end="")
    for i in range (25):
        time.sleep(0.025)
        print("█ ", end="")
    print(" ")

# Début du jeu #
def jouer ():
    print(" ")
    style()
    print(" ")
    b.jeu_de_carte()
    b.distribuer(2)
    print(" ")
    time.sleep(2)
    b.continuer()
#    print(" ")
    while b.cont != len(b.l_joueur) :
        time.sleep(2)
        b.continuer()
#        print(" ")
    b.fin()

jouer()




