import datetime
import os

def ajouter_entree():
    entree = input("Entrez votre note : ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("journal.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {entree}\n")
    print("Note ajoutée avec succès !")

def lire_entrees():
    if not os.path.exists("journal.txt"):
        print("Aucune note trouvée.")
        return
    with open("journal.txt", "r", encoding="utf-8") as f:
        print("\n=== Journal ===\n")
        print(f.read())

def main():
    while True:
        print("\nJournal de Notes")
        print("1. Ajouter une note")
        print("2. Lire les notes")
        print("3. Quitter")
        choix = input("Choisissez une option (1-3) : ")
        
        if choix == "1":
            ajouter_entree()
        elif choix == "2":
            lire_entrees()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()