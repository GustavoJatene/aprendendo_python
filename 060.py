n1 = int(input("Digite um valor: "))
val = n1
fat = 1
while n1 != 1:
    fat = n1 * fat
    n1 = n1 - 1
print("{}! = {}".format(val, fat))
