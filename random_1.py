import random

nombre_secret = random.randint(1, 100)

print("Devine le nombre auquel je pense (entre 1 et 100) !")

tentative = None  
while tentative != nombre_secret:
    tentative = int(input("Entre ton nombre : "))

    if tentative < nombre_secret:
        print("Trop petit ! Essaie encore.")
    elif tentative > nombre_secret:
        print("Trop grand ! Essaie encore.")
    else:
        print(f"Bravo ! Tu as trouvé le nombre secret : {nombre_secret}")
