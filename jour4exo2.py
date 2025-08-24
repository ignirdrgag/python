annuaire = {}

def afficher_annuaire():
    if annuaire:
        print("\n--- Annuaire Téléphonique ---")
        for nom, numero in annuaire.items():
            print(f"{nom} : {numero}")
    else:
        print("\nL'annuaire est vide.")

while True:
    print("\n=== MENU ===")
    print("1 - Ajouter un contact")
    print("2 - Modifier un contact")
    print("3 - Supprimer un contact")
    print("4 - Rechercher un contact")
    print("5 - Afficher l'annuaire")
    print("6 - Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        nom = input("Nom du contact : ")
        numero = input("Numéro de téléphone : ")
        annuaire[nom] = numero
        print(f"{nom} ajouté avec succès.")
    
    elif choix == "2":
        nom = input("Nom du contact à modifier : ")
        if nom in annuaire:
            numero = input("Nouveau numéro de téléphone : ")
            annuaire[nom] = numero
            print(f"Numéro de {nom} mis à jour.")
        else:
            print("Contact introuvable.")
    
    elif choix == "3":
        nom = input("Nom du contact à supprimer : ")
        if nom in annuaire:
            del annuaire[nom]
            print(f"{nom} a été supprimé.")
        else:
            print("Contact introuvable.")
    
    elif choix == "4":
        nom = input("Nom du contact à rechercher : ")
        if nom in annuaire:
            print(f"{nom} : {annuaire[nom]}")
        else:
            print("Contact introuvable.")
    
    elif choix == "5":
        afficher_annuaire()
    
    elif choix == "6":
        print("Programme terminé.")
        break
    
    else:
        print("Option invalide, essayez encore.")
