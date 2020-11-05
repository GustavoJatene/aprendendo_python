nums = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    escolha = int(input('Digite um numero entre 0 e 20: '))
    while escolha > 20:
        escolha = int(input('Digite novamente, tem que ser entre 0 e 20: '))
    if escolha <= 20:
       print(extenso[escolha])