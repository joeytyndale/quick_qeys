import tkinter as tk
from tkinter import ttk


#! Creates window // starts loop
window = tk.Tk()
# * Title
window.title("Quick Qeys")
# * Window Size
window.geometry("350x350")


#! gives weight to the cells in the grid
rows = 0
while rows < 50:
    window.rowconfigure(rows, weight=1)
    window.columnconfigure(rows, weight=1)
    rows += 1

#! Defines and places the notebook widget
tabControl = ttk.Notebook(window)
tabControl.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')


# * attaching tab to notebook
tab1 = ttk.Frame(tabControl)
# * adds page 1 to window
tabControl.add(tab1, text='Add Phrase')


# * attaching tab to notebook
tab2 = ttk.Frame(tabControl)
# * adds page 2 to window
tabControl.add(tab2, text='Automate things')

# * attaching tab to notebook
tab3 = ttk.Frame(tabControl)
# * adds page 3 to window
tabControl.add(tab3, text='Phrases')

#! Tab 1
# * Labels
tk.Label(tab1, text='Trigger phrase').grid(row=1)
tk.Label(tab1, text='Executed Phrase').grid(row=2)

# * Entry Field
ent1t1 = tk.Entry(tab1)
ent2t1 = tk.Entry(tab1)

# * Buttons
tk.Button(tab1, text='Got em').grid(row=3)

tk.Button(tab1, text='Still Got em').grid(row=3, column=2)

# * Placement
ent1t1.grid(row=1, column=1, columnspan=3)
ent2t1.grid(row=2, column=1, columnspan=3)

#! Tab 2
btn1t2 = tk.Button(tab2, text="Button 2").pack()


#! Tab 3
tk.Label(tab3, text="First").grid(row=0, sticky=tk.W)
tk.Label(tab3, text="Second").grid(row=1, sticky=tk.W)

e1 = tk.Entry(tab3)
e2 = tk.Entry(tab3)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


tk.mainloop()
