sal = float(input('Insira o salário do colaborador:'))

if (sal <= 280.00):
    percentual = 20
elif (sal >= 280.00 and sal <= 700.00):
    percentual = 15
elif (sal >= 700.00 and sal <= 1500.00):
    percentual = 10
if (sal >= 1500.00):
    percentual = 5

qpercentual = percentual / 100.0
aumento = qpercentual * sal
salario_novo = sal + aumento

print(f'O seu salário era: R${sal:.2f}')
print(f'O aumento foi de: {percentual}%')
print(f'O seu aumento foi de: R${aumento:.2f}')
print(f'O seu novo salário é: R${salario_novo:.2f}')