import ttkbootstrap as ttk
from screeninfo import get_monitors

from db import open_file

class Tab():
    tab_name = "" 
    tab_index = 0
    widgets = {} 
    file_name = "" 
    headers = []
    full_data = []
    filtered_data = [] 

    def __init__(self, tab_name, tab_index, widgets, file_name, headers, full_data):
        self.tab_name = tab_name
        self.tab_index = tab_index
        self.widgets = widgets
        self.file_name = file_name
        self.headers = headers
        self.full_data = full_data
        self.filtered_data = full_data

    def load_table(self, file_name, headers, full_data):
        table = self.widgets["table"] 

        table.delete(*table.get_children())

        self.file_name = file_name
        self.headers = headers
        self.full_data = full_data
        self.filtered_data = full_data

        table.configure(columns=(headers))
        notebook.tab(self.tab_index, text=file_name)

        for header in headers:
            table.heading(header, text=header)

        for person in full_data:
            table.insert(parent="", index=ttk.END, values=person)

    def init_filter(self):
        print("filter init")
        filter_frame = self.widgets["filter_frame"]
        filter_frame_width = int(WIDTH*0.2)
        filter_frame_height = int(HEIGHT*0.6)

        item_frame = ttk.Frame(filter_frame, width=filter_frame_width*0.8, height=filter_frame_height*0.7, padding=10)       

        test_label = ttk.Label(item_frame, text="item")
        close_button = ttk.Button(self.widgets["filter_frame"], width=int(filter_frame_width*0.5))
        apply_button = ttk.Button(filter_frame, width=int(filter_frame_width*0.5))

        filter_frame.place(relx=0.4, rely=0.2)

        test_label.pack()
        close_button.place(anchor="sw")
        apply_button.place(anchor="se")

def get_primary_geometry():
    for monitor in get_monitors():
        if monitor.is_primary:
            return (monitor.width, monitor.height)

    return (1280, 720)

def delete_tab():
    tab_index = notebook.index("current")
    tabs.pop(tab_index)
    notebook.forget(tab_index)

def debug():
    tab = tabs[notebook.index("current")]

    print("#######################")
    print(tab.tab_name)
    print(tab.widgets)
    print(notebook.index("current"))
    print(window.winfo_width())
    print(window.winfo_height())

def filter_data():
    pass

def new_tab():
    width = window.winfo_width()
    height = window.winfo_height()

    table_frame_width = int(width*0.8)
    option_frame_width = int(width*0.2)
    filter_frame_width = int(width*0.2)

    filter_frame_height = int(height*0.6)

    frame = ttk.Frame(notebook, width=width, height=height)
    table_frame = ttk.Frame(frame, width=table_frame_width, height=height)
    option_frame = ttk.Frame(frame, width=option_frame_width, height=height)
    filter_frame = ttk.Frame(frame, width=filter_frame_width, height=filter_frame_height)

    filter_button = ttk.Button(option_frame, text="Filter", width=option_frame_width-5, command= lambda: tabs[notebook.index("current")].init_filter())
    delete_button = ttk.Button(option_frame, text="Delete Table", width=option_frame_width-5, command= delete_tab)

    scrollx = ttk.Scrollbar(table_frame, orient="horizontal")
    scrolly = ttk.Scrollbar(table_frame, orient="vertical")
    table = ttk.Treeview(table_frame, show="headings")

    scrollx.configure(command=table.xview)
    scrolly.configure(command=table.yview)
    table.configure(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

    frame.pack_propagate(False)
    table_frame.pack_propagate(False)
    option_frame.pack_propagate(False)
    filter_frame.pack_propagate(False)

    frame.pack(side="left", fill="both")
    table_frame.pack(side="left", fill="y")
    option_frame.pack(side="bottom", fill="x")

    scrollx.pack(side="bottom", fill="x")
    scrolly.pack(side="right", fill="y")
    table.pack(side="left", fill="both")
    delete_button.pack(side="bottom")
    filter_button.pack(side="top")

    widgets = {
            "frame": frame,
            "table_frame": table_frame,
            "option_frame": option_frame,
            "filter_frame": filter_frame,
            "scrollx": scrollx,
            "scrolly": scrolly,
            "table": table,
            "filter_button": filter_button,
            "delete_button": delete_button
            }
    notebook.add(frame, text="New tab")

    file_name, headers, full_data = open_file()
    tabnum = len(tabs)

    tabname = f"Tab {tabnum}"

    tab = Tab(tabname, tabnum,  widgets, file_name, headers, full_data)
    tabs.append(tab)

    tab.load_table(file_name, headers, full_data)

tabnum = 1
tabs = []
WIDTH, HEIGHT = get_primary_geometry()

if __name__ == "__main__":
    window = ttk.Window("Excel application", "darkly", size=(WIDTH, HEIGHT))

    menu = ttk.Menu(window)
    file_menu = ttk.Menu(menu, tearoff=False)

    file_menu.add_command(label="New File", command= lambda: new_tab())
    file_menu.add_command(label="Open File", command= lambda: tabs[notebook.index("current")].load_table(*open_file()))

    menu.add_cascade(label="File", menu=file_menu)
    window.configure(menu=menu)

    notebook = ttk.Notebook(window)
    new_tab()
    notebook.pack(fill="both", expand=True)

    window.bind("<Delete>", lambda _: delete_tab())
    window.bind("<Control-KeyPress-n>", lambda _: new_tab())
    window.bind("<d>", lambda _: debug())

    window.mainloop()
