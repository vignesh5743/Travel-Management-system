import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
r=tk.Tk()
r.title("Airline details")
r.geometry("600x300")

con=mysql.connector.connect(host="localhost",user="root",password="vignesh2003",database="transport")
cur=con.cursor()

if con:
    print("connected")
else:
    print("connection error")


cur.execute("SELECT * FROM train")
tree=ttk.Treeview(r)
tree['show']='headings'


s=ttk.Style(r)
s.theme_use("clam")

s.configure(".",font=('Helventica',11))
            
s.configure("Treeview.Heading",foreground='red',font=('Helventica',11,"bold"))

tree["columns"]=("airlinenamevalue","airlinenovalue","routevalue","journeyfromvalue","journeytovalue","classvalue","depdate")
tree.column("airlinenamevalue",width=50,minwidth=150,anchor=tk.CENTER)
tree.column("airlinenovalue",width=100,minwidth=130,anchor=tk.CENTER)
tree.column("routevalue",width=150,minwidth=100,anchor=tk.CENTER)
tree.column("journeyfromvalue",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("journeytovalue",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("classvalue",width=150,minwidth=100,anchor=tk.CENTER)
tree.column("depdate",width=150,minwidth=150,anchor=tk.CENTER)

tree.heading("airlinenamevalue",text="airlinenamevalue",anchor=tk.CENTER)
tree.heading("airlinenovalue",text="airlinenovalue",anchor=tk.CENTER)
tree.heading("routevalue",text="routevalue",anchor=tk.CENTER)
tree.heading("journeyfromvalue",text="journeyfromvalue",anchor=tk.CENTER)
tree.heading("journeytovalue",text="journeytovalue",anchor=tk.CENTER)
tree.heading("classvalue",text="classvalue",anchor=tk.CENTER)
tree.heading("depdate",text="depdate",anchor=tk.CENTER)


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
          
