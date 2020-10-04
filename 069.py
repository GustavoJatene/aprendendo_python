cont = 0
adt = jvm = 0
contm = 0
conth = 0
while True:
    print('-' * 30)
    print('CADASTRO DE USUÁRIO')
    print('-' * 30)
    age = int(input('INFORME A IDADE: '))
    gen = ' '
    while gen not in 'MF':
        gen = str(input('Sexo: [M/F] ')).strip().upper()
    print('-' * 30)
    if gen == 'M':
        contm +=1
    if age >= 18:
        adt += 1
    if age <= 20:
        if gen == 'F':
            jvm += 1
    val = ' '
    while val not in 'SN':
        val = str(input('QUER CONTINUAR? [S/N] ')).strip().upper()
    cont += 1
    if val == 'N':
        break
print(f'Total de pessoas com mais de 18 anos = {adt}\nQuantidade de homens cadastrados = {contm}\n'
      f'Quantidade de mulheres com menos de 20 anos = {jvm}')
