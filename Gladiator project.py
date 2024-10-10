import random
import os
import time
def clear_terminal():
    if os.name=='nt':
        os.system('cls')

print("Hey there wake up it almost time.")
time.sleep(2)
print("Do you remember your name?")
playerName = input()
print("Atleast you remember your name.")
time.sleep(2)
print(playerName, ",we lost the war and got captured and turned into slaves.")
time.sleep(2)
print("And now we are nothing more then there entertainment as gladiator.")
time.sleep(2)
print("If we want to live we have to win every battle.")
time.sleep(2)
print("In the start of every round you can choose your attack.")
time.sleep(2)
print("Punch, Kick or Slam. Those aare the attacks you can use.")
time.sleep(2)
print("Punch is easier to hit but it dosen't hit as much hard.")
time.sleep(2)
print("Kick is somewhat hard to hit but it does good damage.")
time.sleep(2)
print("Slam is hard to hit but it does massive damage.")
time.sleep(5)
clear_terminal()

Hp=int(2)
Fp=int(2)
dice= [1,2,3,4,5,6,7,8,9,10]
punchDamageOutput= [20,21,22,23,24,25]
kickDamageOutput= [25,26,27,28,29,30]
slamDamageOutput= [31,32,33,34,35,36,37,38,39,40]
Playerattack= input("Punch, Slam or kick. Choose your attack: ").lower
def punch():
    punch= random.choice(dice)
    if punch >=3:
        Hp or Fp - punchDamageOutput
    return punch

def kick():
    kick= random.choice(dice)
    if kick >=5:
        Hp or Fp - kickDamageOutput
    return

def slam():
    slam = random.choice(dice)
    if slam >=7:
        Hp or Fp -slamDamageOutput
    return slam

while Hp >=0 or Fp >= 0:
    Playerattack = input("Välja din attack. Kast, slag eller spark: ")
    
    fiende = random.choice(lista)
    print(f"Fiende har valt: {fiende}")
    if Playerattack == fiende:
        print ("Ni valde samma attack och missade")
    elif (Playerattack == "Kast" and fiende == "Slag"):
        Fp -= 1
    elif(Playerattack == "Spark" and fiende =="Kast"):
        Fp -= 2
    elif(Playerattack == "Slag" and fiende == "Spark"):
        Fp -= 1
    elif (fiende == "Kast" and Playerattack== "Slag"):
        Hp -= 1
    elif(fiende == "Spark" and Playerattack =="Kast"):
        Hp -= 2
    elif(fiende == "Slag" and Playerattack == "Spark"):
        Hp -= 1
    print(Hp)
    print(Fp)
    if Fp <=0 or Hp<=0:
        break





name = input("Vad heter du?")
while name == "":
    print("Du har inte skrivit ditt namn")
    name = input("Vad heter du?")
    print (name)
