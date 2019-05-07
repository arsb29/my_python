from tkinter import *
import json

root=Tk()
root.geometry('675x165')
root.title('Менеджер задач')
root.resizable(width='FALSE',height='FALSE')

frame=Frame(root)
frame.grid()

with open('tasks.json', 'w') as f_obj:
    json.dump([], f_obj)

##########################

def write_to_json(task, category, time):
    with open('tasks.json','r') as jfr:
        jf_file = json.load(jfr)
    with open('tasks.json','w') as jf:
        user_info = {'Задача': task, 'Категория': category, 'Время': time}
        jf_file.append(user_info)
        json.dump(jf_file, jf)

def reader(filename):
    '''
    Чтение содержимого json файла 
    '''
    import json    
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e

def a1(event):
    task.delete(0,END)

def a2(event):
    category.delete(0,END)

def a3(event):
    time.delete(0,END)

def fadd():
    global tasks
    t=task.get()
    c=category.get()
    v=time.get()
    write_to_json(t,c,v)
    
def flst():
    result.delete('1.0',END)
    r=reader('tasks.json')
    for i in r:
            result.insert(END,'Задача: '+i['Задача']+' Категория: '+i['Категория']+' Время: '+i['Время']+'\n')
    
##########################

texttask=Label(frame,text='Задача:')
texttask.grid(row=1,column=1)

textcategory=Label(frame,text='Категория:')
textcategory.grid(row=2,column=1)

texttime=Label(frame,text='Время:')
texttime.grid(row=3,column=1)

text1=Label(frame,text='',width=0)
text1.grid(row=1,column=3)

task=Entry(frame,width=20)
task.grid(row=1,column=2)
task.insert(1,'Введите задачу')

category=Entry(frame,width=20)
category.grid(row=2,column=2)
category.insert(1,'Введите категорию')

time=Entry(frame,width=20)
time.grid(row=3,column=2)
time.insert(1,'Введите время')

add=Button(frame,text='Добавить',command=fadd)
add.grid(row=4,column=1,columnspan=2)

lst=Button(frame,text='Список задач',command=flst)
lst.grid(row=5,column=1,columnspan=2)

ex=Button(frame,text='Выход',command = root.destroy)
ex.grid(row=6,column=1,columnspan=2)

result=Text(frame,width=57,height=10)
result.grid(row=1,column=4,rowspan=6)
 
scroll = Scrollbar(frame,command=result.yview)
scroll.grid(row=1,column=6,rowspan=6,sticky='NS')
 
result.config(yscrollcommand=scroll.set)

##########################

task.bind('<Button-1>',a1)
category.bind('<Button-1>',a2)
time.bind('<Button-1>',a3)

root.mainloop()
