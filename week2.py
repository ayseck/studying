#sayılar ile algoritma çalışması
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
    
    
#BİNARY'DEN DECİMAL'E DÖNÜŞÜM
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
    
    
#CLASS ÇALIŞMASI
import time
class animals():
    def __init__(self,animal,name,type,colour,reproduction):
        self.animal=animal
        self.name=name 
        self.type=type
        self.colour=colour
        self.reproduction=reproduction

    def __str__(self):
         return f"""
        Animals Specials:
        animal:{self.animal}
        name:{self.name}
        type:{self.type}
        colour:{self.colour}
        reproduction:{self.reproduction}
        """

class dog(animals):
    def __init__(self,animal,name,type,colour,reproduction,play,hunt):
        super().__init__(animal,name,type,colour,reproduction)
        self.play=play 
        self.hunt=hunt
    def informationdog(self):
    
        print(f"""
        play:{self.play}
        can it hunt?:{self.hunt}
           """)


class bird(animals):
    def __init__(self,animal,name,type,colour,reproduction,visitor,fly):
        super().__init__(animal,name,type,colour,reproduction)
        self.visitor=visitor 
        self.fly=fly
    def informationbird(self):
        
        print(f"""
        is it visitor?:{self.visitor}
        can it fly?:{self.fly}
           
           """)

class horse(animals):
    def __init__(self,animal,name,type,colour,reproduction,forwhat,wild,bloodstock):
        super().__init__(animal,name,type,colour,reproduction)
        self.forwhat=forwhat 
        self.wild=wild
        self.bloodstock=bloodstock
    def informationhorse(self):
        
        print(f"""
        intended use:{self.forwhat}
        wild:{self.wild}
        is it bloodstock?:{self.bloodstock}

           """)

animal1=dog("dog","rocky","husky","black and grey","sexual reproduction",["ball","swim","bury"],"yes")
animal2=bird("bird","boncuk","mockingbird","grey","sexual reproduction","yes","yes")
animal3=horse("horse","karayel","arabian ","brown","sexual reproduction","palfrey","unwild","yes")


while True:
      
    print("""choose step for information:
    1:Dog Information
    2:Bird Information
    3:Horse Information  
    press  "q" for exit
    """)
    step=(input("step:"))

    if step =="1":
        print("loading...")
        time.sleep(1)
        print(animal1)
        dog.informationdog(animal1)

    elif step =="2":
        print("loading...")
        time.sleep(1)
        print(animal2)
        bird.informationbird(animal2)
    elif step =="3":
        print("loading...")
        time.sleep(1)
        print(animal3)
        horse.informationhorse(animal3)
    elif step == "q":
        print("program is closing....")
        time.sleep(2)
        print("close")
        break
