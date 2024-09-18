from tkinter import *

root = Tk()

def update():
    print("Resizing the GUI...")
    w = width.get()
    h = height.get()
    root.geometry(f"{w}x{h}")

root.geometry("500x250")
root.title("Window Resizer")

Label(text="Enter the width: ", padx=20).grid(row=1, column=1)
Label(text="Enter the height: ", padx=20).grid(row=2, column=1)

width = StringVar()
height = StringVar()

Entry(root, textvariable=width).grid(row=1, column=2)
Entry(root, textvariable=height).grid(row=2, column=2)

Button(root, text="Apply", command=update).grid(column=2)

root.mainloop()