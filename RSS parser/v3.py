import sqlite3, requests, os, vk_api, feedparser
import tkinter as tk
from tkinter import ttk, WORD
from PIL import ImageTk, Image
from datetime import datetime

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg = '#d7d8e0', bd = 2)
        toolbar.pack(side = tk.TOP, fill = tk.X)

        self.parser_img = ImageTk.PhotoImage(Image.open("images/parser.jpg"))
        btn_parser_dialog = tk.Button(toolbar,text = 'Парсить', command = self.open_parser_dialog,
                                    bg = '#d7d8e0', bd = 0, compound = tk.TOP, image = self.parser_img)
        btn_parser_dialog.pack(side = tk.LEFT)
        
        self.tree = ttk.Treeview(self, columns = ('ID', 'description', 'image_url', 'date'),
                                 height = 15, show = 'headings')

        self.tree.column("ID", width = 30, anchor = tk.CENTER)
        self.tree.column("description", width = 350, anchor = tk.CENTER)
        self.tree.column("image_url", width = 150, anchor = tk.CENTER)
        self.tree.column("date", width = 100, anchor = tk.CENTER)
        
        self.tree.heading("ID", text = 'ID')
        self.tree.heading("description", text = 'Описание')
        self.tree.heading("image_url", text = 'Изображение')
        self.tree.heading("date", text = 'Дата')

        self.tree.pack(side = 'left')

        self.tree.bind('<Double-1>',self.OnDoubleClick)
        

        self.scroll_tree_y = ttk.Scrollbar(self, orient = "vertical", command = self.tree.yview)
        self.scroll_tree_y.pack(side = 'left', fill = 'y')

        self.tree.configure(yscrollcommand = self.scroll_tree_y.set)
        
    def OnDoubleClick(self, event):
        item = self.tree.identify('item',event.x,event.y)
        self.open_update_dialog()

    def open_update_dialog(self):
        if len(self.tree.selection()) != 0:
            Update()

    def open_parser_dialog(self):
        Parser()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM posts''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values = row) for row in self.db.c.fetchall()]

    def view_one_record(self):
        a, a1, a2 = '', '', ''
        num = self.tree.item(self.tree.selection()[0])['values'][0]
        self.db.c.execute('''SELECT description FROM posts WHERE ID=?''',(num,))
        a = self.db.c.fetchone()[0]
        self.db.c.execute('''SELECT image_url FROM posts WHERE ID=?''',(num,))
        a1 = self.db.c.fetchone()
        self.db.c.execute('''SELECT date FROM posts WHERE ID=?''',(num,))
        a2 = self.db.c.fetchone()
        
        return(a, a1, a2)

    def records(self, description, image_url, date):
        self.db.insert_data(description, image_url, date)
        self.view_records()
        
    def update_record(self, description, image_url, date):
        self.db.c.execute('''UPDATE posts SET description=?, image_url=?, date=? WHERE ID=?''',
                              (description, image_url, date, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        focus = self.tree.get_children().index(self.tree.selection()[0])
        self.view_records()
        self.tree.selection_set(self.tree.get_children()[focus])

    def parser_records(self, posts):
        self.db.insert_parser_data(posts)
        self.view_records()

    def save_photo(self, num, photo):
        with open('photos/'+str(num)+'.jpg','wb') as fout:
            fout.write(photo)

                         
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить новость')
        self.geometry('600x400+400+300')
        self.resizable(False, False)

        self.img = Image.open("images/no.jpg")
        self.img.thumbnail((250,250))
        self.render = ImageTk.PhotoImage(self.img)
        self.label_img = ttk.Label(self, image = self.render)
        self.label_img.place(x = 300, y = 10)

        self.label_description = ttk.Label(self, text = 'Описание')
        self.label_description.place(x = 30, y = 190)

        self.label_image_url = ttk.Label(self, text = 'Изображение')
        self.label_image_url.place(x = 30, y = 130)

        self.label_date = ttk.Label(self, text = 'Дата')
        self.label_date.place(x = 30, y = 160)

        self.entry_description = tk.Text(self, width = 50, height = 9, wrap = WORD)
        self.entry_description.place(x = 150, y = 190)

        self.scroll_description = ttk.Scrollbar(self.entry_description, orient = "vertical", command = self.entry_description.yview)
        self.scroll_description.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        self.entry_description.configure(yscrollcommand = self.scroll_description.set)

        self.entry_image_url = ttk.Entry(self)
        self.entry_image_url.place(x = 150, y = 130)
        
        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x = 150, y = 160)


        btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        btn_cancel.place(x = 500, y = 360)

        self.btn_ok = ttk.Button(self, text = 'Добавить')
        self.btn_ok.place(x = 410, y = 360)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(1.0, 'end'),
                                                                  self.entry_image_url.get(),
                                                                  self.entry_date.get()))
        #self.btn_ok.bind('<Return>', lambda event: self.view.records(self.entry_description.get(1.0, END),
         #                                                         self.entry_image_url.get(),
            #                                                      self.entry_date.get()))

        
        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
       

    def init_edit(self):
        self.title('Просмотр')


        response = self.view.view_one_record()
        self.entry_description.insert(1.0, response[0])
        self.entry_image_url.insert(0, response[1])
        self.entry_date.insert(0, response[2])
        if self.view.tree.item(self.view.tree.selection()[0])['values'][2] != 'pass':
            self.img2 = Image.open("photos/" + str(self.view.tree.item(self.view.tree.selection()[0])['values'][0]) + ".jpg")
            self.img2.thumbnail((250,250))
            self.render2 = ImageTk.PhotoImage(self.img2)
            self.label_img.configure(image = self.render2)
            self.label_img.image = self.render2
        
        self.btn_ok.destroy()


class Parser(Child):
    def __init__(self):
        super().__init__()
        self.init_parser()
        self.view = app

    def init_parser(self):
        self.title('Парсить посты')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_source = tk.Label(self, text = 'Источник')
        label_source.place(x = 50, y = 50)

        self.combobox = ttk.Combobox(self, value = [u'Группа ВКонтакте', u'RSS лента'])
        self.combobox.current(0)
        self.combobox.place(x = 200, y = 80)

        
        self.entry_source = ttk.Entry(self)
        self.entry_source.place(x = 200, y = 50)

        btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        btn_cancel.place(x = 300, y = 170)

        self.btn_parser = ttk.Button(self, text = 'Парсить')
        self.btn_parser.place(x = 220, y = 170)
        self.btn_parser.bind('<Button-1>', lambda event: self.view.parser_records(self.parser()))


        self.label_date.destroy()
        self.btn_ok.destroy()
        self.entry_date.destroy()
        self.entry_image_url.destroy()
        self.entry_description.destroy()
        self.label_image_url.destroy()
        self.label_description.destroy()
        self.label_img.destroy()
        

    def parser(self):
        if self.combobox.get() == 'Группа ВКонтакте':
            return self.get_info(self.entry_source.get())
        else:
            return self.rss_parser(self.entry_source.get())
    

    def group(self,iterable, count):
        return zip(*[iter(iterable)] * count)   

    def rss_parser(self, href):
        all_posts = []
        d = feedparser.parse(href)
        now = int(datetime.now().timestamp()) + 86400
        if len(self.view.tree.get_children()) > 0:
            num = self.view.tree.item(self.view.tree.get_children()[-1])['values'][0]
        else:
            num = 1
        for i in range(10):
            img = d.entries[i]['links'][1]['href']
            photo = requests.get(img, stream=True).content
            self.view.save_photo(num, photo)
            all_posts.extend(list((d.entries[i].description, img, now)))
            now += 3600
            num += 1
        return list(self.group(all_posts, 3))

    def get_info(self, group_id):
        
        vk_session = vk_api.VkApi('','')
        vk_session.auth()
 
        vk = vk_session.get_api()

        response = vk.wall.get(domain = group_id, count = '10')['items']
        all_posts = []
        now = int(datetime.now().timestamp()) + 86400 
        img = 'pass'
        if len(self.view.tree.get_children()) > 0:
            num = self.view.tree.item(self.view.tree.get_children()[-1])['values'][0]
        else:
            num = 1
        for post in response:
            try:
                if post['attachments'][0]['photo']: #если фото есть
                    img = post['attachments'][0]['photo']['sizes'][-1]['url']
                    photo = requests.get(img, stream=True).content
                    self.view.save_photo(num, photo)
                    
                else:
                    img = 'pass'
            except:
                img = 'pass'
                pass
            all_posts.extend(list((post['text'], img, now)))
            now += 3600
            num += 1
        return list(self.group(all_posts, 3))
        
        
                      
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('posts.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS posts (id integer primary key, description text, image_url text, date integers)''')
        self.conn.commit()

    def insert_data(self, description, image_url, date):
        self.c.execute('''INSERT INTO posts(description, image_url, date) VALUES (?, ?, ?)''',
                     (description, image_url, date))
        self.conn.commit()

    def insert_parser_data(self, posts):
        self.c.executemany('''INSERT INTO posts(description, image_url, date) VALUES (?, ?, ?)''',posts)
        self.conn.commit()
     

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Parser 3.0")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
