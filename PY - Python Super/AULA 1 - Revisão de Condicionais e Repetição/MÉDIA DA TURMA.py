# Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entra 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

media = 0

# pedindo a idade de 5 pessoas
for i in range(1,6):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    media += idade / 5

if media <= 25:
    print(f"A turma é jovem! Média de idade: {media}")

elif media <= 60:
    print(f"A turma é adulta! Média de idade: {media}")

else:
    print(f"A turma é idosa! Média de idade: {media}")


