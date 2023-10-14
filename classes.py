from ttkbootstrap import Style
from tkinter import ttk

class App:
    width = None
    height = None
    title = ""
    colortheme = "" 

    def __init__(self, title="App", colortheme="flatly"):
        self.style = Style(theme=colortheme)
        self.window = self.style.master

        self.title = title
        self.colortheme = colortheme

        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()

        self.window.geometry("%dx%d" % (self.width, self.height))
        self.start_app()

    def start_app(self):

        ttk.Button(self.window, text="Button", style="succes.TButton").pack(side="left", padx=5, pady=10)

        self.window.mainloop()
