# Suponha que você está gerenciando uma competição esportiva e tem uma lista de tuplas representando os resultados das equipes em diferentes modalidades. Cada tupla contém o nome da equipe, seguido por uma lista de pontuações obtidas em cada rodada da competição. 
# 1. Calcule a média das pontuações de cada equipe e armazene esses valores em uma nova lista chamada medias. 
# 2. Ordene a lista medias em ordem decrescente.
# 3. Crie uma nova lista chamada classificação que contém tuplas, onde cada tupla contém o nome da equipe e sua média de pontuações. 
# 4. Exiba na tela a classificação final das equipes, mostrando o nome da equipe e sua média, da equipe com a pontuação mais alta para a maixa baixa.

# 1. calculando a média de cada equipe.
competicao = (
['Equipe 1', [10,9,8]],
['Equipe 2', [8,7,9]],
['Equipe 3', [8.5,9.5,7.5]],
)

media = []
soma = 0
for i in competicao:
    soma = sum(i[1]) / len(i[1])
    media.append(soma)

print(f"Média das equipes na lista:\n{media}")

# 2. colocando a média de cada equipe em ordem decrescente.
media.sort(reverse=True)

print("Lista em ordem decrescente:")

print(media)

# 3. lista com tuplas com nome da equipe e sua respectiva média.
classificacao = [
(competicao[0][0], media[0]),
(competicao[1][0], media[1]),
(competicao[2][0], media[2]),
]
print(f"Nome das euipes e suas médias: {classificacao}")

# 4. classificação final com a pontuação mais alta para a mais baixa.
classificacao.sort

print("Pontuação final das equipes e suas respectivas médias:")
for i in classificacao:
    print(i)




