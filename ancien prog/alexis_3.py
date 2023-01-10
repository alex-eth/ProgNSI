fichier = open('Texte_3.txt','r',encoding='utf8')
texte=fichier.read()
liste="abcdefghijklmnopqrstuvwxyz"

vide=[]
for y in liste:
    a=0
    for xx in texte:
        if y == xx :
            a=a+1
    vide.append(a)
mx=max(vide)
le=vide.index(mx)
le=le+1
n=le-5

for i in range (len(texte)):
    lettre = texte[i]
    code = ord(lettre)

#pour les lettres entre a+net z#
    if 65+n-1 <= code <= 90 or 97+n <= code<= 122:
        code = code -n
        lettre_new=chr(code)
        print (lettre_new, end ="")

#pour a+n #
    elif  65 <= code < 65+n-1 or 97 <= code < 97+n :
        code=code +26-n
        lettre_new=chr(code)
        print (lettre_new, end ="")

#pour le reste
    else :
        lettre_new=chr(code)
        print (lettre_new, end ="")
fichier.close()

