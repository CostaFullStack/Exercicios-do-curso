# Faça um Programa que leia três números e mostre o maior deles.

numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
numero_tres = float(input("Digite o terceiro número: "))

if numero_um > numero_dois and numero_um > numero_tres:
    print(f"O maior número é o: {numero_um}")

elif numero_dois > numero_um and numero_dois > numero_tres:
    print(f"O maior número digitado foi o: {numero_dois}")

else:
    print(f"O maior número digitado foi o: {numero_tres}")