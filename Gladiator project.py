import random
import os
import time
#Main factors of the game
def restart():
    print("Do you want to start a new game? (y/n): ")
    choice2 = input()
    if choice2.lower() == 'y':
        clear_terminal()
        game_setup()
    else:
        print("Thanks for playing the gladiator game!")
        time.sleep(1)
        exit()

def clear_terminal():
    if os.name=='nt':
        os.system('cls')

def Random_Dice():
    number = random.randint(1,10)
    return number

#The menu and the starting
def menu_setup():
    print("Welcome to the gladiator game")
    print("1. Start New Game")
    print("2. Exit Game")
    choice = str(input("Choose your number option: "))
    while choice != "1" or choice !="2":
        choice = str(input("Choose your number option: "))
        if choice == "1" or choice == "2":
            break
    if choice == "1":
            print("Hey there wake up it almost time.")
            time.sleep(1)
            print("Do you remember your name?")
            playerName = input("Enter your name: ")
            print("Atleast you remember your name.")
            time.sleep(1)
            print(playerName, ",we lost the war and got captured and turned into slaves.".capitalize())
            time.sleep(1)
            print("And now we are nothing more then there entertainment as gladiator.")
            time.sleep(1)
            print("If we want to live we have to win every battle.")
            time.sleep(1)
            print("In the start of every round you can choose your attack.")
            time.sleep(1)
            print("Punch, Kick or Slam. Those are the attacks you can use.")
            time.sleep(1)
            print("Punch is easier to hit but it dosen't hit as much hard.")
            time.sleep(1)
            print("Kick is somewhat hard to hit but it does good damage.")
            time.sleep(1)
            print("Slam is hard to hit but it does massive damage.")
            input("Press enter to continue")
            clear_terminal()
            game_setup()
    elif choice == "2":
        print("Goodbye!")
        exit()

#The main game loop
def game_setup():
    enemy_gladiators = ["hades","hercules","zeus","hephaestus","poseidon"]
    Hp=int(120)
    Fp=int(120)
    diffcult= str(input("Select your diffculty. 1,Easy 2, Medium 3,Hard: "))
    if diffcult == "1" or diffcult == "Easy":
        Fp -=35
    elif diffcult == "2" or diffcult == "Medium":
        Fp -=0
    elif diffcult == "3" or diffcult == "Hard":
        Fp +=35
    punchDamageOutput= [20,21,22,23,24,25]
    kickDamageOutput= [25,26,27,28,29,30]
    slamDamageOutput= [31,32,33,34,35,36,37,38,39,40]
    lista = ["slam","punch","kick"]
    Battle = input(f"{random.choice(enemy_gladiators)} has appeared! And wants to fight. Do you accept? (yes/no): ")
    if Battle == "no" or Battle == "n" or Battle == "":
        battle = False
        print("You have chosen not to fight.")


    elif Battle == "yes"or Battle == "y":
        battle = True
    while battle == True and Hp > 0 and Fp > 0:

        Playerattack = input("Punch, Slam or kick. Choose your attack: ")
        
        fiende = random.choice(lista)
        print("The enemy chose: ",fiende)
        print("You choose: ",Playerattack)
            
        if Playerattack == "punch":
            print("You rolled ",Random_Dice())
            if Random_Dice() >=3:
                Fp -= random.choice(punchDamageOutput)
                print("You hit him with a punch.")
            elif Random_Dice() <=3:
                print("You tried to punch him but he swiftly dodged your attack.")

        elif Playerattack == "kick":
            print("You rolled ",Random_Dice())
            if Random_Dice() >=5:
                Fp -=random.choice(kickDamageOutput)
                print("You kicked him in the stomach.")
            elif Random_Dice() <=5:
                print("You tried to kick him but he blocked your attack.")

        elif Playerattack == "slam":
            print("You rolled ",Random_Dice())
            if Random_Dice() >=7:
                Fp -=random.choice(slamDamageOutput)
                print("You grabbed him and slam him to the ground.")
            elif Random_Dice() >=7:
                print("You tried to grab him for slam but he countered you back.")

        if fiende == "punch":
            print("The enemy rolled ",Random_Dice())
            if Random_Dice() >=3:
                Hp -= random.choice(punchDamageOutput)
                print("the enemy punched you in the face.")
            elif Random_Dice() <=3:
                print("the enemy tried to punch you in the face but he missed.")

        elif fiende == "kick":
            rolled=print("The enemy rolled ",Random_Dice())
            if rolled >=5:
                Hp -= random.choice(kickDamageOutput)
                print("the enemy kicked you in the stomach.")
            elif rolled <=5:
                print("the enemy tried to kick you in the stomach but he missed.")

        elif fiende == "slam":
            rolled=print("The enemy rolled ",Random_Dice())
            if rolled >=7:
                Hp -=random.choice(slamDamageOutput)
                print("the enemy grabbed you and slam you to the ground.")
            elif rolled <=7:
                print("the enemy tried to grab you for slam but he missed.")
        print("Your health points: ",Hp)
        print("Enemy health points: ",Fp)
        input("press enter to continue")
        clear_terminal()
        if Fp <=0:
            print("You won the fight.Get ready for the next fight.")
            battle = False
            won = input("You won the fight.Are you ready for the next fight? (yes/no):")
            if won == "yes" or won == "y":
                battle = True
            elif won == "no" or won == "n":
                menu_setup()
        elif Hp <=0:
            print("You lost the fight. You are dead.")
            battle = False
            lost= input("Would you like to go back to the menu?:(yes|no)")
            if lost == "yes" or lost == "y":
                menu_setup()
            elif lost == "no" or lost == "n":
                restart()

menu_setup()