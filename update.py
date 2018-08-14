from tkinter import *
import sqlite3
import tkinter.messagebox
from subprocess import call

conn = sqlite3.connect('lib.db')
c = conn.cursor()

result = c.execute("select max(pub_id) from publisher")

for r in result:
    id = r[0]

class PubAdd:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Update Publisher", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        self.id_l = Label(master, text="Enter ID", font=('arial 18 bold'))
        self.id_l.place(x=0, y=0)

        self.id_e = Entry(master, font=('arial 18 bold'), width=10)
        self.id_e.place(x=300, y=0)

        self.btn_search = Button(master, text="Search", width=15, height=2, bg='brown', command=self.search)
        self.btn_search.place(x=550, y=70)

        self.name_l = Label(master, text="Enter Publisher", font=('arial 18 bold'))
        self.name_l.place(x=10, y=120)

        self.address_l = Label(master, text="Enter Publisher Address", font=('arial 18 bold'))
        self.address_l.place(x=10, y=170)

        # entry
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=380, y=120)

        self.address_e = Entry(master, width=25, font=('arial 18 bold'))
        self.address_e.place(x=380, y=170)

        #button to add to database
        self.btn_update = Button(master, text="Update publisher", width=25, height=2, bg="steelblue", fg="white", command=self.update)
        self.btn_update.place(x=370, y=370)

        #btn clear
        self.btn_clear = Button(master, text="Clear all fields", width=18, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=358, y = 420)

        
    def clear_all(self, *args, **kwargs):
        self.id_e.delete(0, END)
        self.name_e.delete(0, END)
        self.address_e.delete(0, END)
        
    #get method
    def search(self, *args, **kwargs):
        sql = "select * from publisher where pub_id = ?"
        result = c.execute(sql,(self.id_e.get()))

        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
        conn.commit()

        self.name_e.delete(0,END)
        self.name_e.insert(0, str(self.n1))

        self.address_e.delete(0,END)
        self.address_e.insert(0, str(self.n2))

    def update(self, *args, **kwargs):
        self.u1 = self.name_e.get()
        self.u2 = self.address_e.get()

        query = "update publisher set pub_name=?, address=? where pub_id=?"
        c.execute(query, (self.u1, self.u2, self.id_e.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Publisher updated")

root = Tk()
b = PubAdd(root)

root.geometry('1366x768+0+0')
root.title("Add Publisher")
root.mainloop()