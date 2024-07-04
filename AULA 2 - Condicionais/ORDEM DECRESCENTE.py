# Faça um Programa que leia três números e mostre-os em ordem decrescente.

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

# Outra forma
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

 




