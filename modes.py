from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import datetime as dt
import tkinter.ttk as tkrtk
import tkinter as tt
from tkinter import ttk
import tkinter.messagebox as mb
from subprocess import call
import mysql.connector
import mysql

con=mysql.connector.connect(host="localhost",user="root",password="vignesh2003",database="transport")
cur=con.cursor()

if con:
    print("connected")
else:
    print("connection error")
    

class modes:

    def flight(self):
        call(["python","aerline2.py"])
        

    def train(self):
        call(["python","railway2.py"])
        self.root.destroy()

    def bus(self):
        call(["python","bus.py"])
        self.root.destroy()

    def __init__(self,root):
        self.root=root
        self.root.title("Project")
        self.root.geometry("1366x768")
        
        self.bg_frame = Image.open('modes\\lap.jpeg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        
        

        self.flight_button = Image.open('modes\\flight.jpg')
        photo = ImageTk.PhotoImage(self.flight_button)
        
        self.flight_button = Button(self.root,image=photo, bg='#040405',command=self.flight)
        self.flight_button.image = photo
        self.flight_button.place(x=800, y=400)


        self.train_im = Image.open('modes\\train.jpg')
        photo = ImageTk.PhotoImage(self.train_im)
        self.train_button = Button(self.root,image=photo, bg='#040405',command=self.train)
        self.train_button.image = photo
        self.train_button.place(x=900, y=400)

        self.bus_im = Image.open('modes\\bus.jpg')
        photo = ImageTk.PhotoImage(self.bus_im)
        self.bus_button = Button(self.root,image=photo, bg='#040405',command=self.bus)
        self.bus_button.image = photo
        self.bus_button.place(x=1000, y=400)

        

        
    


def main():
    root = Tk()
    app=modes(root)
    root.mainloop()
main()
