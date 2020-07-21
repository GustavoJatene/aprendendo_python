altu = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))
imc = peso/(altu*2)
print("Seu IMC é de: {:.2f}".format(imc))
if imc <= 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade grau 1")
elif imc <= 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")