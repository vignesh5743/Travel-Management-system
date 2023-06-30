from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import datetime

class transport:

    def __init__(self,root):
        self.root=root
        self.root.title("Project")
        self.root.geometry("1366x768")
        
        self.bg_frame = Image.open('image\\bus3.jpg')
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

        self.lgn_frame = Frame(self.root, bg='Black', width=950, height=600)
        self.lgn_frame.place(x=50, y=40)
        
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
        self.username_line.place(x=210, y=110)

        

        self.contact = Label(self.lgn_frame, text="Contact no:", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))   
        self.contact.place(x=35, y=125)

        self.contact = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="White", fg="Black",
                                    font=("yu gothic ui ", 16, "bold"))
        self.contact.place(x=210, y=130, width=270)

        self.contact_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.contact_line.place(x=210, y=155)        

        self.dob=Label(self.lgn_frame, text="Date of Birth (DOB)", font=("yu gothic ui", 16, "bold"), bg='Black',fg="White")
        self.dob.place(x=35, y=170) 

        self.dob = DateEntry(self.lgn_frame, font=("Arial", 12), width=15)   
        self.dob.place(x=235, y=178)

        self.dob=Label(self.lgn_frame, text="Gender", font=("yu gothic ui", 16, "bold"), bg='Black',fg="White")
        self.dob.place(x=35, y=210)
        
        gender_strvar=StringVar()
        self.gender=Label(self.lgn_frame, text="Gender",bg="White",fg="White",font=("yu gothic ui", 16, "bold"))
        self.gender=OptionMenu(self.lgn_frame, gender_strvar, 'Male', "Female")
        self.gender.place(x=120, y=210,width=100) 


        self.Email = Label(self.lgn_frame, text="Email", bg="Black", fg="White",
                                    font=("yu gothic ui", 16, "bold"))   
        self.Email.place(x=35, y=250)

        self.Email = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="White", fg="Black",
                                    font=("yu gothic ui ", 16, "bold"))
        self.Email.place(x=120, y=250, width=275)

        self.Email_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.Email_line.place(x=120, y=275)        


                

                  
def main():
    root = Tk()
    app=transport(root)
    root.mainloop()
main()
