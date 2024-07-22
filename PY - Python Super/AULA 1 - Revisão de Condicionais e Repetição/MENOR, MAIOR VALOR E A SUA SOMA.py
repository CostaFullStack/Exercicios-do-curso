# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

maior = float("-inf")
menor = float("inf")

for i in range(1,6):
    numero = float(input(f"Digite o {i}º número: "))
    if numero > maior:
        maior = numero
        
    if numero < menor:
        menor = numero

print(f"""
Maior valor: {maior}
Menor valor: {menor}
Soma dos valores: {maior + menor}
""")