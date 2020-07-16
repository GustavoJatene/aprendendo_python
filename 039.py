from datetime import date
nasci = int(input("Informe o ano de nascimento: "))
anoal = date.today().year
idade = anoal-nasci
print("Quem nasceu no ano {}, tem {} anos".format(nasci,idade))
if idade < 18:
    print("Ainda não pode alistar, seu ano de alistamento é: {}".format(nasci+18))
elif idade == 18:
    print("Está no ano de alistamento")
else:
    print("Seu ano de alistamento foi em: {}".format(nasci+18))
