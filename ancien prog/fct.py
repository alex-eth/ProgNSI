
phrase=["Bonjour","à","toute", "la", "spe","NSI"]
def cinq(phrase) :
    i=0
    for elt in phrase:
        i=i+1
        if len(elt)==5 :
            return i

def voyelle(l) :
    voy="aeiou"
    rep=""
    for elt in l :
        if elt not in voy :
            rep=rep+elt
    return rep

def vo(l) :
    voo=0
    cons=0
    voy="aeiou"
    for elt in l :
        if elt not in voy :
            cons=cons+1
        else :
            voo=voo+1
    return voo, "voyelles et", cons, "consonnes"

def scrabble (l):
    score=0
    point1="aeiustmplnfrtbcd"
    point4="vokjhwq"
    point10="xyz"
    for elt in l:
        if elt in point1 :
            score+=1
        elif elt in point4 :
            score+=4
        elif elt in point10:
            score+=10
    return score

l=[]
def palindrome (liste):
    k=len(liste)
    for i in range (k) :
        l.append(liste[k-i])
    if l == liste:
        return True
    else:
        return False



