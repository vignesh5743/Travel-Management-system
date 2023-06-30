from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import datetime as dt
import tkinter.ttk as tkrtk
import tkinter as tt
from tkinter import ttk
import tkinter.messagebox as mb
import mysql.connector
import mysql
from subprocess import call

con=mysql.connector.connect(host="localhost",user="root",password="vignesh2003",database="transport")
cur=con.cursor()

if con:
    print("connected")
else:
    print("connection error")
    

class transport:

    def __init__(self,root):
        self.root=root
        self.root.title("Project")
        self.root.geometry("1366x768")
        
        self.bg_frame = Image.open('image\\bus7.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        
        Pno = StringVar()
        Pname = StringVar()
        PAddress = StringVar()
        Pmobile = StringVar()
        email= StringVar()
            

        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        def clearData():
            self.txtPno.delete(0,END)
            self.txtPname.delete(0,END)
            self.txtPAddress.delete(0,END)
            self.txtPMobile.delete(0,END)
            self.txtemail.delete(0,END)

        
        '''self.txt = "CUSTOMER"
        self.heading = Label(self.root, text=self.txt, font=('yu gothic ui', 25, "bold"),
                             fg='Black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)'''

        '''self.lblTit = Label(self.root, font=('arial', 20, 'bold'),text="CUSTOMER",bg='#A7BCD6')
        self.lblTit.place(x=30, y=40, width=150, height=30)'''

        self.lgn_frame = Frame(self.root, bg='Black', width=540, height=450)
        self.lgn_frame.place(x=60, y=90)
        
        self.txt = "CUSTOMER"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="Black",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=20, y=30, width=200, height=30)
        
        self.username_label = Label(self.lgn_frame, text="Customer name:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))   
        self.username_label.place(x=35, y=80)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="White", fg="Black",
                                    font=("yu gothic ui ", 16, "bold"))
        self.username_entry.place(x=210, y=85, width=270)

        self.username_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=210, y=112)

        

        self.contact = Label(self.lgn_frame, text="Contact no:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))   
        self.contact.place(x=35, y=125)

        self.contact = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="White", fg="Black",
                                    font=("yu gothic ui ", 16, "bold"))
        self.contact.place(x=210, y=123, width=270)

        self.contact_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.contact_line.place(x=210, y=150)        

        self.dob=Label(self.lgn_frame, text="Date of Birth(DOB):", font=("yu gothic ui", 16, "bold"), bg='Black',fg="White")
        self.dob.place(x=35, y=170) 

        self.dobdata = DateEntry(self.lgn_frame, font=("Arial", 12), width=15)   
        self.dobdata.place(x=235, y=178)

        gender_strvar = StringVar()
        self.gender=Label(self.lgn_frame, text="Gender: ", font=("yu gothic ui ", 16, "bold"), bg="Black",fg="White")
        self.gender.place(x=35, y=220) 
        self.genderoption=ttk.Combobox(self.lgn_frame, textvariable= gender_strvar,state='readonly',font=("yu gothic ui ", 16),width=20)
        self.genderoption['value']=('Female','Male')
        self.genderoption.current(0)
        self.genderoption.place(x=130, y=220,width=100)

        self.email=Label(self.lgn_frame, text="Email ID:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))
        self.email.place(x=35,y=260)

        self.emailentry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="White", fg="Black",
                                    font=("yu gothic ui ", 16, "bold"))
        self.emailentry.place(x=140, y=265, width=270)

        self.email_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.email_line.place(x=140, y=290)



        self.pwd_label = Label(self.lgn_frame, text="Create password:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))   
        self.pwd_label.place(x=35, y=305)

        self.pwd_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="White", fg="Black",
                                    font=("yu gothic ui ", 16, "bold"))
        self.pwd_entry.place(x=210, y=310, width=270)

        self.pwd_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.pwd_line.place(x=210, y=335)



        #date = dobdata.dt.datetime.now()
        
        '''self.date = Label(self.lgn_frame, text="Contact no:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))   
        self.date.place(x=35, y=125)'''

        
        '''self.modes=Label(self.lgn_frame, text="Mode of transport", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))
        self.modes.place(x=95,y=310)

        mode_var=StringVar()
        self.modeoption=ttk.Combobox(self.lgn_frame, textvariable= mode_var,state='readonly',font=("yu gothic ui ", 16),width=20)
        self.modeoption['value']=('Bus','Train','Airlines')
        self.modeoption.current(0)
        self.modeoption.place(x=60, y=350,width=300)'''


        def submitted():

            name=StringVar()
            contact=StringVar()
            DOB=StringVar()
            Gender=StringVar()
            email=StringVar()
            pwd=StringVar()


            name=self.username_entry.get()
            contact=self.contact.get()
            DOB=self.dobdata.get()
            Gender=self.genderoption.get()
            email=self.emailentry.get()
            pwd=self.pwd_entry.get()
            res=con.cursor()
            res2=con.cursor()
            sql="insert into custdetails(name,contact,DOB,Gender,email,pwd) values(%s,%s,%s,%s,%s,%s)"
            sql2="insert into login(username,pwd) values(%s,%s)"
            val=(name,contact,DOB,Gender,email,pwd)
            val2=(name,pwd)
            res2.execute(sql2,val2)
            res.execute(sql,val)
            con.commit()
            print("login succesful")
            #mb.showinfo("success","registered")
            call(["python","logpg.py"])
            self.root.destroy()
            
        self.submit=Button(self.lgn_frame, text='Submit', font=("yu gothic ui", 16, "bold"),command=submitted,bg='White', width=9,activebackground="DeepSkyBlue2")
        self.submit.place(x=75, y=360)
        
        

        
def main():
    root = Tk()
    app=transport(root)
    root.mainloop()
main()
