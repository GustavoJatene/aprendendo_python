dist = float(input("Informe a distancia em km, da sua viagem: "))
if dist <= 200:
    print("O preço a ser pago será de: R${:.2f}".format(dist*0.50))
else:
    print("O preço a ser pago será de: R${}".format(dist*0.45))