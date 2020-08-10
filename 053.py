frase = str(input("Digite algo: ")).lower().strip().split()
frase3 = "".join(frase)
palin = frase3[::-1]
print(frase3,palin)
if frase3 == palin:
    print("Essa frase é um palindromo")
else:
    print("Não é um palindromo")

'''
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase,split
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto)-1, -1, -1)
    inverso +=junto[letra]
if inverso == junto:
    print("Temos um palindromo")
else:
    print("A frase digitada não é um palindromo")
    
    SOLUÇÃO DO CURSO EM VÍDEO
'''