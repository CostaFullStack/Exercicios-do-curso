# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

# com for
maior = float("-inf")
menor = float("inf")

for i in range(1,11):
    numero = float(input(f"Digite o {i}º número: "))
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")

# com while
vezes = 0
maior = float("-inf")
menor = float("inf")

while vezes < 10:
    numero = float(input("Digite um número: "))
    vezes += 1
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero     
  
print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")