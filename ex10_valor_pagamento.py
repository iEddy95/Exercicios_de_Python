valorprestacao = []
valorPagamento = 0
cont = 0

while valorprestacao != 0:
    valorprestacao = float(input('Informe o valor da prestação: '))
    if valorprestacao == 0:
        print(cont)
        print(valorprestacao)
        break
    dias = int(input('Dias atrasada: '))
    if dias > 0:
        multadia = 0.001 * dias
        multa = valorprestacao * 0.03
        valorPagamento = valorprestacao + multadia + multa
        valorprestacao.append(valorPagamento)
        cont += 1
    else:
        valorPagamento = valorprestacao
        valorprestacao.append(valorPagamento)
        cont += 1
    print(f'Print valor a ser pago: {valorPagamento:.2f}')
