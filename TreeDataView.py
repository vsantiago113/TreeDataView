try:
    # Python 2.7
    import Tkinter as tk
    import ttk
    import tkFont as font
except ImportError:
    # Python 3
    import tkinter as tk
    from tkinter import ttk, font

class TreeDataView(tk.Frame):
    def __init__(self, master, tree_columns, height=False, horizontal=True, vertical=True, selectmode=None, Button_1=None, Button_3=None, Double_Button_1=None, Return=None, **options):

        tk.Frame.__init__(self, master)

        def sortby(tree, col, descending):
            '''Sort tree contents when a column is clicked on.'''
            # grab values to sort
            data = [(tree.set(child, col), child) for child in tree.get_children('')]

            # reorder data
            data.sort(reverse=descending)
            for indx, item in enumerate(data):
                tree.move(item[1], '', indx)

            # switch the heading so that it will sort in the opposite direction
            tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))

        container = tk.Frame(self)
        container.pack(fill='both', expand=True)

        if selectmode == None:
            mode = 'extended'
        else:
            mode = selectmode
        self.tree = ttk.Treeview(container, columns=tree_columns, show='headings', selectmode=mode)
        vsb = ttk.Scrollbar(container, orient='vertical', command=self.tree.yview)
        hsb = ttk.Scrollbar(container, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)

        if height == False:
            pass
        else:
            self.tree.configure(height=height)
        
        if vertical == True:
            vsb.grid(column=1, row=0, sticky='ns', in_=container)
            
        if horizontal == True:
            hsb.grid(column=0, row=1, sticky='ew', in_=container)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        for col in tree_columns:
            self.tree.heading(col, text=col, anchor='w',
                command=lambda c=col: sortby(self.tree, c, 0))
            self.tree.column(col, width=font.Font().measure(col.title()))

        if Button_1:
            self.tree.bind('<Button-1>', Button_1)

        if Double_Button_1:
            self.tree.bind('<Double-Button-1>', Double_Button_1)

        if Button_3:
            self.tree.bind('<Button-3>', Button_3)

        if Return:
            self.tree.bind('<Return>', Return)
            
        for index, col in enumerate(tree_columns):
            self.tree.column(tree_columns[index], minwidth=50, stretch=True)

    # Build in functions for ttk.TreeView
    def bbox(self, *arg, **kw):
        return self.tree.bbox(*arg, **kw)

    def get_children(self, **kw):
        return self.tree.get_children(**kw)

    def set_children(self, *args):
        self.tree.set_children(*args)

    def column(self, *args, **kwargs):
        return self.tree.column(*args, **kwargs)

    def delete(self, *arg):
        self.tree.delete(*arg)

    def detach(self, *arg):
        self.tree.detach(*arg)

    def exists(self, *arg):
        return self.tree.exists(*arg)

    def focus(self, **kw):
        return self.tree.focus(**kw)

    def heading(self, *args, **kwargs):
        return self.tree.heading(*args, **kwargs)

    def identify(self, *args):
        return self.tree.identify(*args)

    def identify_row(self, *arg):
        return self.tree.identify_row(*arg)

    def identify_column(self, *arg):
        return self.tree.identify_column(*arg)

    def identify_region(self, *args):
        return self.tree.identify_region(*args)

    def identify_element(self, *args):
        return self.tree.identify_element(*args)

    def index(self, *arg):
        return self.tree.index(*arg)

    def insert(self, *args, **kwargs):
        return self.tree.insert(*args, **kwargs)

    def item(self, *args, **kwargs):
        return self.tree.item(*args, **kwargs)

    def move(self, *args, **kwargs):
        self.tree.move(*args, **kwargs)

    def next(self, *arg):
        return self.tree.next(*arg)

    def parent(self, *arg):
        return self.tree.parent(*arg)

    def prev(self, *arg):
        return self.tree.prev(*arg)

    def reattach(self, *args):
        self.tree.reattach(*args)

    def see(self, *arg):
        self.tree.see(*arg)

    def selection(self, **kwargs):
        return self.tree.selection(**kwargs)

    def selection_set(self, *args):
        self.tree.selection_set(*args)

    def selection_add(self, *args):
        self.tree.selection_add(*args)

    def selection_remove(self, *args):
        self.tree.selection_remove(*args)

    def selection_toggle(self, *args):
        self.tree.selection_toggle(*args)

    def set(self, *args, **kwargs):
        return self.tree.set(*args, **kwargs)

    def tag_configure(self, *args, **kwargs):
        return self.tree.tag_configure(*args, **kwargs)

    def tag_has(self, *arg, **kw):
        return self.tree.tag_has(*arg, **kw)

    def xview(self, *args):
        return self.tree.xview(*args)

    def yview(self, *args):
        return self.tree.yview(*args)

    # Custom Functions
    def insert_data(self, data):
        self.tree.insert('', 'end', values=data)
        data = None
        del data

    def clear(self): 
        for item in self.tree.get_children():
            self.tree.delete(item)

    def get_all_items(self):
        items = []
        for item in self.tree.get_children():
            items.append(self.tree.item(item, 'values'))
        return items
