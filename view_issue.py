from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox


conn = sqlite3.connect('lib.db')
c = conn.cursor()


class PubView:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="View Issue", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        self.roll_l = Label(master, text="Enter Roll No.", font=('arial 40 bold'), fg='blue')
        self.roll_l.place(x=10,y=70)

        self.roll_e = Entry(master, width=25, font=('arial 18 bold'))
        self.roll_e.place(x=270, y=70)
       

        self.btn_go = Button(master, text="Go!!!", width=25, height=2, bg="steelblue", fg="white", command=self.go)
        self.btn_go.place(x=1000, y=70)

        self.tree = ttk.Treeview(height=20, columns=3)
        self.tree.place(x=10, y=200)
        self.tree["column"]=('1','2','3','4','5')
        self.tree.heading('1',text="Issue ID.", anchor=W)
        self.tree.heading('2',text="Roll no.", anchor=W)
        self.tree.heading('3',text="Book Name", anchor=W) 
        self.tree.heading('4', text="Issue Date", anchor=W)
        self.tree.heading('5', text="Expiry Date", anchor=W)


    def go(self):
        self.roll = self.roll_e.get()
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        query = 'select issue.issue_id, issue.roll, book.book_name, issue.i_date, issue.e_date from issue inner join book on issue.book_id = book.book_id  where (issue.roll= (?));'
        entries = c.execute(query,(self.roll_e.get(),))
        conn.commit()
        for row in entries:
            self.tree.insert('',END,values=row)

  
    
        
    



root = Tk()
b = PubView(root)

root.geometry('1366x768+0+0')
root.title("Add Publisher")
root.mainloop()