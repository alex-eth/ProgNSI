#rep=input("As_tu compris le chapitre Equation ?")
#a=0
#while rep == "non":
#    a=a+1
#    print("Fais l'exercice", a)
#    rep = input("As tu compris ?")
#print("C'est terminé, tu as fais ", a ,"exercice")



li=[]
note=int(input("Entre tes notes"))
li.append(note)
a = True
total = 0

while a:
    li.append(note)
    note=input("Entre une autre note")
    if note =="":
        for i in range (len(li)) :
            total=total+li[i]
            i=i+1
        moy=total//len(li)
        print("Ta moyenne est",moy)
        a = False
    note=int()