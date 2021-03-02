# 平均數、變異數、標準差

a = []
for i in range(0,5):
    a.append(float(input()))

avg = 0
for i in range(0,5):
    avg += a[i]
avg = avg/5

dif = 0
for i in range (0,5):
    dif += (a[i] - avg)**2
dif = dif/5

sta = dif**0.5

print('%.2f' % avg)
print('%.2f' % dif)
print('%.2f' % sta)
