# Crie um programa que, utilizando um loop for, encontre o primeiro número na sequência de 1 a 50 que seja divisível por 6 e pare a execução.

for i in range(1,51):
    if i % 6 == 0:
        print(f"O primeiro número de 1 à 50 que é divisível por 6 é: {i}")
        break
