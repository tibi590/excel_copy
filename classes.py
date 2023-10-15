from ttkbootstrap import Style, Window
from tkinter import ttk

STYLE = Style(theme="superhero")
WINDOW = STYLE.master

WIDTH = WINDOW.winfo_screenwidth()
HEIGHT = WINDOW.winfo_screenheight()

NOTEBOOK = ttk.Notebook(WINDOW)
NOTEBOOK.pack(fill="both")

class App:
    title = ""
    tabs = {}

    def __init__(self, title="App"):
        self.title = title


        WINDOW.geometry("%dx%d" % (WIDTH, HEIGHT)) 

        self.start_app()

    def start_app(self):
        self.new_tab()

        WINDOW.mainloop()

    def new_tab(self):
        title = f"Tab {len(self.tabs.keys())+1}"

        self.tabs[title] = Tab(title)

class Tab:
    widgets = {}

    def __init__(self, title):
        self.widgets["main_frame"] = ttk.Frame(NOTEBOOK, width=WIDTH, height=HEIGHT)
        self.widgets["table_frame"] = ttk.Frame(self.widgets["main_frame"], width=WIDTH*0.8, height=HEIGHT)
        self.widgets["option_frame"] = ttk.Frame(self.widgets["main_frame"], width=WIDTH*0.2, height=HEIGHT)

        self.widgets["table_label"] = ttk.Label(self.widgets["table_frame"], background="red")
        self.widgets["option_label"] = ttk.Label(self.widgets["option_frame"], background="blue")

        self.widgets["main_frame"].pack()
        self.widgets["table_frame"].pack(side="left")
        self.widgets["option_frame"].pack(side="right")

        self.widgets["table_label"].pack(fill="both")
        self.widgets["option_label"].pack(fill="both")

        NOTEBOOK.add(self.widgets["main_frame"], text=title)
