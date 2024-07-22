# Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário. O programa deve fornecer as seguintes funcionalidades:
# Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
# Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
# Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrículaO programa deve ser executado em um loop contínuo até que o usuário escolha sair.

armazena = {}

while True:
    try:
        menu = int(input("""
    Escolha umas das opções abaixo:
    1 - Adicionar alunos
    2 - Remover alunos
    3 - Visualizar alunos
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

                matricula = int(input("Digite o número da matrícula: "))
                
                if matricula in armazena.values(): 
                    print(f"Já existe aluno com a matrícula de número {matricula} cadastrado!")
                    continue
                
                cadastro_aluno = {
                    'nome': nome,
                    'matrícula': matricula
                }
                print(f"Aluno {nome} cadastrado com sucesso!")

                armazena.update({nome: matricula})


            case 2: 
                if len(armazena) == 0:
                    print("Não há alunos cadastrados!")  

                else: 
                    for n,m in armazena.items():
                        print(f"""
                        Nome: {n}
                        Matrícula: {m}
                        """)

                    matricula = int(input("Digite o ID da matrícula do aluno que deseja remover: "))

                    if matricula == m:
                        armazena.pop(n)
                        print(f"Aluno {n} removido com sucesso!")
                    
                    else:
                        print(f"Aluno com a matrícula de número {matricula} não encontrado!")

            case 3:
                if len(armazena) == 0:
                    print("Não há alunos cadastrados!")  

                else:
                    for n,m in armazena.items():
                        print(f"""
                        Nome: {n}
                        Matrícula: {m}
                        """)
            case 0:
                print("Programa encerrado!")
                break

            case _:
                print("Opção inválida. Por favor, selecione uma opção válida!")
    except:
        print("Digite apenas números!")

        