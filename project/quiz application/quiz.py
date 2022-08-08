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
    window_login.geometry('270x180')

    username = Label(window_login, text="Username: ")
    username.pack()
    entry_username = Entry(window_login, textvariable=name)
    entry_username.pack()

    password = Label(window_login, text='Password: ')
    password.pack()
    entry_password = Entry(window_login, textvariable= password)
    entry_password.pack()

    bt_login = Button(window_login, text='Log In',padx=10, pady=4, command=lambda:login_true(entry_username, entry_password))
    bt_login.pack(pady= 20)

    window_login.mainloop()



def admin_w():
    window_admin = tkinter.Tk()

    window_admin.title("Admin")
    window_admin.geometry("900x500")

    def add_q():
        no_ques = IntVar()

        def add_question(n):
            ques_1 = StringVar()
            op_1 = StringVar()
            op_2 = StringVar()
            op_3 = StringVar()
            op_4 = StringVar()
            ans_w = StringVar()

            def next_q(a, b, c, d, e, f):
                a = a.get()
                b = b.get()
                c = c.get()
                d = d.get()
                e = e.get()
                f = f.get()
                text_file = open("questionlist.txt", "a")
                # q = f"[{a}], [{b}], [{c}], [{d}], [{e}], [{f}] |-|\n"
                q = f"{a} |-| {b} |-| {c} |-| {d} |-| {e} |-| {f}\n"
                text_file.write(q)

                add_question(n + 1)

            def done_q(a, b, c, d, e, f):
                a = a.get()
                b = b.get()
                c = c.get()
                d = d.get()
                e = e.get()
                f = f.get()
                text_file = open("questionlist.txt", "a")
                q = f"{a} |-| {b} |-| {c} |-| {d} |-| {e} |-| {f}\n"
                text_file.write(q)

                messagebox.showinfo("message", f"No. of questions added are {n}")

                window_admin.destroy()
                admin_w()

                # done_l = Label(window_admin, text= f"No. of questions added are : {no}")
                # done_l.place(x = 500, y = 200)



            ques1 = Label(
                window_admin,
                text=f'Question {n}:'
            )
            ques1.place(x = 70, y = 130)

            ques1_ent = Entry(
                window_admin, 
                textvariable=ques_1,
                width= 120
            )
            ques1_ent.place(x = 70, y = 150)

            op1 = Label(window_admin, text='Option 1:  a)').place(x = 80, y = 190)
            op2 = Label(window_admin, text='Option 2:  b)').place(x = 80, y = 220)
            op3 = Label(window_admin, text='Option 3:  c)').place(x = 80, y = 250)
            op4 = Label(window_admin, text='Option 4:  d)').place(x = 80, y = 280)
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

            
            nxt = Button(window_admin, text='Next', width=19, command=lambda:next_q(ques1_ent, op1_ent, op2_ent, op3_ent, op4_ent, ans_ent))
            nxt.place(x = 500, y = 400)

            done = Button(window_admin, text="Done", width=19, command=lambda:done_q(ques1_ent, op1_ent, op2_ent, op3_ent, op4_ent, ans_ent))
            done.place(x = 660, y = 400)
 
        
        n = Label(
            window_admin,
            text="*Note:- Just enter the question, its options and answer and, for the next questions click next and add the questions\n When all the questions are added click done",
            font=('Comic Sans MS', '10')
        )
        n.place(x = 70, y = 70)

        add_question(1)


    def del_q():
        messagebox.askokcancel("Warning!!", "This will delete all the questions")
        fl = open("questionlist.txt", 'w')
        fl.write('')
        fl.close()



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