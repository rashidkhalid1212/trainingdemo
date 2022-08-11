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
    window_login.resizable(False, False)

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
    window_admin.resizable(False, False)
    window_admin.config(bg = 'light blue')

    def add_q():
        try:
            note_2.destroy()
            txt.destroy()
            save_bt.destroy()

        except:
            NameError()


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


            global ques1
            ques1 = Label(
                window_admin,
                text=f'Question {n}:'
            )
            ques1.place(x = 70, y = 130)

            global ques1_ent
            ques1_ent = Entry(
                window_admin, 
                textvariable=ques_1,
                width= 120
            )
            ques1_ent.place(x = 70, y = 150)

            global op1
            global op2
            global op3
            global op4
            global ans

            op1 = Label(window_admin, text='Option 1:  a)')
            op1.place(x = 80, y = 190)
            op2 = Label(window_admin, text='Option 2:  b)')
            op2.place(x = 80, y = 220)
            op3 = Label(window_admin, text='Option 3:  c)')
            op3.place(x = 80, y = 250)
            op4 = Label(window_admin, text='Option 4:  d)')
            op4.place(x = 80, y = 280)
            ans = Label(window_admin, text='Answer: ')
            ans.place(x = 80, y = 320)

            global op1_ent
            global op2_ent
            global op3_ent
            global op4_ent
            global ans_ent

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

            global nxt
            nxt = Button(window_admin, text='Next', width=19, command=lambda:next_q(ques1_ent, op1_ent, op2_ent, op3_ent, op4_ent, ans_ent))
            nxt.place(x = 500, y = 400)

            global done
            done = Button(window_admin, text="Done", width=19, command=lambda:done_q(ques1_ent, op1_ent, op2_ent, op3_ent, op4_ent, ans_ent))
            done.place(x = 660, y = 400)
 
        
        global note
        note = Label(
            window_admin,
            text="*Note:- Just enter the question, its options and answer and, for the next questions click next and add the questions\n When all the questions are added click done",
            font=('Comic Sans MS', '10')
        )
        note.place(x = 70, y = 70)

        add_question(1)


    def del_q():
        messagebox.askokcancel("Warning!!", "This will delete all the questions")
        fl = open("questionlist.txt", 'w')
        fl.write('')
        fl.close()


    def edit_q():
        try:
            note.destroy()
            ques1.destroy()
            ques1_ent.destroy()
            op1.destroy()
            op2.destroy()
            op3.destroy()
            op4.destroy()
            ans.destroy()
            op1_ent.destroy()
            op2_ent.destroy()
            op3_ent.destroy()
            op4_ent.destroy()
            ans_ent.destroy()
            nxt.destroy()
            done.destroy()

        except:
            NameError()

        global note_2
        note_2 = Label(
            window_admin,
            text='''IMPORTANT INSTRUCTIONS:-
                  1. Each line contains a question with there options and answer
                  2. The questions are in the format:-
                     question |-| option1 |-| option2 |-| option3 |-| option4 |-| answer
                  3. To edit a question, just change the question, options or the answer and then save it in this format''',
            justify= 'left',
            relief='raised',
            pady = 10,
            padx = 8
        )
        note_2.place(x = 90, y =280) 

        def save_text():
            text_file_edit = open("questionlist.txt", 'w')
            text_file_edit.write(txt.get(1.0, END))

            messagebox.showinfo("Message", "Changes saved")

        global txt
        txt = Text(
            window_admin,
            height=12,
            width=90
            )
        txt.place(x = 90, y=60)

        text_file_edit = open("questionlist.txt", 'r')
        t = text_file_edit.read()

        txt.insert(END, t)
        text_file_edit.close()

        global save_bt
        save_bt = Button(window_admin, text='Save', width=19, command=save_text)
        save_bt.place(x = 660, y = 400)


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
    window_student.geometry("800x500")
    window_student.resizable(False, False)
    # window_student.config(bg='light green')

    global right_answer
    right_answer = 0
    
    def nxt_qu(n):
        global option1, option2, option3, option4, stud_answer
        st_answer = StringVar(window_student)
        

        def NEXT_Q(value):
            selected_op = value
            # if (selected_op == stud_answer):
            for i in selected_op:
                for j in stud_answer:
                    if i==j:
                        global right_answer 
                        right_answer += 1

            ans_l = Label(
                window_student, 
                text= f"The right answer is: {stud_answer}",
                font=("Berlin Sans FB", '16')
                )
            ans_l.place(x = 70, y = 380)

            next_ques = Button(window_student, text='Next question', width=22, command=lambda:nxt_qu(n + 1))
            next_ques.place(x = 530, y = 320)


        if n != 0:
            text_st.delete("1.0", "end")
            option1.destroy()
            option2.destroy()
            option3.destroy()
            option4.destroy()


        file_student = open('questionlist.txt', 'r')
        txt_file_st = file_student.readlines()
        z = txt_file_st
        
        try:
            a = z[n]
            q = a.split(" |-| ")
            text_st.insert(1.0, q[0])
            stud_answer = q[5]
            option1 = Radiobutton(window_student, text=f'(a): {q[1]}', variable= st_answer, value= 'a',font=('Bell MT', '12')  , command=lambda:NEXT_Q(st_answer.get()))
            option1.place(x = 60, y = 190)
            option2 = Radiobutton(window_student, text=f'(b): {q[2]}', variable= st_answer, value= 'b',font=('Bell MT', '12')  , command=lambda:NEXT_Q(st_answer.get()))
            option2.place(x = 60, y = 220)
            option3 = Radiobutton(window_student, text=f'(c): {q[3]}', variable= st_answer, value= 'c',font=('Bell MT', '12')  , command=lambda:NEXT_Q(st_answer.get()))
            option3.place(x = 60, y = 250)
            option4 = Radiobutton(window_student, text=f'(d): {q[4]}', variable= st_answer, value= 'd',font=('Bell MT', '12')  , command=lambda:NEXT_Q(st_answer.get()))
            option4.place(x = 60, y = 280)

        except Exception:
            text_st.destroy()
            La = Label(window_student, text='End of Questions', font=('Agency FB', 26, 'bold'))
            La.place(x = 150, y = 100)
            RA = Label(
                window_student,
                text=f'No. of right answers: {right_answer}',
                font=('Arial Unicode MS', '16')
                )
            RA.place(x = 150, y = 150)

    # img2 = PhotoImage(file = 'img_3.png')
    # img_2_l = Label(
    #     window_student,
    #     image=img2
    #     )
    # Place(x = 0, y =0)

    Q_No = Label(
        window_student,
        text= 'Question '
        )
    Q_No.place(x = 50, y = 50)

    text_st = Text(
        window_student, 
        height= 4,
        width=67,
        font=('Cascadia Code', '13')
    )
    text_st.place(x = 50, y = 70)
    
    n = 0
    nxt_qu(n)

    window_student.mainloop()



root = tkinter.Tk()

root.title("Quiz")
root.geometry("480x530")
root.resizable(False, False)

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
    font = ("Chiller", 14, 'bold'),
    pady = 40
)
text1.pack()


root.mainloop()