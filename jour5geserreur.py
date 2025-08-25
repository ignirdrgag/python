def count_words(file_path):
    if not file_path.strip():
        return "Erreur : Aucun chemin de fichier fourni."
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        return f"Erreur : Le fichier '{file_path}' n'existe pas. Vérifiez le chemin et réessayez."
    except PermissionError:
        return f"Erreur : Permission refusée pour accéder au fichier '{file_path}'."
    except UnicodeDecodeError:
        return f"Erreur : Impossible de lire le fichier '{file_path}' (problème d'encodage)."
    except Exception as e:
        return f"Une erreur inattendue s'est produite : {str(e)}"

def main():
    while True:
        file_path = input("Entrez le chemin du fichier texte (ou 'q' pour quitter) : ")
        if file_path.lower() == 'q':
            print("Programme terminé.")
            break
        
        result = count_words(file_path)
        if isinstance(result, int):
            print(f"Le fichier contient {result} mots.")
            break
        else:
            print(result)
            print("Voulez-vous réessayer avec un autre fichier ?")

if __name__ == "__main__":
    main()