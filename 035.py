r1 = float(input("Informe a primeira reta: "))
r2 = float(input("Informe a segunda reta: "))
r3 = float(input("Informe a terceira reta: "))

if r2 - r3 < r1 and r1 < r2 + r3 and r1 - r3 < r2 and r2 < r1 + r3 and r1 - r2 < r3 and r3 < r1 + r2:
    print("Com as retas, é possivel se ter um triangulo")
else:
    print("Impossível se ter um triangulo com o comprimento das retas especificadas.")

