import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.center_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Дневное время (6:00-17:59)',
                                       variable=self.radio_var,
                                       value=10)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Вечернее время (18:00-23:59)',
                                       variable=self.radio_var,
                                       value=12)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Непиковый период (00:00-5:59)',
                                       variable=self.radio_var,
                                       value=5)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()


        self.label = tkinter.Label(self.center_frame,
                             text='Введите количество минут:')
        self.entry = tkinter.Entry(self.center_frame,width=10)

        self.label.pack(side='left')
        self.entry.pack(side='left')


        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='Показать стоимость',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.center_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


    def show_choice(self):
        tkinter.messagebox.showinfo('Общая стоимость', 'Ваши затраты = $' +
                                    str((self.radio_var.get()*int(self.entry.get())/100)))

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()
