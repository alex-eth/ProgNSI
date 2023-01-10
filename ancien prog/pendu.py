from random import randint

l=["bonjour","salut","coucou","table","chaise","ordinateur"]
n=randint(0, len(l)-1)
mot=[]
m=l[n]
for i in range (len(l)):
    mot.append(m[i])

affichage=[]
for i in range (len(mot)):
    print("_", end =" ")
    affichage.append("_")

while mot != affichage :
    lettre=input("Choisit une lettre !!!")
    for i in range (len(mot)):
        if mot[i]==lettre:
            affichage[i]=lettre
##        else :
##            print("Non !!!")
    print(str.join())

print("Trouvé !!!!")

