# Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um intervalo invalido (começando por um valor maior que o valor final) deve ser escrito uma mensagem de erro na tela, “Intervalo de valores inválido”.

# com for
soma = 0

valor_inicial = int(input("Digite o valor inicial do intervalo: "))
valor_final = int(input("Digite o valor final do intervalo: "))

if valor_inicial > valor_final:
    print("Intervalo de valores inválido.")
else:
    for i in range(valor_inicial,valor_final+1):  
        if i % 2 != 0:
            soma += i
    print(f"A soma dos números ímpares no intervalo do número {valor_inicial} e do número {valor_final} é de: {soma}")

# com while
soma = 0

valor_inicial = int(input("Digite o valor inicial do intervalo: "))
valor_final = int(input("Digite o valor final do intervalo: "))

if valor_inicial > valor_final:
    print("Intervalo de valores inválido.")
else:
    while valor_inicial <= valor_final:
        if valor_inicial % 2 != 0:
            soma += valor_inicial
        valor_inicial += 1           
    print(f"A soma dos números ímpares no intervalo dos números é de: {soma}")
