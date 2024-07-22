# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.

par = 0
impar = 0

for i in range(1,11):
    numeros = int(input(f"Digite o {i}º número: "))
    if numeros % 2 == 0:
        par += 1
        
    elif numeros % 2 != 0:
        impar += 1

print(f"""
Quantidade de números pares: {par}
Quantidade de números ímpares: {impar}
""")

