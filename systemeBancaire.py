class Compte:

    def __init__(self, numero: str, titulaire: str, solde: float = 0.0):
        if solde < 0:
            raise ValueError("Le solde initial ne peut pas être négatif.")
        self.numero = numero
        self.titulaire = titulaire
        self.solde = float(solde)

    def deposer(self, montant: float) -> float:
       
        if montant <= 0:
            raise ValueError("Le montant du dépôt doit être positif.")
        self.solde += montant
        return self.solde

    def retirer(self, montant: float) -> float:
        
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif.")
        if montant > self.solde:
            raise ValueError("Fonds insuffisants pour le retrait.")
        self.solde -= montant
        return self.solde

    def afficher_solde(self) -> str:
    
        return f"Compte {self.numero} - Titulaire: {self.titulaire} - Solde: {self.solde:.2f} €"

    def __str__(self) -> str:
        return self.afficher_solde()



if __name__ == "__main__":
    compte1 = Compte("001", "Alice", 500)
    print(compte1)                 
    compte1.deposer(250)
    print(compte1)                
    compte1.retirer(300)
    print(compte1)                 
