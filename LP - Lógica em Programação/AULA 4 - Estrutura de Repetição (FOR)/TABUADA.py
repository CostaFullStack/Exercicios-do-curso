# Com a estrutura de repetição for faça a tabuada de 1 a 10 do número informado pelo usuário.

tabuada = int(input("Digite o número para realizar a tabuada: "))
print(f"Tabuada do número {tabuada}:")

for i in range(11):
    print(f"{tabuada} x {i}: {tabuada*i}")