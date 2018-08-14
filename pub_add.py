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
        self.heading = Label(master, text="Add Publisher", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        # self.i = Label(master, text="ID is reached upto: " +str(id), font=('arial 18 bold'))
        # self.i.place(x=10, y=40)
        #label for windows
        self.name_l = Label(master, text="Enter Publisher", font=('arial 18 bold'))
        self.name_l.place(x=10, y=70)

        self.address_l = Label(master, text="Enter Publisher Address", font=('arial 18 bold'))
        self.address_l.place(x=10, y=120)

        # entry
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=270, y=70)

        self.address_e = Entry(master, width=25, font=('arial 18 bold'))
        self.address_e.place(x=270, y=120)

        #button to add to database
        self.btn_add = Button(master, text="Add publisher", width=25, height=2, bg="steelblue", fg="white", command=self.get_items)
        self.btn_add.place(x=370, y=370)

        # text box
        # self.tBox = Text(master, width=60, height=17)
        # self.tBox.place(x=720, y=70)
        # self.tBox.insert(END, "ID has reached upto: " +str(id))

        #btn clear
        self.btn_clear = Button(master, text="Clear all fields", width=18, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=358, y = 420)

        self.btn_pub_view = Button(master, text="View Publisher", command=self.open)
        self.btn_pub_view.place(x=450, y=450)

    def open(self):
        # root.destroy()
        call(["python pub_view.py"])
        
    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.address_e.delete(0, END)
        
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

        




root = Tk()
b = PubAdd(root)

root.geometry('1366x768+0+0')
root.title("Add Publisher")
root.mainloop()