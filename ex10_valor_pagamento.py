q = t = parcela = dias = valorPagamento = 0

while True:
    parcela = float(input('Valor da prestação: '))
    if parcela == 0:
        print('#'*36)
        print('#         RELATÓRIO DO DIA         #')
        print('#'*36)
        print(f'# Valor total das parcelas: R${t:.2f}\n# Quantidade de parcelas: {q} ')
        print('#' * 36)
        break
    dias = int(input('Dias em atraso: '))
    if dias == 0:
        valorPagamento = parcela
        print(f'Valor a ser pago: {valorPagamento}')
        print('¨¨¨' * 10)
    else:
        multa = parcela * 0.03 + 0.001 * dias
        valorPagamento = parcela + multa
        print(f'Valor a ser pago: {valorPagamento:.2f}')
        print('¨¨¨'*10)
    q += 1
    t += valorPagamento