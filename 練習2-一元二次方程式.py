#一元二次方程式，求實根

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

k = b**2-(4*a*c)

if k > 0:
    x1 = (-b + k**0.5)/(2*a)
    x2 = (-b - k**0.5)/(2*a)
    print(x1)
    print(x2)
elif k == 0:
    x1 = -b/(2*a)
    x2 = x1
    print(x1)
    print(x2)
else:
    print("無解")