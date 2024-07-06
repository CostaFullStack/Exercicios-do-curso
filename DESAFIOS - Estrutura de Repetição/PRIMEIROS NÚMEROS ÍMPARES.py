# Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.

# tentar usar o % 2 != 0
# com for
numero = int(input("Digite um número inteiro: "))
print(f"Os primeiros números naturais ímpares de {numero} são: ")

impar = 1

for i in range(1,numero*2,2):
    if impar <= numero:
        print(i)
        impar += 1

# com while
numero = int(input("Digite um número inteiro: "))
print(f"Os primeiros números naturais ímpares de {numero} são: ")

impar = 1
contador = 1

while contador <= numero:
    print(impar)
    impar += 2
    contador += 1