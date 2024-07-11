# Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano. Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.

# com for
chico = 150
ze = 110
contagem = 0

# idade média de 80 anos
for i in range(1,81):
    contagem += 1
    chico += 2
    ze += 3
    if ze > chico:
        break

print(f"Os anos necessários para que Zé seja maior que Chico são de: {contagem} anos.")

# com while
chico = 150
ze = 110
contagem = 0

while chico >= ze:
    chico += 2
    ze += 3
    contagem += 1

print(f"Os anos necessários para que Zé seja maior que Chico são de: {contagem} anos.")
