import tkinter, random

def click():
    if entry.get()==dic[rr]:
        label.config(text="Угадали!")
    else:
        label.config(text="Неправильно")

dic={"dog":"собака","cat":"кошка","fish":"рыба"}

rr = random.choice(list(dic.keys()))

window = tkinter.Tk()

window.title('Перевод в градусы по Фаренгейту')

frame = tkinter.Frame(window)
frame.pack()

label1=tkinter.Label(frame, text = "Случайное слово")
label1.pack

label2 = tkinter.Label(frame, text = rr)
label2.pack()

entry = tkinter.Entry(frame)
entry.pack()

label = tkinter.Label(frame)
label.pack()

button = tkinter.Button(frame, text="Готово!",command = click)
button.pack()

button1=tkinter.Button(frame, text = "Выход", command = window.destroy)
button1.pack()

window.mainloop()
