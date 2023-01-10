##dico={"France":66, "Autriche":8, "NouvelleZ":5}
##
##personne = {
##"nom" : " BOB ",
##" Age" : 17,
##"hobby" : " NSI "
##}

##print("Je m'appelle",personne["nom"],"j'ai",personne[" Age"],"et j'aime ",personne["hobby"])


personne = {
"nom" : "Omer",
"age" : 10,
"hobby" : "Manger",
"?" : 0
}


def modifier (x,y) :
    personne.pop("?"[0])
    personne["nom"]=x
    personne["age"]=y
    return personne

def spe (dico) :
    a=set()
    for i in dico.values():
        a.add(i)
    return a

def NSI (dico) :
    return [c for c , val in dico.items( ) if val == "NSI"]


##dico={"Ana":"00331","Ben":"00432", "Cid":"0043"}
##
##def Pays (dico,a):
##    l=[]
##    a=str()
##    for cle,valeur in dico.items():
##        if valeur[2] == a[2] and valeur[3] == a[3]:
##            l.append(cle)
##    return l

dico2={"Dauce":"JP","Ashkar":"JP","Edvonio":"Alexis","Danieltchenkov":"Alexis"}

def mesamis (dico,prenom):
    l=[]
    for cle,valeur in dico.items():
        if valeur == prenom :
            l.append(cle)
    return l















