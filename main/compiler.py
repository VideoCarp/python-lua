import PySimpleGUI as sg
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as tkmsg
from tkinter import filedialog; import time
from os import path

def msgbox(title, desc):
      tkmsg.showinfo(title, desc)


def openDialog() -> str:
    readOpened = ''
    openableTypes = [("All Files", "*"), ("Python Files", "*.py"), ("Text Files", "*.txt")]
    openedPath = filedialog.askopenfilename(filetypes=openableTypes)
    if type(openedPath) is str:
        with open(openedPath) as opened:
            readOpened = opened.read()
        msgbox("Opened", "File opened successfully.")
    return readOpened  


def operations(window, values):
    text_box = ScrolledText(background="#000000", foreground="#FFFFFF")
    text_box.delete(1.0, END)
    text_box.insert(1.0, values['-text_box-'])
    
    i_path = "transpile_operations.py"

    if not path.exists(i_path):
        i_path = "main/transpile_operations.py"

    openOperations = open(i_path, "r")
    exec(openOperations.read()); openOperations.close()
    window['-text_box-'].update(text_box.get(1.0, END))

def defaultWindow() -> None:
    lenght = 500
    height = 470
    menu = [['&menu', ['&Open', '&Help', '&Compile', ], ], ]
    layout = [
                [sg.MenubarCustom(menu, k='-menu-')],
                [sg.Multiline(size = (lenght, 28), k='-text_box-', background_color='#000000', text_color='#808080')],
                [sg.Button('Quit', size = (5, 1))], 
                #[sg.Button('Ok',size = (5, 1)), sg.Button('Quit', size = (5, 1))],
            ]
    window = sg.Window('Python-Lua Compiler', layout, size = (lenght, height))

    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        match event:
            case sg.WINDOW_CLOSED | 'Quit':
                break 
            case 'Open':
               window['-text_box-'].update(openDialog())
            case 'Help':
                sg.Popup('Check repository for details.')
            case 'Compile':
                if values['-text_box-'] != '':
                    operations(window, values)
                else:
                    sg.Popup('Input text cannot be empty')


if __name__ == '__main__':
    sg.theme('graygraygray')
    defaultWindow()

