import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
r=tk.Tk()
r.title("Bus details")
r.geometry("600x300")

con=mysql.connector.connect(host="localhost",user="root",password="vignesh2003",database="transport")
cur=con.cursor()

if con:
    print("connected")
else:
    print("connection error")


cur.execute("SELECT * FROM buses")
tree=ttk.Treeview(r)
tree['show']='headings'


s=ttk.Style(r)
s.theme_use("clam")

s.configure(".",font=('Helventica',11))
            
s.configure("Treeview.Heading",foreground='red',font=('Helventica',11,"bold"))

tree["columns"]=("name","start","end","dateofjourney","classes","seat_no","mode")
tree.column("name",width=50,minwidth=50,anchor=tk.CENTER)
tree.column("start",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("end",width=150,minwidth=50,anchor=tk.CENTER)
tree.column("dateofjourney",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("classes",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("seat_no",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("mode",width=150,minwidth=150,anchor=tk.CENTER)

tree.heading("name",text="Name",anchor=tk.CENTER)
tree.heading("start",text="start",anchor=tk.CENTER)
tree.heading("end",text="designation",anchor=tk.CENTER)
tree.heading("dateofjourney",text="dateofjourney",anchor=tk.CENTER)
tree.heading("classes",text="classes",anchor=tk.CENTER)
tree.heading("seat_no",text="seat_no",anchor=tk.CENTER)
tree.heading("mode",text="Mode",anchor=tk.CENTER)


i=0
for ro in cur:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6]))
    i=i+1

hab=ttk.Scrollbar(r,orient="horizontal")
hab.configure(command=tree.xview)
tree.configure(xscrollcommand=hab.set)
hab.pack(fill=X,side=BOTTOM)

tree.pack()
r.mainloop()
          
