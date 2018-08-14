from tkinter import *
import sqlite3
import tkinter.messagebox
from subprocess import call

conn = sqlite3.connect('lib.db')
c = conn.cursor()


class PubAdd:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Add Student", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        c.execute("CREATE TABLE IF NOT EXISTS student (roll INTEGER PRIMARY KEY, st_name TEXT NOT NULL, faculty TEXT NOT NULL)")

        #label for windows
        self.roll_l = Label(master, text="Enter Roll No.", font=('arial 18 bold'))
        self.roll_l.place(x=10, y=70)

        self.st_name_l = Label(master, text="Enter Student Name", font=('arial 18 bold'))
        self.st_name_l.place(x=10, y=120)

        self.faculty_l = Label(master, text="Enter Faculty", font=('arial 18 bold'))
        self.faculty_l.place(x=10, y=170)


        # entry
        self.roll_e = Entry(master, width=25, font=('arial 18 bold'))
        self.roll_e.place(x=270, y=70)

        self.st_name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.st_name_e.place(x=270, y=120)

        self.faculty_e = Entry(master, width=25, font=('arial 18 bold'))
        self.faculty_e.place(x=270, y=170)

        #button to add to database
        self.btn_add = Button(master, text="Add Book", width=25, height=2, bg="steelblue", fg="white", command=self.get_items)
        self.btn_add.place(x=370, y=370)

        #btn clear
        self.btn_clear = Button(master, text="Clear all fields", width=18, height=2, bg="lightgreen", fg='white', command=self.clear_all)
        self.btn_clear.place(x=358, y = 420)
 
    def clear_all(self, *args, **kwargs):
        self.roll_e.delete(0, END)
        self.st_name_e.delete(0, END)
        self.faculty_e.delete(0, END)
        
    #get method
    def get_items(self, *args, **kwargs):

        #get from entries
        self.roll = self.roll_e.get()
        self.st_name = self.st_name_e.get()
        self.faculty = self.faculty_e.get()

        if self.roll == '' and self.st_name == '' and self.faculty == '':
            tkinter.messagebox.showinfo("Error","Please fill the entries")
        else:
            
            sql = "insert into student (roll, st_name, faculty) values (?,?,?)"
            c.execute(sql, (self.roll, self.st_name, self.faculty))
            conn.commit()
            
            tkinter.messagebox.showinfo("Success", "Successfully book added!")

        




root = Tk()
b = PubAdd(root)

root.geometry('1366x768+0+0')
root.title("Add Publisher")
root.mainloop()