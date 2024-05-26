import random
from time import sleep

#Function for when the combat turn is the players
def PlayerTurn(Player, Enemy):
    #the Player has one heal per encounter
    hasHeal = True

    #Selects dialogue based on if the player has a heal
    turnDialogue = ""
    if hasHeal == True:
        turnDialogue = "Will you attack or use your one healing potion?: "
    else:
        turnDialogue = "You must attack. You have consumed your potion"
    turnChoice = input(turnDialogue)
    if turnChoice == "attack":
        #If the player chooses to attack, the player's hitrate is calculated and the player is told if they hit or miss
        print(f"you attack {Enemy.name}")
        hit = random.randint(0, 100)
        if hit <= Player.hitrate:
            sleep(2)
            Enemy.hp -= Player.damage
            print(f"You hit {Enemy.name} for {Player.damage}")
        else:
            sleep(2)
            print("You Missed!")
    elif turnChoice == "heal":
        #If the player chooses to heal, an amount of health to restore is randomly selected
        if hasHeal == True:
            sleep(2)
            heal = random.randint(8, 20)
            Player.hp += heal
            print(f"you were healed for {heal} hp")
            hasHeal = False
        else:
            print("you don't have a heal")

#Simplistic function for enemy turn. Calculates hitrate and prints the output
def EnemyTurn(Player, Enemy):
    print(f"{Enemy.name} attacks")
    EnemyHit = random.randint(0, 100)
    if EnemyHit <= Enemy.hitrate:
        sleep(2)
        Player.hp -= Enemy.damage
        print(f"{Enemy.name} hit you for {Enemy.damage} damage")
    else:
        sleep(2)
        print("The enemy missed!")
        


#Function for combat
def encounter(Enemy, Player):
    print(f"You have encountered a/an {Enemy.name}, it has {Enemy.hp} hp")
    
    #If the players speed is higher, the attack first and vice versa
    if Player.speed > Enemy.speed:
        #Combat scenario if you attack first, Simple back and forth between the player and enemy
        print(f"You Pull out your {Player.weapon} faster")
        while Player.hp> 0 and Enemy.hp > 0:
            PlayerTurn(Player, Enemy)
            sleep(2)
            print("It is now the enemies turn to attack")
            EnemyTurn(Player, Enemy)
            sleep(2)
            print(f"You have {Player.hp} hp and the enemy has {Enemy.hp} hp")
        if Player.hp > 0:
            print("You defeated the enemy your health and potions will be restored")
            sleep(2)
        else:
            #Condition for if you have lost all of your health
            print(f"You have failed to escape")

    else:
        #Combat scenario if enemy is faster
        print(f"The {Enemy.name} pulls out his weapon first")
        while Player.hp > 0 and Enemy.hp > 0:
            sleep(2)
            EnemyTurn(Player, Enemy)
            sleep(2)
            print(f"You have {Player.hp} hp and the enemy has {Enemy.hp} hp")
            sleep(2)
            PlayerTurn(Player, Enemy)
        if Player.hp > 0:
            print("You defeated the enemy your health and potions will be restored")
            sleep(2)
        else:
            print(f"You have failed to escape")

#Selects a random enemy from an enemy list argument for the player to fight.
def randomEncounter(enemyList, Player):
    encounterEnemy = random.choice(enemyList)
    encounter(encounterEnemy, Player)