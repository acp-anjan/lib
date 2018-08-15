from tkinter import *
import sqlite3
import tkinter.messagebox
from subprocess import call
import datetime
import time



conn = sqlite3.connect('lib.db')
c = conn.cursor()

# result = c.execute("select max(id) from inventory")

# for r in result:
#     id = r[0]


class PubAdd:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Issue Book", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        # query ="CREATE TABLE book IF NOT EXISTS (book_id INTEGER PRIMARY KEY AUTOINCREMENT, book_name TEXT NOT NULL, num_book INTEGER NOT NULL, pub_id INTEGER NOT NULL, FOREIGN KEY(pub_id) REFERENCES publisher(pub_id) ON UPDATE CASCADE)"
        c.execute("CREATE TABLE IF NOT EXISTS issue (issue_id INTEGER PRIMARY KEY AUTOINCREMENT, book_id INTEGER NOT NULL, roll INTEGER  NOT NULL, i_date TEXT NOT NULL, e_date TEXT NOT NULL, FOREIGN KEY(book_id) REFERENCES book(book_id) ON UPDATE CASCADE, FOREIGN KEY(roll) REFERENCES student(roll) ON UPDATE CASCADE)")
        # conn.commit()

        # self.i = Label(master, text="ID is reached upto: " +str(id), font=('arial 18 bold'))
        # self.i.place(x=10, y=40)
        #label for windows
        self.book_id_l = Label(master, text="Enter Book ID", font=('arial 18 bold'))
        self.book_id_l.place(x=10, y=70)

        self.book_name_l = Label(master, text="Book Name", font=('arial 18 bold'))
        self.book_name_l.place(x=10, y=120)

        self.num_book_l = Label(master, text="No of Books left", font=('arial 18 bold'))
        self.num_book_l.place(x=10, y=170)

        self.roll_l = Label(master, text="Enter Student's Roll", font=('arial 18 bold'))
        self.roll_l.place(x=10, y=220)

        self.st_name_l = Label(master, text="Student Name", font=('arial 18 bold'))
        self.st_name_l.place(x=10, y=270)

        self.faculty_l = Label(master, text="Faculty", font=('arial 18 bold'))
        self.faculty_l.place(x=10, y=320)

        self.i_date_l = Label(master, text="ISSUE Date", font=('arial 18 bold'))
        self.i_date_l.place(x=10, y=370)

        self.e_date_l = Label(master, text="Expiry Date", font=('arial 18 bold'))
        self.e_date_l.place(x=10, y=420)


        # entry
        self.book_id_e = Entry(master, width=25, font=('arial 18 bold'))
        self.book_id_e.place(x=270, y=70)

        self.book_name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.book_name_e.place(x=270, y=120)

        self.num_book_e = Entry(master, width=25, font=('arial 18 bold'))
        self.num_book_e.place(x=270, y=170)

        self.roll_e = Entry(master, width=25, font=('arial 18 bold'))
        self.roll_e.place(x=270, y=220)

        self.st_name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.st_name_e.place(x=270, y=270)

        self.faculty_e = Entry(master, width=25, font=('arial 18 bold'))
        self.faculty_e.place(x=270, y=320)

        self.i_date_e = Entry(master, width=25, font=('arial 18 bold'))
        self.i_date_e.place(x=270, y=370)

        self.e_date_e = Entry(master, width=25, font=('arial 18 bold'))
        self.e_date_e.place(x=270, y=420)

        

        #btn clear
        # self.btn_clear = Button(master, text="Clear all fields", width=18, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        # self.btn_clear.place(x=500, y = 420)

        unix = time.time()
        datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
        self.issue = time.strftime("%x")
        self.date_1 = datetime.datetime.strptime(self.issue, "%m/%d/%y")
        self.end_date = self.date_1 + datetime.timedelta(days=60)
        

        self.i_date_e.delete(0,END)
        self.i_date_e.insert(0, self.date_1)

        self.e_date_e.delete(0,END)
        self.e_date_e.insert(0, self.end_date)

        self.btn_search = Button(master, text="Search", width=15, height=2, bg='brown', command=self.search)
        self.btn_search.place(x=650, y=70)

        self.btn_search1 = Button(master, text="Search1", width=15, height=2, bg='brown', command=self.search1)
        self.btn_search1.place(x=650, y=220)

        #button to add to database
        self.btn_add = Button(master, text="Issue Book", width=25, height=2, bg="steelblue", fg="white", command=self.get_items)
        self.btn_add.place(x=600, y=600)
        
    def search(self, *args, **kwargs):
        sql = "select * from book where book_id = ?"
        result = c.execute(sql,(self.book_id_e.get()))

        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
        conn.commit()

        self.book_name_e.delete(0,END)
        self.book_name_e.insert(0, str(self.n1))

        self.num_book_e.delete(0,END)
        self.num_book_e.insert(0, str(self.n2))
    
    def search1(self, *args, **kwargs):
        sql = "select * from student where roll=?"
        result = c.execute(sql,(self.roll_e.get(),))

        for r in result:
            self.m1 = r[1]
            self.m2 = r[2]
        conn.commit()

        self.st_name_e.delete(0,END)
        self.st_name_e.insert(0, str(self.m1))

        self.faculty_e.delete(0,END)
        self.faculty_e.insert(0, str(self.m2))
 
    # def clear_all(self, *args, **kwargs):
    #     self.book_id_e.delete(0, END)
    #     self.roll_e.delete(0, END)
    #     self.book_name_e.delete(0, END)
    #     self.book_name_e.delete(0, END)
    #     self.st_name_e.delete(0, END)
    #     self.faculty_e.delete(0, END)
    #     self.num_book_e.delete(0, END)
        # self.i_date_e.delete(0, END)
        # self.e_date_e.delete(0, END)
    

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
            result = c.execute("select book_id from issue where (roll = (?))", (self.roll,))
            b = []
            for i in result:
                b.append(i)
            a=result.fetchall()
            e =int(self.book_id)
            f = ()
            f = (e,)
            d = []
            d.append(f)
            if d[0] in b:
                tkinter.messagebox.showinfo("Flaws","This book has already been issued to this student")
            else:
                sql = "insert into issue (book_id, roll, i_date, e_date) values (?,?,?,?)"
                c.execute(sql, (self.book_id, self.roll, self.i_date, self.e_date))
                q = "update book set num_book = num_book - 1 where book_id = ?"
                c.execute(q, self.book_id)
                conn.commit()
                    
                tkinter.messagebox.showinfo("Success", "Successfully book issued!")
            
                

        




root = Tk()
b = PubAdd(root)

root.geometry('1366x768+0+0')
root.title("Add Publisher")
root.mainloop()