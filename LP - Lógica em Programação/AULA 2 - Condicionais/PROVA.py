# Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado e o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

print("Velocidade máxima permitida: 80km/h")
velocidade = int(input("Informe a velocidade do carro: "))

multa = 0

if velocidade > 80:
    multa = (velocidade - 80) * 20
    print(f"Você foi multado por ultrapassar o excesso de velocidade! Multa: R${float(multa)}")

else:
    print(f"Você está no limite de velocidade. Velocidade atual: {velocidade}km/h")