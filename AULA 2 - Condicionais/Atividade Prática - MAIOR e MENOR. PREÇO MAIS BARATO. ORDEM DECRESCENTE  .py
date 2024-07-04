# Faça um Programa que leia três números e mostre o maior deles.
# Faça um Programa que leia três números e mostre o maior e o menor deles.
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# Faça um Programa que leia três números e mostre-os em ordem decrescente.

# Maior número
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
numero_tres = float(input("Digite o terceiro número: "))

if numero_um > numero_dois and numero_um > numero_tres:
    print(f"O maior número é o: {numero_um}")

elif numero_dois > numero_um and numero_dois > numero_tres:
    print(f"O maior número digitado foi o: {numero_dois}")

else:
    print(f"O maior número digitado foi o: {numero_tres}")

# Maior e menor número
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
numero_tres = float(input("Digite o terceiro número: "))

if numero_um > numero_dois and numero_um > numero_tres:
    print(f"O maior número é o: {numero_um}")

elif numero_dois > numero_um and numero_dois > numero_tres:
    print(f"O maior número digitado foi o: {numero_dois}")

else:
    print(f"O maior número digitado foi o: {numero_tres}")

if numero_um < numero_dois and numero_um < numero_tres:
    print(f"O menor número digitado foi: {numero_um}")

elif numero_dois < numero_um and numero_dois < numero_tres:
    print(f"O menor número digitado foi: {numero_dois}")

else:
    print(f"O menor número digitado foi: {numero_tres}")
    
# Maior e menor número (outra forma)
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
numero_tres = float(input("Digite o terceiro número: "))
maior = numero_um
menor = numero_um

if numero_dois > numero_um and numero_dois > numero_tres:
    maior = numero_dois

elif numero_tres > numero_um and numero_tres > numero_dois:
    maior = numero_tres

elif numero_dois < numero_tres and numero_dois < numero_um:
    menor = numero_dois

elif numero_tres < numero_dois and numero_tres < numero_um:
    menor = numero_tres

print(f'Menor número: {menor}')
print(f'Maior número: {maior}')

# Produto mais barato
primeiro_produto = float(input(f"Digite o preço do primeiro produto: "))
segundo_produto = float(input(f"Digite o preço do segundo produto: "))
terceiro_produto = float(input(f"Digite o preço do terceiro produto: "))

if primeiro_produto < segundo_produto and primeiro_produto < terceiro_produto:
    print(f"O produto mais barato a ser comprado é o primeiro produto. Valor: R${primeiro_produto}")

elif segundo_produto < primeiro_produto and segundo_produto < terceiro_produto:
    print(f"O produto mais barato a ser comprado é o segundo produto. Valor: R${segundo_produto}")

else:
    print(f"O produto mais barato a ser comprado é o segundo produto. Valor: R${terceiro_produto}")

# Faça um Programa que leia três números e mostre-os em ordem decrescente.
# Ordem decrescente
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
numero_tres = float(input("Digite o terceiro número: "))

if numero_um > numero_dois and numero_dois > numero_tres:
    print(f"Ordem decrescente: {numero_um}, {numero_dois}, {numero_tres}")

elif numero_um > numero_tres and numero_tres > numero_dois:
    print(f"Ordem decrescente: {numero_um}, {numero_tres}, {numero_dois}")

elif numero_dois > numero_um and numero_um > numero_tres:
    print(f"Ordem decrescente: {numero_dois}, {numero_um}, {numero_tres}")

elif numero_dois > numero_tres and numero_tres > numero_um:
    print(f"Ordem decrescente: {numero_dois}, {numero_tres}, {numero_um}")

elif numero_tres > numero_um and numero_um > numero_dois:
    print(f"Ordem decrescente: {numero_tres}, {numero_um}, {numero_dois}")

else:
    print(f"Ordem decrescente: {numero_tres}, {numero_dois}, {numero_um}")

# Ordem crescente (outra forma)
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
numero_tres = float(input("Digite o terceiro número: "))

if numero_um > numero_dois and numero_dois > numero_tres:
    maior = numero_um
    meio = numero_dois
    menor = numero_tres

elif numero_um > numero_tres and numero_tres > numero_dois:
    maior = numero_um
    meio = numero_tres
    menor = numero_dois

elif numero_dois > numero_um and numero_um > numero_tres:
    maior = numero_dois
    meio = numero_um
    menor = numero_tres

elif numero_dois > numero_tres and numero_tres > numero_um:
    maior = numero_dois
    meio = numero_tres
    menor = numero_um

elif numero_tres > numero_um and numero_um > numero_dois:
    maior = numero_tres
    meio = numero_um
    menor = numero_dois

else:
    maior = numero_tres
    meio = numero_dois
    menor = numero_um

print(f"Ordem decrescente: {maior}, {meio}, {menor}")

 




