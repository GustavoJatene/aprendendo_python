km = int(input("Insira a quantidade de Km rodado: "))
dias = int(input("Informe a quantidade de dias usado: "))
val_fin = (60 * dias) + (0.15 * km)
print("O valor total a ser pago é de: R${:.2f}".format(val_fin))