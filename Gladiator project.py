import random
print("Hey there wake up it almost time.")
playerName = input("Do you remember your name: ")
print("Atleast you remember your name.")
print(playerName, ",we lost the war and got captured and turned into slaves.")
print("And now we are nothing more then there entertainment as gladiator.")
print("If we want to live we have to win every battle.")
print("In the start of every round you can choose your attack.")
print("Punch, Kick or Slam. Those aare the attacks you can use.")
print("Punch is easier to hit but it dosen't hit as much hard.")
print("Kick is somewhat hard to hit but it does good damage.")
print("Slam is hard to hit but it does massive damage.")
lista=["Spark","Kast","Slag"]
Hp=int(2)
Fp=int(2)

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
