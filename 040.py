n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1+n2)/2

if media >= 5 and media <= 6:
    print("Aluno em recuperação")
elif media > 6:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")