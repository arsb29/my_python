from pprint import pprint
tasks = []

print('Простой todo:\n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.\n')
n = int(input('Укажите число: '))

  
while n != 3:
    if n == 1:
        z = input('Сформулируйте задачу: ')
        k = input('Добавьте категорию к задаче: ')
        v = input('Добавьте время к задаче: ')
        e1 = {'name':z, 'category':k, 'time':v}
        tasks.append(e1)
    if n == 2:
        for i in tasks:
            print('Задача: ',i['name'])
            print('Категория: ',i['category'])
            print('Дата: ',i['time'])
    print('Простой todo:\n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.\n')
    n=int(input('Укажите число: '))
