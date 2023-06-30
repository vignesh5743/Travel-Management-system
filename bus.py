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
    

class bus:

    def __init__(self,root):
        self.root=root
        self.root.title("Project")
        self.root.geometry("1366x768")
        
        self.bg_frame = Image.open('image\\b10.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        total_cost=StringVar()

        self.lgn_frame = Frame(self.root, bg='Black', width=500, height=450)
        self.lgn_frame.place(x=110, y=60)
        
        self.txt = "BUS TICKET BOOKING"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 20, "bold underline"), bg="Black",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=20, y=30, width=500, height=30)
        
        self.username_label = Label(self.lgn_frame, text="Name:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))   
        self.username_label.place(x=35, y=80)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="White", fg="Black",
                                    font=("yu gothic ui ", 16, "bold"))
        self.username_entry.place(x=140, y=85, width=260)

        self.username_line = Canvas(self.lgn_frame, width=260, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=140, y=110)

     
        '''self.tickets=Label(self.lgn_frame,text="Number of tickets:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))
        self.tickets.place(x=35,y=120)

        self.ticketbox=Spinbox(self.lgn_frame,from_=0,to=50)
        self.ticketbox.place(x=245,y=130,width=150)'''

        self.start=Label(self.lgn_frame,text="From:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))
        self.start.place(x=35,y=125)

        start_var=StringVar()
        self.startoption=ttk.Combobox(self.lgn_frame, textvariable= start_var,state='readonly',font=("yu gothic ui ", 16),width=20)
        self.startoption['value']=('madurai','sivakasi','chennai','coimbatore','rameswaram')
        self.startoption.current(0)
        self.startoption.place(x=140, y=125,width=200)


        self.to=Label(self.lgn_frame,text="To:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))
        self.to.place(x=35,y=170)

        end_var=StringVar()
        self.endoption=ttk.Combobox(self.lgn_frame, textvariable= end_var,state='readonly',font=("yu gothic ui ", 16),width=20)
        self.endoption['value']=('madurai','sivakasi','chennai','coimbatore','rameswaram')
        self.endoption.current(0)
        self.endoption.place(x=140, y=170,width=200)

        self.doj=Label(self.lgn_frame, text="Date of Journey:", font=("yu gothic ui", 16, "bold"), bg='Black',fg="White")
        self.doj.place(x=35, y=210) 

        self.dobdata = DateEntry(self.lgn_frame, font=("Arial", 12), width=15)   
        self.dobdata.place(x=230, y=218)

        date = dt.datetime.now()
        self.dates=Label(self.lgn_frame,text=f"{date:%A, %B %d, %Y}",font="Calibri",fg="White",bg="Black")
        self.dates.place(x=95,y=380)

        self.to=Label(self.lgn_frame,text="Type:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))
        self.to.place(x=35,y=260)
        
        varient=StringVar()

        self.coach=ttk.Combobox(self.lgn_frame, textvariable= varient,state='readonly',font=("yu gothic ui ", 16),width=20)
        self.coach['value']=('sleeper','semi-sleeper','sleeper A/C','Semi-sleeper A/C')
        self.coach.current(0)
        self.coach.place(x=140, y=265,width=200)
        

        '''self.seat_label = Label(self.lgn_frame, text="Seat no:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))   
        self.seat_label.place(x=35, y=305)

        self.seat_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="White", fg="Black",
                                    font=("yu gothic ui ", 16, "bold"))
        self.seat_entry.place(x=140, y=310, width=200)'''

        self.seat_label = Label(self.lgn_frame, text="Seat no:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))   
        self.seat_label.place(x=35, y=305)

        vari=StringVar()
        self.seat_entry=ttk.Combobox(self.lgn_frame,textvariable= vari,state='readonly',font=("yu gothic ui ", 16),width=20)
        self.seat_entry['value']=('seat 1','seat 2','seat 3','seat 4','seat 5','seat 6','seat 7','seat 8','seat 9','seat 10')
        self.seat_entry.current(0)
        self.seat_entry.place(x=150,y=315)

        

        

        

        #=====================Bill areea====================
        

        F3 =Frame(root,bg='#2D9290',bd=15,relief=RIDGE)
        F3.place(x=30, y=590,width=1300,height=120)

        '''btn1 = Button(F3, text='Total', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=self.total)
        btn1.grid(row=0,column=0,padx=20,pady=10)'''
        
        btn2 = Button(F3, text='Receipt', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=self.receipt)
        btn2.grid(row=0,column=1,padx=10,pady=10)

        '''btn3 = Button(F3, text='Seat chart',font='arial 25 bold', padx=15, pady=5, bg='yellow',fg='red',width=10,command=self.chart)
        btn3.grid(row=0,column=40,padx=20,pady=10)'''

        btn4 = Button(F3,text='Book',font='arial 25 bold', padx=15, pady=5, bg='yellow',fg='red',width=10,command=self.book)
        btn4.grid(row=0,column=50,padx=50,pady=10)

        
        btn5 = Button(F3,text='Back',font='arial 25 bold', padx=15, pady=5, bg='yellow',fg='red',width=10,command=self.back)
        btn5.grid(row=0,column=70,padx=80,pady=10)
       

        #===========BIOOKING===============================
    def book(self):
        name=StringVar()
        start=StringVar()
        end=StringVar()
        dateofjourney=StringVar()
        classes=StringVar()
        seat_no=StringVar()
        
        name=self.username_entry.get()
        start=self.startoption.get()
        end=self.endoption.get()
        dateofjourney=self.dobdata.get()
        classes=self.coach.get()
        seat_no=self.seat_entry.get()
        

        res=con.cursor()
        sql="insert into bus(name,start,end,dateofjourney,classes,seat_no) values(%s,%s,%s,%s,%s,%s)"
        val=(name,start,end,dateofjourney,classes,seat_no)
        res.execute(sql,val)
        con.commit()
        print("updated")
        mb.showinfo("booking","booked successfully")
            
    
    #=============================================================

    def chart(self):
        
        self.seat_frame = Image.open('modes\\seatplan.jpg')
        photo = ImageTk.PhotoImage(self.seat_frame)
        self.seat_panel = Label(self.root, image=photo)
        self.seat_panel.image = photo
        self.seat_panel.place(x=900,y=50)
        self.seat_panel.after(5000,lambda:self.seat_panel.destroy())

    def receipt(self):

        F2=Frame(self.root,relief=GROOVE,bd=10)
        F2.place(x=820,y=90,width=430,height=500)
        bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F2,orient=VERTICAL)
        scrol_y.pack(side=RIGHT,fill=Y)
        textarea=Text(F2,font='arial 15',yscrollcommand=scrol_y.set)
        textarea.pack(fill=BOTH)
        scrol_y.config(command=textarea.yview)

        name=StringVar()
        start=StringVar()
        end=StringVar()
        dj=StringVar()
        model=StringVar()
        seat=StringVar()
        total_cost=StringVar()

        name=self.username_entry.get()
        start=self.startoption.get()
        end=self.endoption.get()
        dj=self.dobdata.get()
        model=self.coach.get()
        seat=self.seat_entry.get()
        
        if self.startoption.get()=="madurai" and self.endoption.get()=="sivakasi":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 175")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 250")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 200")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 150")
        elif self.startoption.get()=="madurai" and self.endoption.get()=="chennai":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 500")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 920")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 420")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 319")
            
        elif self.startoption.get()=="madurai" and self.endoption.get()=="coimbatore":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 500")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 920")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 420")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 319")
                
        elif self.startoption.get()=="madurai" and self.endoption.get()=="rameswaram":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 555")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 890")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 420")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 351")
                



        elif self.startoption.get()=="sivakasi" and self.endoption.get()=="madurai":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 200")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 500")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 150")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 100")
                
        elif self.startoption.get()=="sivakasi" and self.endoption.get()=="chennai":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 700")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 1075")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 500")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 450")
        elif self.startoption.get()=="sivakasi" and self.endoption.get()=="coimbatore":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 600")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 750")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 500")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 360")
        elif self.startoption.get()=="sivakasi" and self.endoption.get()=="rameswaram":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 450")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 350")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 150")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 250")
        elif self.startoption.get()=="coimbatore" and self.endoption.get()=="sivakasi":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 980")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 1050")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 615")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 532")
        elif self.startoption.get()=="coimbatore" and self.endoption.get()=="chennai":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 687")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 954")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 547")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 460")
        elif self.startoption.get()=="coimbatore" and self.endoption.get()=="madurai":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 650")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 789")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 453")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 456")
        elif self.startoption.get()=="coimbatore" and self.endoption.get()=="rameswaram":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 687")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 954")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 547")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 460")

        elif self.startoption.get()=="chennai" and self.endoption.get()=="coimbatore":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 654")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 568")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 487")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 367")
        elif self.startoption.get()=="chennai" and self.endoption.get()=="sivakasi":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 654")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 568")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 487")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 367")
        elif self.startoption.get()=="chennai" and self.endoption.get()=="rameswaram":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 654")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 568")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 487")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 367")
        elif self.startoption.get()=="chennai" and self.endoption.get()=="madurai":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 654")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 568")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 487")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 367")

        elif self.startoption.get()=="rameswaram" and self.endoption.get()=="chennai":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 412")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 556")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 789")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 356")
        elif self.startoption.get()=="rameswaram" and self.endoption.get()=="coimbatore":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 876")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 789")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 456")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 367")
        elif self.startoption.get()=="rameswaram" and self.endoption.get()=="sivakasi":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 789")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 654")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 753")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 528")
        elif self.startoption.get()=="rameswaram" and self.endoption.get()=="madurai":
            if self.coach.get()=="sleeper":
                total_cost.set("₹ 756")
            elif self.coach.get()=="sleeper A/C":
                total_cost.set("₹ 654")
            elif self.coach.get()=="Semi-sleeper A/C":
                total_cost.set("₹ 456")
            elif self.coach.get()=="semi-sleeper":
                total_cost.set("₹ 654")
        
        textarea.delete(1.0,END)
        textarea.insert(END,' \t       SHA TRAVELS\n')
        textarea.insert(END, f"\t      *******************")
        textarea.insert(END,f'\nName:\t\t{self.username_entry.get()}\t')
        textarea.insert(END,f'\n\nStart:\t\t{self.startoption.get()}\t')
        textarea.insert(END,f'\n\nEnd:\t\t{self.endoption.get()}\t')
        textarea.insert(END,f'\n\nDateofJourney:\t\t{self.dobdata.get()}\t')
        textarea.insert(END,f'\n\nClass:\t\t{self.coach.get()}\t')
        
        textarea.insert(END,f'\n\nSeatno:\t\t{self.seat_entry.get()}\t')
        textarea.insert(END, f"\n\n================================")
        textarea.insert(END,f'\nTotal Price\t\t{total_cost.get()}')
        textarea.insert(END, f"\n================================")

        
    def print(self):
        q=textarea.get('1.0','end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'Print')

    def back(self):
        call(["python","modes.py"])
        self.root.destroy()
        
    
def main():
    root = Tk()
    app=bus(root)
    root.mainloop()
main()
