# Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ımpares de 1 até N em ordem crescente.

# com for
numero = int(input("Digite um número inteiro positivo: "))
print(f"Número {numero} em ordem crescente até 1:")

for i in range(numero):
    if i % 2 != 0:
        numero -= 1
        print(i)

# com while
numero = int(input("Digite um número inteiro positivo: "))
print(f"Número {numero} em ordem crescente até 1:")

while numero >= 0:
    print(numero)
    numero += 1

    