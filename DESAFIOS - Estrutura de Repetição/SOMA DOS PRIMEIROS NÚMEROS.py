# Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais.

# com for
numero = int(input("Digite um número inteiro positivo: "))

soma = 0

for i in range(numero+1):
    soma += i

print(f"A soma dos primeiros números naturais é de: {soma}")

# com while
numero = int(input("Digite um número inteiro positivo: "))

soma = 0
contador = 0

while contador < numero:
    contador += 1 
    soma += contador
    print(soma)




