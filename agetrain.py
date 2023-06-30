import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
r=tk.Tk()
r.title("Train details")
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

tree["columns"]=("quotavalue","trainnamevalue","trainnovalue","journeyfromvalue","journeytovalue","depdate","classvalue")
tree.column("quotavalue",width=50,minwidth=50,anchor=tk.CENTER)
tree.column("trainnamevalue",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("trainnovalue",width=150,minwidth=50,anchor=tk.CENTER)
tree.column("journeyfromvalue",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("journeytovalue",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("depdate",width=150,minwidth=150,anchor=tk.CENTER)
tree.column("classvalue",width=150,minwidth=150,anchor=tk.CENTER)


tree.heading("quotavalue",text="quotavalue",anchor=tk.CENTER)
tree.heading("trainnamevalue",text="trainnamevalue",anchor=tk.CENTER)
tree.heading("trainnovalue",text="trainnovalue",anchor=tk.CENTER)
tree.heading("journeyfromvalue",text="journeyfromvalue",anchor=tk.CENTER)
tree.heading("journeytovalue",text="journeytovalue",anchor=tk.CENTER)
tree.heading("depdate",text="depdate",anchor=tk.CENTER)
tree.heading("classvalue",text="classvalue",anchor=tk.CENTER)


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
          
