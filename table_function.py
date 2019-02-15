value = input("Введите атомный номер элемента: ")
if value:
    z = float(value)
    if z == 3.0:
        print("Li")
    elif z == 25.0:
        print("Mn")
    elif z == 80.0:
        print("Hg")
    elif z == 17.0:
        print("Cl")
    else:
        print("Что это?!")
else:
    print("Введите атомный номер!")
