import tkinter as tk
from tkinter import ttk, font


class TreeDataView(tk.Frame):
    def __init__(self, master, headers, height=False, scrollbar_x=True, scrollbar_y=True, selectmode=None,
                 left_click=None, right_click=None, double_click=None, return_key=None, **options):

        tk.Frame.__init__(self, master)

        def sortby(tree, col, descending):
            # Sort tree contents when a column is clicked on.
            # grab values to sort
            data = [(tree.set(child, col), child) for child in tree.get_children('')]

            # reorder data
            data.sort(reverse=descending)
            for indx, item in enumerate(data):
                tree.move(item[1], '', indx)

            # switch the heading so that it will sort in the opposite direction
            tree.heading(col, command=lambda func=col: sortby(tree, col, int(not descending)))

        container = tk.Frame(self)
        container.pack(fill='both', expand=True)

        if selectmode is None:
            mode = 'extended'
        else:
            mode = selectmode
        self.tree = ttk.Treeview(container, columns=headers, show='headings', selectmode=mode)
        vsb = ttk.Scrollbar(container, orient='vertical', command=self.tree.yview)
        hsb = ttk.Scrollbar(container, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)

        if bool(height) is True:
            self.tree.configure(height=height)
        
        if bool(scrollbar_y) is True:
            vsb.grid(column=1, row=0, sticky='ns', in_=container)
            
        if bool(scrollbar_x) is True:
            hsb.grid(column=0, row=1, sticky='ew', in_=container)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        for column in headers:
            self.tree.heading(column, text=column, anchor='w', command=lambda c=column: sortby(self.tree, c, 0))
            self.tree.column(column, width=font.Font().measure(column.title()))

        if left_click:
            self.tree.bind('<<TreeviewSelect>>', left_click)

        if double_click:
            self.tree.bind('<Double-Button-1>', double_click)

        if right_click:
            self.tree.bind('<Button-3>', right_click)

        if return_key:
            self.tree.bind('<Return>', return_key)
            
        for index, _ in enumerate(headers):
            self.tree.column(headers[index], minwidth=50, stretch=True)

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

    def selection(self):
        return self.tree.selection()

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

    def clear(self): 
        for item in self.tree.get_children():
            self.tree.delete(item)

    def get_all_items(self):
        items = []
        for item in self.tree.get_children():
            items.append(self.tree.item(item, 'values'))
        return items
