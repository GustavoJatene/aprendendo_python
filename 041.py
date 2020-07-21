from datetime import date
ano = int(input("Informe o ano de nascimento: "))
ida = date.today().year - ano
print("O atleta tem {} anos".format(ida))
if ida <= 9:
    print("E concorrerá na categoria MIRIN")
elif ida <= 14:
    print("E concorrerá na categoria INFANTIL")
elif ida <= 19:
    print("E concorrerá na categoria JUNIOR")
elif ida <= 25:
    print("E concorrerá na categoria SÊNIOR")
else:
    print("E concorrerá na categoria MASTER")
