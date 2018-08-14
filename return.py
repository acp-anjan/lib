from tkinter import *
import sqlite3
import tkinter.messagebox
from subprocess import call
import datetime
import time



conn = sqlite3.connect('lib.db')
c = conn.cursor()


class PubAdd:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Return Book", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        #label for windows
        self.issue_id_l = Label(master, text="Enter Issue ID", font=('arial 18 bold'))
        self.issue_id_l.place(x=10, y=70)

        self.roll_l = Label(master, text="Student Roll No.", font=('arial 18 bold'))
        self.roll_l.place(x=10, y=120)

        self.book_id_l = Label(master, text="Book ID", font=('arial 18 bold'))
        self.book_id_l.place(x=10, y=170)

        self.book_name_l = Label(master, text="Book Name", font=('arial 18 bold'))
        self.book_name_l.place(x=10, y=220)

        self.i_date_l = Label(master, text="Issued Date", font=('arial 18 bold'))
        self.i_date_l.place(x=10, y=270)

        self.e_date_l = Label(master, text="Expiry Date", font=('arial 18 bold'))
        self.e_date_l.place(x=10, y=320)

        # entry
        self.issue_id_e = Entry(master, width=25, font=('arial 18 bold'))
        self.issue_id_e.place(x=270, y=70)

        self.roll_e = Entry(master, width=25, font=('arial 18 bold'))
        self.roll_e.place(x=270, y=120)

        self.book_id_e = Entry(master, width=25, font=('arial 18 bold'))
        self.book_id_e.place(x=270, y=170)

        self.book_name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.book_name_e.place(x=270, y=220)

        self.i_date_e = Entry(master, width=25, font=('arial 18 bold'))
        self.i_date_e.place(x=270, y=270)

        self.e_date_e = Entry(master, width=25, font=('arial 18 bold'))
        self.e_date_e.place(x=270, y=320)

        self.btn_search = Button(master, text="Search", width=15, height=2, bg='brown', command=self.search)
        self.btn_search.place(x=650, y=70)
    
        #button to add to database
        self.btn_add = Button(master, text="Return Book", width=25, height=2, bg="steelblue", fg="white", command=self.get_items)
        self.btn_add.place(x=600, y=600)

        self.btn_clear = Button(master, text="Clear all fields", width=18, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=500, y = 420)
        
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

        self.book_name_e.delete(0,END)
        self.book_name_e.insert(0, str(self.n2))

        self.book_id_e.delete(0,END)
        self.book_id_e.insert(0, str(self.n0))

        self.roll_e.delete(0,END)
        self.roll_e.insert(0, str(self.n1))
        
        self.i_date_e.delete(0,END)
        self.i_date_e.insert(0, str(self.n3))

        self.e_date_e.delete(0,END)
        self.e_date_e.insert(0, str(self.n4))

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
        self.issue_id_e.delete(0, END)
        self.book_name_e.delete(0, END)
        self.roll_e.delete(0, END)
        self.i_date_e.delete(0, END)
        self.e_date_e.delete(0, END)
        self.book_id_e.delete(0, END)
                    

        




root = Tk()
b = PubAdd(root)

root.geometry('1366x768+0+0')
root.title("Add Publisher")
root.mainloop()