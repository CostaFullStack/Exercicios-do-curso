# Desenvolva um programa que receba um dicionário, uma chave e um valor como entrada e adiciona a chave e o valor ao dicionário, atualizando o valor se a chave já existir.

informacoes_pessoas = {
    'Nome': 'Matheus Costa Gomes',
    'Idade': 29,
    'Peso': 100,
    'Filme favorito': 'Lilya 4-ever',
    'Música favorita': 'Suicide Song'
}

informacoes_pessoas['Esporte favorito'] = 'Basquete'

for c,v in informacoes_pessoas.items():
    print(f"{c}: {v}")

# outra forma

informacoes_pessoas = {
'João': 25, 
'Maria': 30, 
'Pedro': 22, 
'Ana': 28
}

informacoes_pessoas['Ana'] = 23

for c,v in informacoes_pessoas.items():
    print(f"""
Nome: {c}
Idade: {v} anos
""")