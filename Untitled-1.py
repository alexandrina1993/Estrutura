valor_hora = float(input("Informe quanto você ganha por hora (R$): "))
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11       # Imposto de Renda
inss = salario_bruto * 0.08     # INSS
sindicato = salario_bruto * 0.05  # Sindicato
salario_liquido = salario_bruto - ir - inss - sindicato
print("\n--- Folha de Pagamento ---")
print(f"+ Salário Bruto   : R$ {salario_bruto:.2f}")
print(f"- IR (11%)         : R$ {ir:.2f}")
print(f"- INSS (8%)       : R$ {inss:.2f}")
print(f"- Sindicato (5%)  : R$ {sindicato:.2f}")
print(f"= Salário Líquido  : R$ {salario_liquido:.2f}")

