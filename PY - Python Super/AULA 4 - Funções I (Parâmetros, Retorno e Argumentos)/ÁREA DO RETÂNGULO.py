# Crie um programa que define uma função calcular_area_retangulo que recebe dois argumentos, comprimento e largura de um retângulo, e retorna a área desse retângulo. Em seguida, o programa deve solicitar ao usuário que insira o comprimento e a largura e imprimir a área calculada.

def calcular_area_retangulo(comprimento,largura):
    area = comprimento * largura
    return area

area_retangulo = calcular_area_retangulo(
largura=float(input("Informe a largura do retângulo: ")),
comprimento=float(input("Informe a comprimento do retângulo: "))
)

print(f"A área do retângulo é de: {area_retangulo}")