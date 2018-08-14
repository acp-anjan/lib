from tkinter import *
import sqlite3
import tkinter.messagebox
from subprocess import call

conn = sqlite3.connect('lib.db')
c = conn.cursor()

# result = c.execute("select max(id) from inventory")

# for r in result:
#     id = r[0]


class PubAdd:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Add Book", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        # query ="CREATE TABLE book IF NOT EXISTS (book_id INTEGER PRIMARY KEY AUTOINCREMENT, book_name TEXT NOT NULL, num_book INTEGER NOT NULL, pub_id INTEGER NOT NULL, FOREIGN KEY(pub_id) REFERENCES publisher(pub_id) ON UPDATE CASCADE)"
        c.execute("CREATE TABLE IF NOT EXISTS issue ()")
        # conn.commit()

        # self.i = Label(master, text="ID is reached upto: " +str(id), font=('arial 18 bold'))
        # self.i.place(x=10, y=40)
        #label for windows
        self.name_l = Label(master, text="Enter Book Name", font=('arial 18 bold'))
        self.name_l.place(x=10, y=70)

        self.num_book_l = Label(master, text="Enter No. of Books", font=('arial 18 bold'))
        self.num_book_l.place(x=10, y=120)

        self.pub_id_l = Label(master, text="Enter Publisher ID", font=('arial 18 bold'))
        self.pub_id_l.place(x=10, y=170)


        # entry
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=270, y=70)

        self.num_book_e = Entry(master, width=25, font=('arial 18 bold'))
        self.num_book_e.place(x=270, y=120)

        self.pub_id_e = Entry(master, width=25, font=('arial 18 bold'))
        self.pub_id_e.place(x=270, y=170)

        #button to add to database
        self.btn_add = Button(master, text="Add Book", width=25, height=2, bg="steelblue", fg="white", command=self.get_items)
        self.btn_add.place(x=370, y=370)

        #btn clear
        self.btn_clear = Button(master, text="Clear all fields", width=18, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=358, y = 420)
 
    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.num_book_e.delete(0, END)
        self.pub_id_e.delete(0, END)
        
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

        




root = Tk()
b = PubAdd(root)

root.geometry('1366x768+0+0')
root.title("Add Publisher")
root.mainloop()