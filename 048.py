imp = 0
for c in range(3,501,3):
    if c%2!=0:
        imp = imp+c
print("O resultado da soma entre os numeros impares de 1 a 500, multiplos de 3 é: {}".format(imp))
