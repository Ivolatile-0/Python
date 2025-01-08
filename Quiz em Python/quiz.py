#Projeto para iniciantes - Quiz em Python

#Imprime mensagem ao usuário
print("Olá! Seja bem-vindo ao Quiz de Avatar: A Lenda de Aang!")

#Guarda e imprime nome do jogador
userName = input("Primeiro, digite seu nome: \n")
print(f"Seu nome é {userName}")


#Pergunta ao usuário e recebe resposta
print("Pronto para começar?")
answerUser = input("Digite sim ou não (S / N): \n") 

#Verificar resposta do usuário
if answerUser == "N" or answerUser == "n":
    quit()

#Variável para contar os pontos
score = 0

#Criar pergunta com alternativas
print("1. Em Avatar, quais os elementos de dobra existentes? \n")
print("(A) Água, Terra, Fogo e Ar")
print("(B) Terra, Fogo, Metal e Água")
print("(C) Fogo, Lava, Metal e Ar")
print("(D) Água, Terra, Fogo, Ar, Metal e Lava")

#Receber resposta do usuário
answer1 = input("Resposta: ")

#Conferir a resposta
if answer1 == "A" or answer1 == "a":
    print("Você acertou! \n Parabéns!!!")
    score += 10
else:
    print("Resposta errada! \n Quem sabe da próxima vez?")

# Adicionar mais perguntas
print("2. O que é um Avatar? \n")
print("(A) Um mestre dos 4 elementos")
print("(B) Uma ponte entre o mundo dos humanos e o mundo dos espíritos")
print("(C) Um ")
print("(D) Todas as opções anteriores")

#Receber resposta do usuário
answer1 = input("Resposta: ")

#Conferir a resposta
if answer1 == "A" or answer1 == "a":
    print("Você acertou! \n Parabéns!!!")
    score += 10
else:
    print("Resposta errada! \n Quem sabe da próxima vez?")

print("Término do Quiz!")
print(f"Pontuação final: \n O jogador {userName} fez {score} pontos")
