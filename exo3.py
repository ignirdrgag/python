prenom=input("Donner votre prénom: ")
nom=input("Donner votre nom: ")
date_naissance=input("Donner votre date de naissance: ")
print("Bonjour", nom, prenom)
age=2025-int(date_naissance.split("-")[0])
if age < 18:
    print("Vous êtes mineur.")
    age=age*12
    print("votre age en mois est ",age)
else:
    print("Vous êtes majeur.")

    age=age*12
    print("votre age en mois est ",age)