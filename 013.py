prec = float(input("Informe o valor: R$"))
desc = (prec * 5) / 100
val = prec - desc
print("Valor que será descontado é de: R${:.2f}".format(desc))
print("O preço com desconto é de: R${:.2f}".format(val))
