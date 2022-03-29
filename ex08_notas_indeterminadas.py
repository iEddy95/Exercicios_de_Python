notas = []
pos = 1

escolha = int(input('[1] Informe as notas [-1] Sair \nQual a sua escolha? '))
if escolha == 1:
    while True:
        nota = float(input(f'Digite a {pos}º nota:'))
        if nota == -1:
            break
        notas.append(nota)
        pos += 1
print('Fim da Linha')


quantidade = len(notas)
inverso = notas[::-1]
soma = sum(notas)
media = soma/quantidade
acimamedia = len([n for n in notas if n >= media])
menorque7 = len([n for n in notas if n < 7])


print(f'{quantidade} Notas lidas')

print(f'Notas informadas:{notas}')

print(f'A soma das notas:{soma}')

print(f'A média das notas:{media}')

print(f'Notas acima da média:{acimamedia}')

print(f'Notas abaixo de 7:{menorque7}')

print('Muito obrigado por fazer uso do nosso programa!')