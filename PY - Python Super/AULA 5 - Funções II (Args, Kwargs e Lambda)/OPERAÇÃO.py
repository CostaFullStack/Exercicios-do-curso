# Crie uma função que aceite dois números e uma operação (por exemplo, adição, subtração, multiplicação, divisão) como argumentos e use funções lambda para realizar a operação especificada. A função deve retornar o resultado da operação.

def operacao(x,y, operacao):
        if operacao == '+':
            return (lambda x,y: x+y)(x,y)
        
        elif operacao == '-':
            return (lambda x,y: x-y)(x,y)
        
        elif operacao == '*':
            return (lambda x,y: x*y)(x,y)
        
        elif operacao == '/':
            return (lambda x,y: 'Erro! Divisão por zero!' if x == 0 else x/y)(x,y)
            
while True:
    operacao_mat = str(input("""
    Escolha uma das opções à seguir:
    '+' para somar
    '-' para subtrair
    '*' para multiplicar
    '/' para dividir
    '0' para sair 
                                               
"""))
    
    if operacao_mat in " ":
        print('Não pode haver espaços em branco!')

    if operacao_mat in '0':
        print('Programa encerrado!')
        break
  
    elif operacao_mat not in '+-*/':
        print("Digite apenas + - * / ou 0")

    else:
        try:
            numero_um = float(input("Digite o primeiro número: "))
            numero_dois = float(input("Digite o segundo número: "))

            if operacao_mat in '+':
                print(operacao(x=numero_um, y=numero_dois, operacao=operacao_mat))

            elif operacao_mat in '-':
                print(operacao(x=numero_um, y=numero_dois, operacao=operacao_mat))

            elif operacao_mat in '*':
                print(operacao(x=numero_um, y=numero_dois, operacao=operacao_mat))

            elif operacao_mat in '/':
                print(operacao(x=numero_um, y=numero_dois, operacao=operacao_mat))

            else:
                print('Opção inválida. Por favor, selecione uma opção válida!')
        except:
            print("Digite apenas números!")

# com match e case
while True:
    try: 
        menu = str(input("""
    Escolha uma das opções à seguir:
    '+' para somar
    '-' para subtrair
    '*' para multiplicar
    '/' para dividir
    '0' para sair 
                        
    """))
        
        if menu in " ":
            print('Não pode haver espaços em branco!')

        else:
            if menu in '+-*/':
                numero_um = float(input("Digite um número: "))
                numero_dois = float(input("Digite um número: "))
    
            match menu:
                case '+':
                    print(operacao(x=numero_um, y=numero_dois, operacao=menu))
                
                case '-':
                    print(operacao(x=numero_um, y=numero_dois, operacao=menu))
                
                case '*':
                    print(operacao(x=numero_um, y=numero_dois, operacao=menu))
                
                case '/':
                    print(operacao(x=numero_um, y=numero_dois, operacao=menu))
                
                case '0':   
                    print("Programa encerrado!")
                    break

                case _:
                    print("Digite apenas + - * / ou 0")

    except:
        print("Digite apenas números!")
