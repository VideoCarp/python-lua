from transpile_operations import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as tkmsg
from tkinter import filedialog
window = Tk()

window.title("Python-Lua Compiler")
window.configure(bg="#000000")
window.tk.call('tk', 'scaling', 3.0) # Fix resolution

# Func

def openDialog():
  openableTypes = [("All Files", "*"), ("Python Files", "*.py"), ("Text Files", "*.txt")]
  openedPath = filedialog.askopenfilename(filetypes=openableTypes)
  opened = open(openedPath)
  readOpened = opened.read()
  opened.close()
  text_box.delete(1.0, END)
  text_box.insert(1.0, readOpened)
  msgbox("Opened", "File opened successfully.")

def pyluaTranspile():
  toParse = text_box.get(1.0, END)
  text_box.delete(1.0, END)
  text_box.insert(1.0, '-- Result:\n' + "\n".join(result_array))

# widgets
text_box = ScrolledText(background="#000000", foreground="#FFFFFF")

# menus
_menu = Menu()
mainMenu = Menu(_menu, tearoff=0)
mainMenu.add_command(label="Open", command=openDialog)
mainMenu.add_command(label="Help", command= lambda: tkmsg.showinfo("Help", "Check repository for details."))
mainMemu.add_command(label="Compile", command=pyluaTranspile)

_menu.add_cascade(label="Menu", menu=mainMenu)
