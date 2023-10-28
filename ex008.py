x = float(input('Uma distancia em metros:'))
km = x/1000
hm = x/100
dam = x/10
dm = int(x*10)
cm = int(x*100)
mm = int(x*1000)
print('A distancia corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(km, hm, dam, dm, cm, mm))