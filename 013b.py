sal = float(input("Informe o salário: R$"))
sal_plu = (sal*15)/100
sal_fin = sal + sal_plu
print("O valor acrescentado será de: R${:.2f}".format(sal_plu))
print("O salário com aumento de 15% é de: R${:.2f}".format(sal_fin))