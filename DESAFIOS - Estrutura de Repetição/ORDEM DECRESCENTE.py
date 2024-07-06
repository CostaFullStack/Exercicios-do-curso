# Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente.

# com for
numero = int(input("Digite um número inteiro positivo: "))
print(f"Número {numero} em ordem decrescente até 0:")

for i in range(numero,-1,-1):
    print(i)

# com while
numero = int(input("Digite um número inteiro positivo: "))
print(f"Número {numero} em ordem decrescente até 0:")

while numero >= 0:
    print(numero)
    numero -= 1

