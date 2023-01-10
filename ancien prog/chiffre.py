entier=int(input("Donner un chiffre"))
chiffre=0
a=1
nb=1
while nb >= 1 :
    chiffre=chiffre+1
    nb=entier//a
    a=a*10
print("Il y a ",chiffre-1,"chiffres")