# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.

# com for
maior = float("-inf")
contagem = 0

qtd_numeros = int(input("Digite a quantidade de números a serem lidos: "))

for i in range(1,qtd_numeros+1):
    numeros = int(input(f"Digite o {i}º número: "))
    if numeros > maior:
        maior = numeros
        contagem = 1

    elif numeros == maior:
        contagem += 1

print(f"""
Maior número lido: {maior}
Quantidade de vezes lida: {contagem}
""")

# com while
maior = float("-inf")
contagem = 0
vezes = 0

qtd_numeros = int(input("Digite a quantidade de números a serem lidos: "))

while vezes < qtd_numeros:
    numeros = int(input("Digite um número: "))
    vezes += 1
    if numeros > maior:
        maior = numeros
        contagem = 1

    elif maior == numeros:
        contagem += 1

print(f"""
Maior número lido: {maior}
Quantidade de vezes lida: {contagem}
""")






