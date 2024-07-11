# Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual o número foi gerado, a cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando o usuário acertar o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.

# com for
numero_aleatorio = 350
tentativas = 0

print("Tente acertar o número aleatório entre 1 e 1000!")
for i in range(1000):
    numero = int(input("Digite um número aleatório: "))
    tentativas += 1
    if numero == numero_aleatorio:
        print(f"Parabéns! Você acertou o número! Número: {numero_aleatorio}. Tentativas: {tentativas}")
        break
    elif numero < numero_aleatorio:
        print(f"Número muito baixo! Tente um número mais alto!")

    elif numero > numero_aleatorio:
        print(f"Número muito alto! Tente um número mais alto!")

# com while
numero_aleatorio = 350
tentativas = 0

print("Tente acertar o número aleatório entre 1 e 1000!")
while True:
    numero = int(input("Digite um número aleatório: "))
    tentativas += 1
    if numero == numero_aleatorio:
        print(f"Parabéns! Você acertou o número! Número sorteado: {numero_aleatorio}. Tentativas: {tentativas}")
        break  
    elif numero < numero_aleatorio:
        print("Número muito baixo! Tente um número mais alto!")
    elif numero > numero_aleatorio:
        print("Número muito alto! Tente um número mais alto!")

