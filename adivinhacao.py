import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

pontos = 1000
numero_secreto = random.randrange(1,101)
total_de_tentativas = 0

print("qual o nivel da ificuldade?")
print("(1) facil | (2) medio | (3) difícil")

nivel = int (input ("defina o nivel:"))
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
  total_de_tentativas = 10 
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):  
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite seu numero: ")
    print("Você digitou ",chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
      print("voce deve digitar um número entre 1 e 100!")
      continue 
    

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if(acertou):
        print("voce acertou e fez {} pontos!, parabéns!!'" format(pontos))
        break
    else:   
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
        pontos_perdidos = abs  (numero_secreto - chute)   
        pontos = pontos - pontos_perdidos
print("Fim do jogo!")
