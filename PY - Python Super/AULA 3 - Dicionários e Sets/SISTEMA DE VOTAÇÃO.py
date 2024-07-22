# Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção. Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use while True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.

votacao = {
    'Gabriel': 0,
    'Matheus': 0,
    'Maria': 0
}

while True:
    try:
        menu = int(input("""
    Escolha uma das opções à seguir:
    1 - Ver eleitores
    2 - Realizar votação
    0 - Sair
                        
    """))
        match menu:
            case 1:
                for eleitor in votacao:
                    print(f"- {eleitor}\n")

            case 2:
                nome_eleitor = str(input("Digite o nome do eleitor: ")).strip()

                if nome_eleitor.strip() in votacao:
                    votacao[nome_eleitor] += 1
                    print("Voto realizado com sucesso!")

                else:
                    print(f"Nome do eleitor '{nome_eleitor}' não encontrado!")

            case 0:
                print("Votações encerradas!")
                for n, v in votacao.items():                       
                    print(f"""
                    Nome do eleitor: {n}
                    Votos: {v}
                    """)
                break

            case _:
                print("Opção inválida. Por favor, selecione uma opção válida.")
    except:
        print("Digite apenas números!")

# outra forma

votacao = {
    'Marina': 0,
    'Márcio': 0,
    'Rafaela': 0
}

while True:
    print("Eleitores:")
    for n, v in votacao.items():
         print(f"- {n}")

    nome_eleitor = str(input("Digite o nome do eleitor ou 0 para encerrar: ")).strip()

    if nome_eleitor in votacao:
            votacao[nome_eleitor] += 1

    elif nome_eleitor == "0":
        for n, v in votacao.items():
            print(f"""
            Nome do eleitor: {n}
            Votos: {v}
            """)
        break

    else:
        print(f"Nome do eleitor '{nome_eleitor}' não encontrado!")
