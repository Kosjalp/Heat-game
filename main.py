#Imports
import time
import random
water = 50
energy = 50
temp = 37
day = 1
avg_temp = 35
isDead = False
def day_end(): #Day end script
        global water
        global day
        global temp
        global energy
        global isDead
        water = round(water)
        if temp <= 37: #Check for minimum temperature
            temp = 37
        day += 1
        print("")
        #Check for deaths
        if water <= 0:
            isDead = True
            print("Tu as perdu.")
            print("Tu n'avait pas assez d'eau.")
            print("")
            print("Le jeu reccomencera dans 5 secondes.")
            time.sleep(5)
        elif energy <= 0:
            isDead = True
            print("Tu as perdu.")
            print("Tu n'avait pas assez d'énergie.")
            print("")
            print("Le jeu reccomencera dans 5 secondes.")
            time.sleep(5)
        elif temp >= 42:
            isDead = True
            print("Tu as perdu.")
            print("Il y avait trop de chaleur.")
            print("")
            print("Le jeu reccomencera dans 5 secondes.")
            time.sleep(5)
#Game loop
while True:
    #Variables
    water = 50
    energy = 75
    temp = 37
    day = 1
    avg_temp = 35
    isDead = False
    #Intro
    for i in range(100):
        print("")
    print("")
    print("Appuyez sur entrée↵ pour continuer")
    input("Vous vous retrouvez dans le desert.")
    input("Vous devez survivre dans cette chaleur.")
    input("Si votre eau ou votre énergie atteint zéro, vous perdez.")
    input("Si votre température atteint 42° ou plus, vous perdez.")
    print("")
    input("Chaque jour, vous pouvez soit: \n" \
    "1) Rester à l'ombre, qui descend ta température et ton eau et monte ton énergie, \n" \
    "2) Chercher de l'eau, qui a une chance de monter votre eau et de decendre votre température, mais decends votre énergie et monte votre température, ou \n" \
    "3) Chercher un endroit plus froid, qui à une chance de réinitialiser votre température à 37°C, ou de decendre votre énergie par 25. \n")
    print("")
    input("Tous les quelque jours, la consommation de l'eau monte.")
    input("Vous devez survivre 25 jours.")
    input("Bonne chance!")
    print("...")
    time.sleep(1)
    for i in range(100):
        print("")
    while True:
        print("")
        print(f"Jour {day}:")
        print("")
        print(f"Eau: {water} Énergie: {energy} Température: {temp}°")
        print("Qu'est-ce que vous faites?")
        choice = input("Mettez 1 pour rester à l'ombre, 2 pour chercher de l'eau, ou 3 pour chercher quelque part plus froid, puis appuyez sur entrée. ")
        if choice == "1":
            input("Vous avez choisi de rester à l'ombre.")
            temp -= random.randrange(1, 2)
            energy += random.randrange(8, 16)
            water -= (avg_temp / 20 / 2 + avg_temp/temp)*4+random.randrange(1, 2)
            day_end()
            if isDead == True:
                break
        elif choice == "2":
            input("Vous avez choisi de chercher pour de l'eau.")
            temp += random.randrange(1, 2)
            energy -= random.randrange(9, 11)
            if random.randrange(1, 5) == 1:
                water += random.randrange(7, 11)
                temp -= 2
            else:
                water -= (avg_temp / 20 / 2 + avg_temp/temp)*4
            day_end()
            if isDead == True:
                break
        elif choice == "3":
            input("Vous avez choisi de chercher pour quelque part plus froid.")
            water -= (avg_temp / 20 / 2 + avg_temp/temp)*5
            energy -= 14
            if random.randrange(1, 4) == 1:
                temp = 37
            else:
                temp += random.randrange(2, 4)
            day_end()
            if isDead == True:
                break
        elif choice == "test.win":
            day = 25
        else:
            print("")
            print("Je n'ai pas compris. Réssayez. ")
            print("")
        if day == 25:
            for i in range(3):
                print("")
            input("Bravo!")
            input("Vous avez gagné!")
            input("Vous avez survécu 25 jours dans le désert.")
            print("")
            print("Le jeu recommencera en 10 secondes.")
            time.sleep(10)
            for i in range(100):
                print("")
            break
