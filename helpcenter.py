from tkinter import *
from tkinter import ttk
root = Tk()
login = Frame()
dashboard = Frame()
Personaldetails = Frame()
Calldetails = Frame()
Specialist = Frame()
Problems = Frame()

login.place(x=0,y=0, relheight=1, relwidth=1)
dashboard.place(x=0,y=0, relheight=1, relwidth=1)
Personaldetails.place(x=0,y=0, relheight=1, relwidth=1)
Calldetails.place(x=0,y=0, relheight=1, relwidth=1)
Specialist.place(x=0,y=0, relheight=1, relwidth=1)
Problems.place(x=0,y=0, relheight=1, relwidth=1)
login.lift()

# login
def gotologin(root,gotologin):
    login.lift()



l1 = Label(login,text="Username")
l1.pack()
e1 = Entry(login)
e1.pack()

l2 = Label(login,text="Password")
l2.pack()
e2 = Entry(login,show="*")
e2.pack()

from tkinter import messagebox
def gotologin():
    if e1.get() == "Nishan"and e2.get() == "Yonjan":
        messagebox.showinfo("a","Login sucessful")
        dashboard.lift()
    else:
        messagebox.showinfo("b","Invalid username or password")    

b2 = Button(login,text="Login",command=gotologin)
b2.pack()

# dashboard
def gotodashboard():
    dashboard.lift()

def gotoPersonaldetails():
    Personaldetails.lift()

def gotoCalldetails():
    Calldetails.lift()

def gotoSpecialist():
    Specialist.lift()

def gotoProblems():
    Problems.lift()

d_b1 = Button(dashboard,text="personaldetails",command=gotoPersonaldetails)
d_b2 = Button(dashboard,text="Calldetails",command=gotoCalldetails)
d_b3 = Button(dashboard,text="Specialist",command=gotoSpecialist)
d_b4 = Button(dashboard,text="Problems",command=gotoProblems)
d_b1.pack()
d_b2.pack()
d_b3.pack()
d_b4.pack()

#Personal details
from tkinter import ttk
import psycopg2
connection = psycopg2.connect(
  host='localhost',
  database='assignment',
  user='postgres',
  password='Mushashi416'
)
cursor = connection.cursor()
cursor.execute("select * from Personaldetails")
c = cursor.fetchall()

p_b1 = Button (Personaldetails,text='Go back',command=gotodashboard)
p_b1.pack()
p_l1 = Label(Personaldetails,text="Personal Details List")
p_l1.pack()

p_tree = ttk.Treeview(Personaldetails,columns=['a','b','c'])
p_tree['show'] = 'headings'
p_tree.heading('a',text='Id')
p_tree.heading('b',text='Job title')
p_tree.heading('c',text='Department')
p_tree.pack()

p_l2 = Label(Personaldetails,text="Id")
p_l2.pack()
p_e2 = Entry(Personaldetails)
p_e2.pack()

p_l3 = Label(Personaldetails,text="Job title")
p_l3.pack()
p_e3 = Entry(Personaldetails)
p_e3.pack()

p_l4 = Label(Personaldetails,text="Department")
p_l4.pack()
p_e4 = Entry(Personaldetails)
p_e4.pack()

def insert_Personaldetails():
    cursor = connection.cursor()
    cursor.execute(f"""insert into Personaldetails values({p_e2.get()},'{p_e3.get()}','{p_e4.get()}')""")
    connection.commit()
    p_tree.insert("",END,values=(p_e2.get(),p_e3.get(),p_e4.get(),"yes"))
    p_e2.delete(0,END)
    p_e3.delete(0,END)
    p_e4.delete(0,END)

p_b3 = Button(Personaldetails,text="Add",command=insert_Personaldetails)
p_b3.pack()    

def delete_Personaldetails():
    id = p_tree.focus()
    if id:
        p_tree.delete(id)

p_b4 = Button(Personaldetails,text="delete",command=delete_Personaldetails)        
p_b4.pack()

#calldetails
from tkinter import ttk
from datetime import datetime
import psycopg2
connection = psycopg2.connect(
  host='localhost',
  database='assignment',
  user='postgres',
  password='Mushashi416'
)
cursor = connection.cursor()
cursor.execute("select * from Calldetails")
c = cursor.fetchall()
c_b1 = Button(Calldetails,text='go back',command=gotodashboard)
c_b1.pack()
c_l1 = Label(Calldetails,text="Caller Details")
c_l1.pack()

c_tree = ttk.Treeview(Calldetails,column=['a','b','c','d','e','f','g','h'])
c_tree['show'] = 'headings'
c_tree.heading('a',text="Caller id")
c_tree.heading('b',text="Caller Name")
c_tree.heading('c',text="Operator id")
c_tree.heading('d',text="Operator Name")
c_tree.heading('e',text="Problem")
c_tree.heading('f',text="Problem Discription")
c_tree.heading('g',text="Software id")
c_tree.heading('h',text="Call time")
c_tree.pack()

c_l1 = Label(Calldetails,text="Caller id")
c_l1.pack()
c_e1 = Entry(Calldetails)
c_e1.pack()

c_l2 = Label(Calldetails,text="Caller Name")
c_l2.pack()
c_e2 = Entry(Calldetails)
c_e2.pack()

c_l3 = Label(Calldetails,text="Operator id")
c_l3.pack()
c_e3 = Entry(Calldetails)
c_e3.pack()

c_l4 = Label(Calldetails,text="Operator Name")
c_l4.pack()
c_e4 = Entry(Calldetails)
c_e4.pack()

c_l5 = Label(Calldetails,text="Problem")
c_l5.pack()
c_e5 = Entry(Calldetails)
c_e5.pack()

c_l6 = Label(Calldetails,text="Problem Description")
c_l6.pack()
c_e6 = Entry(Calldetails)
c_e6.pack()

c_l7 = Label(Calldetails,text="Software id")
c_l7.pack()
c_e7 = Entry(Calldetails)
c_e7.pack()



def insert_Calldetails():
    calltime = datetime.now()
    cursor = connection.cursor()
    cursor.execute(f"""insert into Calldetails values({c_e1.get()},'{c_e2.get()}',{c_e3.get()},'{c_e4.get()}','{c_e5.get()}','{c_e6.get()}',{c_e7.get()},'{calltime}')""")
    connection.commit()
    

    c_tree.insert("",END,values=(c_e1.get(),c_e2.get(),c_e3.get(),c_e4.get(),c_e5.get(),c_e6.get(),c_e7.get(),calltime,"yes"))
    c_e1.delete(0,END) 
    c_e2.delete(0,END) 
    c_e3.delete(0,END)
    c_e4.delete(0,END)
    c_e5.delete(0,END)
    c_e6.delete(0,END)
    c_e7.delete(0,END) 
    

c_b2 = Button(Calldetails,text="Add",command=insert_Calldetails)
c_b2.pack()

def delete_Calldetails():
    caller = c_tree.focus()
    if caller:
        c_tree.delete(caller)

c_b3 = Button(Calldetails,text="delete",command=delete_Calldetails)
c_b3.pack()

#specialist
from tkinter import ttk
import psycopg2
connection = psycopg2.connect(
  host='localhost',
  database='assignment',
  user='postgres',
  password='Mushashi416'
)
cursor = connection.cursor()
cursor.execute("select * from Specialist")
c = cursor.fetchall()
s_b1 = Button (Specialist,text='Go back',command=gotodashboard)
s_b1.pack()
s_l1 = Label(Specialist,text="Specialist")
s_l1.pack()

s_tree = ttk.Treeview(Specialist,columns=['a','b','c','d','e'])
s_tree['show'] = 'headings'
s_tree.heading('a',text='Specialist id')
s_tree.heading('b',text='Specialist Name')
s_tree.heading('c',text='Experties')
s_tree.heading('d',text='Pending work')
s_tree.heading('e',text='Completed')
s_tree.pack()

s_l2 = Label(Specialist,text=" Specialist id")
s_l2.pack()
s_e2 = Entry(Specialist)
s_e2.pack()

s_l3 = Label(Specialist,text="Specialist Name")
s_l3.pack()
s_e3 = Entry(Specialist)
s_e3.pack()

s_l4 = Label(Specialist,text="Experties")
s_l4.pack()
s_e4 = Entry(Specialist)
s_e4.pack()

s_l5 = Label(Specialist,text="Pending Work")
s_l5.pack()
s_e5 = Entry(Specialist)
s_e5.pack()

s_l6 = Label(Specialist,text="Completed")
s_l6.pack()
s_e6 = Entry(Specialist)
s_e6.pack()

def insert_Specialist():
    cursor = connection.cursor()
    cursor.execute(f"""insert into Specialist values({s_e2.get()},'{s_e3.get()}','{s_e4.get()}',{s_e5.get()},{s_e6.get()})""")
    connection.commit()

    s_tree.insert("",END,values=(s_e2.get(),s_e3.get(),s_e4.get(),s_e5.get(),s_e6.get(),"yes"))
    s_e2.delete(0,END)
    s_e3.delete(0,END)
    s_e4.delete(0,END)
    s_e5.delete(0,END)
    s_e6.delete(0,END)

s_b3 = Button(Specialist,text="Add",command=insert_Specialist)
s_b3.pack()    

def delete_Specialist():
    id = s_tree.focus()
    if id:
        s_tree.delete(id)

s_b4 = Button(Specialist,text="delete",command=delete_Specialist)        
s_b4.pack()

#problems page
from tkinter import ttk
import psycopg2
connection = psycopg2.connect(
  host='localhost',
  database='assignment',
  user='postgres',
  password='Mushashi416'
)
cursor = connection.cursor()
cursor.execute("select * from Problems")
c = cursor.fetchall()
i_b1 = Button(Problems,text='go back',command=gotodashboard)
i_b1.pack()
i_l1 = Label(Problems,text="Problems")
i_l1.pack()

i_tree = ttk.Treeview(Problems,column=['a','b','c','d','e','f','g','h'])
i_tree['show'] = 'headings'
i_tree.heading('a',text="Problem id")
i_tree.heading('b',text="Problem type")
i_tree.heading('c',text="Problem")
i_tree.heading('d',text="Discription")
i_tree.heading('e',text="Specialist id")
i_tree.heading('f',text="Status")
i_tree.heading('g',text="Resolution")


i_tree.pack()

i_l1 = Label(Problems,text="Problem id")
i_l1.pack()
i_e1 = Entry(Problems)
i_e1.pack()

i_l2 = Label(Problems,text="Problem type")
i_l2.pack()
i_e2 = Entry(Problems)
i_e2.pack()

i_l3 = Label(Problems,text="Problem")
i_l3.pack()
i_e3 = Entry(Problems)
i_e3.pack()

i_l4 = Label(Problems,text="Discription")
i_l4.pack()
i_e4 = Entry(Problems)
i_e4.pack()

i_l5 = Label(Problems,text="Specialist id")
i_l5.pack()
i_e5 = Entry(Problems)
i_e5.pack()

i_l6 = Label(Problems,text="Status")
i_l6.pack()
i_e6 = Entry(Problems)
i_e6.pack()

i_l7 = Label(Problems,text="Resolution")
i_l7.pack()
i_e7 = Entry(Problems)
i_e7.pack()




def insert_Problems():
    cursor = connection.cursor()
    cursor.execute(f"""Insert into Problems values({i_e1.get()},'{i_e2.get()}','{i_e3.get()}','{i_e4.get()}',{i_e5.get()},'{i_e6.get()}','{i_e7.get()}')""")
    connection.commit()

    i_tree.insert("",END,values=(i_e1.get(),i_e2.get(),i_e3.get(),i_e4.get(),i_e5.get(),i_e6.get(),i_e7.get(),"yes"))
    i_e1.delete(0,END) 
    i_e2.delete(0,END) 
    i_e3.delete(0,END)
    i_e4.delete(0,END)
    i_e5.delete(0,END)
    i_e6.delete(0,END)
    i_e7.delete(0,END) 



i_b2 = Button(Problems,text="Add New Problem",command=insert_Problems)
i_b2.pack()

def delete_Problems():
    Problemid = i_tree.focus()
    if Problemid:
        i_tree.delete(Problemid)

i_b3 = Button(Problems,text="delete",command=delete_Problems)
i_b3.pack()

root.geometry('500x500')
root.mainloop()
