import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label = tkinter.Label(self.top_frame,
                             text='')

        self.label.pack(side='left')

        self.l_button = tkinter.Button(self.bottom_frame,
                                        text='Left',
                                command=self.do_l)
        self.c_button = tkinter.Button(self.bottom_frame,
                                    text='Centr',
                                    command=self.do_c)
        self.r_button = tkinter.Button(self.bottom_frame,
                                    text='Right',
                                    command=self.do_r)
        
        self.l_button.pack(side='left')
        self.c_button.pack(side='left')
        self.r_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def do_l(self):
        self.label.config(text='Left')

    def do_c(self):
        self.label.config(text='Centr')

    def do_r(self):
        self.label.config(text='Right')

my_gui = MyGUI()
