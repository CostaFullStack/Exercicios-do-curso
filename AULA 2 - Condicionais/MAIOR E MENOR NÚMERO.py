# Faça um Programa que leia três números e mostre o maior e o menor deles.

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
    
# Outra forma
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

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
