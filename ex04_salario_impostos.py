print('Faremos um cálculo dos seus descontos')
ph = float(input('Quanto você ganha por hora? '))
htpm = int(input('Quantas horas trabalha por mês? '))
smes = ph * htpm
imprenda = smes * 0.11
inss = smes * 0.08
sindicato = smes * 0.05
sliquido = smes - (imprenda + inss + sindicato)
print(f'Você trabalha {htpm}hrs/m e recebe R${ph:.2f} p/h trabalhado. ')
print(f'Salário bruto mensal: R${smes:.2f}')
print(f'Imposto de renda: {imprenda:.2f}')
print(f'INSS: {inss:.2f}')
print(f'Sindicato: {sindicato:.2f}')
print(f'Salário líquido: {sliquido:.2f}')