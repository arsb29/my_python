import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label = tkinter.Label(self.top_frame,
                             text='',justify='left')

        self.label.pack(side='left')

        self.my_button = tkinter.Button(self.bottom_frame,
                                        text='Показать инфо',
                                command=self.do_something)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                    text='Выйти',
                                    command=self.main_window.destroy)
        self.my_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def do_something(self):
        self.label.config(text='Стивен Маркус\n274 Бейли\nУэйнзвилль, Северная Каролина 27999')

my_gui = MyGUI()
