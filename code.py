from tkinter import *
import subprocess
from tkinter.filedialog import asksaveasfilename, askopenfilename


file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def open_as():
    path = askopenfilename(filetypes=[('Python', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
        set_file_path(path)


def save_as():
    path = asksaveasfilename(defaultextension="", filetypes=[('Python', '*.py')])
    print(file_path)
    with open(path, 'w') as file:
        code = editor.get(1.0, END)
        file.write(code)
        set_file_path(path)


def save():
    if file_path == '':
        path = asksaveasfilename(defaultextension="", filetypes=[('Python', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get(1.0, END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        msg = Toplevel()
        note = Label(msg, text='Please Save Your Code First')
        note.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete(1.0, END)
    code_output.insert(1.0, output)
    code_output.insert(1.0, error)


compiler = Tk()
compiler.title("Python Editor")
editor = Text()
editor.pack()
code_output = Text(height=10)
code_output.pack()
menu_bar = Menu(compiler)
run_bar = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=run_bar)
run_bar.add_command(label="Open", command=open_as)
run_bar.add_command(label="Save", command=save)
run_bar.add_command(label="Save As", command=save_as)
run_bar.add_command(label="Exit", command=exit)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)


compiler.config(menu=menu_bar)
compiler.mainloop()
