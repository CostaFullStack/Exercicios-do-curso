# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

# com for
maior = float("-inf")
menor = float("inf")

for i in range(1,11):
    numero = float(input(f"Digite o {i}º número: "))
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f"""
Maior número: {maior}
Menor número: {menor}
""")

# com while
vezes = 0
maior = float("-inf")
menor = float("inf")

while vezes < 10:
    numero = float(input("Digite um número: "))
    vezes += 1
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero     
  
print(f"""
Maior número: {maior}
Menor número: {menor}
""")
