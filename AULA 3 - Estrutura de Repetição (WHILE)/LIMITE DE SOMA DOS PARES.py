# Crie um programa que solicite ao usuário que digite números inteiros. O programa deve continuar solicitando números até que a soma dos números pares digitados seja maior que 50. Ao atingir ou ultrapassar esse limite, o programa deve exibir a soma total e encerrar.

soma = 0
limite = 50

while True:
    numero_inteiro = int(input("Digite números inteiros: "))    
    if numero_inteiro % 2 == 0:
            soma += numero_inteiro
            if soma >= limite:
                print(f"Ultrapassou ou atingtiu o limite de {limite}! Soma total: {soma}")
                break

