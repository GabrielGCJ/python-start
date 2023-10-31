price = float(input('Qual o preço do produto? R$'))
newPrice = price / 100 * 95
print('O produto que custava r${}, na promoção com \n desconto de 5% vai custar r${:.2f}'.format(price, newPrice))