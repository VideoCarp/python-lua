
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as tkmsg
from tkinter import filedialog; import time
window = Tk()

window.title("Python-Lua Compiler")
window.configure(bg="#000000")
window.tk.call('tk', 'scaling', 3.0) # Fix resolution

# Func
def msgbox(title, desc):
  tkmsg.showinfo(title, desc)
def openDialog():
  openableTypes = [("All Files", "*"), ("Python Files", "*.py"), ("Text Files", "*.txt")]
  openedPath = filedialog.askopenfilename(filetypes=openableTypes)
  opened = open(openedPath)
  readOpened = opened.read()
  opened.close()
  text_box.delete(1.0, END)
  text_box.insert(1.0, readOpened)
  msgbox("Opened", "File opened successfully.")


# widgets
text_box = ScrolledText(background="#000000", foreground="#FFFFFF")
# Operations
class to:
    result = []
def operations():
    openOperations = open("transpile_operations.py", "r")
    exec(openOperations.read()); openOperations.close()
# menus
_menu = Menu()
mainMenu = Menu(_menu, tearoff=0)
mainMenu.add_command(label="Open", command=openDialog)
mainMenu.add_command(label="Help", command= lambda: tkmsg.showinfo("Help", "Check repository for details."))
mainMenu.add_command(label="Compile", command=operations)
_menu.add_cascade(label="Menu", menu=mainMenu)
window.config(menu=_menu)
text_box.pack()
window.mainloop()
