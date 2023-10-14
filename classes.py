from ttkbootstrap import Style
from tkinter import ttk

STYLE = Style(theme="superhero")
WINDOW = STYLE.master
NOTEBOOK = ttk.Notebook(WINDOW)
NOTEBOOK.pack(fill="both")

class App:
    width = None
    height = None
    title = ""

    def __init__(self, title="App"):
        self.title = title

        self.width = WINDOW.winfo_screenwidth()
        self.height = WINDOW.winfo_screenheight()

        WINDOW.geometry("%dx%d" % (self.width, self.height))
        self.start_app()

    def start_app(self):
        Tab()

        WINDOW.mainloop()

class Tab:
    widgets = {}

    def __init__(self):
        self.widgets["main_frame"] = ttk.Frame(NOTEBOOK)

        self.widgets["main_frame"].pack(fill="both")

        title = f"Tab {len(self.widgets.keys())}"

        NOTEBOOK.add(self.widgets["main_frame"], text=title)
