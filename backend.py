# --------------------------------------------------------------------------------------------------------
# Matrix Text Editor
# Customized Text Editor based on the movie Matrix
# December 17, 2018
# ------------------------------------------
# Authors: Imtiaz Raqib
# ------------------------------------------
# Language: Python with tkinter module
# --------------------------------------------------------------------------------------------------------

# --IMPORTS -----------------------------------------------------------
import os
from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
# ----------------------------------------------------------------------

# Root for main window
root = Tk(className=" Matrix")
textArea = scrolledtext.ScrolledText(root, width=100, height=50)

#------------------
# Functions
#------------------

def newFile():
    if len(textArea.get('1.0', END + '-1c')) > 0:
        if messagebox.askyesno("Woah, Save the file maybe?", "Do you want to save your work?"):
            saveFile()
            textArea.delete('1.0', END)
            
        else:
            textArea.delete('1.0', END)


def openFile():
    file = filedialog.askopenfile(parent=root, title='Select a text file', filetype=(("Text files", "*.txt"), ("All files", "*.*")))

    root.title("Matrix@" + os.path.basename(file.name))

    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode='w')

    if file != None:
        # Slice off the last character from get as an extra return is added
        data = textArea.get('1.0', END + '-1c')
        file.write(data)
        file.close()

def exitFile():
    if messagebox.askyesno("Quit", "Are you sure you want to exit?"):
        root.destroy()

def aboutMatrix():
    messagebox.showinfo("About Matrix", "Matrix is alternative text editor that is based on the movie Matrix.")

def find():
    findString = simpledialog.askstring("Find...", "Enter your query below:")
    textData = textArea.get('1.0', END + '-1c')

    count = textData.lower().count(findString.lower())

    if textData.lower().count(findString.lower()) > 0:
        messagebox.showinfo("Results@Count Instances", 'Your query ' + '> ' + findString + ' <' + ' has ' + str(count) + ' instances.')


# Listing the Menu Options
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
editMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitFile)

menu.add_cascade(label="Help")
menu.add_cascade(label="About", command=aboutMatrix)

menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Count Instances", command=find)

textArea.pack()

# Keep the window open when program runs
root.mainloop()