from tkinter import *
from tkinter import messagebox
def login():
    global entry_userVar, entry_passVar
    user = entry_userVar.get()
    password = entry_passVar.get()

    if user == "cjnalaunan21@gmail.com" and password == "cjnalaunan21":
        messagebox.showinfo(title="Login Success!", message="Successfully Logged In")
    else:
        messagebox.showwarning(title="Login Failed!", message="Incorrect Username & Password")

root = Tk()
root.geometry("500x500+433+134")
icon = PhotoImage(file="Py-GUI\lock.png")
root.resizable(False, False)
root.iconphoto(True, icon)

root.title("Login Page")
root.config(background="#d3d3d3")
# frame

window = Frame(root, highlightbackground="black", highlightthickness=2, bg="#e5e4e2", width=250, height=250).place(x=125,y=125)
window_label = Label(window, text="Login Form", bg="#e5e4e2", font=("Helvetica", 20)).place(x=180,y=160)

# string var 
entry_userVar = StringVar()
entry_passVar = StringVar()

Label(window, text="Username:", font=("Helvetica", 10), bg="#e5e4e2").place(x=150 ,y=210)
entry_user = Entry(window, textvariable=entry_userVar, font=("Helvetica", 10), bg="white", width=27).place(x=152 ,y=235)
Label(window, text="Password:", font=("Helvetica", 10), bg="#e5e4e2").place(x=150 ,y=260)
entry_pass = Entry(window, textvariable=entry_passVar, font=("Helvetica", 10), bg="white", width=27, show="*").place(x=152 ,y=285)

Button(window, text="Login", bg="#2d3142", activebackground="#2d3142", fg="white", activeforeground="white", width=26, command=login ).place(x=151,y=320)
root.mainloop()
