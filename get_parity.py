a = int(input('Введите число:\n'))
def part(x):
    if x%2 == 0:
        return 'Число четное'
    else:
        return 'Число нечетное'
print(part(a))
