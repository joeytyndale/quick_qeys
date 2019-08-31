import tkinter as tk
from tkinter import ttk


#! Creates window // starts loop
window = tk.Tk()
# * Title
window.title("Quick Qeys")
# * Window Size
window.geometry("500x500")


#! gives weight to the cells in the grid
rows = 0
while rows < 50:
    window.rowconfigure(rows, weight=1)
    window.columnconfigure(rows, weight=1)
    rows += 1

#! Defines and places the notebook widget
tabControl = ttk.Notebook(window)
tabControl.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')


# * attaching page to notebook
tab1 = ttk.Frame(tabControl)
# * adds page 1 to window
tabControl.add(tab1, text='Add Phrase')


# * attaching page to notebook
tab2 = ttk.Frame(tabControl)
# * adds page 2 to window
tabControl.add(tab2, text='Automate things')


ent1t1 = tk.Entry(tab1).pack()
btn1t2 = tk.Button(tab2, text="Button 2").pack()


tk.mainloop()
