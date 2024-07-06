# Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.

# com for
soma = 0

for i in range(101):
    if i % 2 == 0:
        soma += i

print(f"A soma dos 50 primeiros números pares é de: {soma}")

# com while
soma = 0
par = 0
contador = 0

while contador < 100:
        contador += 2
        soma += contador

print(f"A soma dos 50 primeiros números pares é de: {soma}")





