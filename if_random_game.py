from random import randint
k=randint(1,4)
n=int(input('Введите число от 1 до 4: '))
if n!=k:
    while n!=k:
        print('Вы проиграли!')
        if n>k:
            print('Загаданное число меньше')
        else:
            print('Загаданное число больше')
        n=int(input('Попробуйте еще раз: '))
print('Победа!')
