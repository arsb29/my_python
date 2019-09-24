import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Замена масла - $30.00',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Смазочные работы - $20.00',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Промывка радиатора - $40.00',
                                       variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame,
                                       text='Замена жидкости в трансмиссии - $100.00',
                                       variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame,
                                       text='Осмотр - $35.00',
                                       variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame,
                                       text='Замена глушителя выхлопа - $200.00',
                                       variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame,
                                       text='Перестановка шин - $20.00',
                                       variable=self.cb_var7)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='Показать стоимость',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                 command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()
    def show_choice(self):

        mm = 0

        if self.cb_var1.get() == 1:
            mm+=30
        if self.cb_var2.get() == 1:
            mm+=20
        if self.cb_var3.get() == 1:
            mm+=40
        if self.cb_var4.get() == 1:
            mm+=100
        if self.cb_var5.get() == 1:
            mm+=35
        if self.cb_var6.get() == 1:
            mm+=200
        if self.cb_var7.get() == 1:
            mm+=20
        

        tkinter.messagebox.showinfo('Общая стоимость', f"Ваши затраты: $ {mm}")

my_gui = MyGUI()