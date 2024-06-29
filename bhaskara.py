import math

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Esta equação não possui raízes reais.")
elif delta == 0:
    X = -b / (2*a)
    print(f"A raiz dupla desta equação é {X}")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    X, Y = (sorted([x1, x2]))  # Ordena as raízes em ordem crescente
    print(f"As raízes da equação são {X} e {Y}")
