import time

def style ():
    for i in range (25):
        print("❚", end="")
        time.sleep(0.04)

def txt_bin(mot):
    b = ""
    for lettre in mot :
        l1 = ord(lettre)
        l2 = bin(l1)
        b = b + l2 + " "
    return b


def xor (b, b1):
    b2 = ""
    for i in range(len(b)):
        if b[i] != b1[i] :
            b2 = b2 + "1"
        elif b1[i] == " " or b[i] ==" ":
            b2 = b2 + " "
        elif b1[i] == "b" or b[i] == "b":
            pass
        else :
            b2 = b2 + "0"
    return b2


def bin_txt (mot):
    l = []
    tmp = ""
    for lettre in mot:
        if lettre != " ":
            tmp = tmp + lettre
        elif lettre == "b":
            pass
        else:
            l.append(tmp)
            tmp = ""
    print(l)
    m = ""
    for e in l:
        n = int(e, 2)
        n2 = chr(n)
        m = m + n2
    return m

def chiffre (mot,cle):
    print("Chiffrement .....")
    b1 = txt_bin(mot)
    print("mot : ",b1)
    b2 = txt_bin(cle)
    print("cle : ",b2)
    resultat = xor(b1,b2)
    #b3 = bin_txt(resultat)
    print(resultat)
    return resultat

def dechiffre (mot, cle):
    print("Dechiffrement .....")
    resultat = xor(mot,cle)
    print(resultat)
    txt = bin_txt(resultat)
    return txt


a = chiffre("Hello","lycee")
dechiffre(a,"0b1101100 0b1111001 0b1100011 0b1100101 0b1100101")
style()
