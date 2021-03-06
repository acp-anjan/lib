import tkinter as tk
import sqlite3
import tkinter.messagebox
from tkinter import ttk
import time
import datetime

LARGE_FONT= ("Verdana", 12)

conn = sqlite3.connect('lib.db')
c = conn.cursor()

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        conn = sqlite3.connect('lib.db')
        c = conn.cursor()

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        refresh = tk.Button(container, text='Refresh', command = container.update())
        refresh.grid(row=2, column=0, sticky=tk.W)

        self.frames = {}

        for F in (StartPage, PubAdd, PubView, PubUpdate, BookAdd, BookView, StudentAdd, IssueBook, ViewIssue, Return):

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
        frame = tk.Frame(self, borderwidth=5)
        refresh = tk.Button(frame, text='Refresh', command = frame.update())
        refresh.grid(row=2, column=0, sticky=tk.W)
        conn = sqlite3.connect('lib.db')
        c = conn.cursor()

        label = tk.Label(self, text="Menu", font=('arial 40 bold'), fg='brown')
        label.pack(pady=10,padx=10)     

        photo = tk.PhotoImage(file='lib1.png')
        label = tk.Label(self,image=photo)
        label.image = photo
        label.place(x=250, y=150)


        button = tk.Button(self, text="Add Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubAdd))
        button.place(x=1000, y= 70)

        button2 = tk.Button(self, text="View Publisher",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=1000, y= 120)

        button3 = tk.Button(self, text="Update Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.place(x=1000, y= 170)

        button4 = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookAdd))
        button4.place(x=1000, y= 220)

        button5 = tk.Button(self, text="View Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookView))
        button5.place(x=1000, y= 270)

        button6 = tk.Button(self, text="Add Student", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StudentAdd))
        button6.place(x=1000, y= 320)

        button7 = tk.Button(self, text="Issue Book",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(IssueBook))
        button7.place(x=1000, y= 370)

        button8 = tk.Button(self, text="View Issues", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(ViewIssue))
        button8.place(x=1000, y= 420)

        button9 = tk.Button(self, text="Return Books", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(Return))
        button9.place(x=1000, y= 470)

        button10 = tk.Button(self, text="Home", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button10.place(x=1000, y= 520)

        refresh = tk.Button(frame, text='Refresh', command = frame.update())
        refresh.grid(row=2, column=0, sticky=tk.W)

        conn.close()

class PubAdd(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = tk.Frame(self, borderwidth=5)
        refresh = tk.Button(frame, text='Refresh', command = frame.update())
        refresh.grid(row=2, column=0, sticky=tk.W)
        conn = sqlite3.connect('lib.db')
        c = conn.cursor()

        heading = tk.Label(self, text="Add Publisher", font=('arial 40 bold'), fg='blue')
        heading.place(x=400,y=0)

        #label for windows
        name_l = tk.Label(self, text="Enter Publisher", font=('arial 18 bold'))
        name_l.place(x=10, y=70)

        address_l = tk.Label(self, text="Enter Publisher Address", font=('arial 18 bold'))
        address_l.place(x=10, y=120)

        # entry
        self.name_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.name_e.place(x=350, y=70)

        self.address_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.address_e.place(x=350, y=120)

        #button to add to database
        btn_add = tk.Button(self, text="Add publisher", width=25, height=2, bg="purple1", fg="white", command=self.get_items)
        btn_add.place(x=350, y=170)

        #btn clear
        btn_clear = tk.Button(self, text="Clear all fields", width=25, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        btn_clear.place(x=350, y = 220)

        button = tk.Button(self, text="Add Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubAdd))
        button.place(x=1000, y= 70)

        button2 = tk.Button(self, text="View Publisher",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=1000, y= 120)

        button3 = tk.Button(self, text="Update Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.place(x=1000, y= 170)

        button4 = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookAdd))
        button4.place(x=1000, y= 220)

        button5 = tk.Button(self, text="View Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookView))
        button5.place(x=1000, y= 270)

        button6 = tk.Button(self, text="Add Student", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StudentAdd))
        button6.place(x=1000, y= 320)

        button7 = tk.Button(self, text="Issue Book",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(IssueBook))
        button7.place(x=1000, y= 370)

        button8 = tk.Button(self, text="View Issues", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(ViewIssue))
        button8.place(x=1000, y= 420)

        button9 = tk.Button(self, text="Return Books", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(Return))
        button9.place(x=1000, y= 470)

        button10 = tk.Button(self, text="Home", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button10.place(x=1000, y= 520)
        
        
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
            conn.close()

        


class PubView(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = tk.Frame(self, borderwidth=5)
        refresh = tk.Button(frame, text='Refresh', command = frame.update())
        refresh.grid(row=2, column=0, sticky=tk.W)

        conn = sqlite3.connect('lib.db')
        c = conn.cursor()

        
        
        button = tk.Button(self, text="Add Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubAdd))
        button.place(x=1000, y= 70)

        button2 = tk.Button(self, text="View Publisher",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=1000, y= 120)

        button3 = tk.Button(self, text="Update Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.place(x=1000, y= 170)

        button4 = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookAdd))
        button4.place(x=1000, y= 220)

        button5 = tk.Button(self, text="View Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookView))
        button5.place(x=1000, y= 270)

        button6 = tk.Button(self, text="Add Student", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StudentAdd))
        button6.place(x=1000, y= 320)

        button7 = tk.Button(self, text="Issue Book",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(IssueBook))
        button7.place(x=1000, y= 370)

        button8 = tk.Button(self, text="View Issues", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(ViewIssue))
        button8.place(x=1000, y= 420)

        button9 = tk.Button(self, text="Return Books", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(Return))
        button9.place(x=1000, y= 470)

        button10 = tk.Button(self, text="Home", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button10.place(x=1000, y= 520)

        self.heading = tk.Label(self, text="View Publisher", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        # tree = ttk.Treeview(self,height=20, columns=3)
        # tree.place(x=100, y=150)
        # tree["column"]=('1','2','3')
        # tree.heading('1',text="pub_id", anchor=tk.W)
        # tree.heading('2',text="Publisher Name", anchor=tk.W) 
        # tree.heading('3', text="Adderss", anchor=tk.W)
        self.btn_view = tk.Button(self, text="Show publishers", width=18, height=2, bg='maroon2', fg='white', command=self.view)
        self.btn_view.place(x=100, y=100)
        
    def view(self, *args, **kwargs):
        tree = ttk.Treeview(self,height=20, columns=3)
        tree.place(x=100, y=150)
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
        self.id_l.place(x=10, y=70)

        self.id_e = tk.Entry(self, font=('arial 18 bold'), width=10, )
        self.id_e.place(x=380, y=70)

        self.btn_search = tk.Button(self, text="Search", width=15, height=2, bg='brown', fg='white', command=self.search)
        self.btn_search.place(x=560, y=70)

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
        self.btn_update = tk.Button(self, text="Update publisher", width=25, height=2, bg="purple1", fg="white", command=self.update)
        self.btn_update.place(x=380, y=220)

        #btn clear
        self.btn_clear = tk.Button(self, text="Clear all fields", width=25, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=380, y = 270)

        button = tk.Button(self, text="Add Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubAdd))
        button.place(x=1000, y= 70)

        button2 = tk.Button(self, text="View Publisher",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=1000, y= 120)

        button3 = tk.Button(self, text="Update Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.place(x=1000, y= 170)

        button4 = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookAdd))
        button4.place(x=1000, y= 220)

        button5 = tk.Button(self, text="View Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookView))
        button5.place(x=1000, y= 270)

        button6 = tk.Button(self, text="Add Student", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StudentAdd))
        button6.place(x=1000, y= 320)

        button7 = tk.Button(self, text="Issue Book",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(IssueBook))
        button7.place(x=1000, y= 370)

        button8 = tk.Button(self, text="View Issues", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(ViewIssue))
        button8.place(x=1000, y= 420)

        button9 = tk.Button(self, text="Return Books", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(Return))
        button9.place(x=1000, y= 470)

        button10 = tk.Button(self, text="Home", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button10.place(x=1000, y= 520)
        
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

        conn = sqlite3.connect('lib.db')
        c = conn.cursor()

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
        self.btn_add = tk.Button(self, text="Add Book", width=25, height=2, bg="purple1", fg="white", command=self.get_items)
        self.btn_add.place(x=270, y=220)

        #btn clear
        self.btn_clear = tk.Button(self, text="Clear all fields", width=25, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=270, y = 270)

        button = tk.Button(self, text="Add Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubAdd))
        button.place(x=1000, y= 70)

        button2 = tk.Button(self, text="View Publisher",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=1000, y= 120)

        button3 = tk.Button(self, text="Update Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.place(x=1000, y= 170)

        button4 = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookAdd))
        button4.place(x=1000, y= 220)

        button5 = tk.Button(self, text="View Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookView))
        button5.place(x=1000, y= 270)

        button6 = tk.Button(self, text="Add Student", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StudentAdd))
        button6.place(x=1000, y= 320)

        button7 = tk.Button(self, text="Issue Book",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(IssueBook))
        button7.place(x=1000, y= 370)

        button8 = tk.Button(self, text="View Issues", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(ViewIssue))
        button8.place(x=1000, y= 420)

        button9 = tk.Button(self, text="Return Books", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(Return))
        button9.place(x=1000, y= 470)

        button10 = tk.Button(self, text="Home", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button10.place(x=1000, y= 520)

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

        conn = sqlite3.connect('lib.db')
        c = conn.cursor()

        self.heading = tk.Label(self, text="View Books", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        
        button = tk.Button(self, text="Add Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubAdd))
        button.place(x=10, y= 550)

        button2 = tk.Button(self, text="View Publisher",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=250, y= 550)

        button3 = tk.Button(self, text="Update Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.place(x=490, y= 550)

        button4 = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookAdd))
        button4.place(x=730, y= 550)

        button5 = tk.Button(self, text="View Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookView))
        button5.place(x=970, y= 550)

        button6 = tk.Button(self, text="Add Student", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StudentAdd))
        button6.place(x=10, y= 610)

        button7 = tk.Button(self, text="Issue Book",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(IssueBook))
        button7.place(x=250, y= 610)

        button8 = tk.Button(self, text="View Issues", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(ViewIssue))
        button8.place(x=490, y= 610)

        button9 = tk.Button(self, text="Return Books", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(Return))
        button9.place(x=730, y= 610)

        button10 = tk.Button(self, text="Home", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button10.place(x=970, y= 610)
        
        self.tree = ttk.Treeview(self, height=20, columns=3)
        self.tree.place(x=10, y=100)
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

        conn = sqlite3.connect('lib.db')
        c = conn.cursor()

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
        self.btn_add = tk.Button(self, text="Add Student", width=25, height=2, bg="purple1", fg="white", command=self.get_items)
        self.btn_add.place(x=270, y=220)

        #btn clear
        self.btn_clear = tk.Button(self, text="Clear all fields", width=25, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=270, y = 270)

        button = tk.Button(self, text="Add Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubAdd))
        button.place(x=1000, y= 70)

        button2 = tk.Button(self, text="View Publisher",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=1000, y= 120)

        button3 = tk.Button(self, text="Update Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.place(x=1000, y= 170)

        button4 = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookAdd))
        button4.place(x=1000, y= 220)

        button5 = tk.Button(self, text="View Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookView))
        button5.place(x=1000, y= 270)

        button6 = tk.Button(self, text="Add Student", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StudentAdd))
        button6.place(x=1000, y= 320)

        button7 = tk.Button(self, text="Issue Book",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(IssueBook))
        button7.place(x=1000, y= 370)

        button8 = tk.Button(self, text="View Issues", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(ViewIssue))
        button8.place(x=1000, y= 420)

        button9 = tk.Button(self, text="Return Books", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(Return))
        button9.place(x=1000, y= 470)

        button10 = tk.Button(self, text="Home", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button10.place(x=1000, y= 520)
 
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


class IssueBook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        conn = sqlite3.connect('lib.db')
        c = conn.cursor()
        self.heading = tk.Label(self, text="Issue Book", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        c.execute("CREATE TABLE IF NOT EXISTS issue (issue_id INTEGER PRIMARY KEY AUTOINCREMENT, book_id INTEGER NOT NULL, roll INTEGER  NOT NULL, i_date TEXT NOT NULL, e_date TEXT NOT NULL, FOREIGN KEY(book_id) REFERENCES book(book_id) ON UPDATE CASCADE, FOREIGN KEY(roll) REFERENCES student(roll) ON UPDATE CASCADE)")
        
        self.book_id_l = tk.Label(self, text="Enter Book ID", font=('arial 18 bold'))
        self.book_id_l.place(x=10, y=70)

        self.book_name_l = tk.Label(self, text="Book Name", font=('arial 18 bold'))
        self.book_name_l.place(x=10, y=120)

        self.num_book_l = tk.Label(self, text="No of Books left", font=('arial 18 bold'))
        self.num_book_l.place(x=10, y=170)

        self.roll_l = tk.Label(self, text="Enter Student's Roll", font=('arial 18 bold'))
        self.roll_l.place(x=10, y=220)

        self.st_name_l = tk.Label(self, text="Student Name", font=('arial 18 bold'))
        self.st_name_l.place(x=10, y=270)

        self.faculty_l = tk.Label(self, text="Faculty", font=('arial 18 bold'))
        self.faculty_l.place(x=10, y=320)

        self.i_date_l = tk.Label(self, text="ISSUE Date", font=('arial 18 bold'))
        self.i_date_l.place(x=10, y=370)

        self.e_date_l = tk.Label(self, text="Expiry Date", font=('arial 18 bold'))
        self.e_date_l.place(x=10, y=420)


        # entry
        self.book_id_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.book_id_e.place(x=270, y=70)

        self.book_name_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.book_name_e.place(x=270, y=120)

        self.num_book_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.num_book_e.place(x=270, y=170)

        self.roll_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.roll_e.place(x=270, y=220)

        self.st_name_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.st_name_e.place(x=270, y=270)

        self.faculty_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.faculty_e.place(x=270, y=320)

        self.i_date_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.i_date_e.place(x=270, y=370)

        self.e_date_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.e_date_e.place(x=270, y=420)


        unix = time.time()
        datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
        self.issue = time.strftime("%x")
        self.date_1 = datetime.datetime.strptime(self.issue, "%m/%d/%y")
        self.end_date = self.date_1 + datetime.timedelta(days=60)
        

        self.i_date_e.delete(0,tk.END)
        self.i_date_e.insert(0, self.date_1)
        # self.i_date_e.config(status=tk.DISABLED)

        self.e_date_e.delete(0,tk.END)
        self.e_date_e.insert(0, self.end_date)
        # self.e_date_e.config(status=tk.DISABLED)

        self.btn_search = tk.Button(self, text="Search", width=25, height=2, bg='brown',fg='white', command=self.search)
        self.btn_search.place(x=620, y=65)

        self.btn_search1 = tk.Button(self, text="Search", width=25, height=2, bg='brown',fg='white', command=self.search1)
        self.btn_search1.place(x=620, y=215)

        #button to add to database
        self.btn_add = tk.Button(self, text="Issue Book", width=25, height=2, bg="purple1", fg="white", command=self.get_items)
        self.btn_add.place(x=270, y=470)

        button = tk.Button(self, text="Add Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubAdd))
        button.place(x=1000, y= 70)

        button2 = tk.Button(self, text="View Publisher",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=1000, y= 120)

        button3 = tk.Button(self, text="Update Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.place(x=1000, y= 170)

        button4 = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookAdd))
        button4.place(x=1000, y= 220)

        button5 = tk.Button(self, text="View Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookView))
        button5.place(x=1000, y= 270)

        button6 = tk.Button(self, text="Add Student", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StudentAdd))
        button6.place(x=1000, y= 320)

        button7 = tk.Button(self, text="Issue Book",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(IssueBook))
        button7.place(x=1000, y= 370)

        button8 = tk.Button(self, text="View Issues", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(ViewIssue))
        button8.place(x=1000, y= 420)

        button9 = tk.Button(self, text="Return Books", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(Return))
        button9.place(x=1000, y= 470)

        button10 = tk.Button(self, text="Home", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button10.place(x=1000, y= 520)
        
    def search(self, *args, **kwargs):
        sql = "select * from book where book_id = ?"
        result = c.execute(sql,(self.book_id_e.get()))

        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
        conn.commit()

        self.book_name_e.delete(0,tk.END)
        self.book_name_e.insert(0, str(self.n1))

        self.num_book_e.delete(0,tk.END)
        self.num_book_e.insert(0, str(self.n2))
    
    def search1(self, *args, **kwargs):
        sql = "select * from student where roll=?"
        result = c.execute(sql,(self.roll_e.get(),))

        for r in result:
            self.m1 = r[1]
            self.m2 = r[2]
        conn.commit()

        self.st_name_e.delete(0,tk.END)
        self.st_name_e.insert(0, str(self.m1))

        self.faculty_e.delete(0,tk.END)
        self.faculty_e.insert(0, str(self.m2))

    #get method
    def get_items(self, *args, **kwargs):

        #get from entries
        self.book_id = self.book_id_e.get()
        self.roll = self.roll_e.get()
        self.i_date = self.i_date_e.get()
        self.e_date = self.e_date_e.get()

        if self.book_id == '' and self.roll == '':
            tkinter.messagebox.showinfo("Error","Please fill the entries")
        else:
        
            sql = "insert into issue (book_id, roll, i_date, e_date) values (?,?,?,?)"
            c.execute(sql, (self.book_id, self.roll, self.i_date, self.e_date))
            q = "update book set num_book = num_book - 1 where book_id = ?"
            c.execute(q, self.book_id)
            conn.commit()
                
            tkinter.messagebox.showinfo("Success", "Successfully book issued!")


class ViewIssue(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        conn = sqlite3.connect('lib.db')
        c = conn.cursor()

        self.heading = tk.Label(self, text="View Issue", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        self.roll_l = tk.Label(self, text="Enter Roll No.", font=('arial 18 bold'))
        self.roll_l.place(x=10,y=70)

        self.roll_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.roll_e.place(x=270, y=70)
       

        self.btn_go = tk.Button(self, text="Go!!!", width=25, height=2, bg="purple1", fg="white", command=self.go)
        self.btn_go.place(x=620, y=65)

        button = tk.Button(self, text="Add Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubAdd))
        button.place(x=10, y= 580)

        button2 = tk.Button(self, text="View Publisher",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=250, y= 580)

        button3 = tk.Button(self, text="Update Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.place(x=490, y= 580)

        button4 = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookAdd))
        button4.place(x=730, y= 580)

        button5 = tk.Button(self, text="View Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookView))
        button5.place(x=970, y= 580)

        button6 = tk.Button(self, text="Add Student", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StudentAdd))
        button6.place(x=10, y= 640)

        button7 = tk.Button(self, text="Issue Book",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(IssueBook))
        button7.place(x=250, y= 640)

        button8 = tk.Button(self, text="View Issues", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(ViewIssue))
        button8.place(x=490, y= 640)

        button9 = tk.Button(self, text="Return Books", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(Return))
        button9.place(x=730, y= 640)

        button10 = tk.Button(self, text="Home", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button10.place(x=970, y= 640)

        self.tree = ttk.Treeview(self,height=20, columns=3)
        self.tree.place(x=10, y=150)
        self.tree["column"]=('1','2','3','4','5')
        self.tree.heading('1',text="Issue ID.", anchor=tk.W)
        self.tree.heading('2',text="Roll no.", anchor=tk.W)
        self.tree.heading('3',text="Book Name", anchor=tk.W) 
        self.tree.heading('4', text="Issue Date", anchor=tk.W)
        self.tree.heading('5', text="Expiry Date", anchor=tk.W)


    def go(self):
        self.roll = self.roll_e.get()
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        query = 'select issue.issue_id, issue.roll, book.book_name, issue.i_date, issue.e_date from issue inner join book on issue.book_id = book.book_id  where (issue.roll= (?));'
        entries = c.execute(query,(self.roll_e.get(),))
        conn.commit()
        for row in entries:
            self.tree.insert('',tk.END,values=row)

class Return(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        conn = sqlite3.connect('lib.db')
        c = conn.cursor()

        self.heading = tk.Label(self, text="Return Book", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        #label for windows
        self.issue_id_l = tk.Label(self, text="Enter Issue ID", font=('arial 18 bold'))
        self.issue_id_l.place(x=10, y=70)

        self.roll_l = tk.Label(self, text="Student Roll No.", font=('arial 18 bold'))
        self.roll_l.place(x=10, y=120)

        self.book_id_l = tk.Label(self, text="Book ID", font=('arial 18 bold'))
        self.book_id_l.place(x=10, y=170)

        self.book_name_l = tk.Label(self, text="Book Name", font=('arial 18 bold'))
        self.book_name_l.place(x=10, y=220)

        self.i_date_l = tk.Label(self, text="Issued Date", font=('arial 18 bold'))
        self.i_date_l.place(x=10, y=270)

        self.e_date_l = tk.Label(self, text="Expiry Date", font=('arial 18 bold'))
        self.e_date_l.place(x=10, y=320)

        # entry
        self.issue_id_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.issue_id_e.place(x=270, y=70)

        self.roll_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.roll_e.place(x=270, y=120)

        self.book_id_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.book_id_e.place(x=270, y=170)

        self.book_name_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.book_name_e.place(x=270, y=220)

        self.i_date_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.i_date_e.place(x=270, y=270)

        self.e_date_e = tk.Entry(self, width=25, font=('arial 18 bold'))
        self.e_date_e.place(x=270, y=320)

        self.btn_search = tk.Button(self, text="Search", width=15, height=2, bg='brown',fg='white', command=self.search)
        self.btn_search.place(x=620, y=65)
    
        #button to add to database
        self.btn_add = tk.Button(self, text="Return Book", width=25, height=2, bg="purple1", fg="white", command=self.get_items)
        self.btn_add.place(x=270, y=370)

        self.btn_clear = tk.Button(self, text="Clear all fields", width=25, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=270, y = 420)

        button = tk.Button(self, text="Add Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubAdd))
        button.place(x=1000, y= 70)

        button2 = tk.Button(self, text="View Publisher",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubView))
        button2.place(x=1000, y= 120)

        button3 = tk.Button(self, text="Update Publisher", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(PubUpdate))
        button3.place(x=1000, y= 170)

        button4 = tk.Button(self, text="Add Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookAdd))
        button4.place(x=1000, y= 220)

        button5 = tk.Button(self, text="View Book", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(BookView))
        button5.place(x=1000, y= 270)

        button6 = tk.Button(self, text="Add Student", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StudentAdd))
        button6.place(x=1000, y= 320)

        button7 = tk.Button(self, text="Issue Book",  width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(IssueBook))
        button7.place(x=1000, y= 370)

        button8 = tk.Button(self, text="View Issues", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(ViewIssue))
        button8.place(x=1000, y= 420)

        button9 = tk.Button(self, text="Return Books", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(Return))
        button9.place(x=1000, y= 470)

        button10 = tk.Button(self, text="Home", width=25, height=2, bg="steelblue", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button10.place(x=1000, y= 520)
        
    def search(self, *args, **kwargs):
        sql1 = "select issue.roll, issue.book_id, book.book_name, issue.i_date, issue.e_date from issue inner join book on issue.book_id = book.book_id  where (issue.issue_id= (?))"
        result = c.execute(sql1,(self.issue_id_e.get(),))

        for r in result:
            self.n1 = r[0]
            self.n0 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            
        conn.commit()

        self.book_name_e.delete(0,tk.END)
        self.book_name_e.insert(0, str(self.n2))
        self.book_name_e.config(state=tk.DISABLED)

        self.book_id_e.delete(0,tk.END)
        self.book_id_e.insert(0, str(self.n0))
        self.book_id_e.config(state=tk.DISABLED)

        self.roll_e.delete(0,tk.END)
        self.roll_e.insert(0, str(self.n1))
        self.roll_e.config(state=tk.DISABLED)
        
        self.i_date_e.delete(0,tk.END)
        self.i_date_e.insert(0, str(self.n3))
        self.i_date_e.config(state=tk.DISABLED)

        self.e_date_e.delete(0,tk.END)
        self.e_date_e.insert(0, str(self.n4))
        self.e_date_e.config(state=tk.DISABLED)

        self.n1 = ''
        self.n2 = ''
        self.n3 = ''
        self.n4 = ''
        self.n0 = ''
 
    #get method
    def get_items(self, *args, **kwargs):

        #get from entries
        self.issue_id = self.issue_id_e.get()
        self.roll = self.roll_e.get()
        self.book_name = self.book_name_e.get()
        self.i_date = self.i_date_e.get()
        self.e_date = self.e_date_e.get()
        self.book_id = self.book_id_e.get()

        if self.book_name == '' and self.roll == '' and self.i_date == '' and self.e_date == '':
            tkinter.messagebox.showinfo("Error","No issues")
        else:
        
            sql = "delete from issue where issue_id = ?"
            c.execute(sql, (self.issue_id,))
            q = "update book set num_book = num_book + 1 where book_id = ?"
            c.execute(q, (self.book_id,))
            conn.commit()
                
            tkinter.messagebox.showinfo("Success", "Successfully book returned!")

    def clear_all(self, *args, **kwargs):
        self.issue_id_e.delete(0, tk.END)
        self.book_name_e.delete(0, tk.END)
        self.roll_e.delete(0, tk.END)
        self.i_date_e.delete(0, tk.END)
        self.e_date_e.delete(0, tk.END)
        self.book_id_e.delete(0, tk.END)



app = SeaofBTCapp()
# app.update()
app.geometry('1366x768+0+0')
app.title("Library Management System")
# app.wm_iconbitmap('icon.ico')
app.mainloop()

