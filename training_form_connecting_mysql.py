from tkinter import *
from tkinter import messagebox
import mysql.connector

class DB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user='root',
            passwd='#mysql@learning098',
            database='learning_mysql',
        )

        mycursor = self.conn.cursor()
        mycursor.execute("create table if not exists regform(name varchar(40), email varchar(100), gender varchar(50), age int)")

    def insert_user(self):
        cur = self.conn.cursor()
        cur.execute("insert into regform(name, email, gender, age) values('{}', '{}','{}', {})".format(entry_1.get(), entry_2.get(), var.get(), entry_4.get()))
        messagebox.showinfo("message", "record submitted")
        self.conn.commit()

        print("Data is recorded...")

def exit_me():
    a = messagebox.askyesno("warning", "Do you really want to exit!")
    if a == 1:
        root.destroy()

ob = DB()

root = Tk()

root.geometry('500x500')
root.title("Registration Form")
root.configure(bg = 'dark green')

top = Label(root, text="REGISTRATION FORM", width=20, font=("bold", 20), bg="light green", padx=4,pady=2)
top.place(x=90,y=53)

label_1 = Label(root, text="Full Name:", width=10, font=("bold", 10), bg="light blue")
label_1.place(x=100,y=130)

entry_1 = Entry(root, bg="grey", borderwidth=4)
entry_1.place(x=260, y=130)

label_2 = Label(root, text="Email:", width=10, font=("bold", 10), bg="light blue")
label_2.place(x=100, y=180)

entry_2 = Entry(root, bg="grey", borderwidth=4)
entry_2.place(x=260, y=180)

label_3 = Label(root, text="Gender:", width=10, font=("bold", 10), bg="light blue")
label_3.place(x=100, y=230)

var = IntVar()
Radiobutton(root, text="Male", padx = 0, variable=var, value=1, bg="grey", borderwidth=4).place(x=260, y=230)
Radiobutton(root, text="Female", padx = 5, variable=var, value=2, bg="grey", borderwidth=4).place(x=310, y=230)

label_4 = Label(root, text="Age:", width=10, font=("bold", 10), bg="light blue")
label_4.place(x=100, y=280)

entry_4 = Entry(root, bg="grey", borderwidth=4)
entry_4.place(x=260, y=280)

Button(root, text='Submit', width=20, bg='light green', fg='black', command=ob.insert_user).place(x=180,y=380)

Button(root, text='exit', width=10, bg='light green', fg='black', command=exit_me).place(x=340,y=380)

root.mainloop()

