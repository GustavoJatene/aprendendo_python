print('='*20,'\nSIMULADOR DE CAIXA')
print('='*20)
valor = int(input('Qual o valor quer sacar? R$'))
tval = valor
nota = 50
cont = 0
while True:
    if tval >= nota:
        tval -= nota
        cont +=1
    else:
        print(f'foram {cont} cédulas de {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        cont = 0
        if tval == 0:
            break

