from math import sin
n=float(input('Введите число: '))
if 0.2<=n<=0.9:
    print('f=',round(sin(n),2))
else:
    print('f=',1)
