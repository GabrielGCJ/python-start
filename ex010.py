x = float(input('Quanto dinheiro você tem na carteira? R$'))
cotaDolar = 3.27
valorConvert = x / cotaDolar
print('Com R${:.2f} você pode comprar US${:.2f}'.format(x, valorConvert))