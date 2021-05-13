from connections import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
from ttkthemes import themed_tk as tk

class AddCrimeType:
    def __init__(self):
        self.root = tk.ThemedTk(theme="blue")
        self.root.title("Add Crime Type")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        Label(self.root, text='Add Crime Type', font=('arial',24,'bold','underline')).pack()
        body = Frame(self.root)
        body.pack(pady=20)



        self.name = Label(body, text="Name")
        self.en_name = Entry(body, width=80)
        self.name.grid(row=0, column=0)
        self.en_name.grid(row=0, column=1)

        self.description = Label(body, text="Description")
        self.en_description = Text(body)
        self.description.grid(row=1, column=0)
        self.en_description.grid(row=1, column=1)

        btn =ttk.Button(body, text="Submit", command= self.btnSubmit)
        btn.grid(row=2,column=1)

        self.root.mainloop()

    def btnSubmit(self):
        name = self.en_name.get()
        description = self.en_description.get('1.0',END)

        if name=='' or description=='' or description=='\n':
            messagebox.showinfo("","All Fields Are Required !!!")
        else:
            query=f"SELECT * FROM `crimetype` where name = '{name}'"
            conn = makeConnections()
            cr = conn.cursor()
            cr.execute(query)
            result = cr.fetchall()
            if len(result)>0:
                messagebox.showinfo("","All Ready Exist!!")
            else:
                query =f"INSERT INTO `crimetype`(`name`, `descripition`) VALUES ('{name}','{description}')"
                cr.execute(query)
                conn.commit()
                messagebox.showinfo('','Success Fully Added Crime {}'.format(name))
if __name__ == '__main__':
    obj = AddCrimeType()