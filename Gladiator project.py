import random
import os
import time
dice= [1,2,3,4,5,6,7,8,9,10]
def punch1():
    punch= random.choice(dice)
    return punch,punch1

def kick1():
    kick_roll= random.choice(dice)
    return kick1,kick_roll

def slam1():
    slam = random.choice(dice)
    return slam

def roll_dice():
    num=random.randint(1,10)
    return num

def clear_terminal():
    if os.name=='nt':
        os.system('cls')

number = roll_dice()
punch=punch1()
kick= kick1()
slam= slam1()

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
print("Punch, Kick or Slam. Those are the attacks you can use.")
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
punchDamageOutput= [20,21,22,23,24,25]
kickDamageOutput= [25,26,27,28,29,30]
slamDamageOutput= [31,32,33,34,35,36,37,38,39,40]
Playerattack= str(input("Punch, Slam or kick. Choose your attack: ").lower)
lista = ["slam","punch","kick"]
fiende = random.choice(lista)
print("You choose: ",Playerattack)
print(f"The enemy has chosen: {fiende}")
if Playerattack == punch:
    if punch >=3:
        Fp -= random.choice(punchDamageOutput)

elif Playerattack == kick:
    if kick >=5:
        Fp -=random.choice(kickDamageOutput)

elif Playerattack == slam:
    if slam >=7:
        Fp -=random.choice(slamDamageOutput)

if fiende == "punch":
    print(number)
    if number >=3:
        Hp -= random.choice(punchDamageOutput)

elif fiende == "kick":
    print(number)
    if number >=5:
        Hp -= random.choice(kickDamageOutput)

elif fiende == "slam":
    print(number)
    if number >=7:
        Hp -=random.choice(slamDamageOutput)
time.sleep(2)
clear_terminal()
print(Hp)
print(Fp)
while Hp > 0 or Fp > 0:
    Playerattack = str(input("Punch, Slam or kick. Choose your attack: ").lower)
    
    fiende = random.choice(lista)
    print(f"Fiende har valt: {fiende}")
    print("You choose: ",Playerattack)
    if Playerattack == punch:
        if punch >=3:
            Fp -= random.choice(punchDamageOutput)

    elif Playerattack == kick:
        if kick >=5:
            Fp -=random.choice(kickDamageOutput)

    elif Playerattack == slam:
        if slam >=7:
            Fp -=random.choice(slamDamageOutput)

    if fiende == "punch":
        print(number)
        if number >=3:
            Hp -= random.choice(punchDamageOutput)

    elif fiende == "kick":
        print(number)
        if number >=5:
            Hp -= random.choice(kickDamageOutput)

    elif fiende == "slam":
        print(number)
        if number >=7:
            Hp -=random.choice(slamDamageOutput)
    time.sleep(2)
    clear_terminal()
    print(Hp)
    print(Fp)
    if Fp <=0 or Hp<=0:
        break