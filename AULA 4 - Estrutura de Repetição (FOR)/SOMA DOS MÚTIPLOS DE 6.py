# Crie uma programa que solicite 10 números para o usuário. O programa deve somar todos os números múltiplos de 6 digitados. Se a soma for igual ou maior que 30, o programa dever parar e mostrar o resultado da soma.

soma = 0
limite = 30

for num in range(1,11):
    numeros = int(input(f"Digite o {num}º número: "))
    if numeros % 6 == 0:
        soma += numeros
        
        if soma >= limite:      
            print(f"Ultrapassou ou atingtiu o limite de {limite}! Soma total: {soma}")
            break
