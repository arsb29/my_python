kod = int(input('Введите код города:\n'))
t = float(input('Введите длительность переговоров в секундах:\n'))
if kod == 343:
    print('Город-Екатеринбург. Код: ',kod,'\nТариф: 15 руб/мин. Стоимость разговора:',t*(15/60),' руб.')
elif kod == 381:
    print('Город-Омск. Код: ',kod,'\nТариф: 18 руб/мин. Стоимость разговора:',t*(18/60),' руб.')
elif kod == 473:
    print('Город-Воронеж. Код: ',kod,'\nТариф: 13 руб/мин. Стоимость разговора:',t*(13/60),' руб.')
elif kod == 485:
    print('Город-Ярославль. Код: ',kod,'\nТариф: 11 руб/мин. Стоимость разговора:',t*(11/60),' руб.')
else:
    print('Ошибка ввода')
