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

print("Responda a cada pergunta de acordo com as alternativas")
#Primeira pergunta
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

#Segunda pergunta
print("2. O que é um Avatar? \n")
print("(A) Um mestre dos 4 elementos")
print("(B) Uma ponte entre o mundo dos humanos e o mundo dos espíritos")
print("(C) Um pacificador")
print("(D) Todas as opções anteriores")

#Recebe resposta do usuário
answer2 = input("Resposta: ")

#Conferir a resposta
if answer2 == "D" or answer2 == "d":
    print("Você acertou! \n Parabéns!!!")
    score += 10
else:
    print("Resposta errada! \n Quem sabe da próxima vez?")

#Terceira pergunta
print("3. Quais os nomes dos irmãos que encontraram Aang preso no iceberg? \n")
print("(A) Kiana e Sora")
print("(B) Katara e Sokka")
print("(C) Zuko e Azula")
print("(D) Sokka e Toph")

#Recebe resposta do usuário
answer3 = input("Resposta: ")

#Conferir a resposta
if answer3 == "B" or answer3 == "b":
    print("Você acertou! \n Parabéns!!!")
    score += 10
else:
    print("Resposta errada! \n Quem sabe da próxima vez?")

#Quarta pergunta
print("4. Qual país foi responsável pela destruição da nação do Ar? \n")
print("(A) Reino da Terra")
print("(B) Tribo da Água do Sul")
print("(C) Nação do Fogo")
print("(D) Tribo da Água do Norte")

#Recebe resposta do usuário
answer4 = input("Resposta: ")

#Conferir a resposta
if answer4 == "C" or answer4 == "c":
    print("Você acertou! \n Parabéns!!!")
    score += 10
else:
    print("Resposta errada! \n Quem sabe da próxima vez?")


print("Término do Quiz!")
print(f"Pontuação final: \n O jogador {userName} fez {score} pontos")
