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
            messagebox.showinfo("message", "Your username or password is incorrect")

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

    def add_q():
        no_ques = IntVar()

        def add_question(n):
            ques_1 = StringVar()
            op_1 = StringVar()
            op_2 = StringVar()
            op_3 = StringVar()
            op_4 = StringVar()
            ans_w = StringVar()

            ques1 = Label(
                window_admin,
                text=f'Write question {n+1}:'
            )
            ques1.place(x = 70, y = 130)

            ques1_ent = Entry(
                window_admin, 
                textvariable=ques_1,
                width= 120
            )
            ques1_ent.place(x = 70, y = 150)

            op1 = Label(window_admin, text='option 1: a)').place(x = 80, y = 190)
            op2 = Label(window_admin, text='option 2: b)').place(x = 80, y = 220)
            op3 = Label(window_admin, text='option 3: c)').place(x = 80, y = 250)
            op4 = Label(window_admin, text='option 4: d)').place(x = 80, y = 280)
            ans = Label(window_admin, text='Answer: ').place(x = 80, y = 320)

            op1_ent = Entry(window_admin, textvariable= op_1)
            op1_ent.place(x = 220, y = 190)
            op2_ent = Entry(window_admin, textvariable= op_2)
            op2_ent.place(x = 220, y = 220)
            op3_ent = Entry(window_admin, textvariable= op_3)
            op3_ent.place(x = 220, y = 250)
            op4_ent = Entry(window_admin, textvariable= op_4)
            op4_ent.place(x = 220, y = 280)
            ans_ent = Entry(window_admin, textvariable=ans_w)
            ans_ent.place(x = 220, y = 320)

            nxt = Button(window_admin, text='Next', width=24)
            nxt.place(x = 600, y = 400)
        
        n = Label(
            window_admin,
            text="No. of questions you want to add: "
        )
        n.place(x = 50, y = 90)

        n_entry = Entry(
            window_admin,
            textvariable=no_ques
        )
        n_entry.place(x = 300, y = 90)

        global number_of_questions
        number_of_questions = 1

        for i in range(int(number_of_questions)):
            add_question(i)
            number_of_questions = n_entry


    def del_q():
        pass
    def edit_q():
        pass




    bt1 = Button(window_admin, text="Add", width= 8, command=add_q)
    bt2 = Button(window_admin, text="Delete", width= 8, command= del_q)
    bt3 = Button(window_admin, text="Edit", width= 8, command=edit_q)

    bt1.place(x=30, y=10)
    bt2.place(x=100, y=10)
    bt3.place(x=170, y=10)

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