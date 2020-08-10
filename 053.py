frase = str(input("Digite algo: ")).lower().strip().split()
frase3 = "".join(frase)
palin = frase3[::-1]
print(palin)
if frase3 == palin:
    print("Essa frase é um palindromo")
else:
    print("Não é um palindromo")