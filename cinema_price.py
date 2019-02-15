film = input('Выберите фильм: ')
date = input('Выберите день (сегодня,завтра): ')
time = int(input('Выберите время: '))
num = int(input('Выберите количество билетов: '))

a = 1
sk1 = 1
sk2 = 1
bilet = 0

if num > 19:
    sk1 = 0.8
if date == 'завтра':
    sk2 = 0.95
elif date != 'сегодня':
        a = 0

if film == 'Пятница':
    if time == 12:
        bilet = 250
    elif time == 16:
        bilet = 350
    elif time == 20:
        bilet = 450
    else:
        a = 0
elif film == 'Чемпионы':
    if time == 10:
        bilet = 250
    elif time == 13:
        bilet = 350
    elif time == 16:
        bilet = 350
    else:
        a = 0
elif film == 'Пернатая банда':
    if time == 10:
        bilet = 350
    elif time == 14:
        bilet = 450
    elif time == 18:
        bilet = 450
    else:
        a = 0
else:
    a = 0

if a == 1:
    print('Фильм:',film,'День: ',date,'Время: ',time,'Количество билетов: ',num,'\nСтоимость: ',num*bilet*sk1*sk2,'руб.')
else:
    print('Ошибка ввода')
    
