
# Sistema de Cadastro de Alunos - passo 1 
# Cadastro de alunos: O programa deve permitir ao usuário cadastrar alunos. Cada aluno terá as seguintes informações: nome, idade e notas em três disciplinas: Matemática, Ciências e história. Os dados de cada aluno devem ser armazenados em um dicionário com as seguintes chaves: 'nome', 'idade', 'notas'. As notas devem ser armazenadas em uma tupla.

# Sistema de Cadastro de Alunos - passo 2
# Visualização de Alunos: O programa deve permitir ao usuário visualizar todos os alunos cadastrados, exibindo suas infomrações de forma organizada.

# Média de notas: O programa deve calcular a média das notas de cada aluno e exibi-la.
# Aluno com Melhor Média: O programa deve identificar oe exibir o aluno com a melhor média de notas.

armazena = []
nome_maior = ""
media_maior = float("-inf")

while True:
    try:
        menu = int(input("""
    1 - Cadastrar aluno
    2 - Ver aluno cadastrado
    3 - Média dos alunos
    4 - Aluno com maior média
    0 - Sair
                        
    """))
        match menu:
            case 1:
                nome = str(input("Digite o nome do aluno: "))
                if nome in "0123456789!@#$%¨&*+=-;\}{^: ":
                    print("Digite apenas letras!")
                    continue

                elif " " not in nome:
                    print("Digite o nome completo do aluno!")
                    continue

                idade = int(input("Digite a idade do aluno: "))
                notas = (
                float(input("Digite a nota em Matemática: ")), 
                float(input("Digite a nota em Ciências: ")), 
                float(input("Digite a nota em História: "))
                )

                print(f"Aluno {nome} cadastrado com sucesso!")

                aluno = {
                    'nome': nome,
                    'idade': idade,
                    'notas': notas
                }
                armazena.append(aluno)

            case 2:
                if len(armazena) == 0:
                    print("Não há alunos cadastrados!")
                else:
                    for i in armazena:
                        print(f"""
                        Nome: {i['nome']}
                        Idade: {i['idade']} anos
                        Notas: {(i['notas'])}
                    """)
            
            case 3:
                if len(armazena) == 0:
                    print("Não há alunos cadastrados!")
                else:
                    for i in armazena:
                        media = sum(i['notas']) / len(i['notas'])

                        print(f"""
                        Nome: {i['nome']}
                        Média: {media:.1f}    
                        """)
            
            case 4:
                if len(armazena) == 0:
                    print("Não há alunos cadastrados!")
                else:
                    for i in armazena:
                        media = sum(i['notas']) / len(i['notas'])

                        if media > media_maior:
                            media_maior = media
                            nome_maior = i['nome']

                    print(f"""
                    Nome do aluno com maior média: {nome_maior}
                    Média: {media_maior:.1f}
                    """)
                            
            case 0:
                print("Programa encerrado!")
                break

            case _:
                print("Opção inválida. Por favor, selecioen uma opção válida!")
    except:
        print("Digite apenas números!")