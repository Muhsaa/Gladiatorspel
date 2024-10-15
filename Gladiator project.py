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

Hp=int(120)
Fp=int(120)
dice= [1,2,3,4,5,6,7,8,9,10]
punchDamageOutput= [20,21,22,23,24,25]
kickDamageOutput= [25,26,27,28,29,30]
slamDamageOutput= [31,32,33,34,35,36,37,38,39,40]
def punch():
    punch= random.choice(dice)
    return punch

def kick():
    kick= random.choice(dice)
    return kick

def slam():
    slam = random.choice(dice)
    return slam
Playerattack= str(input("Punch, Slam or kick. Choose your attack: ")).lower
lista = [slam,punch,kick]
fiende = random.choice(lista)
print("You choose: ",Playerattack)
print(f"The enemy has chosen: {fiende}")
if Playerattack == punch():
    if Playerattack >=3:
        Fp -= random.choice(punchDamageOutput)
elif fiende == punch():
    if fiende >=3:
        Hp -= random.choice(punchDamageOutput)
elif Playerattack == kick():
    if Playerattack >=5:
        Fp -=random.choice(kickDamageOutput)
elif fiende == kick():
    if fiende >=7:
        Hp -= random.choice(kickDamageOutput)
elif Playerattack == slam():
    if Playerattack >=7:
        Fp -=random.choice(slamDamageOutput)
elif fiende == slam():
    if fiende >=7:
        Hp -=random.choice(slamDamageOutput)
clear_terminal()
print(Hp)
print(Fp)
while Hp > 0 or Fp > 0:
    Playerattack = str(input("Punch, Slam or kick. Choose your attack: ")).lower
    
    fiende = random.choice(lista)
    print(f"Fiende har valt: {fiende}")
    print("You choose: ",Playerattack)
    if Playerattack == punch():
        if Playerattack >=3:
            Fp -= random.choice(punchDamageOutput)
    elif fiende == punch():
        if fiende >=3:
            Hp -= random.choice(punchDamageOutput)
    elif Playerattack == kick():
        if Playerattack >=5:
            Fp -=random.choice(kickDamageOutput)
    elif fiende == kick():
        if fiende >=7:
            Hp -= random.choice(kickDamageOutput)
    elif Playerattack == slam():
        if Playerattack >=7:
            Fp -=random.choice(slamDamageOutput)
    elif fiende == slam():
        if fiende >=7:
            Hp -=random.choice(slamDamageOutput)
    clear_terminal()
    print(Hp)
    print(Fp)
    if Fp <=0 or Hp<=0:
        break