# Utilize um loop for para imprimir os números de 1 a 20, pulando os múltiplos de 3.

print("Números que não são mútiplos de 3 de 1 à 20:")

for i in range(20):
    if i % 3 != 0:
        continue
    print(i)