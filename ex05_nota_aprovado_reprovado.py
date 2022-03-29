print('Vamos calcular sua média.')
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) /2

if media < 7:
    print('Reprovado!')
if media == 10:
    print('Aprovado com distinção!')
if media >= 7 and media < 10:
    print('Aprovado!')