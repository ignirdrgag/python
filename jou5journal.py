import datetime
import os

def add_entry(file_path, message):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {message}\n")
        return "Entrée ajoutée avec succès."
    except PermissionError:
        return f"Erreur : Permission refusée pour écrire dans '{file_path}'."
    except Exception as e:
        return f"Une erreur s'est produite lors de l'ajout : {str(e)}"

def read_entries(file_path):
    try:
        if not os.path.exists(file_path):
            return f"Erreur : Le fichier '{file_path}' n'existe pas."
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                return "Le journal est vide."
            return lines
    except PermissionError:
        return f"Erreur : Permission refusée pour lire '{file_path}'."
    except UnicodeDecodeError:
        return f"Erreur : Impossible de lire le fichier '{file_path}' (problème d'encodage)."
    except Exception as e:
        return f"Une erreur s'est produite lors de la lecture : {str(e)}"

def delete_entry(file_path, line_number):
    try:
        if not os.path.exists(file_path):
            return f"Erreur : Le fichier '{file_path}' n'existe pas."
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if line_number < 1 or line_number > len(lines):
            return f"Erreur : Numéro de ligne {line_number} invalide. Le journal contient {len(lines)} entrées."
        lines.pop(line_number - 1)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        return f"Entrée à la ligne {line_number} supprimée avec succès."
    except PermissionError:
        return f"Erreur : Permission refusée pour modifier '{file_path}'."
    except Exception as e:
        return f"Une erreur s'est produite lors de la suppression : {str(e)}"

def main():
    file_path = "journal.txt"
    while True:
        print("\n=== Journal de Bord ===")
        print("1. Ajouter une entrée")
        print("2. Afficher le journal")
        print("3. Supprimer une entrée")
        print("4. Quitter")
        choice = input("Choisissez une option (1-4) : ")

        if choice == '1':
            message = input("Entrez votre message : ")
            if message.strip():
                result = add_entry(file_path, message)
                print(result)
            else:
                print("Erreur : Le message ne peut pas être vide.")
        elif choice == '2':
            result = read_entries(file_path)
            print("\n=== Contenu du Journal ===")
            if isinstance(result, list):
                for i, line in enumerate(result, 1):
                    print(f"{i}. {line.strip()}")
            else:
                print(result)
            # print( Investigation complete."")
        elif choice == '3':
            result = read_entries(file_path)
            if isinstance(result, list):
                print("\n=== Contenu du Journal ===")
                for i, line in enumerate(result, 1):
                    print(f"{i}. {line.strip()}")
                try:
                    line_number = int(input("Entrez le numéro de ligne à supprimer : "))
                    result = delete_entry(file_path, line_number)
                    print(result)
                except ValueError:
                    print("Erreur : Veuillez entrer un numéro de ligne valide.")
            else:
                print(result)
        elif choice == '4':
            print("Programme terminé.")
            break
        else:
            print("Option invalide. Veuillez choisir 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()