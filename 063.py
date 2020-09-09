seq = int(input("Quantos termos você quer mostrar: "))
fib = 1
ant = 0
res = 0
while seq != 0:
    print("{}".format(res), end= ",")
    res = fib + ant
    ant = fib
    fib = res
    seq -= 1
print("FIM")

'''
RESPOSTA DO CURSO EM VÍDEO
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print("{}>{}".format(t1, t2), end= "")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(">{}".format(t3), end= "")
    t1 = t2
    t2 = t3
    cont += 1
print("FIM")
'''