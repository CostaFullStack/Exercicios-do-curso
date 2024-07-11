# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.

# com for
maior = float("-inf")
menor = float("inf")
numero_positivo = False

for _ in range(10000000000):
    numero = int(input("Digite um número inteiro: "))   
    if numero < 0:
        if numero_positivo:
            break
        else:
            print("Nenhum número positivo foi digitado!")
            break   
    else:
        numero_positivo = True
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
if numero_positivo:
    print(f"O maior número digitado foi: {maior}")
    print(f"O menor número digitado foi: {menor}")


# com while
maior = float("-inf")
menor = float("inf")

numero_positivo = False

while True:
    numero = int(input("Digite um número inteiro: "))           
    if numero < 0:
        if numero_positivo:
            break
        else:
            print("Nenhum número positivo foi digitado!")
            break
    else:
        numero_positivo = True
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

if numero_positivo:
    print(f"""
Maior número digitado: {maior}
Menor número digitado: {menor}
""")


    
