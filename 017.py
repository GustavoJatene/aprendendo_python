#import math
cat_opo = float(input("informe o valor do cateto oposto: "))
cat_adj = float(input("Informe o valor do cateto adjacente: "))
hipo = pow(cat_opo,2) +pow(cat_adj,2)
#hipo = math.hypot(cat_adj,cat_opo) Com a importação da classe math, eu poderia usar dessa forma
print("A hipotenusa tem o valor de: {:.2f}".format(hipo **(1/2)))