from connections import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class Login:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry('500x500')
        self.root.config(background='#ccffe6')
        Label(self.root, text="Login", font=('aria l',28,'bold')).pack(pady=20)

        self.email = Label(self.root, text='Email')
        self.en_email = Entry(self.root)
        self.email.pack()
        self.en_email.pack(pady=5)

        self.password = Label(self.root, text='password')
        self.en_password = Entry(self.root)
        self.password.pack(pady=5)
        self.en_password.pack()

        submit = Button(self.root, text="Login", command=self.btnSubmit)
        submit.pack(pady=10)


        self.root.mainloop()

    def btnSubmit(self):
        email = self.en_email.get()
        password = self.en_password.get()

        if email =="" or password =="":
            messagebox.showinfo("Msg", "All Fields Are Required")
        else:
            conn = makeConnections()
            cr = conn.cursor()
            query ="Select * from admin where email='{}' and password='{}'".format(email,password)
            cr.execute(query)
            result = cr.fetchall()
            if len(result)>0:
                messagebox.showinfo("Login", "SuccessFully Login")
            else:
                messagebox.showinfo("Login", "Wrong Password or Email")



if __name__ == '__main__':
    Login()