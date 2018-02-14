import sys
from TreeDataView import TreeDataView
import random

if sys.version_info.major == 2:
    import Tkinter as tk
    import ttk
elif sys.version_info.major == 3:
    import tkinter as tk
    from tkinter import ttk
else:
    print('This version of Python is not supported!')
    sys.exit(1)


def main():
    root = tk.Tk()
    root.wm_title('TreeDataView as a Table')

    def callback(event):
        rowid = tdv1.identify_row(event.y)
        column = tdv1.identify_column(event.x)
        selitems = tdv1.selection()
        if selitems:
            selitem = selitems[0]
            text = tdv1.item(selitem, 'values')
            cell = int(column[1])-1
            print('Click on row:', rowid[0])
            print('Row data:', text)
            print('Clicked on Cell:', cell)
            print('Cell data:', text[cell])

    def get_row_data():
        selected_row = tdv1.selection()
        prev_item = tdv1.prev(selected_row)
        text = tdv1.item(selected_row, 'values')
        tags = tdv1.item(prev_item, 'tags')
        if tags:
            print(tags[0])
        else:
            pass
        print(text)

    def delete_row():
        selected_row = tdv1.selection()
        tdv1.delete(selected_row)

    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label='Print row', command=get_row_data)
    menu.add_command(label='Add', command=None)
    menu.add_command(label='Edit', command=None)
    menu.add_command(label='Delete', command=delete_row)

    def mymenu(event):
        row_id = tdv1.identify_row(event.y)
        tdv1.selection_set(row_id)
        menu.post(event.x_root, event.y_root)

    tree_columns = ['Name', 'Phone', 'Email', 'Company', 'Date']
    tdv1 = TreeDataView(root, tree_columns, scrollbar_x=True, scrollbar_y=True, double_click=callback)
    tdv1.pack(fill='both', expand=1)

    def insert_data():
        # Lets generate a random phone number, and a date.
        phone = '(800) {}-{}'.format(random.randint(300, 900), random.randint(5000, 9000))
        date = '{:02d}/{:02d}/{}'.format(random.randint(1, 12), random.randint(1, 31), random.randint(2010, 2017))

        # Lets pick a random name, email and company name from the lists then create the email address.
        name_list = ['Kari Turner', 'Melinda Blanks', 'Russell Wise', 'James Garcia']
        company_list = ['Mansmann', 'Merrymaking', 'Monk Real Estate']
        name = random.choice(name_list)
        company = random.choice(company_list)
        email = '{}@{}'.format(name[0].lower() + name.split()[-1].lower(), company.replace(' ', '').lower())

        # Now lets insert a row with random data into the table.
        new_item = tdv1.insert('', 'end', values=(name, phone, email, company, date))
        tdv1.table_set_striped(new_item)

    button1 = ttk.Button(root, text='Insert random data', command=insert_data)
    button1.pack(side='bottom')
    
    root.mainloop()


if __name__ == '__main__':
    main()
