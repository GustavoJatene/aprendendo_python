gen = str(input("Informe seu sexo [M/F]: ")).upper().strip()
while "M" != gen != "F":
    gen = str(input("Valor invalido, por favor digite novamente: ")).upper().strip()
if gen == "M":
    print("Seu sexo é {}asculino".format(gen))
else:
    print("Seu sexo é {}eminino".format(gen))