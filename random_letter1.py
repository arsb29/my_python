from random import choice
s = ['весна','лето','самовар']
k = choice(s)
l = list(k)
u = choice(l)
n = l.index(u)
l[n] = '?'
n = ''.join(l)
print(n)
m = input('Введите букву: ')
if m == u:
    print('Победа!\nСлово:',k)
else:
    print('Увы! Попробуйте в другой раз.\nСлово:',k)
