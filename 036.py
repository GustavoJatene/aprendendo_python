imv = float(input("Informe o valor do imóvel: "))
sal = float(input("Informe o salário do comprador: "))
ano = int(input("Informe a quantidade de anos do financiamento: "))
mano = ano * 12
pimv = imv/mano
tsal = (sal*30)/100

if pimv < tsal:
    print("Para pagar uma casa de R${:.2f} em {} anos as prestações ficarão no valor de {:.2f}/MÊS, seu empréstimo foi Aprovado!".format(imv, ano, pimv))
else:
    print("Para pagar uma casa de R${:.2f} em {} anos as prestações ficarão no valor de {:.2f}/MÊS, seu empréstimo foi Negado!".format(imv, ano, pimv))