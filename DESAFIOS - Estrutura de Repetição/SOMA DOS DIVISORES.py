# Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele próprio. Ex: a soma dos divisores do número 66 e 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

# com for
soma = 0

numero = int(input("Digite um número inteiro: "))

for i in range(1,numero):
    if numero % i == 0:
        soma += i

print(f"A soma dos divisores do número {numero} é de: {soma}")


# com while
soma = 0
contagem = 0

numero = int(input("Digite um número inteiro: "))

while contagem != (numero) -1:
    contagem += 1
    if numero % contagem == 0:
        soma += contagem

print(f"A soma dos divisores do número {numero} é de: {soma}")



