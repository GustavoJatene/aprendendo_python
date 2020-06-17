import math
num = int(input("Digite um numero: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {:.2f}".format(num,raiz))
print("A raiz de {}, arredondando para cima é igual a {}".format(num,math.ceil(raiz)))
print("A raiz de {}, arredondando para baixo é igual a {}".format(num,math.floor(raiz)))