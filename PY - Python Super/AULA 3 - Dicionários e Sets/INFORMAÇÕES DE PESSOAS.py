# Escreva um programa que exiba um dicionário contendo informações de pessoas (nome,idade) e exiba essas informações.

informacoes_pessoas = [
{'nome': 'João da Silva', 'idade': 23},
{'nome': 'Maria de Fátima Azevedo', 'idade': 67},
{'nome': 'Cássio de Costa', 'idade': 38}
]

for i in informacoes_pessoas:
    print(f"""
Nome: {i['nome']}
Idade: {i['idade']} anos
""")
