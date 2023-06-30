import sys
import tkinter as tk  # tkinter for gui
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk  # PIL for opening jpeg or jpg formatted images
import mysql.connector
w1=tk.Tk()
w1.geometry("1366x720")     #size of the window
w1.title("REGISTER")
#variables storing entered data

db = mysql.connector.connect(host ="localhost",user = "root",password = "vignesh2003",database ="transport")
cur = db.cursor()

if db:
    print("connected")
else:
    print("not connected")


quotavalues=StringVar()
trainnamevalues=StringVar()
trainnovalues=StringVar()
journeyfromvalues=StringVar()
journeytovalues=StringVar()
classvalues=StringVar()
depdates=StringVar()

quotaentry=StringVar()
trainnameentry=StringVar()
trainnoentry=StringVar()
journeyfromentry=StringVar()
journeytoentry=StringVar()
classentry=StringVar()
depdate=StringVar()



def reserve():

    quotavalue=StringVar()
    trainnamevalue=StringVar()
    trainnovalue=StringVar()
    journeyfromvalue=StringVar()
    journeytovalue=StringVar()
    classvalue=StringVar()
    depdate=StringVar()

    quotavalues=quotaentry.get()
    trainnamevalues=trainnameentry.get()
    trainnovalues=trainnoentry.get()
    journeyfromvalues=journeyfromentry.get()
    journeytovalues=journeytoentry.get()
    depdates=depdate.get()
    classvalues=classentry.get()


    
    res=db.cursor()  
    q = "INSERT INTO train(quotavalue,trainnamevalue,trainnovalue,journeyfromvalue,journeytovalue,depdate,classvalue) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    val=(quotavalues,trainnamevalues,trainnovalues,journeyfromvalues,journeytovalues,depdates,classvalues)
    res.execute(q,val)
    db.commit()
    print("updated")
    

    
    
    #displaying a message when reserve button is clicked
    if (quotavalue.get() == "GN - General Quota"):
        if (classvalue.get() == "First Class (FC)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))               
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
        
        elif (classvalue.get() == "Sleeper Class (SL)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
        elif (classvalue.get() == "Second Class (2S)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
        elif (classvalue.get() == "Unreserved/General Class (2S)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
    elif (quotavalue.get() == "LD - Ladies Quota"):
        if (classvalue.get() == "First Class (FC)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
        elif (classvalue.get() == "Sleeper Class (SL)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
        elif (classvalue.get() == "Second Class (2S)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
        elif (classvalue.get() == "Unreserved/General Class (2S)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
    elif (quotavalue.get() == "DF - Defence Quota"):
        if (classvalue.get() == "First Class (FC)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
        elif (classvalue.get() == "Sleeper Class (SL)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
        elif (classvalue.get() == "Second Class (2S)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
        elif (classvalue.get() == "Unreserved/General Class (2S)"):
            if (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Madurai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Chennai" and journeytovalue.get() == "Kanya Kumari"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Madurai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Chennai"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "Kanya Kumari" and journeytovalue.get() == "Trichy"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nQuota: {}\nClass: {}\nTotal cost: Rs.1200".format(journeyfromvalue.get(),journeytovalue.get(),quotavalue.get(),classvalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")

    

def main():
    f = Image.open("train_railway_platform_124422_3840x2400.jpg")  #opening background image
    f = f.resize((1366,720))        #setting size for background image
    f = ImageTk.PhotoImage(f)
    l=tk.Label(image=f)
    l.pack()
    #setting variables as global
    global quotavalue
    global trainnamevalue
    global trainnovalue
    global journeyfromvalue
    global journeytovalue
    global classvalue

    global journeyfromlist
    global journeytolist

    quotavalue=StringVar()
    trainnamevalue=StringVar()
    trainnovalue=StringVar()
    journeyfromvalue=StringVar()
    journeytovalue=StringVar()
    classvalue=StringVar()
    depdate=StringVar()

    
    

    
    frame_input=tk.Frame(w1,bg='#000000')       #using black color for background of the register frame
    frame_input.place(x=820,y=100,height=500,width=400)     #setting size for the register frame
    tk.Label(text="RAILWAY TICKET RESERVATION",font=("Century Gothic BOLD",18),bg="black",fg="grey").place(x=833,y=150)    #setting a heading for the register frame with bg and fg
    
    #creating and placing attributes' label
    
    tk.Label(text="RESERVATION QUOTA",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=200)
    tk.Label(text="TRAIN NAME",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=250)
    tk.Label(text="TRAIN NO",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=300)
    tk.Label(text="JOURNEY FROM",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=350)
    tk.Label(text="JOURNEY TO",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=400)
    tk.Label(text="CLASS",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=500)
    tk.Label(text="DEPARTURE/JOURNEY DATE",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=450)
    
    #creating option lists
    
    journeyfromlist=["Madurai","Chennai","Trichy","Kanya Kumari"]
    journeyfromvalue.set("Select City")
    journeytolist=["Madurai","Chennai","Trichy","Kanya Kumari"]
    journeytovalue.set("Select City")
    quotalist=["GN - General Quota","LD - Ladies Quota","DF - Defence Quota"]
    quotavalue.set("Select Quota")
    
    #creating textfields
    
    quotaentry = tk.OptionMenu(w1,quotavalue, *quotalist)
    quotaentry.config(bg="darkgrey", fg="black")
    quotaentry["menu"].config(bg="darkgrey")
    quotaentry.pack()
    trainnameentry = tk.Entry(w1,fg="black",bg="darkgrey",textvariable=trainnamevalue)
    trainnoentry = tk.Entry(w1,fg="black",bg="darkgrey",textvariable=trainnovalue)
    journeyfromentry = tk.OptionMenu(w1, journeyfromvalue, *journeyfromlist)
    journeyfromentry.pack()
    journeyfromentry.config(bg="darkgrey", fg="black")
    journeyfromentry["menu"].config(bg="darkgrey")

    journeytoentry = tk.OptionMenu(w1, journeytovalue, *journeytolist)
    journeytoentry.pack()
    journeytoentry.config(bg="darkgrey", fg="black")
    journeytoentry["menu"].config(bg="darkgrey")
    classentry = ttk.Combobox(w1, textvariable=classvalue, values=["First Class (FC)","Sleeper Class (SL)","Second Class (2S)","Unreserved/General Class (2S)"],width=24)
    classentry.pack()
    depdate = DateEntry(w1,selectmode='day',fg="black",bg="darkgrey",font=("Ariel",10),width=13)
    depdate.place(x=1040,y=450)
    
    #placing textfields
    
    quotaentry.place(x=1040,y=200)
    trainnameentry.place(x=1040,y=250)
    trainnoentry.place(x=1040,y=300)
    journeyfromentry.place(x=1040,y=350)
    journeytoentry.place(x=1040,y=400)
    classentry.place(x=1000,y=500)
    
    #creating reserve button
    
    btn1=tk.Button(frame_input,text="RESERVE",font=("Century Gothic",10),bg="darkgrey",fg="black",command=reserve)
    btn1.place(x=150,y=450)
                
    
    
    w1.mainloop()       #used to display the above code
    
main()      #main function call
