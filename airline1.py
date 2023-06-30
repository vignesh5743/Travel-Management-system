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

routevalue=tk.StringVar()
airlinenamevalue=tk.StringVar()
airlinenovalue=tk.StringVar()
journeyfromvalue=tk.StringVar()
journeytovalue=tk.StringVar()
classvalue=tk.StringVar()
depdate=tk.StringVar()




con = mysql.connector.connect(host ="localhost",user = "root",password = "vignesh2003",db ="transport")
cur = con.cursor()
def reserve():
        airlinenamevalues=airlinenamevalue.get()
        airlinenovalues=airlinenovalue.get()
        routevalues=routevalue.get()
        journeyfromvalues=journeyfromvalue.get()
        journeytovalues=journeytovalue.get()
        depdates=depdate.get()
        classvalues=classvalue.get()

        res=con.cursor()
        q = "INSERT INTO airline(airlinenamevalue,airlinenovalue,routevalue,journeyfromvalue,journeytovalue,classvalue,depdate) VALUES(%s,%s,%s,%s,%s,%s,%s);"
        val=(airlinenamevalues,airlinenovalues,routevalues,journeyfromvalues,journeytovalues,classvalues,depdates)
        res.execute(q,val)
        con.commit()
        print("updated")
    
    #displaying a message when reserve button is clicked
        if (routevalue.get() == "Connecting Flight" and classvalue.get() == "Economic Class"):
            if (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nRoute: {}\nClass: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get(),routevalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 299".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 399".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 359".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Sacramento"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 249".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Denver"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "San Luis Obispo"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 199".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 279".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 289".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 399".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 299".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 222".format(journeyfromvalue.get(),journeytovalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
        #messagebox.showinfo("Reserved","YOUR SEAT HAS BEEN RESERVED SUCCESSFULLY")
        
        if (routevalue.get() == "Connecting Flight" and classvalue.get() == "Business Class"):
            if (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nRoute: {}\nClass: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get(),routevalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 420".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 599".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 590".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Sacramento"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 399".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Denver"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 599".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "San Luis Obispo"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 599".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 399".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 599".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 599".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 399".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 599".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
                
        elif (routevalue.get() == "Connecting Flight" and classvalue.get() == "Normal Class"):
            if (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nRoute: {}\nClass: {}\nTotal cost: $ 350".format(journeyfromvalue.get(),journeytovalue.get(),routevalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 150".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 300".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 250".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 450".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Sacramento"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 290".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Denver"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 390".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "San Luis Obispo"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 399".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 420".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 299".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 399".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 352".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 499".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 299".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 399".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 299".format(journeyfromvalue.get(),journeytovalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
                
        
        elif (routevalue.get() == "Straight Flight" and classvalue.get() == "Economic Class"):
            if (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nRoute: {}\nClass: {}\nTotal cost: $ 550".format(journeyfromvalue.get(),journeytovalue.get(),routevalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 350".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 500".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 450".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 550".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Sacramento"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 350".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Denver"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 500".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "San Luis Obispo"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 450".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 550".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 350".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 500".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 450".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 550".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 350".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 500".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 450".format(journeyfromvalue.get(),journeytovalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
                
        
        elif (routevalue.get() == "Straight Flight" and classvalue.get() == "Business Class"):
            if (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nRoute: {}\nClass: {}\nTotal cost: $ 750".format(journeyfromvalue.get(),journeytovalue.get(),routevalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 550".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 700".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 650".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 750".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Sacramento"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 550".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Denver"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 700".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "San Luis Obispo"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 650".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 850".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 550".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 690".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 650".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 750".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 550".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 600".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 659".format(journeyfromvalue.get(),journeytovalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
                
                
        elif (routevalue.get() == "Straight Flight" and classvalue.get() == "Normal Class"):
            if (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nRoute: {}\nClass: {}\nTotal cost: $ 450".format(journeyfromvalue.get(),journeytovalue.get(),routevalue.get(),classvalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 320".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 420".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Fransisco" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 380".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 480".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Sacramento"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 270".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "Denver"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 460".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Diego" and journeytovalue.get() == "San Luis Obispo"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 370".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 490".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 260".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Boston"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 410".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "Denver" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 380".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "New York"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 400".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Portland"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 250".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "Chicago"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 400".format(journeyfromvalue.get(),journeytovalue.get()))
            elif (journeyfromvalue.get() == "San Luis Obispo" and journeytovalue.get() == "San Jose"):
                messagebox.showinfo("BILL","From: {}\nTo: {}\nTotal cost: $ 300".format(journeyfromvalue.get(),journeytovalue.get()))
            else:
                messagebox.showerror("RESERVE ERROR","Source and Destination inputs are Invalid!!")
def main():
    f = Image.open("wp2956890-aeroplane-wallpaper-hd.jpg")  #opening background image
    f = f.resize((1366,720))        #setting size for background image
    f = ImageTk.PhotoImage(f)
    l=tk.Label(image=f)
    l.pack()
    
    #setting variables as global
    global routevalue
    global airlinenamevalue
    global airlinenovalue
    global journeyfromvalue
    global journeytovalue
    global classvalue
    
    frame_input=tk.Frame(w1,bg="goldenrod")       #using black color for background of the register frame
    frame_input.place(x=110,y=100,height=500,width=400)     #setting size for the register frame
    tk.Label(text="AIRLINE TICKET RESERVATION",font=("Century Gothic BOLD",18),bg="black",fg="white").place(x=125,y=135)    #setting a heading for the register frame with bg and fg
    
    #creating and placing attributes' label
    
    tk.Label(text="ROUTE",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=120,y=300)
    tk.Label(text="Flight NAME",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=120,y=200)
    tk.Label(text="Flight NO",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=120,y=250)
    tk.Label(text="JOURNEY FROM",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=120,y=350)
    tk.Label(text="JOURNEY TO",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=120,y=400)
    tk.Label(text="CLASS",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=120,y=450)
    tk.Label(text="DEPARTURE/JOURNEY DATE",font=("Century Gothic",10),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=120,y=500)
    
    #def disable_option(journeyfromlist):
    #    journeytoentry['menu'].entryconfigure(journeyfromlist, state = "disabled")
    
    #creating option lists
    
    journeyfromlist=["San Fransisco","San Diego","Dallas","Denver","San Luis Obispo"]
    journeyfromvalue.set("Select Country")
    journeytolist=["New York","San Jose","Boston","Chicago","Portland","Sacramento"]
    journeytovalue.set("Select Country")
    routelist=["Connecting Flight","Straight Flight"]
    routevalue.set("Select Route")
    
    #creating textfields
    
    routeentry = tk.OptionMenu(w1,routevalue, *routelist)
    routeentry.config(bg="darkgrey", fg="black")
    routeentry["menu"].config(bg="darkgrey")
    routeentry.pack()
    #quotaentry=tk.Entry(w1,fg="black",bg="darkgrey",textvariable=quotavalue)
    flightnameentry = tk.Entry(w1,fg="black",bg="darkgrey",textvariable=airlinenamevalue)
    flightnoentry = tk.Entry(w1,fg="black",bg="darkgrey",textvariable=airlinenovalue)
    journeyfromentry = tk.OptionMenu(w1, journeyfromvalue, *journeyfromlist)
    journeyfromentry.pack()
    journeyfromentry.config(bg="darkgrey", fg="black")
    journeyfromentry["menu"].config(bg="darkgrey")
    #for i in journeytolist:
    #    if(x == i):
    #        journeytolist.remove(i)
    journeytoentry = tk.OptionMenu(w1, journeytovalue, *journeytolist)
    #command = lambda journeytolist: disable_option(journeyfromlist)
    journeytoentry.pack()
    journeytoentry.config(bg="darkgrey", fg="black")
    journeytoentry["menu"].config(bg="darkgrey")
    classentry = ttk.Combobox(w1, textvariable=classvalue, values=["Economic Class","Business Class","Normal Class"],width=15)
    classentry.pack()
    depdate = DateEntry(w1,selectmode='day',fg="black",bg="darkgrey",font=("Ariel",11),width=13)
    depdate.place(x=320,y=500)
    
    #placing textfields
    
    routeentry.place(x=320,y=300)
    flightnameentry.place(x=320,y=200)
    flightnoentry.place(x=320,y=250)
    journeyfromentry.place(x=320,y=350)
    journeytoentry.place(x=320,y=400)
    classentry.place(x=320,y=450)
    
    #creating reserve button
    
    btn1=tk.Button(frame_input,text="RESERVE",font=("Century Gothic",10),bg="darkgrey",fg="black",command=reserve)
    btn1.place(x=150,y=450)
                
    
    
    w1.mainloop()       #used to display the above code
    
main()      #main function call

