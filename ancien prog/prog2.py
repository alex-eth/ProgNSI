


def Syracuse (x):
    vol=0
    alt=x
    while x !=1 :
        if x%2==0 :
            x=x/2
            vol=vol+1
            if x > alt :
                alt=x
        else :
            x=3*x+1
            vol+=1
            if x > alt :
                alt=x
    return vol, alt


##x=int(input("Nombre"))
##
##if x %2==0 :
##    print("paire")
##else :
##    print("impaire")


def parité(x):
    if x%2==0:
        return True
    return False

def parité2(x):
    return  x%2==0








class Emprunteur (object) :
    def __init__(self,nom,classe) :
        self.nom=nom
        self.classe=classe
        self.l=[]

    def ajout (self,livre):
        self.l.append(livre)

    def nombre (self):
        self.nb=len(self.l)
        print(self.nb)

    def rendre(self,n):
        if n > len(self.l):
            return "Pas assez de livres"
        for i in range (n):
            self.l.pop()

    def pret (self,nom,nom2):
        livre = nom.l.pop()
        nom2.l.append(livre)
















