class Voiture:
    def __init__(self, marque: str, vitesse: float = 0.0):
        if vitesse < 0:
            raise ValueError("La vitesse ne peut pas être négative.")
        self.marque = marque
        self.vitesse = float(vitesse)

    def accelerer(self, delta: float) -> float:
        self.vitesse = max(0.0, self.vitesse + float(delta))
        return self.vitesse

    def __str__(self) -> str:
        return f"{self.marque} roulant à {self.vitesse:.1f} km/h"


class Moto(Voiture):
    def __init__(self, marque: str, vitesse: float = 0.0, type_moto: str = "Sport"):
        
        super().__init__(marque, vitesse)
        self.type_moto = type_moto

    def faire_wheelie(self) -> str:
        return f"La moto {self.marque} fait un wheelie !"

    def __str__(self) -> str:
        return f"Moto {self.type_moto} - {self.marque} roulant à {self.vitesse:.1f} km/h"



if __name__ == "__main__":
    m = Moto("Yamaha", 20, "Cross")
    print(m)                
    m.accelerer(30)         
    print(m)                
    print(m.faire_wheelie())  
