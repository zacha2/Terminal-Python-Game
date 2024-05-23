import random

def PlayerTurn(Player, Enemy):
    hasHeal = True
    turnChoice = input("Will you attack (attack) or use your 1 healing potion? (heal): ")
    if turnChoice == "attack":
        hit = random.randint(0, 100)
        if hit <= Player.hitrate:
            Enemy.hp -= Player.damage
            print(f"You hit {Enemy} for {Player.damage}")
        else:
            print("You Missed!")
    elif turnChoice == "heal":
        if hasHeal == True:
            heal = random.randint(5, 10)
            Player.hp += heal
            print(f"you were healed for f{heal} hp")
            hasHeal = False
        else:
            print("you don't have a heal")


def EnemyTurn(Player, Enemy):
    EnemyHit = random.randint(0, 100)
    if EnemyHit <= Enemy.hitrate:
        Player.hp -= Enemy.damage
        print(f"{Enemy.name} hit you for {Enemy.damage} damage")
        



def Encounter(Enemy, Player):
    print(f"You have encountered a/an {Enemy.name}, it has {Enemy.hp} hp")
    
    if Player.speed > Enemy.speed:
        print("Your turn")
        while Player.hp> 0 and Enemy.hp > 0:
            PlayerTurn(Player, Enemy)
            print("It is now the enemies turn to attack")

    else:
        while Player.hp > 0 and Enemy.hp > 0:
            print(f"{Enemy.name} attacks")
            EnemyTurn()
