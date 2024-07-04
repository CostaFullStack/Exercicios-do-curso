
soma = 0

for i in range(1,6):
    produto = float(input(f"Digite o preço do {i}º produto: "))
    soma += produto

print(f"O preço dos produtos de 1 à 5 é de: R${soma}")