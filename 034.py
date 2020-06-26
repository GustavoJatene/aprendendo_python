sal = float(input("Informe o salário: "))
if sal >= 1250:
    aum = sal + ((sal*10)/100)
    print("Seu salário terá acréscimo de 10% e será: R${}".format(aum))
else:
    aum = sal +((sal*15)/100)
    print("Seu salário terá acréscimo de 15% e será: {}".format(aum))