ano = int(input("Informe um ano: "))
ban = ano % 4
if ban == 0:
    print("O ano digitado é BISSEXTO")
else:
    print("O ano digitado não é BISSEXTO")
