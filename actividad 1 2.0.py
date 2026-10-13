#Hacer un programa (01.circulo.py) que pida el radio e imprima el área del correspondiente círculo


import math


radio=float (input("Dame un radio:"))
print("el radio es :",radio)
print("pi es:",math.pi)
area=math.pi*radio
print("El área es:",area)  
print(f"El area es:{area}")