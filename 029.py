vel = int(input("Informe a velocidade do carro: "))
if vel <= 80:
    print("Dentro do limite permitido")
else:
    mul = (vel-80)*7
    print("Deverá pagar multa no valor de: {}R$".format(mul))