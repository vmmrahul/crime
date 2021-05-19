from connections import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re


class searchCiminalByName:
    def __init__(self):
        self.root = Tk()
        self.root.title("Search Criminal")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))



        Label(self.root, text='Search Criminal', font=('arial', 24, 'bold', 'underline')).pack()
        body = Frame(self.root)
        body.pack(pady=20)

        search = Label(body, text='Search by name or crime: ')
        self.search = Entry(body)
        search.grid(row=0, column=0)
        self.search.grid(row=0, column=1)

        btn = Button(body, text='search', command=self.showCriminalData)
        btn.grid(row=0,column=2)


        columns = ('id','name', 'name', 'caseStatus', 'crimeType')
        self.tree = ttk.Treeview(self.root, selectmode='browse',
                                 column=columns)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        for row in columns:
            self.tree.heading(row, text=row)

        self.tree.pack(side="top", fill="both", expand=1)
        self.tree.column('#0', stretch=False, minwidth=0, width=0)

        # self.tree.bind("<Double-1>", self.onDoubleClick)

        self.showCriminalData()

        self.root.mainloop()


    def showCriminalData(self):
        search = self.search.get()
        if search == "":
            query ="SELECT criminal.id,criminal.name, cases.name, cases.caseStatus, cases.crimeType from cases INNER JOIN criminal ON cases.criminal=criminal.id INNER JOIN crimetype on crimetype.name = cases.crimeType"
        else:
            query = "SELECT criminal.id,criminal.name, cases.name, cases.caseStatus, cases.crimeType from cases INNER JOIN criminal ON cases.criminal=criminal.id INNER JOIN crimetype on crimetype.name = cases.crimeType where criminal.name LIKE '%{0}%' or cases.crimeType LIKE '%{0}%'".format(search)
        print(query)
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()

        for k in self.tree.get_children():
            self.tree.delete(k)
        for i in range(0, len(result)):
            self.tree.insert("", value=result[i], index=i)
if __name__ == '__main__':
    searchCiminalByName()