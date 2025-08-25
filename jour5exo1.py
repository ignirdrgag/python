def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        return "Erreur : Le fichier spécifié n'existe pas."
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"

def main():
    file_path = input("Entrez le chemin du fichier texte : ")
    result = count_words(file_path)
    if isinstance(result, int):
        print(f"Le fichier contient {result} mots.")
    else:
        print(result)

if __name__ == "__main__":
    main()