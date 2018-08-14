import tkinter as tk
import sqlite3
import tkinter.messagebox
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)
conn = sqlite3.connect('lib.db')
c = conn.cursor()

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PubAdd, PubView, PubUpdate, BookAdd, BookView, StudentAdd):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Add Publisher",
                            command=lambda: controller.show_frame(PubAdd))
        button.pack()

        button2 = tk.Button(self, text="View Publisher",
                            command=lambda: controller.show_frame(PubView))
        button2.pack()

        button3 = tk.Button(self, text="Update Publisher",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.pack()

        button4 = tk.Button(self, text="Add Book",
                            command=lambda: controller.show_frame(BookAdd))
        button4.pack()

        button5 = tk.Button(self, text="View Book",
                            command=lambda: controller.show_frame(BookView))
        button5.pack()

        button5 = tk.Button(self, text="Add Student",
                            command=lambda: controller.show_frame(StudentAdd))
        button5.pack()

class PubAdd(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        heading = tk.Label(self, text="Add Publisher", font=('arial 40 bold'), fg='blue')
        heading.place(x=400,y=0)

        # self.i = Label(master, text="ID is reached upto: " +str(id), font=('arial 18 bold'))
        # self.i.place(x=10, y=40)
        #label for windows
        name_l = tk.Label(self, text="Enter Publisher", font=('arial 18 bold'))
        name_l.place(x=10, y=70)

        address_l = tk.Label(self, text="Enter Publisher Address", font=('arial 18 bold'))
        address_l.place(x=10, y=120)

        # entry
        self.name_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.name_e.place(x=270, y=70)

        self.address_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.address_e.place(x=270, y=120)

        #button to add to database
        btn_add = tk.Button(self, text="Add publisher", width=25, height=2, bg="steelblue", fg="white", command=self.get_items)
        btn_add.place(x=370, y=370)

        # text box
        # self.tBox = Text(master, width=60, height=17)
        # self.tBox.place(x=720, y=70)
        # self.tBox.insert(END, "ID has reached upto: " +str(id))

        #btn clear
        btn_clear = tk.Button(self, text="Clear all fields", width=18, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        btn_clear.place(x=358, y = 420)

        button1 = tk.Button(self, text="Main Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=1150, y=70)

        button2 = tk.Button(self, text="View Publisher",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=1150, y=110)
        
    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, tk.END)
        self.address_e.delete(0, tk.END)
        
    #get method
    def get_items(self, *args, **kwargs):

        #get from entries
        self.pub_name = self.name_e.get()
        self.address = self.address_e.get()

        if self.pub_name == '' and self.address == '':
            tkinter.messagebox.showinfo("Error","Please fill the entries")
        else:
            
            sql = "insert into publisher (pub_name, address) values (?,?)"
            c.execute(sql, (self.pub_name, self.address))
            conn.commit()
            
            tkinter.messagebox.showinfo("Success", "Successfully publisher added!")


        


class PubView(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        button1 = tk.Button(self, text="Main Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=1150, y=70)

        button2 = tk.Button(self, text="Add Publisher",
                            command=lambda: controller.show_frame(PubAdd))
        button2.place(x=1150, y=110)

        self.heading = tk.Label(self, text="View Publisher", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        tree = ttk.Treeview(self,height=20, columns=3)
        tree.place(x=100, y=200)
        tree["column"]=('1','2','3')
        tree.heading('1',text="pub_id", anchor=tk.W)
        tree.heading('2',text="Publisher Name", anchor=tk.W) 
        tree.heading('3', text="Adderss", anchor=tk.W)

        items = tree.get_children()
        for item in items:
            tree.delete(item)
        query = 'select * from publisher'
        entries = self.execute_db_query(query)
        for row in entries:
            tree.insert('',tk.END,values=row)

    def execute_db_query(self, query, parameters=()):
        with sqlite3.connect('lib.db') as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result


class PubUpdate(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.heading = tk.Label(self, text="Update Publisher", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        self.id_l = tk.Label(self, text="Enter ID", font=('arial 18 bold'))
        self.id_l.place(x=0, y=0)

        self.id_e = tk.Entry(self, font=('arial 18 bold'), width=10)
        self.id_e.place(x=300, y=0)

        self.btn_search = tk.Button(self, text="Search", width=15, height=2, bg='brown', command=self.search)
        self.btn_search.place(x=550, y=70)

        self.name_l = tk.Label(self, text="Enter Publisher", font=('arial 18 bold'))
        self.name_l.place(x=10, y=120)

        self.address_l = tk.Label(self, text="Enter Publisher Address", font=('arial 18 bold'))
        self.address_l.place(x=10, y=170)

        # entry
        self.name_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.name_e.place(x=380, y=120)

        self.address_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.address_e.place(x=380, y=170)

        #button to add to database
        self.btn_update = tk.Button(self, text="Update publisher", width=25, height=2, bg="steelblue", fg="white", command=self.update)
        self.btn_update.place(x=370, y=370)

        #btn clear
        self.btn_clear = tk.Button(self, text="Clear all fields", width=18, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=358, y = 420)

        
    def clear_all(self, *args, **kwargs):
        self.id_e.delete(0, tk.END)
        self.name_e.delete(0, tk.END)
        self.address_e.delete(0, tk.END)
        
    #get method
    def search(self, *args, **kwargs):
        sql = "select * from publisher where pub_id = ?"
        result = c.execute(sql,(self.id_e.get()))

        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
        conn.commit()

        self.name_e.delete(0,tk.END)
        self.name_e.insert(0, str(self.n1))

        self.address_e.delete(0,tk.END)
        self.address_e.insert(0, str(self.n2))

    def update(self, *args, **kwargs):
        self.u1 = self.name_e.get()
        self.u2 = self.address_e.get()

        query = "update publisher set pub_name=?, address=? where pub_id=?"
        c.execute(query, (self.u1, self.u2, self.id_e.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Publisher updated")


class BookAdd(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.heading = tk.Label(self, text="Add Book", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        c.execute("CREATE TABLE IF NOT EXISTS book (book_id INTEGER PRIMARY KEY AUTOINCREMENT, book_name TEXT NOT NULL, num_book INTEGER NOT NULL, pub_id INTEGER NOT NULL, FOREIGN KEY(pub_id) REFERENCES publisher(pub_id) ON UPDATE CASCADE)")
        # conn.commit()

        #label for windows
        self.name_l = tk.Label(self, text="Enter Book Name", font=('arial 18 bold'))
        self.name_l.place(x=10, y=70)

        self.num_book_l = tk.Label(self, text="Enter No. of Books", font=('arial 18 bold'))
        self.num_book_l.place(x=10, y=120)

        self.pub_id_l = tk.Label(self, text="Enter Publisher ID", font=('arial 18 bold'))
        self.pub_id_l.place(x=10, y=170)


        # entry
        self.name_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.name_e.place(x=270, y=70)

        self.num_book_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.num_book_e.place(x=270, y=120)

        self.pub_id_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.pub_id_e.place(x=270, y=170)

        #button to add to database
        self.btn_add = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white", command=self.get_items)
        self.btn_add.place(x=370, y=370)

        #btn clear
        self.btn_clear = tk.Button(self, text="Clear all fields", width=18, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=358, y = 420)
 
    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, tk.END)
        self.num_book_e.delete(0, tk.END)
        self.pub_id_e.delete(0, tk.END)
        
    #get method
    def get_items(self, *args, **kwargs):

        #get from entries
        self.book_name = self.name_e.get()
        self.num_book = self.num_book_e.get()
        self.pub_id = self.pub_id_e.get()

        if self.book_name == '' and self.num_book == '' and self.pub_id == '':
            tkinter.messagebox.showinfo("Error","Please fill the entries")
        else:
            
            sql = "insert into book (book_name, num_book, pub_id) values (?,?,?)"
            c.execute(sql, (self.book_name, self.num_book, self.pub_id))
            conn.commit()
            
            tkinter.messagebox.showinfo("Success", "Successfully book added!")


class BookView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.heading = tk.Label(self, text="View Books", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        
   
        
        self.tree = ttk.Treeview(self, height=20, columns=3)
        self.tree.place(x=10, y=200)
        self.tree["column"]=('1','2','3','4','5','6')
        self.tree.heading('1',text="Book_id", anchor=tk.W)
        self.tree.heading('2',text="Pub_id", anchor=tk.W) 
        self.tree.heading('3', text="Book_name", anchor=tk.W)
        self.tree.heading('4', text="Pub_name", anchor=tk.W)
        self.tree.heading('5', text="Adderss", anchor=tk.W)
        self.tree.heading('6', text="num_book", anchor=tk.W)


        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        query = 'select book.book_id, publisher.pub_id, book.book_name, publisher.pub_name, publisher.address, book.num_book from book inner join publisher on book.pub_id = publisher.pub_id'
        entries = self.execute_db_query(query)
        for row in entries:
            self.tree.insert('',tk.END,values=row)

    def execute_db_query(self, query, parameters=()):
        with sqlite3.connect('lib.db') as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result


class StudentAdd(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.heading = tk.Label(self, text="Add Student", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        c.execute("CREATE TABLE IF NOT EXISTS student (roll INTEGER PRIMARY KEY, st_name TEXT NOT NULL, faculty TEXT NOT NULL, CONSTRAINT roll_unique UNIQUE (roll))")

        #label for windows
        self.roll_l = tk.Label(self, text="Enter Roll No.", font=('arial 18 bold'))
        self.roll_l.place(x=10, y=70)

        self.st_name_l = tk.Label(self, text="Enter Student Name", font=('arial 18 bold'))
        self.st_name_l.place(x=10, y=120)

        self.faculty_l = tk.Label(self, text="Enter Faculty", font=('arial 18 bold'))
        self.faculty_l.place(x=10, y=170)


        # entry
        self.roll_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.roll_e.place(x=270, y=70)

        self.st_name_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.st_name_e.place(x=270, y=120)

        self.faculty_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.faculty_e.place(x=270, y=170)

        #button to add to database
        self.btn_add = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white", command=self.get_items)
        self.btn_add.place(x=370, y=370)

        #btn clear
        self.btn_clear = tk.Button(self, text="Clear all fields", width=18, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=358, y = 420)
 
    def clear_all(self, *args, **kwargs):
        self.roll_e.delete(0, tk.END)
        self.st_name_e.delete(0, tk.END)
        self.faculty_e.delete(0, tk.END)
        
    #get method
    def get_items(self, *args, **kwargs):

        #get from entries
        self.roll = self.roll_e.get()
        self.st_name = self.st_name_e.get()
        self.faculty = self.faculty_e.get()

        if self.roll == '' and self.st_name == '' and self.faculty == '':
            tkinter.messagebox.showinfo("Error","Please fill the entries")
        else:
            try:
                sql = "insert into student (roll, st_name, faculty) values (?,?,?)"
                c.execute(sql, (self.roll, self.st_name, self.faculty))
                conn.commit()
                
                tkinter.messagebox.showinfo("Success", "Successfully Student Added!")
            except sqlite3.IntegrityError: 
                tkinter.messagebox.showerror("Error","Check roll no once again!!!")

app = SeaofBTCapp()
app.geometry('1366x768+0+0')
app.mainloop()

