#Pedir los catetos de un triángulo rectángulo e imprimir su hipotenusa (catetoA2 + catetoB2 = hipotenusa2). Usar float(). Para calcular la raíz cuadrada recordar que hay que importar math (import math) y llamar a math.sqrt(valor).También podemos hacerlo aún más rápido usando valor**0.5

CatetoK=float (input("dame K:"))
CatetoL=float (input("dame L"))
Hipotenuza=(CatetoK**2+CatetoL**2)**0.5
print("La hipotenuza es:",Hipotenuza)
