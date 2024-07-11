# Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.

# com for
soma = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(f"A soma dos números naturais abaixo de 1000 que são múltiplos de 3 ou 5 é de: {soma}")

# com while
contador = 0
soma = 0 

while contador < 1000:
    if contador % 3 == 0 or contador % 5 == 0:
        soma += contador
    contador += 1

print(f"A soma dos números naturais abaixo de 1000 que são múltiplos de 3 ou 5 é de: {soma}")



