from connections import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re


class ViewCrimeType:
    def __init__(self):
        self.root = Tk()
        self.root.title("Add Crime Type")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        Label(self.root, text='Add Crime Type', font=('arial', 24, 'bold', 'underline')).pack()


        columns = ("Name", 'Descripiton')
        self.tree = ttk.Treeview(self.root, selectmode='browse',
                                 column=columns)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        for row in columns:
            self.tree.heading(row, text=row)

        self.tree.pack(side="top", fill="both", expand=1)
        self.tree.column('#0', stretch=False, minwidth=0, width=0)

        self.tree.bind("<Double-1>", self.onDoubleClick)

        self.showCrimeTypeData()
        body = Frame(self.root)
        body.pack(pady=20)

        btnEdit = Button(body, text='Edit', command=self.btnEdit)
        btnEdit.pack()

        self.root.mainloop()

    def btnEdit(self):
        currentItem = self.tree.item(self.tree.focus())['values']
        if not (currentItem == ''):
            self.win = Toplevel()
            self.win.title("Edit Crime Type")
            self.win.geometry("{0}x{0}+0+0".format(self.win.winfo_screenwidth(), self.win.winfo_screenheight()))

            Label(self.win, text='Edit Crime Type', font=('arial', 24, 'bold', 'underline')).pack()
            body = Frame(self.win)
            body.pack(pady=20)

            self.name = Label(body, text="Name")
            self.en_name = Entry(body, width=80)
            self.en_name.insert(0, currentItem[0])
            self.en_name.config(state='readonly')
            self.name.grid(row=0, column=0)
            self.en_name.grid(row=0, column=1)

            self.description = Label(body, text="Description")
            self.en_description = Text(body)
            self.en_description.insert(END, currentItem[1])
            self.description.grid(row=1, column=0)
            self.en_description.grid(row=1, column=1)

            btn = Button(body, text="Submit", command=self.btnSubmit)
            btn.grid(row=2, column=1)

            self.win.mainloop()
        else:
            messagebox.showinfo('','Select one Item in Table')

    def btnSubmit(self):
        name = self.en_name.get()
        description = self.en_description.get('1.0',END)

        if name=='' or description=='' or description=='\n':
            messagebox.showinfo("","All Fields Are Required !!!")
        else:
            conn = makeConnections()
            cr = conn.cursor()
            query =f"UPDATE `crimetype` SET `descripition`='{description}' WHERE `name`='{name}'"
            cr.execute(query)
            conn.commit()
            messagebox.showinfo('','Success Fully Update Crime type {}'.format(name))
            self.win.destroy()
            self.showCrimeTypeData()


    def onDoubleClick(self,event):
        currentItem = self.tree.item(self.tree.focus())['values']
        ans = messagebox.askquestion('', 'Are you sure to delete')
        if ans == 'yes':
            query = "DELETE FROM `crimetype` WHERE name='{}'".format(currentItem[0])
            conn = makeConnections()
            cr = conn.cursor()
            cr.execute(query)
            conn.commit()
            self.showCrimeTypeData()
            messagebox.showinfo("", 'Deleted {} is  successfully!!!'.format(currentItem[0]))


    def showCrimeTypeData(self):
            query = "select * from crimetype"
            conn = makeConnections()
            cr = conn.cursor()
            cr.execute(query)
            result = cr.fetchall()

            for k in self.tree.get_children():
                self.tree.delete(k)
            for i in range(0, len(result)):
                self.tree.insert("", value=result[i], index=i)

if __name__ == '__main__':
    obj = ViewCrimeType()