#n'e kadar 10'ar '10'ar hizalı yazdırma
n=int(input("n:"))
değer=0
for i in range(1,n+1):
    for j in range (1,n+1):
        değer=i*j
        print("{0:4}".format(değer),end="  ")
    print()


#verilen listeyi küçükten büyüğe doğru sıralama
l=[2,45,3,7,56,12,9,0]
for j in range(0,len(l)-1):
    for i in range(0,len(l)-1):
        if l[i]> l[i+1]:
            tmp=l[i+1]
            l[i+1]=l[i]
            l[i]=tmp
    print(l)
    
#verilen kelimeyi tırnak içine aldırma
s=input("cümle:")
 a=input("kelime:")
 c=""
 for x in range (len(s)):
     if s[x:x+len(a)]==a:
         c+= s[0:x]
         c+="'"+a+"'"
         c+=s[x+len(a):len(s)]
 print(c)
