diasAlugados = int(input('Quantos dias alugados?'))
kmRodados = float(input('Quantos Km rodados?'))

valorPagar = diasAlugados * 60 + kmRodados * 0.15

print('O valor total a pagar é R${:.2f}'.format(valorPagar))