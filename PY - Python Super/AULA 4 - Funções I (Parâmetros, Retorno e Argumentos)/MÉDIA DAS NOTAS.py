# Crie um programa que solicita ao usuário que insira três notas e, em seguida, calcule a média dessas notas usando uma função. A função deve receber as três notas como argumentos e retornar a média. Por fim, o programa deve imprimir a média calculada.

notas = []

for i in range(1,4):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

def media_notas(notas):
    media = sum(notas) / len(notas)
    return media

media = media_notas(notas)

print(f"A média das notas é de: {media:.1f}")