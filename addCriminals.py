import cv2

from connections import makeConnections
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import  datetime

class Criminal:
    font = ('arial', 16)
    font_u = ('arial', 16, 'underline')
    font_b = ('arial', 16, 'bold')
    heading = ('arial', 24, 'bold', 'underline')
    px = 15
    py = 15
    bg = '#ccccff'
    fg = '#00134d'
    width=50
    s_width =15
    height =2

    def __init__(self):
        self.root = Tk()
        self.root.title("Add Title")
        self.root.config(bg=self.bg)
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        Label(self.root, text="Add Criminal", font=('arial', 28, 'bold', 'underline')).pack()

        body = Frame(self.root, bg=self.bg)
        body.pack(pady=self.py+20)

        self.name = Label(body, text='Name',font=self.font, bg=self.bg)
        self.en_name = Entry(body, width=self.width)
        self.name.pack()
        self.en_name.pack(pady=self.py)

        self.Lbdob = Label(body, text='Date of Birth',font=self.font, bg=self.bg)
        dob = Frame(body, bg=self.bg)
        self.Lbdob.pack()
        dob.pack(pady=self.py)

        day = Label(dob,text='Day', bg=self.bg)
        day.grid(row=0,column=0)
        self.day = Spinbox(dob, from_=1, to=31, width=self.s_width)
        self.day.grid(row=1, column=0)

        day = Label(dob, text='month', bg=self.bg)
        day.grid(row=0, column=1)
        self.month = Spinbox(dob, from_=1, to=12, width=self.s_width)
        self.month.grid(row=1, column=1)

        day = Label(dob, text='year', bg=self.bg)
        day.grid(row=0, column=2)
        self.year = Spinbox(dob, from_=1950, to=2050, width=self.s_width)
        self.year.grid(row=1, column=2)



        self.gender = Label(body, text="Gender",font=self.font, bg=self.bg)
        self.en_gender = ttk.Combobox(body, values=('Male', 'Female','Other'), width=self.width)
        self.gender.pack()
        self.en_gender.pack(pady=self.py)

        self.address = Label(body, text='Address:',font=self.font, bg=self.bg)
        self.en_address = Entry(body, width=self.width)
        self.address.pack()
        self.en_address.pack(pady=self.py)

        self.age = Label(body, text='age',font=self.font, bg=self.bg)
        self.en_age = Entry(body, width=self.width)
        self.age.pack()
        self.en_age.pack(pady=self.py)

        self.file = Label(body, text='choose File', font=self.font, bg=self.bg)
        self.file_button = Button(body, text="choose File(.png)", command=self.chooseFile)
        self.file.pack()
        self.file_button.pack(pady=self.py)

        btn = Button(body, text="Submit", command =self.btnSubmit)
        btn.pack()

        self.root.mainloop()

    def btnSubmit(self):
        fileName = self.filename
        name = self.en_name.get()
        gender = self.en_gender.get()
        address = self.en_address.get()
        age = self.en_age.get()
        dob = f"{self.year.get()}-{self.month.get()}-{self.day.get()}"
        dob = datetime.strptime(dob, '%Y-%m-%d')
        if len(self.filename) != 0:
            query = "INSERT INTO `criminal`(`name`, `dob`, `gender`, `address`, `age`) VALUES ('{}','{}','{}','{}','{}')".format(name,dob,gender,address,age)
            conn = makeConnections()
            cr = conn.cursor()
            cr.execute(query)
            conn.commit()
            id = cr.lastrowid

            print(fileName)
            path = f'Images/{str(id)}.png'
            cv2.imwrite(path,self.img)
            query = "UPDATE `criminal` SET `image`='{}' WHERE id ='{}'".format(path,id)
            cr.execute(query)
            conn.commit()
            self.root.destroy()
            messagebox.showinfo("Success", 'Added Criminal ')
        else:
            messagebox.showinfo("info", "Image is Not Selected")

    def chooseFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(('jpg', '*.jpg'), ("png", "*.png"), ('jpeg', '*.jpeg')))
        if len(self.filename) != 0:
            print(self.filename)
            self.img = cv2.imread(self.filename)
            self.img =cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.file_button.config(text=self.filename)
        else:
            messagebox.showinfo("info", "Image is Not Selected")

if __name__ == '__main__':
    obj = Criminal()
