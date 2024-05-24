import random
from time import sleep

def PlayerTurn(Player, Enemy):
    hasHeal = True
    healCount = 1
    turnChoice = input(f"Will you attack (attack) or use your {1} healing potion? (heal): ")
    if turnChoice == "attack":
        hit = random.randint(0, 100)
        if hit <= Player.hitrate:
            sleep(2)
            Enemy.hp -= Player.damage
            print(f"You hit {Enemy} for {Player.damage}")
        else:
            print("You Missed!")
    elif turnChoice == "heal":
        if hasHeal == True:
            heal = random.randint(5, 10)
            Player.hp += heal
            print(f"you were healed for {heal} hp")
            hasHeal = False
            healCount = 0
        else:
            print("you don't have a heal")


def EnemyTurn(Player, Enemy):
    EnemyHit = random.randint(0, 100)
    if EnemyHit <= Enemy.hitrate:
        Player.hp -= Enemy.damage
        print(f"{Enemy.name} hit you for {Enemy.damage} damage")
    else:
        print("The enemy missed!")
        



def Encounter(Enemy, Player):
    print(f"You have encountered a/an {Enemy.name}, it has {Enemy.hp} hp")
    
    if Player.speed > Enemy.speed:
        print("Your turn")
        while Player.hp> 0 and Enemy.hp > 0:
            PlayerTurn(Player, Enemy)
            sleep(2)
            print("It is now the enemies turn to attack")
            EnemyTurn(Player, Enemy)
            sleep(2)
            print(f"You have {Player.hp} hp and the enemy has {Enemy.hp} hp")

    else:
        while Player.hp > 0 and Enemy.hp > 0:
            print(f"{Enemy.name} attacks")
            sleep(2)
            EnemyTurn(Player, Enemy)
            print(f"You have {Player.hp} hp and the enemy has {Enemy.hp} hp")
            PlayerTurn(Player, Enemy)
