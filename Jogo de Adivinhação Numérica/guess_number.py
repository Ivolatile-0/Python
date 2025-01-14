import random

# Define o número aleatório fixo entre 1 e 100
random_number = random.randint(1, 100)

# Inicia o valor nulo para o número de tentativas do usuário
n_choices = 0

# Mensagem Inicial
print("Seja muito bem-vindo ao Adivinhe o Número!")
print("Como Jogar: Você precisa adivinhar um número escolhido aleatoriamente pelo computador, entre 1 e 100. ")
print("Ao começar o jogo, você irá digitar um número, que será o seu palpite. \nO programa vai te avisar quando o número for maior, menor ou igual o número escolhido pelo computador. \nO jogo conta o seu número de tentativas e quanto menor o número de tentativas, maior sua pontuação.")
print("Boa sorte e divirta-se!")

while True:
    answer_user = input("Por favor, digite um número (entre 1 e 100): ")

    # Validação do número inserido pelo usuário
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado não é numérico. Por favor, informe um número entre 1 e 100!")
        continue

    n_choices += 1

    # Resposta ao usuário
    if answer_user == random_number:
        print(f"Acertou, miserávi! O número randômico é {random_number}!")
        break
    elif answer_user > random_number:
        print(f"Chutou alto! O número randômico é menor que {answer_user}.")
    else:
        print(f"Chutou baixo! O número randômico é maior que {answer_user}.")

# Calcula os pontos baseados no número de tentativas
pontos = max(0, 100 - (n_choices - 1) * 10)

# Informa o número de tentativas e a pontuação do usuário
print("N° de tentativas: " + str(n_choices))
print(f"Sua pontuação é: {pontos} pontos!")