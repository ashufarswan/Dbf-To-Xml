from tkinter import *
from package.frontwin import Mainwindow
from  customtkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
root = CTk()
h = Mainwindow(root)
root.mainloop() 
