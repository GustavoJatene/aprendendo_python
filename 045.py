#IMPORTANDO A BIBLIOTECA RANDOM E A BIBLIOTECA SLEEP
import random
from time import sleep
print("======JOKENPÔ======\n[1]PEDRA\n[2]PAPEL\n[3]TESOURA")
#CRIANDO O RANGEQ DA ESCOLHA
jogo = random.choice(["PEDRA","PAPEL","TESOURA"])
#HORA DO JOGADOR ESCOLHER SUA OPÇÃO
escolha = int(input("Digite a opção: "))
opcao = str
print("JO")
sleep(0.5) #DANDO UM PEQUENO TEMPO
print("KEN")
sleep(0.5) #DANDO UM PEQUENO TEMPO
print("PÔ")
sleep(0.5) #DANDO UM PEQUENO TEMPO
if escolha == 1:
    opcao = "PEDRA"
elif escolha == 2:
    opcao = "PAPEL"
else:
    opcao = "PEDRA"

print("#"*50,"\nO compudor escolheu: {}\nE você: {}".format(jogo,opcao))
sleep(1)
if (opcao == "PEDRA" and jogo == "PEDRA") or (opcao == "PAPEL" and jogo == "PAPEL") or (opcao == "TESOURA" and jogo == "TESOURA"):
    print("Resultado: Você EMPATOU")
elif (opcao == "PEDRA" and jogo == "PAPEL") or (opcao == "PAPEL" and jogo == "TESOURA") or (opcao == "TESOURA" and jogo == "PEDRA"):
    print("Resultado: Você PERDEU")
elif (opcao == "PEDRA" and jogo == "TESOURA") or (opcao == "PAPEL" and jogo == "PEDRA") or (opcao == "TESOURA" and jogo == "PAPEL"):
    print("Resultado: Você GANHOU")