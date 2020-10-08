total = contP = 0
nPdt = ''
contPb = 0
mPrcb = 0
print('-' * 30)
print('LOJA LOJA')
print('-' * 30)
while True:
    pdt = str(input('Nome do produto: '))
    prc = float(input('Preço: R$'))
    total += prc
    if prc >= 1000:
        contP += 1
    if contPb == 0:
        mPrcb = prc
    if prc <= mPrcb and nPdt == '':
        mPrcb = prc
        nPdt = pdt
        contPb +=1
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'O total da compra é de {total}\nTemos {contP} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {nPdt} que custa R${mPrcb}')
