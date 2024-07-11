# Exercício de Revisão) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# Imposto de Renda
# Salário bruto
# Quanto pagou ao INSS.
# Quanto pagou ao sindicato.
# O salário líquido.
# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# Salário Bruto : R$
# IR (11%) : R$
# INSS (8%) : R$
# Sindicato (5%) : R$
# Salário Liquido : R$

ganho_hora = float(input("Digite quanto você ganha por hora: "))
horas_mes = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# Salário bruto
salario_bruto = ganho_hora * horas_mes

# Total descontado para o Imposto de Renda
desconto_renda = salario_bruto * 0.11

# Total descontado para o INSS
desconto_inss = salario_bruto * 0.08

# Total descontado para o sindicato
desconto_sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (desconto_renda + desconto_inss + desconto_sindicato)

print(f"""
Salário bruto: R${salario_bruto}
INSS (8%): R${desconto_inss}
Sindicato (5%): R${desconto_sindicato}
Salário Líquido: R${salario_liquido}
""")