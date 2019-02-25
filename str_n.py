a=input('Введите строку: ')
b=int(input('Введите число: '))
def str_n(s,n):
    if len(s)>n:
        return s.upper()
    else:
        return s
print(str_n(a,b))
