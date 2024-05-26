import random
from combat import encounter, randomEncounter
from time import sleep

#Class for the Player and enemies
class Thing:
    def __init__(self, name, hp, damage, hitrate, speed):
        self.hp = hp
        self.name = name
        self.damage = damage 
        self.hitrate = hitrate
        self.speed = speed

#Class for weapons
class Weapon:
    def __init__(self, name, damage, hitrate):
        self.name = name
        self.damage = damage
        self.hitrate = hitrate

#Weapons available to player
sword = Weapon("sword", 15, 65)
spear = Weapon("spear", 12, 80)
axe = Weapon("axe", 20, 50)

#Story explanation
print("You are trapped in an orc dungeon. You must clear the 5 rooms of the dungeon before you see the light of day.")
sleep(2)

#asks for player name
enterName = input("enter a name: ")

#The player as an object
Player = Thing(enterName, 50, 0, 0, 5)

#The available enemies
Orc = Thing("orc", 75, 12, 60, 8)
Goblin = Thing("goblin", 50, 16, 70, 16)
Troll = Thing("troll", 120, 15, 50, 4)

enemyList = [Orc, Goblin, Troll]



#Asks player to select a weapon with different damage, hitrate, etc.
weaponSelect = input("Select a weapon, Sword, Spear, or Axe: ")
if weaponSelect == "sword":
    Player.damage = sword.damage
    Player.hitrate = sword.hitrate
elif weaponSelect == "spear":
    Player.damage = spear.damage
    Player.hitrate = spear.hitrate
elif weaponSelect == "axe":
    Player.damage = axe.damage
    Player.hitrate = axe.hitrate
else:
    print("you didn't select a valid option. rerun the program")

#asks player of their nature, Player nature affects stats
build = input("select a nature, strength or agility?: ")

if build == "strength":
    Player.damage += 5
elif build == "agility":
    Player.speed += 5
    Player.hitrate += 15
else:
    print("you didn't select a valid option. rerun the program")

#Confirmation of player stats
print(f"You are about to begin your escape. Your name is {Player.name}, Your weapon is a/an {weaponSelect}, You deal {Player.damage} damage, your hitrate is {Player.hitrate}% and your speed is {Player.speed}")
sleep(3)

#The room cycle
for i in range(5):
    #Randomly selects enemy to fight
    randomEncounter(enemyList, Player)

    #Checks if player is still alive
    if Player.hp > 0:
        print(f"You are about to enter room {i + 1}")
        sleep(1)
    else:
        #If not, ends the game
        break
