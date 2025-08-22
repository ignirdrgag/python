boisson1="eau"
boisson2="soda"
boisson3="jus"
prix1=400
prix2=800
prix3=1300
print("choisissez une boisson :")
if boisson1:
    print("1. Eau -", prix1, "fcfa")
if boisson2:
    print("2. Soda -", prix2, "fcfa")
if boisson3:    
    print("3. Jus -", prix3, "fcfa")
choix=int(input("Entrez le numéro de votre choix : "))
if choix == 1:
    print("Vous avez choisi de l'eau", prix1, "fcfa")
elif choix == 2:
    print("Vous avez choisi du soda", prix2, "fcfa")  
elif choix == 3:
    print("Vous avez choisi du jus", prix3, "fcfa")
else:
    print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
if choix in [1, 2, 3]:
    montant=int(input("Entrer le montant: "))
    while montant < prix1 and montant < prix2 and montant < prix3:
        print("montant insuffisant, veuillez entrer un montant valide.")
        montant=int(input("montant: "))

        if montant >= prix1 or montant >= prix2 or montant >= prix3:
            monaie=montant - (prix1 or prix2 or prix3)
            print("merci pour votre achat")
            if monaie > 0:
                print("voici votre monaie de ", monaie, "fcfa")
            else: 
                print("pas de monaie")
