inventaire = {
    "1984": ("Orwell", 1949, 3),
    "Dune": ("Herbert", 1965, 10),
    "Harry Potter": ("Rowling", 1997, 4)
}

def livres_faible_stock(d):
    return [titre for titre, (_, _, quantite) in d.items() if quantite < 5]


print("Inventaire :", inventaire)
print("Livres en faible stock :", livres_faible_stock(inventaire))
