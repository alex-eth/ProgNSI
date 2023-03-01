def chiffre (mot,cle):
    b = ""
    b1=""
    b2 = ""
    for lettre in mot :
        l1 = ord(lettre)
        l2 = bin(l1)
        b = b + l2 + " "
    for let in cle :
        l1 = ord(let)
        l2 = bin(l1)
        b1 = b1 + l2 + " "
    for i in range(len(b)):
        if b[i] != b1[i] :
            b2 = b2 + "1"
        elif b1[i] == " " :
            b2 = b2 + " "
        elif b1[i] == "b" :
            pass
        else :
            b2 = b2 + "0"
    l=[]
    tmp=""
    for lettre in b2:
        if lettre != " ":
            tmp = tmp + lettre
        else:
            l.append(tmp)
            tmp=""
    print(l)
    m=""
    for e in l :
        n = int(e,2)
        n2 = chr(n)
        m = m + n2

    return b,b1,b2,m

def dechiffre (mot, cle):
    b = ""
    m=""
    b1=""
    b2 = ""
    for lettre in mot :
        l1 = ord(lettre)
        l2 = bin(l1)
        b = b + l2 + " "
    for let in cle :
        l1 = ord(let)
        l2 = bin(l1)
        b1 = b1 + l2 + " "
    for i in range(len(b)):
        if b[i] != b1[i] :
            b2 = b2 + "1"
        elif b1[i] == " " :
            b2 = b2 + " "
        elif b1[i] == "b" :
            pass
        else :
            b2 = b2 + "0"
    print(b2)
    tmp = ""
    l =[]
    for lettre in mot:
        if lettre != " ":
            tmp = tmp + lettre
        else:
            l.append(tmp)
            tmp=""
    print(l)
    for e in l :
        n = int(e,2)
        n2 = chr(n)
        m = m + n2
    return m

