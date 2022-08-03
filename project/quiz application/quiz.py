import tkinter
from tkinter import *
from tkinter import messagebox




def login():
    name = StringVar()
    password = IntVar()

    def login_true(name, password):
        naam = name.get()
        ps = password.get()
        if naam == 'admin' and ps == '0000':
            window_login.destroy()
            admin_w()
        else:
            messagebox.showinfo("message", "You are not an admin")

    window_login = tkinter.Tk()
    window_login.title('Login Window')
    window_login.geometry('300x200')

    username = Label(window_login, text="Username: ")
    username.pack()
    entry_username = Entry(window_login, textvariable=name)
    entry_username.pack()

    password = Label(window_login, text='Password: ')
    password.pack()
    entry_password = Entry(window_login, textvariable= password)
    entry_password.pack()

    bt_login = Button(window_login, text='Log In', command=lambda:login_true(entry_username, entry_password))
    bt_login.pack()

    window_login.mainloop()


def admin_w():
    window_admin = tkinter.Tk()

    window_admin.title("Admin")
    window_admin.geometry("900x600")



    window_admin.mainloop()

def student_w():
    window_student = tkinter.Tk()

    window_student.title("Student")
    window_student.geometry("1200x700")


    window_student.mainloop()




root = tkinter.Tk()

root.title("Quiz")
root.geometry("500x550")

img_icon = PhotoImage(file = "quiz_icon.png")
icon = Label(
    root,
    image = img_icon
)
icon.pack()

text = Label(
    root, 
    text="WHO ARE YOU?",
    font= ("Agency FB", 24, "bold")
)
text.pack()

bt_admin = Button(
    root,
    text='Admin',
    activebackground= "light green",
    bd=6,
    pady= 4,
    width=24,
    command=login
)
bt_admin.pack()

bt_student = Button(
    root,
    text='Student',
    activebackground= "light green",
    bd = 6,
    pady= 4,
    width=24,
    command=student_w
)
bt_student.pack()

text1 = Label(
    root, 
    text = "If you want to edit questions click \"Admin\" \n if you want to solve the questions click \'student\'",
    font = ("Chiller", 12, 'bold'),
    pady = 40
)
text1.pack()



root.mainloop()