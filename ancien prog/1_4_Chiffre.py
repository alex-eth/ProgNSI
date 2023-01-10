# -*- coding: utf-8 *-*
# Chiffre de César, décalage de 3 rangs.
# Code ASCII de A = 65 à Z 90 et  a = 97 à z = 122

# Ouvrir un fichier
fichier = open('Texte_1.txt','r',encoding='utf8')
texte=fichier.read()

# Ecrire le texte chiffré avec un décalage de 3 rangs.
print("Texte clair : ")
print(texte)
print("")
print("Texte chiffré: ")

#Encryptage#

for i in range (len(texte)):
    lettre = texte[i]
    code = ord(lettre)
#pour les lettres entre A et W#
    if 65 <= code <= 88 or 97 <= code<= 119:
        code = code + 3
        lettre_new=chr(code)
        print (lettre_new, end ="")
#pour x,y et z#
    elif  87 <= code <= 90 or 120 <= code <= 122 :
        code=code -26
        lettre_new=chr(code)
        print (lettre_new, end ="")
#pour le reste
    else :
        lettre_new=chr(code)
        print (lettre_new, end ="")
fichier.close()



