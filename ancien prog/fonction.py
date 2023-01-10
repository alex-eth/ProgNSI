import math
def ff(n1,n2):
    m=(n1+n2)/2
    return m


def concour (Nnsi, Nmath,mot) :
    if mot == nsi :
        resul=((Nmath+2)*Nnsi)/3
        resul=float()
    if mot == math :
        resul=((Nnsi+2)*Nmath)/3
    return resul

def cercle(r):
    longueur=math.pi*r*2
    aire=math.pi*r**2
    return "longueur : "+str(longueur) + " Aire: " +str(aire)

def Degre(x):
    temp=(x-32)*5/9
    return "temperature :" + str(temp)+" °"



def nb_case (R) :
    case=1
    u=1
    somme=u
    while somme <R :
        u=u*2
        somme=somme+u
        case=case+1
    return case



def multiple(N2,N1):
    if N2%N1==0 or N1%N2 ==0 :
        return True
    return False

def operation(nb1,nb2) :
    somme = nb1+nb2
    produit = nb1*nb2
    return somme, produit


def carre (num):
    if math.sqrt(num) == int(math.sqrt(num)) :
        return True
    return False

def is_integer(a) :
    if a==int(a):
        return True
    return False


mention ="pas de mention"

def Trimestre(note) :
    if note >= 14 :
        return "Bon trimestre"
    elif note >= 10:
        return "trimestre correct"
    return "Attention"


k=10
def f() :
    global k
    k=k+3
print("k vaut", k)
f()
print("k vaut ", k)
f()
print("k vaut ", k)



def moyenne (liste):
    moy=0
    for i in liste :
        moy=moy+i
    total=moy/len(liste)
    return total


def trie (liste) :
    for i in liste :
        if liste[i] > liste[i+1] :
            return False
        return True

l=[]
def inverse (liste):
    k=len(liste)
    for i in range (k) :
        l.append(liste[k-i])
    return l

def extrema (L) :
    min=L[0]
    max=L[0]
    for i in range (len(L)):
        if L[i] < min :
            min=L[i]
        if L[i] > max :
            max=L[i]
    return "Max est :"+ str(max)+ "Min est :"+ str(min)

def position (L):
    max=L[0]
    pos=0
    for i in range (len(L)):
        if L[i] > max :
            max=L[i]
            pos=pos+1
    return "Max est :"+ str(max)+ " Position est :" + str(pos+1)

def longueur (l) :
    a=0
    try :
        while True:
            l[a]
            a=a+1
    except IndexError :
        return str(a)








































