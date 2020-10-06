import numpy as np
total = contP = 0
nPdt = ''
mPrc = []
print('-' * 30)
print('LOJA LOJA')
print('-' * 30)
while True:
    pdt = str(input('Nome do produto: '))
    prc = float(input('Preço: R$'))
    total += prc
    if prc >= 1000:
        contP += 1
    mPrc.append(prc)
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'O total da compra é de {total}\nTemos {contP} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {nPdt} que custa R${np.min(mPrc)}')