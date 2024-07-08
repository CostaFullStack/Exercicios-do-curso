# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))

media = (nota_um + nota_dois) / 2

if media == 10:
    print(f"Aprovado com distinção. Média: {media}")
elif media >= 7:
    print(f"Aprovado. Média: {media}")
else:
    print(f"Reprovado. Média: {media}")