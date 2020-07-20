n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1+n2)/2

if media >= 5 and media <= 6:
    print("Sua média é {}, portanto estará de recuperação".format(media))
elif media > 6:
    print("Sua média é {}, portanto estará aprovado".format(media))
else:
    print("Sua média é {}, portanto estará reprovado".format(media))