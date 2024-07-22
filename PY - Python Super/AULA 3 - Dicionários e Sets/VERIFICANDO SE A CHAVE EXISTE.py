# Escreva um programa que receba um dicionário e uma lista de chaves como entrada e verifica se todas as chaves da lista existem no dicionário. A função deve retornar True se todos as chaves existirem e False caso o contrário.

dicionario = {
'Título': 'Lilya 4-ever',
'Ano': 2002,
'Gênero': 'Drama'
}

lista = ['título', 'ano', 'gênero']

resultado = True

for i in lista:
    if i not in dicionario:
        resultado = False

if resultado:
    print(resultado)