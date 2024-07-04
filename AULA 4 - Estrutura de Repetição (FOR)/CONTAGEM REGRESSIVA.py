# Faça uma contagem regressiva de um número inteiro passado pelo usuário até 0.

numero = int(input("Digite um número inteiro: "))
print(f"Contagem regressiva do número {numero}:")

for i in range(numero,-1,-1):
    print(i)