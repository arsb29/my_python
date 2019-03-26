def ff(x,y,z):
            x=float(x)
            y=float(y)
            if z=="+":
                return x+y
            elif z=="-":
                return x-y
            elif z=="*":
                return x*y
            elif z=="/":
                return x/y

a=input("Введите первое число: ")
b=input("Введите второе число: ")
c=input("Операнд: ")


try:
    ff(a,b,c)
except ValueError:
    print("Error! Ошибка в формате")
except ZeroDivisionError:
    print("Error! Деление на ноль")
else:
    print(1)
finally:
    print(ff(a,b,c))
