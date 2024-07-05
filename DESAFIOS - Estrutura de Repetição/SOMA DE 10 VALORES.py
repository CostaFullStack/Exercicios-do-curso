# Faça um programa que peça ao usuário para digitar 10 valores e some-os.

# com for
soma = 0
for i in range(1,11):
    numero = float(input(f"Digite o {i}º valor: "))
    soma += numero

print(f"A soma dos números é de: {soma}")

# com while
vezes = 0
soma = 0
while vezes < 10:
    numero = float(input("Digite o valor: "))
    vezes += 1
    soma += numero    

print(f"A soma dos números é de: {soma}")
