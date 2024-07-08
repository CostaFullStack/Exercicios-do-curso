# Faça um programa que leia um número positivo e imprima seus divisores.

# com for
numero = int(input("Digite um número positivo: "))
print(f"Os os divisores do número {numero} são:")

for i in range (1,numero+1):
    if numero % i == 0:
        print(i)

# com while
contagem = 0

numero = int(input("Digite um número positivo: "))
print(f"Os os divisores do número {numero} são:")

while contagem < numero:
    contagem += 1
    if numero % contagem == 0:
        print(contagem)
