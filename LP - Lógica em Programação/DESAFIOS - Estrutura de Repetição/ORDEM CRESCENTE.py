# Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ımpares de 1 até N em ordem crescente.

# com for
numero = int(input("Digite um número inteiro positivo: "))
print(f"Ordem crescente dos ímpares do número {numero} começando por 1:")

for i in range(numero):
    if i % 2 != 0:
        numero -= 1
        print(i)

# com while
contagem = 0
vezes = 0

numero = int(input("Digite um número inteiro positivo: "))
print(f"Ordem crescente dos ímpares do número {numero} começando por 1:")

while contagem < numero:
    vezes += 1
    if contagem % 2 != 0:
        print(contagem)
    contagem += 1
    
    


    