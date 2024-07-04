# Crie um programa que solicite ao usuário adivinhar um número entre 1 e 100, dando dicas se a tentativa é muito alta, muito baixa ou correta. Adicione um limite de tentativas.

# Com break
numero_aleatorio = 72
tentativas = 5
print(f"Tente acertar o número aleatório entre 1 e 100! Você possui {tentativas} tentativas!")

while True:
    numero_tentado = int(input("Digite um número aleatório: "))
    tentativas -= 1
    if tentativas == 0:
        print(f"Suas tentativas acabaram! O número sorteado era: {numero_aleatorio}")
        break

    elif numero_tentado < numero_aleatorio:
        print(f"Número muito baixo! Tentativas restantes: {tentativas}")

    elif numero_tentado > numero_aleatorio:
        print(f"Número muito alto! Tentativas restantes: {tentativas}")
 
    else:
        print(f"Você acertou o número! Número sorteado: {numero_aleatorio}")
        break

# Sem break
numero_aleatorio = 72
tentativas = 3
print(f"Tente acertar o número aleatório entre 1 e 100! Você possui {tentativas} tentativas!")
numero_tentado = int(input("Digite um número aleatório: "))

while numero_aleatorio != numero_tentado and tentativas > 1:
    tentativas -= 1
    if numero_tentado < numero_aleatorio:
        print(f"Número muito baixo! Tentativas restantes: {tentativas}")

    elif numero_tentado > numero_aleatorio:
        print(f"Número muito alto! Tentativas restantes: {tentativas}")

    numero_tentado = int(input("Digite outro número: "))   

if tentativas == 0:
    print(f"Suas tentativas acabaram! O número sorteado era: {numero_aleatorio}")

else:
    print(f"Você acertou o número! Número sorteado: {numero_aleatorio}")








