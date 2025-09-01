class Bibliotheque:
    

    def __init__(self):
       
        self.livres = {}

    def ajouter_livre(self, titre: str, auteur: str, annee: int, quantite: int = 1):
        """Ajoute un livre ou augmente la quantité s'il existe déjà."""
        if titre in self.livres:
            a, an, q = self.livres[titre]
            self.livres[titre] = (auteur, annee, q + quantite)
        else:
            self.livres[titre] = (auteur, annee, quantite)

    def emprunter_livre(self, titre: str) -> bool:
        """
        Permet d'emprunter un livre si disponible.
        Retourne True si l'emprunt est réussi, False sinon.
        """
        if titre in self.livres:
            auteur, annee, quantite = self.livres[titre]
            if quantite > 0:
                self.livres[titre] = (auteur, annee, quantite - 1)
                return True
        return False

    def afficher_stock(self):
        """Affiche le stock actuel des livres."""
        print("\n--- Stock de la Bibliothèque ---")
        if not self.livres:
            print("Aucun livre en stock.")
        for titre, (auteur, annee, quantite) in self.livres.items():
            print(f"{titre} - {auteur} ({annee}) : {quantite} exemplaire(s)")


if __name__ == "__main__":
    biblio = Bibliotheque()
    
    biblio.ajouter_livre("1984", "George Orwell", 1949, 3)
    biblio.ajouter_livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, 2)
    biblio.ajouter_livre("L'Étranger", "Albert Camus", 1942, 4)

    
    biblio.afficher_stock()

   
    print("\nEmprunt de '1984' :", "Réussi" if biblio.emprunter_livre("1984") else "Échec")

    
    biblio.afficher_stock()
