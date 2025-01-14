import random

print("Seja muito bem-vindo ao Guess Number do Iury!")

# Define o número aleatório fixo entre 1 e 100
random_number = random.randint(1, 100)

#Inicia o valor nulo para o número de tentativas do usuário
n_choices = 0

while True:
    answer_user = input("Adivinhe o número (entre 1 e 100): ")

    #Validação do número inserido pelo usuário
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado não é numérico. Favor informe um número!")
        continue

    n_choices += 1
