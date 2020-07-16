num = int(input("Informe um numero inteiro: "))
print("Digite [1] para BINÁRIO\nDigite [2] para OCTAL\nDigite [3] para HEXADECIMAL")
nbin = bin(num)
noct = oct(num)
nhex = hex(num)
esc = int(input("Tecle a opção: "))
if esc == 1:
    print("{} convertido para BINÁRIO é: {}".format(num, nbin[2:]))
elif esc == 2:
    print("{} convertido para OCTAL é: {}".format(num, noct[2:]))
else:
    print("{} convertido para HEXADECIMAL é: {}".format(num, nhex[2:]))

