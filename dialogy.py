
from os.path import basename, splitext
import tkinter as tk
from tkinter import messagebox, filedialog
import pylab as pl






class Application(tk.Tk):
    name = "Foo"
    soubor = filedialog.askopenfilename(title="soubor")

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="graf")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn = tk.Button(self, text="graf", command=self.show)
        self.btn.pack()
    

    def show(self):
        axisx=[]
        axisy=[]
        with open(self.soubor, "r") as f:

            while line := f.readline():
                x, y = line.split()
                axisx.append(float(x))
                axisy.append(float(y))

        pl.plot(axisx, axisy)
        pl.show()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()






