n = int(input("Digite um numero: "))
cont = []
for c in range(1,n+1):
    if n%c==0:
        print(c, end=" ")
        '''cont.append(n%c==0)
print(cont)'''