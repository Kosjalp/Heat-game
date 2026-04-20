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
    input("Tu te retrouves dans le desert.")
    input("Tu dois survivre dans cette chaleur.")
    input("Si ton eau ou ton énergie atteint zéro, tu perds.")
    input("Si ta température devient 42° ou plus, tu perds.")
    print("")
    input("Chaque jour, tu peut soit: \n" \
    "1) Rester à l'ombre, qui descends ta température et ton eau et monte ton énergie, \n" \
    "2) Chercher pour de l'eau, qui a une chance de monter ton eau et de decendre ta température, mais decends ton énergie et monte ta température, ou \n" \
    "3) Chercher quelque part plus froid, qui à une chance de réinitialiser ta température à 37°C, ou de decendre ton énergie par 25. \n")
    print("")
    input("Chaque quelque jours, la consommation de l'eau monte.")
    input("Tu dois survivre 25 jours.")
    input("Bon chance!")
    print("...")
    time.sleep(1)
    for i in range(100):
        print("")
    while True:
        print("")
        print(f"Jour {day}:")
        print("")
        print(f"Eau: {water} Énergie: {energy} Température: {temp}°")
        print("Qu'est-ce que tu fais?")
        choice = input("Mets 1 pour rester à l'ombre, 2 pour chercher pour de l'eau, ou 3 pour chercher quelque part plus froid, puis appuyez sur entrée. ")
        if choice == "1":
            input("Tu as choisi de rester à l'ombre.")
            temp -= random.randrange(1, 2)
            energy += random.randrange(8, 16)
            water -= (avg_temp / 20 / 2 + avg_temp/temp)*4+random.randrange(1, 2)
            day_end()
            if isDead == True:
                break
        elif choice == "2":
            input("Tu as choisi de chercher pour de l'eau.")
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
            input("Tu as choisi de chercher pour quelque part plus froid.")
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