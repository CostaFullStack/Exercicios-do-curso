# Crie um loop while que imprima os números pares de 2 a 10.

par = 0
contador = 10

print("Números pares de 2 à 10:")
while par < contador:
    if par % 2 == 0:
        par += 2
        print(par)
