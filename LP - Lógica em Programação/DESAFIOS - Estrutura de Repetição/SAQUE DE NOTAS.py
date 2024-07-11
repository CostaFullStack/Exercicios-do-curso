# Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.

# com for
for i in range(1):
    valor = float(input("Digite quanto deseja sacar: "))

    cem = int(valor/100)
    valor = valor - (cem * 100)

    cinquenta = int(valor/50)
    valor = valor - (cinquenta * 50)

    vinte = int(valor/20)
    valor = valor - (vinte * 20)

    dez = int(valor/10)
    valor = valor - (dez * 10)

    cinco = int(valor/5)
    valor = valor - (cinco * 5)

    dois = int(valor/2)
    valor = valor - (dois * 2)

    um = int(valor)
    break

print(f"""
Notas de R$100,00: {cem}
Notas de R$50,00: {cinquenta}
Notas de R$20,00: {vinte}
Notas de R$10,00: {dez}
Notas de R$5,00: {cinco}
Notas de R$2,00: {dois}
Notas de R$1,00: {um}
""")

# com while
while True:
    valor = float(input("Digite quanto deseja sacar: "))

    cem = int(valor/100)
    valor = valor - (cem * 100)

    cinquenta = int(valor/50)
    valor = valor - (cinquenta * 50)

    vinte = int(valor/20)
    valor = valor - (vinte * 20)

    dez = int(valor/10)
    valor = valor - (dez * 10)

    cinco = int(valor/5)
    valor = valor - (cinco * 5)

    dois = int(valor/2)
    valor = valor - (dois * 2)

    um = int(valor)
    break

print(f"""
Notas de R$100,00: {cem}
Notas de R$50,00: {cinquenta}
Notas de R$20,00: {vinte}
Notas de R$10,00: {dez}
Notas de R$5,00: {cinco}
Notas de R$2,00: {dois}
Notas de R$1,00: {um}
""")
