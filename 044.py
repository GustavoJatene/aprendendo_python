val = float(input("Informe o valor a ser pago: "))
cond = int(input("Informe a condição de pagamento"
      "\n[1]À Vista\n[2]À Vista no cartão\n[3]Em 2x no Cartão\n[4]Em 3x ou mais no Cartão\nDigite a opção: "))
avi =  val-(val*10)/100
avic = val-(val*5)/100
car2 = val
car3 = val+(val*20)/100

if cond == 1:
    print("O valor do produto fica por: R${}".format(avi))
elif cond == 2:
    print("O valor do produto fica por: R${}".format(avic))
elif cond == 3:
    print("O valor do produto fica por: R${}".format(val))
else:
    parc = int(input("Informe a quantidade de parcelas: "))
    print("O valor sairá por: R${} em {} parcelas de R${}".format(car3,parc,car3/parc))