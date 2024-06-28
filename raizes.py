import math
a =float(input("escreva o valor de a: "))
b =float(input("escreva o valor de b: "))
c =float(input("escreva o valor de c: "))

delta = b**2 - 4*a*c
if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    print("a equação possui uma raiz real: ", raiz1)
elif delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print("a equação possui raízes complexas (não reais) ", raiz1, raiz2)
else:
    print("sexo")
