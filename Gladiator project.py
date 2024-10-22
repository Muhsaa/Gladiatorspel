import random
import os
import time

def clear_terminal():
    if os.name=='nt':
        os.system('cls')

number = random.randint(1,10)
number2 = random.randint(1,10)

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
lista = ["slam","punch","kick"]
round = 1
battle = True
while battle:
    Playerattack = input("Punch, Slam or kick. Choose your attack: ")
    
    fiende = random.choice(lista)
    print(f"Fiende har valt: {fiende}")
    print("You choose: ",Playerattack)
    if Playerattack == "punch":
        print(number)
        if number >=3:
            Fp -= random.choice(punchDamageOutput)
            print("You hit him with a punch.")
        elif number <=3:
            print("You tried to punch him but he swiftly dodged your attack.")

    elif Playerattack == "kick":
        print(number)
        if number >=5:
            Fp -=random.choice(kickDamageOutput)
            print("You kicked him in the stomach.")
        elif number <=5:
            print("You tried to kick him but he blocked your attack.")

    elif Playerattack == "slam":
        print(number)
        if number >=7:
            Fp -=random.choice(slamDamageOutput)
            print("You grabbed him and slam him to the ground.")
        elif number >=7:
            print("You tried to grab him for slam but he countered you back.")

    if fiende == "punch":
        print(number2)
        if number2 >=3:
            Hp -= random.choice(punchDamageOutput)
            print("the enemy punched you in the face.")
        elif number2 <=3:
            print("the enemy tried to punch you in the face but he missed.")

    elif fiende == "kick":
        print(number2)
        if number2 >=5:
            Hp -= random.choice(kickDamageOutput)
            print("the enemy kicked you in the stomach.")
        elif number2 <=5:
            print("the enemy tried to kick you in the stomach bu1t he missed.")

    elif fiende == "slam":
        print(number2)
        if number2 >=7:
            Hp -=random.choice(slamDamageOutput)
            print("the enemy grabbed you and slam you to the ground.")
        elif number2 >=7:
            print("the enemy tried to grab you for slam but he missed.")
    time.sleep(2)
    clear_terminal()
    print(Hp)
    print(Fp)
    if Fp <=0:
        print("You won the fight.Get ready for the next fight.")
        battle = False
        break
    elif Hp <=0:
        print("You lost the fight. You are dead.")
        battle = False
        break