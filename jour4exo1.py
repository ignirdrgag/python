courses = []

def afficher_liste():
    if courses:
        print("\nListe de courses :")
        for i, item in enumerate(courses, 1):
            print(f"{i}. {item}")
    else:
        print("\nLa liste est vide.")

while True:
    print("\n=== MENU ===")
    print("1 - Ajouter un article")
    print("2 - Supprimer un article")
    print("3 - Trier la liste")
    print("4 - Afficher la liste")
    print("5 - Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        article = input("Entrez l'article à ajouter : ")
        courses.append(article)
        print(f"{article} ajouté à la liste.")
    
    elif choix == "2":
        afficher_liste()
        try:
            index = int(input("Entrez le numéro de l'article à supprimer : "))
            if 1 <= index <= len(courses):
                removed = courses.pop(index - 1)
                print(f"{removed} a été supprimé.")
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    elif choix == "3":
        courses.sort()
        print("La liste a été triée.")
    
    elif choix == "4":
        afficher_liste()
    
    elif choix == "5":
        print("Programme terminé.")
        break
    
    else:
        print("Option invalide, essayez encore.")