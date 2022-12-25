#MATRİS OLUŞTURMA ÇEŞİTLERİ
m=4
n=3
m1=[[0 for x in range(m)]for y in range(n)]
print(m1)



import random
for i in range(n):
    for j in range(m):
        m1[i][j]=random.randint(0,9)
        m2[i][j]=random.randint(0,9)
print(m1)
print()
print(m2)
print()


def matris(m,n):
    x=[[0 for x in range(m)]for y in range(n)]
    for i in range(n):
        for j in range(m):
            x[i][j]=random.randint(0,9)
    for i in range(len(x)):
        for j in range (len(x[i])):
            print(x[i][j],end=" ")
        print()
matris(4,4)


#MATRİS TOPLAMA İŞLEMİ
import random
def matristopla(m,n):
    t=[[0 for i in range(m)]for j in range(n)]
    x=[[0 for i in range(m)]for j in range(n)]
    y=[[0 for i in range(m)]for j in range(n)]
    for i in range(n):
        for j in range(m):
            x[i][j]=random.randint(0,9)
            y[i][j]=random.randint(0,9)
            t[i][j]=x[i][j]+y[i][j] 
    for i in range(len(x)):
        for j in range (len(x[i])):
            print(x[i][j],end=" ")
        print()
    print("---------------")
    for i in range(len(y)):
        for j in range (len(y[i])):
            print(y[i][j],end=" ") 
        print()
    print("---------------")
    for i in range(len(t)):
        for j in range (len(t[i])):
            print(t[i][j],end=" ")
        print()
    print("---------------")

        
matristopla(3,3)

#MATRİSTE SATIR VE SÜTUN TOPLAMI
a=[[1,3,0,3],[4,8,1,1],[4,1,5,9]]
satırtop=0
sutuntop=0
for i in range(len(a)):
    satırtop=0
    for j in range(len(a[i])):
        satırtop+=a[i][j]
        
    print(i+1,".satır toplamı:",satırtop)
print("---------------------------")

for k in range (len(a[i])):
    sutuntop=0
    for m in range(len(a)):
        sutuntop+=a[m][k]
      
    print(k+1,".sütun toplamı:",sutuntop)
print()

#MATRİSTE DİAGONAL TOPLAM
a=[[6,4,9,2],[5,2,0,1],[4,1,2,3],[2,4,7,8]]
diagonal=0
for i in range(len(a)):
    diagonal+=a[i][i]
print(diagonal)

#GİRİLEN DEĞERİ MATRİSİN İSTENİLEN İNDEKSİNE YERLEŞTİRME
a=[[6,4,9,2],[5,2,0,1],[4,1,2,3],[2,4,7,8]]
s=int(input("s:"))
m=int(input("m:"))
n=int(input("n:"))
for i in range(len(a)):
    a[m][n]=s

print(a)

#MATRİSİN TRANSPOZUNU ALMA
a=[[6,4,3,4],[5,2,0,9]]
n=0
for i in range(len(a[n])):
    n+=1
    for j in range(len(a)):
        print(a[j][i],end=" ")
    print()
    
#MATRİSTE EN BÜYÜK VE EN KÜÇÜK DEĞERİ TESPİT ETME
a=[[6,4,12,-1],[5,2,15,9]]
max=0
min=0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]>max:
            max=a[i][j]


        else:
            if min>a[i][j]:
                min=a[i][j]
print(max,min)



