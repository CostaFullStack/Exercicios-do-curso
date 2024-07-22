# Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.

lista = []
par = []
impar = []
contagem_par = 0
contagem_impar = 0

for i in range(1,11):
    numeros = float(input(f"Digite o {i}º número: "))
    lista.append(numeros)

    if numeros % 2 == 0:
        par.append(numeros)
        contagem_par += 1

    else:
        impar.append(numeros)
        contagem_impar += 1

# Números pares e ímpares em uma lista.
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")

# Números pares e ímpares em uma tupla.
print(f"Números pares: {tuple(par)}")
print(f"Números pares: {tuple(impar)}")

# Quantidade de números pares e ímpares.
print(f"Quantidade de pares: {contagem_par}")
print(f"Quantidade de ímpares: {contagem_impar}")

# Soma total, dos pares e ímpares. 
print(f"Soma total dos números: {sum(lista)}")
print(f"Soma dos pares: {sum(par)}")
print(f"Soma dos ímpares: {sum(impar)}")
