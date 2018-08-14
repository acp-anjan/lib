from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox


conn = sqlite3.connect('lib.db')
c = conn.cursor()


class PubView:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="View Publisher", font=('arial 40 bold'), fg='blue')
        self.heading.place(x=400,y=0)

        
   
        
        self.tree = ttk.Treeview(height=20, columns=3)
        self.tree.place(x=100, y=200)
        self.tree["column"]=('1','2','3')
        self.tree.heading('1',text="pub_id", anchor=W)
        self.tree.heading('2',text="Publisher Name", anchor=W) 
        self.tree.heading('3', text="Adderss", anchor=W)

        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        query = 'select * from publisher'
        entries = self.execute_db_query(query)
        for row in entries:
            self.tree.insert('',END,values=row)

    def execute_db_query(self, query, parameters=()):
        with sqlite3.connect('lib.db') as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result
    
        
    



root = Tk()
b = PubView(root)

root.geometry('1366x768+0+0')
root.title("Add Publisher")
root.mainloop()