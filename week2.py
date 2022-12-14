#algorithm
sayı=int(input("Bir değer giriniz: "))
x=0
for i in range(1,sayı):
    for j in range(1,i+1):
        x+=1
        print(x,end=" ")
    print()
   
sayı=int(input("Bir değer giriniz: "))
for i in range(1,sayı+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
#binary to decimal
s=input("İkilik sayıyı giriniz: ")
sayac=0
toplam=0
k=0
for i in s:
    sayac+=1

for j in range((sayac-1),-1,-1):
    if s[j]=="1":
        toplam+=2**k
        k+=1
    else:
        k+=1
print(toplam)

#listedekieleman tekrarını bulma
l=[1,2,3,3,4,5,3,2,2,6,7]

for j in range(len(l)):
    sayac=0
    for i in range(len(l)):
        if l[j]==l[i]:
            sayac+=1
    print(l[j],"=",sayac)
