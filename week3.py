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
def değerata():
    x=int(input("x:"))    #x ve y koordinatlarımız
    y=int(input("y:")) 
    b=int(input("b:"))    #b atayacağımız değer 
    for i in range(len(a)):
        a[x][y]=b
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j],end=" ") 
        print()
değerata()

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

#MATRİSTE BOYAMA İŞLEMİ
a=[[6,4,9,2],[5,2,0,1],[4,1,0,3],[2,0,7,8]]
def matrisboya(): 
    b=int(input("b:"))    
    w=int(input("w:"))
    for i in range(len(a)):
        for j in range(len(a[i])):
            if  a[i][j]==b:        
               a[i][j]=w         
            else:
                pass

    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j],end=" ") 
        print()
matrisboya()



#RECURSIVE ÖZELLİKLİ FONKSİYONLAR

#decimal'den binary'ye dönüşüm
def fun(n):
     if n==0:
         return ;
     fun(int(n/2));
     print(n%2)
 fun(11)

#girilen değere göre yıldız bastırma
def fun(n):
     i=0;
     if n>1:
         fun(n-1);
     for i in range(n):
         print("*",end=" ")
     print("\n")
 fun(5)

#hanoi kulesi
 def h(n):
     if n==1:
         return 1
     if n>1:
         return 2*h(n-1)+1  
          
 print(h(4))




