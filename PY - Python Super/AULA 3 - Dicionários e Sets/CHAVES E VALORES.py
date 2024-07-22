# Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

filmes = {
    'Lilya 4-ever': 'Drama',
    'Black Swan': 'Thriller, Drama',
    'Fallen Angels': 'Crime, Romance, Ação',
}

for c,v in filmes.items():
    print(f"""
Filme: {c}
Gênero: {v}
""")
