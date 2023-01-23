import tkinter
from tkinter import *
from tkinter import ttk
import getfiles


def destination_dialog():
    des = tkinter


root = Tk()
root.title("Wally")
# root.geometry("300x300")

# load theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

checkVal = tkinter.BooleanVar()


def showVal(checkVal):
    val = checkVal.get()
    print(val)


# put elements here
mainframe = ttk.Frame(root, style='Card.TFrame', padding=(5, 5, 10, 10))
# mainframe = ttk.LabelFrame(root, text="Get Files", padding=(5, 5, 10, 10))
mainframe.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
ttk.Label(mainframe, text="Please select destination folder: ", font=('Helvetica', 12)).grid(column=0, row=0, padx=10,
                                                                                             pady=5)
ttk.Button(mainframe, text="Choose", style='Accent.TButton').grid(column=1, row=0, padx=10, pady=10)

# Entry
entry = ttk.Entry(mainframe, justify='center')
entry.insert(0, getfiles.DESTINATION)
entry.config(state="disabled")
entry.grid(column=0, row=1, columnspan=2, sticky="we", padx=10, pady=(20, 10))

# Section 2
section = ttk.Frame(root, style='Card.TFrame', padding=(5, 5, 10, 10))
section.grid(column=0, row=1, sticky='nsew', padx=10, pady=10)
ttk.Label(section, text='Start collecting spotlight wallpapers', anchor='center', font=('Helvetica', 12)) \
    .grid(column=0, row=0, columnspan=2, padx=10, pady=10)
spotlight = ttk.Button(section, text="Get Spotlight!", style='Accent.TButton')
spotlight.grid(column=0, row=1, padx=10, pady=10, columnspan=2, sticky='nswe')
ttk.Label(section, text='rename and then save the files: ', font=('Helvetica', 10), justify='left') \
    .grid(column=0, row=2, padx=10, pady=10, sticky='w')
switch = ttk.Checkbutton(section, style="Switch.TCheckbutton",
                         onvalue=True,
                         offvalue=False,
                         command=lambda: showVal(checkVal),
                         variable=checkVal
                         )
switch.grid(column=1, row=2, padx=10, pady=10, sticky='e')

# make widgets to the center by giving weight of size 1
# to the widget at 0th index.
section.grid_columnconfigure(0, weight=1)

# rename section
re = ttk.Frame(root, style='Card.TFrame', padding=(5, 5, 10, 10))
re.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)
name = ttk.Entry(re, justify='center', name='name')
name.grid(column=0, row=0, padx=10, pady=10, sticky='we')
rename = ttk.Button(re, text="Batch rename", state='disabled', style='Accent.TButton')
rename.grid(column=1, row=0, padx=10, pady=10, sticky='e')
re.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    root.mainloop()
