from time import time
from random import *
import matplotlib.pyplot as plt
import numpy as np
from math import *

def echange(a,b) :
    c=a
    a=b
    b=c
    return a,b

def Tri (a,b,c):
    if a<b<c :
        return a,b,c
    if a<c<b:
        return a,c,b
    if b<a<c :
        return b,a,c
    if b<c<a :
        return b,c,a
    if c<a<b :
        return c,a,b
    if c<b<a :
        return c,b,a


def Triliste(l):
    li=[]
    liste=[]
    for elt in l :
        if elt == 0 :
            li.append(0)
        else :
            liste.append(1)
    li.append(liste)
    return li



def tri(tab) :
    debut = 0
    fin = len(tab)-1
    while debut != fin :
        if tab[debut] == 0 :
            debut = debut+1
        else :
            tab[debut],tab[fin]=tab[fin],tab[debut]
            fin = fin-1
    return tab

def Horner (mot):
    debut=time()
    mot=str(mot)
    resultat=1
    for i in range (len(mot)-1):
        resultat=resultat*2+int(mot[i+1])
    fin=time()
    return resultat, "en base de 2",(fin-debut)*1000,"miliseconde"


def double(x):
    return 2*x
assert double(2)==4, "erreur"


def TRI(l):
    mini=l[0]
    for i in range (len-1):
        for elt in l :
            if elt<mini :
                mini,elt =elt, mini
                mini=l[elt]
    return l

def tri_selection (t) :
    n = len(t)
    for i in range(n-1):
        min = i
        for j in range (i + 1, n):
            if t [ j ] < t [min] :
                min = j
        t [i ], t [min] = t [min],t [i ]
    return t

def grande_liste (x):
    l=[]
    for i in range (x):
        l.append(randint(1,99))
    return l

##
##l=grande_liste(1000000)
##
##debut=time()
##tri_selection(l)
##fin=time()
##
##print(fin-debut)


def Syracuse (x):
    nb=0
    l=[]
    while x!=1 :
        if x%2 ==0 :
            nb+=1
            x=x/2
            l.append(x)
        else :
            nb=nb+1
            x=3*x+1
            l.append(x)
    return nb ,"vols","et",l

def cherche (x,l):
    for elt in l :
        if x==elt:
            return True
    return False

def cherche_2 (x,l):
    for i in range (len(l)+1):
        if l[i] ==x :
            return True
    return False

def cherche_3 (x,l):
    return x in l

##x=int(input("chiffre de Syracuse"))
##x,y=Syracuse(x)
##
##plt.style.use('classic')
##fig=plt.figure(figsize=(5,3))
##ax = plt.axes(facecolor='#E6E6E6')
##ax.plot(x,y)
##plt.show()


def recherche (x,l):
    i=0
    while x >= l[i]:
        if x == l[i]:
            return True
        i=i+1
    return False

def bac (a,mot):
    nb=0
    for elt in mot:
        if elt==a:
            nb=nb+1
    return nb

def bac_1 (a,b):
    return b.count(a)


def dichotomie (l,x):
    debut=l[0]
    fin=len(l)-1
    while debut <fin :
        millieu=(fin+debut)//2
        if x < l[millieu] :
            fin=millieu-1
        elif x > l[millieu] :
            debut=millieu+1
        elif x==l[millieu]:
            return True
    return False

def compte(note):
    a=0
    for i in range (len(note)) :
        if note[i] == 20 :
            a=a+1
    return a

def compte_2 (note):
    a=0
    for elt in note :
        if elt ==20 :
            a=a+1
    return a

def compte_3 (note):
    return note.count(20)

def moyenne (note) :
    a=0
    for i in range (len(note)):
        a=a+note[i]
    return a/len(note)

def moyenne_2 (note):
    a=0
    for elt in note :
        a=a+elt
    return a/len(note)

def moyenne_3 (note) :
    return sum(note)/len(note)


def inverse (note):
    L=[]
    for i in range (len(note)) :
        a=note.pop()
        L.append(a)

    return L

def patinage(note):
    ma=max(note)
    mi=min(note)
    note.remove(ma)
    note.remove(mi)
    note.sort()
    return note



def moy_el (note):
    for l in note :
        print (l[0],"a eu",l[1])



def oral (l):
    li=[]
    for elt in l :
        if elt[1]=="NSI":
            li.append(elt[0])
    return li


def moy_mat (l):
    a=0
    b=0
    c=0
    for elt in l :
            if elt[0] == "Maths" and len(elt)>1 :
##                for n in range (1,len(elt)-1):
##                    a=a+n
##                math=a/n
                math=sum(elt[1:])/(len(l)-1)
            elif elt[0]=="Maths" :
                math="pas de note"

            if elt[0] == "NSI" and len(elt)>1 :
##                for n in range (1,len(elt)-1):
##                    b=b+n
##                nsi=b/n
                nsi=sum(elt[1:])/(len(l)-1)
            elif elt[0]=="NSI" :
                nsi="pas de note"

            if elt[0] == "SVT" and len(elt)>1 :
##                for n in range (1,len(elt)-1):
##                    c=c+n
##                svt=c/n
                svt=sum(elt[1:])/(len(l)-1)
            elif elt[0]=="SVT" :
                svt="pas de note"
    return "Maths :",math ,"NSI :", nsi, "SVT :",svt



def carte ():
    l=[]
    for i in range (1,14):
        if i <= 9 :
            l.append(str(i+1)+" ♦")
            l.append(str(i+1)+" ❤")
            l.append(str(i+1)+" ♠")
            l.append(str(i+1)+" ♣")

        if i == 10 :
            l.append("valet ♦")
            l.append("valet ❤")
            l.append("valet ♠")
            l.append("valet ♣")

        if i == 11 :
            l.append("dame ♦")
            l.append("dame ❤")
            l.append("dame ♠")
            l.append("dame ♣")

        if i == 12 :
            l.append("roi ♦")
            l.append("roi ❤")
            l.append("roi ♠")
            l.append("roi ♣")

        if i ==13 :
            l.append("as ♦")
            l.append("as ❤")
            l.append("as ♠")
            l.append("as ♣ ")
##    shuffle(l)
##    a=l.pop()
    return l

def car (n):
    table =[]
    for i in range (n) :
        if i %2 ==0 :
            table.append(i**2)
    return table

l=[i**2 for i in range (10) if i %2 ==0]


l1=[i*5 for i in range (10) if i%3==0  ]

liste = ["Anna" , "Ben" , "Chloe" , "Ali"]
la=[liste[i] for i in range (len(liste)) if liste[i][0]=="A" ]
laa=[nom for nom in liste if nom[0]=="A"]

l3=[nom for nom in liste if len(nom)==3]
liste2 = [["Anna",18],["Ben",14],["Chloe",11],["Don",15]]


l14=[nom[0] for nom in liste if nom[1] == 14 ]


e2={i for i in range (21) if i%2==0}
e3={i for i in range (11) if i%3==0}

e5={i for i in range (11) if i%5==0}












