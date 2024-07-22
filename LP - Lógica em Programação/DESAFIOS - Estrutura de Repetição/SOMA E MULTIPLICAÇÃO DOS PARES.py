# Faça um programa que receba dois números. Calcule e mostre:
# A soma dos números pares desse intervalo de números, incluindo os números
# digitados;
# A multiplicação dos números ımpares desse intervalo, incluindo os digitados;

# com for
mult = 1
soma = 0

numero_um = int(input("Digite o 1º número: "))
numero_dois = int(input("Digite o 2º número: "))

for i in range(numero_um,numero_dois+1):
    if i % 2 == 0:
        soma += i
    elif i % 2 != 0:
        mult *= i

print(f"A soma dos números pares no intervalo do número {numero_um} e {numero_dois} é de: {soma}")
print(f"A multiplicação dos números ímpares no intervalo do número {numero_um} e {numero_dois} é de: {mult}")

# com while
mult = 1
soma = 0

numero_um = int(input("Digite o 1º número: "))
numero_dois = int(input("Digite o 2º número: "))

while numero_um <= numero_dois:
    if numero_um % 2 == 0:
        soma += numero_um
        
    else:
        mult *= numero_um
    numero_um += 1

print(f"A soma dos números pares no intervalo do números é de: {soma}")
print(f"A multiplicação dos números ímpares no intervalo dos números é de: {mult}")




