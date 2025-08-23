import math

def hypotenuse(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Les côtés doivent être positifs et non nuls.")
    return math.sqrt(a**2 + b**2)
print(hypotenuse(3, 4))    
print(hypotenuse(5, 12))   
print(hypotenuse(1, 1))   
