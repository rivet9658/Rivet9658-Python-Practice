#買書問題
a = int(input())
b = int(input())
c = int(input())
total = 0

#A的計算
if a <= 10:
    total += 380*a
elif a >= 11 and a <= 20:
    total += (380*a)*0.9
elif a >= 21 and a <=30:
    total += (380*a)*0.85
elif a >= 31:
    total += (380*a)*0.8

#B的計算
if b <= 10:
    total += 1200*b
elif b >= 11 and b <= 20:
    total += (1200*b)*0.95
elif b >= 21 and b <=30:
    total += (1200*b)*0.85
elif b >= 31:
    total += (1200*b)*0.8

#C的計算
if c <= 10:
    total += 180*c
elif c >= 11 and c <= 20:
    total += (180*c)*0.85
elif c >= 21 and c <=30:
    total += (180*c)*0.8
elif c >= 31:
    total += (180*c)*0.7

print(total)