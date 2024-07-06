# Implemente um jogo em que o usuário tenta adivinhar um número aleatório entre 1 e 20, dando dicas se a tentativa é muito alta ou muito baixa.

# sem break
numero_aleatorio = 15

print("Tente acertar o número aleatório entre 1 e 20!")
numero_tentado = int(input("Digite um número aleatório: "))

while numero_aleatorio != numero_tentado:
    if numero_tentado < numero_aleatorio:
        print("Número muito baixo!")

    elif numero_tentado > numero_aleatorio:
        print("Número muito alto!")
    numero_tentado = int(input("Digite outro número: "))   
     
else:
    print(f"Você acertou o número! Número sorteado: {numero_aleatorio}")

# com break
numero_aleatorio = 12
print("Tente acertar o número aleatório entre 1 e 20!")

while True:
    numero_tentado = int(input("Digite um número aleatório: "))
    if numero_tentado < numero_aleatorio:
        print("Número muito baixo!")
    elif numero_tentado > numero_aleatorio:
        print("Número muito alto!")
    else:
        print(f"Você acertou o número! Número sorteado: {numero_aleatorio}")
        break





