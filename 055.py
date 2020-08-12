import numpy as np
peso = 0
lpeso = []
for c in range (1,6):
    peso = float(input("Digite o {}° peso: ".format(c)))
    lpeso.append(peso)
print("O maior peso é: {}kg".format(np.max(lpeso)))
print("O menor peso é: {}kg".format(np.min(lpeso)))


'''maior = 0
menor = 0
for p in range(1,6):
    peso = float(input("Peso da {}° pessoa".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso
print("O maior peso lido foi de {}kg".format(maior))
print("O menor peso lido foi de {}kg".format(menor))
    SOLUÇÃO CURSO EM VÍDEO
'''

