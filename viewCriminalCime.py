from connections import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime


class ViewVictim:
    font = ('arial', 16)
    font_u = ('arial', 16, 'underline')
    font_b = ('arial', 16, 'bold')
    heading = ('arial', 24, 'bold', 'underline')
    px = 15
    py = 15
    bg = '#ccccff'
    fg = '#00134d'
    width = 50
    s_width = 15
    height = 2

    def __init__(self, id):
        self.id = id

        self.root = Tk()
        self.root.title("View Case")
        self.root.config(bg=self.bg)
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        Label(self.root, text='Manage Victim', font=self.heading, bg=self.bg, fg=self.fg).pack(pady=self.py + 20)

        columns = ('id', "Name", 'Address', 'Mobile', 'Case')
        self.tree = ttk.Treeview(self.root, selectmode='browse',
                                 column=columns)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        for row in columns:
            self.tree.heading(row, text=row)

        self.tree.pack(side="top", fill="both", expand=1)
        self.tree.column('#0', stretch=False, minwidth=0, width=0)

        btnContainer = Frame(self.root)
        btnContainer.pack(pady=self.py + 20)

        self.viewVictimData(id)

        self.root.mainloop()

    def viewVictimData(self, id):
        query = "SELECT * FROM `victim` where cases ='{}'".format(id)
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()

        for k in self.tree.get_children():
            self.tree.delete(k)
        for i in range(0, len(result)):
            self.tree.insert("", value=result[i], index=i)

class addVictim:
    font = ('arial', 16)
    font_u = ('arial', 16, 'underline')
    font_b = ('arial', 16, 'bold')
    heading = ('arial', 24, 'bold', 'underline')
    px = 15
    py = 15
    bg = '#ccccff'
    fg = '#00134d'
    width = 50
    s_width = 15
    height = 2

    def __init__(self, id):
        self.root= Tk()
        self.root.title("Add Victim")
        self.root.config(bg=self.bg)
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        Label(self.root, text='Add Victim', font=('arial', 24, 'bold', 'underline')).pack()
        body = Frame(self.root)
        body.pack(pady=20)

        self.caseid = Label(body, text="case id")
        self.en_caseid = Entry(body, width=80)
        self.en_caseid.insert(0, id)
        self.en_caseid.config(state='readonly')
        self.caseid.grid(row=0, column=0)
        self.en_caseid.grid(row=0, column=1)


        self.name = Label(body, text='Name')
        self.en_name = Entry(body, width=80)
        self.name.grid(row=1,column=0)
        self.en_name.grid(row=1,column=1)

        self.Address = Label(body, text='Address')
        self.en_Address = Entry(body, width=80)
        self.Address.grid(row=2,column=0)
        self.en_Address.grid(row=2,column=1)

        self.Mobile = Label(body, text='Mobile')
        self.en_Mobile = Entry(body, width=80)
        self.Mobile.grid(row=3,column=0)
        self.en_Mobile.grid(row=3,column=1)


        submitbtn = Button(body, text='submit', command=self.btnSubmit)
        submitbtn.grid(row=4, column=1)


        self.msglabel = Label(self.root)
        self.msglabel.pack()

        self.root.mainloop()

    def btnSubmit(self):
        en_caseid = self.en_caseid.get()
        en_name = self.en_name.get()
        en_Address = self.en_Address.get()
        en_Mobile = self.en_Mobile.get()

        if en_caseid == '' or en_name == '' or en_Address == '' or en_Mobile == '':
            self.msglabel.config(text="All Fields Are required",padx=self.px, pady=self.py, bg='red', fg='white')
        else:
            if checkNumber(en_Mobile):
                query =f"INSERT INTO `victim`(`name`, `Address`, `mobile`, `cases`) VALUES ('{en_name}','{en_Address}','{en_Mobile}','{en_caseid}')"
                conn = makeConnections()
                cr = conn.cursor()
                cr.execute(query)
                conn.commit()
                self.msglabel.config(text="Added Success Fully {}".format(en_name), padx=self.px, pady=self.py, bg='green',
                                     fg='white')
            else:
                self.msglabel.config(text="{} is invalid".format(en_Mobile), padx=self.px, pady=self.py, bg='red', fg='white')


class editCasePage:
    font = ('arial', 16)
    font_u = ('arial', 16, 'underline')
    font_b = ('arial', 16, 'bold')
    heading = ('arial', 24, 'bold', 'underline')
    px = 15
    py = 15
    bg = '#ccccff'
    fg = '#00134d'
    width = 50
    s_width = 15
    height = 2

    def __init__(self, id):
        query = f"SELECT * FROM `cases` where id ='{id}'"
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        self.criminaldata = cr.fetchone()

        self.root = Tk()
        self.root.title("Edit Case")
        self.root.config(bg=self.bg)
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        Label(self.root, text='Add Victim', font=('arial', 24, 'bold', 'underline')).pack()
        body = Frame(self.root)
        body.pack(pady=20)

        self.criminalId = Label(body, text="Criminal:", font=self.font, bg=self.bg, fg=self.fg)
        self.en_criminalId = Entry(body, width=80)
        self.en_criminalId.insert(0, self.criminaldata[6])
        self.en_criminalId.config(state='readonly')
        self.criminalId.grid(row=0, column=0, pady=self.py)
        self.en_criminalId.grid(row=0, column=1, pady=self.py)


        self.casename = Label(body, text="Case Name", font=self.font, bg=self.bg, fg=self.fg)
        self.en_casename = Entry(body, width=80)
        self.en_casename.insert(0, self.criminaldata[1])
        self.casename.grid(row=2, column=0, pady=self.py)
        self.en_casename.grid(row=2, column=1, pady=self.py)

        self.caseStatus = Label(body, text="case Status", font=self.font, bg=self.bg, fg=self.fg)
        self.en_caseStatus = ttk.Combobox(body,  values=('pending','finish'), state='readonly', width=80)
        self.caseStatus.grid(row=3, column=0, pady=self.py)
        self.en_caseStatus.grid(row=3, column=1, pady=self.py)


        self.incidentDateTime = Label(body, text="incident Date Time", font=self.font, bg=self.bg, fg=self.fg)
        incidentDateTimeBox = Frame(body, bg=self.bg)
        self.incidentDateTime.grid(row=5, column=0, pady=self.py)
        incidentDateTimeBox.grid(row=5, column=1, pady=self.py)

        day = Label(incidentDateTimeBox, text='Day', bg=self.bg)
        day.grid(row=0, column=0)
        self.day = Spinbox(incidentDateTimeBox, from_=1, to=31, width=5, state='readonly')
        self.day.grid(row=1, column=0)

        day = Label(incidentDateTimeBox, text='month', bg=self.bg)
        day.grid(row=0, column=1)
        self.month = Spinbox(incidentDateTimeBox, from_=1, to=12, width=5, state='readonly')
        self.month.grid(row=1, column=1)

        day = Label(incidentDateTimeBox, text='year', bg=self.bg)
        day.grid(row=0, column=2)
        self.year = Spinbox(incidentDateTimeBox, from_=2018, to=2080, width=5, state='readonly')
        self.year.grid(row=1, column=2)

        Hour = Label(incidentDateTimeBox, text='Hour', bg=self.bg)
        Hour.grid(row=0, column=3)
        self.Hour = Spinbox(incidentDateTimeBox, from_=1, to=12, width=5, state='readonly')
        self.Hour.grid(row=1, column=3)

        Min = Label(incidentDateTimeBox, text='Min', bg=self.bg)
        Min.grid(row=0, column=4)
        self.Min = Spinbox(incidentDateTimeBox, from_=0, to=60, width=5, state='readonly')
        self.Min.grid(row=1, column=4)

        sec = Label(incidentDateTimeBox, text='sec', bg=self.bg)
        sec.grid(row=0, column=5)
        self.sec = Spinbox(incidentDateTimeBox, from_=0, to=60, width=5, state='readonly')
        self.sec.grid(row=1, column=5)


        btnSubmit = Button(body, text='Submit', command=self.btnEditSubmit)
        btnSubmit.grid(row=7, column=1)

        self.root.mainloop()

    def btnEditSubmit(self):
        en_criminalId = self.en_criminalId.get()
        en_casename = self.en_casename.get()
        caseStatus = self.en_caseStatus.get()
        insDateTime = f"{self.year.get()}-{self.month.get()}-{self.day.get()} {self.Hour.get()}:{self.Min.get()}:{self.sec.get()}"
        insDateTime = datetime.datetime.strptime(insDateTime, '%Y-%m-%d %H:%M:%S')
        query = f"UPDATE `cases` SET `name`='{en_casename}',`caseStatus`='{caseStatus}',`incidentDateTime`='{insDateTime}' WHERE `id`='{self.criminaldata[0]}'"

        conn =makeConnections()
        cr =conn.cursor()
        cr.execute(query)
        conn.commit()
        messagebox.showinfo("","Success Fully update")
        self.root.destroy()



class ViewCriminal:
    font = ('arial', 16)
    font_u = ('arial', 16, 'underline')
    font_b = ('arial', 16, 'bold')
    heading = ('arial', 24, 'bold', 'underline')
    px = 15
    py = 15
    bg = '#ccccff'
    fg = '#00134d'
    width = 50
    s_width = 15
    height = 2

    def __init__(self):
        self.root = Tk()
        self.root.title("Criminal Database Management")
        self.root.config(bg=self.bg)
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        Label(self.root, text='Manage Criminal', font=self.heading, bg=self.bg, fg=self.fg).pack(pady=self.py + 20)

        columns = ('id', "Name", "DOB", 'Gender', 'Address', 'Age', 'Photo')
        self.tree = ttk.Treeview(self.root, selectmode='browse',
                                 column=columns)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        for row in columns:
            self.tree.heading(row, text=row)

        self.tree.pack(side="top", fill="both", expand=1)
        self.tree.column('#0', stretch=False, minwidth=0, width=0)

        btnContainer = Frame(self.root)
        btnContainer.pack(pady=self.py + 20)

        btnDelete = Button(btnContainer, text='Delete', command=self.btndelet)
        btnDelete.grid(row=0, column=0)
        AddCase = Button(btnContainer, text='Add Cases', command=self.btnAddCases)
        AddCase.grid(row=0, column=1)
        viewCase = Button(btnContainer, text='view Cases', command=self.btnViewCase)
        viewCase.grid(row=0, column=2)

        self.showCriminalData()

        self.root.mainloop()

    def btnViewCase(self):
        currentItem = self.tree.item(self.tree.focus())['values']
        if not (currentItem == ''):
            self.viewCases = Toplevel()
            self.viewCases.title("View Case")
            self.viewCases.config(bg=self.bg)
            self.viewCases.geometry(
                "{0}x{0}+0+0".format(self.viewCases.winfo_screenwidth(), self.viewCases.winfo_screenheight()))

            Label(self.viewCases, text='View Cases', font=self.heading, bg=self.bg, fg=self.fg).pack(pady=self.py + 20)

            columns = ('id','name', 'caseStatus', 'incidentDateTime', 'incidentPlace', 'crimeType', 'criminal', 'fileNo')
            self.ViewCasetree = ttk.Treeview(self.viewCases, selectmode='browse',
                                             column=columns)
            vsb = ttk.Scrollbar(self.viewCases, orient="vertical", command=self.ViewCasetree.yview)
            vsb.pack(side=RIGHT, fill=Y)
            self.ViewCasetree.configure(yscrollcommand=vsb.set)

            for row in columns:
                self.ViewCasetree.heading(row, text=row)

            self.ViewCasetree.pack(side="top", fill="both", expand=1)
            self.ViewCasetree.column('#0', stretch=False, minwidth=0, width=0)
            self.viewCaseData(currentItem[0])

            victimFrame = Frame(self.viewCases)
            victimFrame.pack(pady=self.py + 20)


            btnVictim = Button(victimFrame, text="Victim", command=self.btnVictimView)
            btnVictim.grid(row=0, column=0)
            btnAddVictim = Button(victimFrame, text="Add Victim", command=self.btnVictimAdd)
            btnAddVictim.grid(row=0, column=1)
            btnEditcase = Button(victimFrame, text="Edit Case", command=self.btnEditcase)
            btnEditcase.grid(row=0, column=2)

            self.viewCases.mainloop()
        else:
            messagebox.showinfo('', 'Select one Item in Table')

    def btnEditcase(self):
        data = self.ViewCasetree.item(self.ViewCasetree.focus())['values']
        print(data)
        if not (data == ''):
            obj = editCasePage(data[0])
        else:
            messagebox.showinfo('', "Plz select one Row in Table !!")

    def btnVictimAdd(self):
        data = self.ViewCasetree.item(self.ViewCasetree.focus())['values']
        if not (data == ''):
            obj = addVictim(data[0])
        else:
            messagebox.showinfo('', "Plz select one Row in Table !!")

    def btnVictimView(self):
        data = self.ViewCasetree.item(self.ViewCasetree.focus())['values']
        if not (data == ''):
            obj = ViewVictim(data[0])
        else:
            messagebox.showinfo('', "Plz select one Row in Table !!")

    def viewCaseData(self, id):
        query = "SELECT * FROM `cases` where criminal='{}'".format(id)
        print(query)
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()

        for k in self.ViewCasetree.get_children():
            self.ViewCasetree.delete(k)
        for i in range(0, len(result)):
            self.ViewCasetree.insert("", value=result[i], index=i)

    def btnAddCases(self):
        currentItem = self.tree.item(self.tree.focus())['values']
        if not (currentItem == ''):
            self.win = Toplevel()
            self.win.title("Add Case")
            self.win.config(bg=self.bg)
            self.win.geometry("{0}x{0}+0+0".format(self.win.winfo_screenwidth(), self.win.winfo_screenheight()))

            Label(self.win, text='Add Cases', font=self.heading, bg=self.bg, fg=self.fg).pack(pady=self.py + 20)
            body = Frame(self.win, bg=self.bg)
            body.pack(pady=self.py)

            self.criminalId = Label(body, text="Criminal:", font=self.font, bg=self.bg, fg=self.fg)
            self.en_criminalId = Entry(body, width=80)
            self.en_criminalId.insert(0, currentItem[0])
            self.en_criminalId.config(state='readonly')
            self.criminalId.grid(row=0, column=0, pady=self.py)
            self.en_criminalId.grid(row=0, column=1, pady=self.py)

            query = "select * from crimetype"
            conn = makeConnections()
            cr = conn.cursor()
            cr.execute(query)
            result = cr.fetchall()
            crimeTypeList = []
            for row in result:
                crimeTypeList.append(row[0])

            self.crimeType = Label(body, text="Crime Type", font=self.font, bg=self.bg, fg=self.fg)
            self.en_crimeType = ttk.Combobox(body, values=crimeTypeList, state='readonly', width=80)
            self.crimeType.grid(row=1, column=0, pady=self.py)
            self.en_crimeType.grid(row=1, column=1, pady=self.py)

            self.casename = Label(body, text="Case Name", font=self.font, bg=self.bg, fg=self.fg)
            self.en_casename = Entry(body, width=80)
            self.casename.grid(row=2, column=0, pady=self.py)
            self.en_casename.grid(row=2, column=1, pady=self.py)

            self.caseStatus = Label(body, text="case Status", font=self.font, bg=self.bg, fg=self.fg)
            self.en_caseStatus = ttk.Combobox(body, values=('pending','finish'), state='readonly', width=80)
            self.caseStatus.grid(row=3, column=0, pady=self.py)
            self.en_caseStatus.grid(row=3, column=1, pady=self.py)

            self.incidentPlace = Label(body, text="incident Place", font=self.font, bg=self.bg, fg=self.fg)
            self.en_incidentPlace = Entry(body, width=80)
            self.incidentPlace.grid(row=4, column=0, pady=self.py)
            self.en_incidentPlace.grid(row=4, column=1, pady=self.py)

            self.incidentDateTime = Label(body, text="incident Date Time", font=self.font, bg=self.bg, fg=self.fg)
            incidentDateTimeBox = Frame(body, bg=self.bg)
            self.incidentDateTime.grid(row=5, column=0, pady=self.py)
            incidentDateTimeBox.grid(row=5, column=1, pady=self.py)

            day = Label(incidentDateTimeBox, text='Day', bg=self.bg)
            day.grid(row=0, column=0)
            self.day = Spinbox(incidentDateTimeBox, from_=1, to=31, width=5, state='readonly')
            self.day.grid(row=1, column=0)

            day = Label(incidentDateTimeBox, text='month', bg=self.bg)
            day.grid(row=0, column=1)
            self.month = Spinbox(incidentDateTimeBox, from_=1, to=12, width=5, state='readonly')
            self.month.grid(row=1, column=1)

            day = Label(incidentDateTimeBox, text='year', bg=self.bg)
            day.grid(row=0, column=2)
            self.year = Spinbox(incidentDateTimeBox, from_=2018, to=2080, width=5, state='readonly')
            self.year.grid(row=1, column=2)

            Hour = Label(incidentDateTimeBox, text='Hour', bg=self.bg)
            Hour.grid(row=0, column=3)
            self.Hour = Spinbox(incidentDateTimeBox, from_=1, to=12, width=5, state='readonly')
            self.Hour.grid(row=1, column=3)

            Min = Label(incidentDateTimeBox, text='Min', bg=self.bg)
            Min.grid(row=0, column=4)
            self.Min = Spinbox(incidentDateTimeBox, from_=0, to=60, width=5, state='readonly')
            self.Min.grid(row=1, column=4)

            sec = Label(incidentDateTimeBox, text='sec', bg=self.bg)
            sec.grid(row=0, column=5)
            self.sec = Spinbox(incidentDateTimeBox, from_=0, to=60, width=5, state='readonly')
            self.sec.grid(row=1, column=5)

            self.fileNo = Label(body, text="File No", font=self.font, bg=self.bg, fg=self.fg)
            self.en_fileNo = Entry(body, width=80)
            self.fileNo.grid(row=6, column=0, pady=self.py)
            self.en_fileNo.grid(row=6, column=1, pady=self.py)

            btnSubmit = Button(body, text='Submit', command=self.btnSubmitCases)
            btnSubmit.grid(row=7, column=1)

            self.win.mainloop()


        else:
            messagebox.showinfo('', 'Select one Item in Table')

    def btnSubmitCases(self):
        en_criminalId = self.en_criminalId.get()
        en_crimeType = self.en_crimeType.get()
        en_casename = self.en_casename.get()
        caseStatus = self.en_caseStatus.get()
        en_incidentPlace = self.en_incidentPlace.get()
        en_fileNo = self.en_fileNo.get()
        insDateTime = f"{self.year.get()}-{self.month.get()}-{self.day.get()} {self.Hour.get()}:{self.Min.get()}:{self.sec.get()}"
        insDateTime = datetime.datetime.strptime(insDateTime, '%Y-%m-%d %H:%M:%S')
        query = "SELECT * FROM `cases` WHERE `fileNo`='{}'".format(en_fileNo)
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()

        if len(result) > 0:
            messagebox.showinfo('', "File No Allready alocated!!")
        else:
            query = f"INSERT INTO `cases`(`name`, `caseStatus`, `incidentDateTime`, `incidentPlace`, `crimeType`, `criminal`, `fileNo`) VALUES ('{en_casename}','{caseStatus}','{insDateTime}','{en_incidentPlace}','{en_crimeType}','{en_criminalId}','{en_fileNo}')"
            cr.execute(query)
            conn.commit()
            self.win.destroy()
            messagebox.showinfo("", 'Added Success Fully')

    def showCriminalData(self):
        query = "select * from criminal"
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()

        for k in self.tree.get_children():
            self.tree.delete(k)
        for i in range(0, len(result)):
            self.tree.insert("", value=result[i], index=i)

    def btndelet(self):
        data = self.tree.item(self.tree.focus())['values']
        # print(data)
        ans = messagebox.askquestion('', "Are you Sure to Delete?")
        if ans == 'yes':
            if data == '':
                messagebox.showinfo("", "Plz select data in Table for delete operations!!!")
            else:
                conn = makeConnections()
                query = "DELETE FROM `criminal` WHERE id='{}'".format(data[0])
                cr = conn.cursor()
                cr.execute(query)
                conn.commit()
                messagebox.showinfo("", 'criminal {} is deleted successfully'.format(data[1]))
                self.showCriminalData()


if __name__ == '__main__':
    ViewCriminal()
