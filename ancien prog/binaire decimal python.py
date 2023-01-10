entier=input("Quel entier ?")
n=0
k=0
o=0
for i in range(len(entier)):
    n=n-1
    nb=int(entier[n])
    if nb==1:
        k=2**i
        o=o+k
print(o)

#ou bien on peut faire :

#res=0
#l=len(x)
#for i in range(l):
#    res=res+int(x[i])*2**(l-i-1)
#print(res)