import math
numero1 = int(input("insira um número: "))
numero2 = int(input("insira um número: "))
numero3 = int(input("insira um número: "))
numero4 = int(input("insira um número: "))
x1 = numero1
y1 = numero2
x2 = numero3
y2 = numero4
distanciaxy = math.sqrt(((x1 + x2)**2) +((y1 - y2)**2))
if distanciaxy >= 10:
    print("longe")
else:
    print("perto")