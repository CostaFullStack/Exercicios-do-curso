#  Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.

alunos = [
{'nome': 'Ana', 'notas': [8.0, 7.5, 9.0]}, 
{'nome': 'João', 'notas': [7.0, 8.5, 9.5]}, 
{'nome': 'Maria', 'notas': [9.0, 8.0, 8.5]}
]

print("Média dos alunos:")
for i in alunos:
    media = sum(i['notas']) / len(i['notas'])
    print(f"{i['nome']}: {media:.1f}")

# outra forma

notas_alunos = {
'Ana': [8.0, 7.5, 9.0], 
'João': [7.0, 8.5, 9.5], 
'Maria': [9.0, 8.0, 8.5]
}

print("Média dos alunos:")
for nome, nota in notas_alunos.items():
    media = sum(nota) / len(nota)
    print(f"{nome}: {media:.1f}")