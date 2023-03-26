import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

import getFiles

root = Tk()
root.title("Wally")
# root.geometry("300x300")
root.resizable(False, False)

# load theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

checkVal = tkinter.BooleanVar()


def pop_up(title: str, icon: str, color: str, copy_msg: str, rn_msg: str):
    pop = Toplevel(root)
    # pop.geometry("300x100")
    # pop.resizable(False, False)
    pop.title(title)
    pop.resizable(False, False)
    if title == "Success":
        pop.configure(bg='#2d4835')
    else:
        pop.configure(bg='#682829')
    container = ttk.Frame(pop, style='Card.TFrame', padding=(5, 5, 10, 10))
    container.grid(column=0, row=0, sticky="nsew", pady=(1, 5), padx=1)
    ttk.Label(container, anchor='center', justify='center', text=icon, font=('Helvetica', 20), foreground=color) \
        .grid(column=0, row=0, padx=10, pady=5, sticky="we")
    ttk.Label(container, anchor='center', justify='center',
              font=('Helvetica', 11),
              text=f"Getting wallpapers - {rn_msg}",
              ).grid(column=0, row=1, padx=10, pady=5, sticky='we')
    container.grid_columnconfigure(0, weight=1)
    ttk.Button(pop, text="OK", style='Accent.TButton', command=pop.destroy) \
        .grid(column=0, row=1, padx=2, pady=(2, 5))


def start_copy():
    msg = getFiles.copy_files()
    if msg == "PathError":
        return pop_up("Failed", "❌", "red", "Error: ", "Select Destination Folder")
    rename_status = getFiles.ren("img")
    if msg == "Success!" and rename_status == "Rename Success!":
        # messagebox.showinfo(message=f"Your wallpaper status: {msg} \nYour wallpaper save status: {rename_status}")
        pop_up("Success", "✔️", "green", msg, rename_status)
        return
    # messagebox.showerror(message=f"Your wallpaper status: {msg} \nYour wallpaper save status: {rename_status}")
    pop_up("Failed", "❌", "red", msg, rename_status)


def showVal(checkVal):
    val = checkVal.get()
    if val:
        re.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)
    elif not val:
        re.grid_forget()


def renameFiles():
    val = name.get()
    print(f"renaming files with val {val}")
    getFiles.ren(val)
    print("Done")


def getDes():
    getFiles.DESTINATION = fd.askdirectory()
    entry.delete(0, END)
    entry.insert(0, getFiles.DESTINATION)
    print(f"value: {getFiles.DESTINATION}")
    return getFiles.DESTINATION


# put elements here
mainframe = ttk.Frame(root, style='Card.TFrame', padding=(5, 5, 10, 10))
# mainframe = ttk.LabelFrame(root, text="Get Files", padding=(5, 5, 10, 10))
mainframe.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
ttk.Label(mainframe, text="Please select destination folder: ", font=('Helvetica', 12)).grid(column=0, row=0, padx=10,
                                                                                             pady=5)
ttk.Button(mainframe, text="Choose", style='Accent.TButton', command=lambda: getDes()).grid(column=1, row=0, padx=10,
                                                                                            pady=10)

# Entry
entry = ttk.Entry(mainframe, justify='center')
entry.insert(0, getFiles.DESTINATION)
entry.config(state="normal")
entry.grid(column=0, row=1, columnspan=2, sticky="we", padx=10, pady=(20, 10))

# Section 2
section = ttk.Frame(root, style='Card.TFrame', padding=(5, 5, 10, 10))
section.grid(column=0, row=1, sticky='nsew', padx=10, pady=10)
ttk.Label(section, text='Start collecting spotlight wallpapers', anchor='center', font=('Helvetica', 12)) \
    .grid(column=0, row=0, columnspan=2, padx=10, pady=10)
spotlight = ttk.Button(section, text="Get Spotlight!", style='Accent.TButton',
                       command=lambda: start_copy())
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
# re.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)
name = ttk.Entry(re, justify='center', name='name')
name.grid(column=0, row=0, padx=10, pady=10, sticky='we')
rename = ttk.Button(re, text="Batch rename", style='Accent.TButton', command=lambda: renameFiles())
rename.grid(column=1, row=0, padx=10, pady=10, sticky='e')
re.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    root.bind_all("<1>", lambda event: event.widget.focus_set())
    root.mainloop()
