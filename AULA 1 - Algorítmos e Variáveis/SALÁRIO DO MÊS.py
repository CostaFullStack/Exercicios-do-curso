# 5. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Digite quando você ganha por hora: "))
horas_mes = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salario = ganho_hora * horas_mes
print(f"O salário total do referido mês é de: R${salario}")