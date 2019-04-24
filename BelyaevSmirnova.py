import tkinter,math

def click():
    try:
        label4.config(text=round(4/3*math.pi*float(entry1.get())**3,2))
    except ValueError as er:
        label4.config(text="Error")

def save():
    s="Радиус сферы: "+entry1.get()+". Результат вычислений: "+str(label4.cget("text"))
    if variable.get()=="Текст":
        my_file = open("result.txt", "w")
        my_file.write(s)
        my_file.close()
    else:
        aa = ["<!DOCTYPE html>","<head>","<meta charset="'sp1251'">","<title>Вычисление объема сферы</title>"," <link rel=""stylesheet"" type=""text/css"" href=""style.css"">" ,"<script src=""script.js""></script>", "</head>","<body>",s,"</body>","</html>"]
        with open("result.html", "w") as file:
            for  line in aa:
                file.write(line + '\n')

window = tkinter.Tk()

window.title('Программа для вычисления объема сферы')

frame = tkinter.Frame(window)
frame.grid()

label1=tkinter.Label(frame, text = "Программа для вычислений объема сферы")
label1.grid(row=0,column=0,columnspan=2)

label2 = tkinter.Label(frame, text = "Введите радиус:")
label2.grid(row=1,column=0)

label3 = tkinter.Label(frame, text = "Результат вычислений:")
label3.grid(row=2,column=0)

entry1= tkinter.Entry(frame)
entry1.grid(row=1,column=1)

label4= tkinter.Label(frame)
label4.grid(row=2,column=1)

button = tkinter.Button(frame, text="Вычислить",command = click)
button.grid(row=3,column=0,columnspan=2)

button1=tkinter.Button(frame, text = "Сохранить как", command = save)
button1.grid()

variable = tkinter.StringVar(frame)
variable.set("Текст") 

w = tkinter.OptionMenu(frame, variable, "Текст", "HTML")
w.grid(row=4,column=1)

window.mainloop()
