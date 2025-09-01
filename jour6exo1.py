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



if __name__ == "__main__":
    v = Voiture("Toyota", 10)
    print(v)                   
    v.accelerer(25)              
    print(v)                      
    v.accelerer(-50)              
    print(v)                      
