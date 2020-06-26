n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))
men = n1
if n2 < n1 and n2 < n3:
    men = n2
if n3 < n1 and n3 < n2:
    men = n3
mai = n1
if n2 > n1 and n2 > n3:
    mai = n2
if n3 > n1 and n3 > n2:
    mai = n3
print("O menor valor é : {}".format(men))
print("O maior valor é: {}".format(mai))