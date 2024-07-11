# A partir do que aprendemos até agora: Crie um exemplo de cada uma das principais tipagens de variáveis. Crie uma solicitação de dados ao usuário. Imprima a solicitação anterior na tela com uma mensagem personalizada.

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
estado_civil = False

print(f"""
Nome: {nome}
Idade: {idade} anos
Altura: {altura} M
Peso: {peso} KG
Estado Civil: {estado_civil}
""")
