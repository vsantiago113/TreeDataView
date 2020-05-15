# TreeDataView
The TreeDataView is a table for Tkinter using Tkinter TreeView class. It supports Python 2.7+ and Python 3+.  
It has been tested with up to 9000 rows and 6 columns in a regular workstation with a duo core CPU and 2GB of Memory.  

```python
class TreeDataView(master, headers, height=False, scrollbar_x=True, scrollbar_y=True, selectmode=None,
    left_click=None, right_click=None, double_click=None, return_key=None, table_striped=False):
```

#### Required
**master**: The Tkinter window/frame.  
**headers**: A list of the column names as string.   
#### Optional
**scrollbar_x**: A scroll bar on the bottom value must be bool.  
**scrollbar_y**: Shows a scroll bar on the right side value must be bool.  
**left_click**: A callback when mouse left click.  
**right_click**: A callback when mouse right click.  
**double_click**: A callback when double left click on mouse.  
**return_key**: A callback when press return/enter key on the keyboard.  
**table_striped**: Create a gray row every other row, pass value as bool.  
#### Don't use not fully working yet.
**height**: This one I am still thinking what to do with it. I might remove it.
**selectmode**: Don't use this one, is not finished yet.  


#### Methods: I am going to add this later----------------

#### How to create a table.
```python
from TreeDataView import TreeDataView
import tkinter as tk

def main():
    root = tk.Tk()
    root.wm_title('TreeDataView as a Table')
    
    tree_columns = ['Name', 'Phone', 'Email', 'Company', 'Date']
    tdv1 = TreeDataView(root, tree_columns, scrollbar_x=True, scrollbar_y=True, double_click=callback)
    tdv1.pack(fill='both', expand=1)

    root.mainloop()
    
if __name__ == '__main__':
    main()
```
