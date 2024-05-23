import random
from test import Encounter

class Thing:
    def __init__(self, name, hp, damage, hitrate, speed):
        self.health = hp
        self.name = name
        self.damage = damage 
        self.hitrate = hitrate
        self.speed = speed


class Weapon:
    def __init__(self, name, damage, hitrate):
        self.name = name
        self.damage = damage
        self.hitrate = hitrate


sword = Weapon("sword", 15, 65)
spear = Weapon("spear", 12, 80)
axe = Weapon("axe", 20, 50)

enterName = input("enter a name: ")

Player = Thing(enterName, 50, 0, 0, 5)

#def Encounter(Enemy):
    #print(f"You have encountered a/an {Enemy}, it has {Enemy.health} health")
    #hasHeal = True
    #if Player.speed > Enemy.speed:
        #print("Your turn first")
        #while Player.health > 0 and Enemy.health > 0:
            #turnChoice = input("Will you attack or use your 1 healing potion?: ")
            #if turnChoice == "attack":
                #hit = random.randint(0, 100)
                #if hit <= Player.hitrate:
                    #Enemy.health -= Player.damage
                    #print(f"You hit {Enemy} for {Player.damage}")
                #else:
                    #print("You Missed!")
                
    #else:
        #print(f"{Enemy} attacks first")

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

build = input("strength or agility?: ")

if build == "strength":
    Player.damage += 5
elif build == "agility":
    Player.speed += 5
else:
    print("you didn't select a valid option. rerun the program")

print(f"You are about to venture forth. Your name is {Player.name}, Your weapon is a/an {weaponSelect}, You deal {Player.damage} damage, your hitrate is {Player.hitrate}% and your speed is {Player.speed}")


