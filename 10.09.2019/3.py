import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.m_frame = tkinter.Frame(self.main_window)
        self.m2_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.g_label = tkinter.Label(self.top_frame,
                             text='Введите количество галлонов:')
        self.g_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        self.g_label.pack(side='left')
        self.g_entry.pack()
        
        self.m_label = tkinter.Label(self.m_frame,
                             text='Введите количество миль:')
        self.m_entry = tkinter.Entry(self.m_frame,
                                        width=10)

        self.m_label.pack(side='left')
        self.m_entry.pack()

        self.label = tkinter.Label(self.m2_frame,text='Мили на галлон (MPG)=')
        self.label.pack()

        self.calc_button = tkinter.Button(self.bottom_frame,
                                    text='Вычислить MPG',
                                    command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                    text='Выйти',
                                    command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.m_frame.pack()
        self.m2_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):

        g = float(self.g_entry.get())
        m = float(self.m_entry.get())

        mm = m/g

        self.label.config(text=f"Мили на галлон (MPG)={mm}")

my_GUI = MyGUI()
