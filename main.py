import random
from test import Encounter

class Thing:
    def __init__(self, name, hp, damage, hitrate, speed):
        self.hp = hp
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


Orc = Thing("orc", 75, 12, 60, 8)

enemyList = [Orc]

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
    Player.hitrate += 15
else:
    print("you didn't select a valid option. rerun the program")

print(f"You are about to venture forth. Your name is {Player.name}, Your weapon is a/an {weaponSelect}, You deal {Player.damage} damage, your hitrate is {Player.hitrate}% and your speed is {Player.speed}")

Encounter(Orc, Player)
