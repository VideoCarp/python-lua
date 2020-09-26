from transpile_operations import *
from tkinter import *
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
