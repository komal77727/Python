import pyqrcode
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def CreateWidgets():
    lable=Label(text="ENTER TEXT:",bg="darkolivegreen4")
    lable.grid(row=0,column=2,padx=5,pady=5)

    root.entry=Entry(width=30,textvariable=qrInput)
    root.entry.grid(row=0,column=2,padx=5,pady=5)

    button = Button(width=10, text="GENERATE",command=QRCodeGenerate)
    button.grid(row=0, column=3, padx=5,pady=5)

    lable = Label(text="QR CODE:", bg="darkolivegreen4")
    lable.grid(row=1, column=1, padx=5, pady=5)

    root.imageLabel= Label(root, background="darkolivegreen4")
    root.imageLabel.grid(row=2, column=1,columnspan=3, padx=5, pady=5)

def QRCodeGenerate():
    qrString = qrInput.get()

    if qrString !='':
        qrGenerate=pyqrcode.create(qrString)

        qrCodePath= 'path to save the image'

        qrCodeName= qrCodePath + qrString +".png"

        qrGenerate.png(qrCodeName,scale= 10)
        image=Image.open(qrCodeName)

        image=image.resize((400,400), Image.ANTIALIAS)

        image= ImageTk.PhotoImage(image)

        root.imageLabel.config(image=image)
        root.imageLabel.photo=image

    else:
        messagebox.showerror("ERROR","Enter a text...!!!")

root=tk.Tk()

root.title("Python QRCODE GENERATOR")
root.geometry("510x500")
root.resizable(False,False)
root.config(background="darkolivegreen4")

qrInput = StringVar()

CreateWidgets()

root.mainloop()


