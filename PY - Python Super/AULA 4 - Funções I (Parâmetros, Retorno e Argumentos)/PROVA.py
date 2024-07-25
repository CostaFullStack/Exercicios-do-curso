# Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.

notas = []

while True:
    try:

        nota = float(input("Digite a nota ou -1 para sair: "))
        if nota == -1:
            print("Programa encerrado!")
            break
        
        elif nota >= 11 or nota < 0:
            print("Digite notas entre 0 e 10!")
            continue

        else:
            notas.append(nota)

    except:
        print("Digite apenas números!")

def media_aluno(notas):
    if len(notas) == 0:
        return 0
    else:
        media = sum(notas) / len(notas)
        return media

def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10"

    elif media >= 7:
        return "Aprovado"
    
    else:
        return "Reprovado"

media = media_aluno(notas)
situacao = verificar_situacao(media)

if len(notas) > 0:
    print(f"""
    Média do aluno: {media:.1f}
    Situação: {situacao}
    """)

else:
    print("Você não digitou nenhuma nota ou os números informados foram inválidos!")




        





