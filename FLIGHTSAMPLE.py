import tkinter as tk    #tkinter for gui
import sys
from tkinter import messagebox
from tkcalendar import Calendar
from PIL import ImageTk, Image  #PIL for opening jpeg or jpg formatted images

w1=tk.Tk()
w1.geometry("1366x720")     #size of the window
w1.title("REGISTER")
#variables storing entered data

quotavalue=tk.StringVar()
trainnamevalue=tk.StringVar()
trainnovalue=tk.IntVar()
journeyfromvalue=tk.StringVar()
journeytovalue=tk.StringVar()
classvalue=tk.StringVar()

def reserve1():
    #displaying a message when reserve button is clicked
    messagebox.showinfo("Reserved","YOUR SEAT HAS BEEN RESERVED SUCCESSFULLY")

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
    
    
    frame_input=tk.Frame(w1,bg='#000000')       #using black color for background of the register frame
    frame_input.place(x=820,y=100,height=500,width=400)     #setting size for the register frame
    tk.Label(text="AIRLINE TICKET RESERVATION",font=("Century Gothic BOLD",18),bg="black",fg="grey").place(x=833,y=150)    #setting a heading for the register frame with bg and fg
    
    #creating and placing attributes' label
    
    tk.Label(text="RESERVATION QUOTA",font=("Century Gothic",9),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=200)
    tk.Label(text="AIRLINE NAME",font=("Century Gothic",9),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=250)
    tk.Label(text="FLIGHT NO",font=("Century Gothic",9),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=300)
    tk.Label(text="JOURNEY FROM",font=("Century Gothic",9),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=350)
    tk.Label(text="JOURNEY TO",font=("Century Gothic",9),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=400)
    tk.Label(text="CLASS",font=("Century Gothic",9),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=450)
    tk.Label(text="DEPARTURE/JOURNEY DATE",font=("Century Gothic",9),fg="black",borderwidth=3,relief=tk.RIDGE).place(x=840,y=500)
    
    #creating textfields
    
    quotaentry=tk.Entry(w1,fg="black",bg="darkgrey",textvariable=quotavalue)
    trainnameentry=tk.Entry(w1,fg="black",bg="darkgrey",textvariable=trainnamevalue)
    trainnoentry=tk.Entry(w1,fg="black",bg="darkgrey",textvariable=trainnovalue)
    journeyfromentry=tk.Entry(w1,fg="black",bg="darkgrey",textvariable=journeyfromvalue)
    journeytoentry=tk.Entry(w1,fg="black",bg="darkgrey",textvariable=journeytovalue)
    classentry=tk.Entry(w1,fg="black",bg="darkgrey",textvariable=classvalue)
    
    #placing textfields
    
    quotaentry.place(x=1040,y=200)
    trainnameentry.place(x=1040,y=250)
    trainnoentry.place(x=1040,y=300)
    journeyfromentry.place(x=1040,y=350)
    journeytoentry.place(x=1040,y=400)
    classentry.place(x=1040,y=450)
    
    #adding calandar
    
    cal = Calendar(w1, selectmode = 'day',year = 2020, month = 5,day = 22)
    cal.pack(pady = 20)
    date = tk.Label(w1, text = "")
    date.pack(pady = 20)
    
    #creating reserve button
    
    btn1=tk.Button(frame_input,text="RESERVE",font=("Century Gothic",10),bg="darkgrey",fg="black",command=reserve1)
    btn1.place(x=150,y=450)
    
    
    w1.mainloop()       #used to display the above code
    
main()      #main function call
