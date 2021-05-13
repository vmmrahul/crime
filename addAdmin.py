from connections import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re


class AddAdmin:
    def __init__(self):
        self.root = Tk()
        self.root.title("Add Title")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        Label(self.root, text="Manage Admin", font=('arial', 28, 'bold')).pack(pady=20)
        main = Frame(self.root)
        main.pack()

        body = LabelFrame(main, text="Add Admin Data", pady=10, padx=10)
        body.pack(side=LEFT, padx=20)

        self.name = Label(body, text='Full Name')
        self.en_name = Entry(body)

        self.name.grid(row=0, column=0, pady=5)
        self.en_name.grid(row=0, column=1, pady=5)

        self.email = Label(body, text='Email')
        self.en_email = Entry(body)
        self.email.grid(row=1, column=0, pady=5)
        self.en_email.grid(row=1, column=1, pady=5)

        self.Username = Label(body, text='Username')
        self.en_Username = Entry(body)
        self.Username.grid(row=2, column=0, pady=5)
        self.en_Username.grid(row=2, column=1, pady=5)

        self.Password = Label(body, text='Password')
        self.en_Password = Entry(body, show="*")
        self.Password.grid(row=3, column=0, pady=5)
        self.en_Password.grid(row=3, column=1, pady=5)

        self.Mobile = Label(body, text='Mobile')
        self.en_Mobile = Entry(body)
        self.Mobile.grid(row=4, column=0, pady=5)
        self.en_Mobile.grid(row=4, column=1, pady=5)

        self.type = Label(body, text='Type')
        self.en_type = ttk.Combobox(body, values=(''
                                                  'admin', 'sub-admin'), state='readonly')
        self.type.grid(row=5, column=0, pady=5)
        self.en_type.grid(row=5, column=1, pady=5)

        btn = Button(body, text="Submit", command=self.btnsubmit)
        btn.grid(row=6, column=1)

        columns = ("Name", "Email", 'Password', 'Mobile', 'Type')
        self.tree = ttk.Treeview(main, selectmode='browse',
                                 column=columns)
        vsb = ttk.Scrollbar(main, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        for row in columns:
            self.tree.heading(row, text=row)

        self.tree.pack(side="top", fill="both", expand=1)
        self.tree.column('#0', stretch=False, minwidth=0, width=0)

        self.tree.bind("<Double-1>", self.onDoubleClick)

        self.showAdminData()

        self.root.mainloop()

    def onDoubleClick(self, event):
        currentItem = self.tree.item(self.tree.focus())['values']
        print(currentItem)

        self.win = Toplevel()
        Label(self.win, text="Manage Admin", font=('arial', 28, 'bold')).pack(pady=20)

        body = Frame(self.win)
        body.pack()

        self.edit_name = Label(body, text='Full Name')
        self.edit_en_name = Entry(body, text=currentItem[4])
        self.edit_en_name.insert(0, currentItem[4])
        self.edit_name.grid(row=0, column=0, pady=5)
        self.edit_en_name.grid(row=0, column=1, pady=5)

        self.edit_email = Label(body, text='Email')
        self.edit_en_email = Entry(body)
        self.edit_en_email.insert(0, currentItem[0])
        self.edit_en_email.config(state='readonly')

        self.edit_email.grid(row=1, column=0, pady=5)
        self.edit_en_email.grid(row=1, column=1, pady=5)

        self.edit_Username = Label(body, text='Username')
        self.edit_en_Username = Entry(body)
        self.edit_en_Username.insert(0, currentItem[1])
        self.edit_Username.grid(row=2, column=0, pady=5)
        self.edit_en_Username.grid(row=2, column=1, pady=5)

        self.edit_Mobile = Label(body, text='Mobile')
        self.edit_en_Mobile = Entry(body)
        self.edit_en_Mobile.insert(0, currentItem[3])
        self.edit_Mobile.grid(row=4, column=0, pady=5)
        self.edit_en_Mobile.grid(row=4, column=1, pady=5)

        self.edit_type = Label(body, text='Type')
        self.edit_en_type = ttk.Combobox(body, values=(''
                                                       'admin', 'sub-admin'), state='readonly')
        self.edit_en_type.insert(0, currentItem[5])
        self.edit_type.grid(row=5, column=0, pady=5)
        self.edit_en_type.grid(row=5, column=1, pady=5)

        btn = Button(body, text="Submit", command=self.btnEdit)
        btn.grid(row=6, column=1)

        self.win.mainloop()

    def btnEdit(self):
        name = self.edit_en_name.get()
        email = self.edit_en_email.get()
        Username = self.edit_en_Username.get()

        Mobile = self.edit_en_Mobile.get()
        type = self.edit_en_type.get()
        if name == '' or email == '' or Username == '' or Mobile == '' or type == '':
            messagebox.showinfo("field", "All Fields Are Required!!!")
        else:
            print("Write Edit Code Here")

    def showAdminData(self):
        query = "select * from admin"
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()

        for k in self.tree.get_children():
            self.tree.delete(k)
        for i in range(0, len(result)):
            self.tree.insert("", value=result[i], index=i)

    def checkNumber(self, number):
        number = number
        if re.match(r'[6789]\d{9}$', number):
            return True
        elif re.match(r'(91)?[6789]\d{9}$', number):
            return True
        elif re.match(r'^([0])?[6789]\d{9}$', number):
            return True
        else:
            return False

    def btnsubmit(self):
        name = self.en_name.get()
        email = self.en_email.get()
        Username = self.en_Username.get()
        Password = self.en_Password.get()
        Mobile = self.en_Mobile.get()
        type = self.en_type.get()
        if name == '' or email == '' or Username == '' or Password == '' or Mobile == '' or type == '':
            messagebox.showinfo("field", "All Fields Are Required!!!")
        else:
            checkMobile = self.checkNumber(Mobile)
            if checkMobile:
                query = f"select * from `admin` where email='{email}' or `Username`='{Username}'"
                conn = makeConnections()
                cr = conn.cursor()
                cr.execute(query)
                result = cr.fetchall()
                if len(result) > 0:
                    messagebox.showinfo('data', "Allready registerd")
                else:
                    query = f"INSERT INTO `admin`(`email`, `Username`, `password`, `Mobile`, `fullName`, `type`) VALUES ('{email}','{Username}','{Password}','{Mobile}','{name}','{type}')"
                    cr.execute(query)
                    conn.commit()
                    conn.close()
                    self.showAdminData()
                    messagebox.showinfo("Done", f"Success Fully Added New {type}")
            else:
                messagebox.showerror("", "invalid Mobile Number")



if __name__ == '__main__':
    AddAdmin()
