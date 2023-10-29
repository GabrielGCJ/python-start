lar = float(input('Digite a largura da parede em metros:'))
alt = float(input('Digite a altura da parede em metros:'))
mts = float(input('A tinta que usaremos cobre quantos m² em media?'))

m2 = lar * alt
lit = m2 / mts

print('Sua parede tem a dimenção de {} x {} e sua area é de {}m².'.format(lar, alt, m2))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(lit))