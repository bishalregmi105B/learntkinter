from tkinter import*
import tkinter as tk
import tkinter

root = tkinter.Tk()
root.title("My Python Tkinter Tutorial")
root.geometry("1024x480")
root.iconbitmap("./icon.ico")

def xyz():
    Label(root,text="Btn Clicked").pack()
Button(root,text="Hello World",activebackground="green",foreground="red",font=("Arial",20),command=xyz).pack()
root.mainloop()