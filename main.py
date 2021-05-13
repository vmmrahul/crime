from tkinter import *
from tkinter import ttk
from addCrimeType import AddCrimeType
from viewCrimeType import ViewCrimeType
from addCriminals import Criminal
from viewCriminalCime import ViewCriminal
from ttkthemes import themed_tk as tk
from addAdmin import AddAdmin


class main:
    def __init__(self):
        font = ('arial', 16)
        font_u = ('arial', 16, 'underline')
        font_b = ('arial', 16, 'bold')
        heading = ('arial', 24, 'bold', 'underline')
        px = 15
        py = 15
        bg = '#ccccff'
        fg = '#00134d'

        self.root = tk.ThemedTk(theme="scidmint")
        self.root.config(bg=bg)
        self.root.title("Criminal DataBase")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        menubar = Menu(self.root)
        fileMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=fileMenu)
        fileMenu.add_command(label='Admin', command=AddAdmin)
        fileMenu.add_command(label='File')
        fileMenu.add_separator()
        fileMenu.add_command(label='open')
        fileMenu.add_command(label='Exit')
        crime = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Crime', menu=crime)
        crime.add_command(label='Add Crime', command=AddCrimeType)
        crime.add_command(label='View Crime', command=ViewCrimeType)
        criminal = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='criminal', menu=criminal)
        criminal.add_command(label='Add criminal', command=Criminal)
        criminal.add_command(label='View criminal', command=ViewCriminal)
        self.root.config(menu=menubar)

        Label(self.root, text="Criminal DataBase Managment system", font=heading, bg=bg, fg=fg).pack()

        body = Frame(self.root)
        body.pack()

        leftFrame = Frame(body)
        leftFrame.pack(side=LEFT)

        RightFrame = Frame(body)
        RightFrame.pack(side=RIGHT)

        self.root.mainloop()


if __name__ == '__main__':
    main()
