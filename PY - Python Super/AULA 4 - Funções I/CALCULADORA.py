# Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair. (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.) Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos.
# Dica: Utilize de condicionais e Laços de Repetição para realizar esse exercício.

def soma(num1,num2):
    return num1 + num2

def multiplicacao(num1,num2):
    return num1 * num2

def subtracao(num1,num2): 
    return num1 - num2

def divisao(num1,num2):
    if num1 == 0:
        return "Erro! Divisão por zero!"  
    else:
        return num1 / num2


while True:
    try: 
        menu = int(input("""
    Escolha uma das opções à seguir:
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    0 - Sair
                        
    """))
        
        if 0 < menu <= 4:
            numero_um = float(input("Digite um número: "))
            numero_dois = float(input("Digite um número: "))
    
        match menu:
            case 1:
                print(soma(num1=numero_um, num2=numero_dois))
            
            case 2:
                print(subtracao(num1=numero_um, num2=numero_dois))
            
            case 3:
                print(multiplicacao(num1=numero_um, num2=numero_dois))
            
            case 4:
                print(divisao(num1=numero_um, num2=numero_dois))
            
            case 0:   
                print("Programa encerrado!")
                break

            case _:
                print("Opção inválida. Por favor, selecione uma opção válida!")

    except:
        print("Digite apenas números!")

    