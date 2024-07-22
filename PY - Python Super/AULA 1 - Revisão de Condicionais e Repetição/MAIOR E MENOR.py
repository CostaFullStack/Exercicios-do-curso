# Faça um programa que leia 3 números e informe o maior e o menor.

numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
numero_tres = float(input("Digite o terceiro número: "))

if numero_um > numero_dois and numero_um > numero_tres:
    print(f"O maior número foi o: {numero_um}")

elif numero_dois > numero_um and numero_dois > numero_tres:
    print(f"O maior número foi o: {numero_dois}")

elif numero_tres > numero_um and numero_tres > numero_dois:
    print(f"O maior número foi o: {numero_tres}")

if numero_um < numero_dois and numero_um < numero_tres:
    print(f"O menor número foi o: {numero_um}")

elif numero_dois < numero_um and numero_dois < numero_tres:
    print(f"O menor número foi o: {numero_dois}")   
 
else:
    print(f"O menor número foi o: {numero_tres}")

# outra forma
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
numero_tres = float(input("Digite o terceiro número: "))
maior = numero_um
menor = numero_um

if numero_dois > maior and numero_dois > numero_tres:
    maior = numero_dois

elif numero_tres > maior and numero_tres > numero_dois:
    maior = numero_tres

if numero_dois < menor and numero_dois < numero_tres :
    menor = numero_dois

elif numero_tres < menor and numero_tres < numero_dois:
    menor = numero_tres
    
print(f"""
Maior número: {maior}
Menor número: {menor}
""")






