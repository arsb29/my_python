s='У лукоморья 123 дуб зеленый 456'
print('Индекс буквы Я, если нет, то -1: ',s.find('я'))
print('Количесвто букв У: ',s.count('у'))
if s.isalpha():
    'Строка состоит из букв'
else:
    print(s.upper())
if len(s)>4:
    print(s.lower())
s='О'+s[1:]
print(s)
