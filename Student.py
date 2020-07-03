from tkinter import *
from tkinter import ttk
#import mysql.connector
import pymysql

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #---------- Variables --------------
        self.roll_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()


        # -------- Left Frame Input Details --------
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=590)

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        roll_no=Label(Manage_Frame,text="Roll Number:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        roll_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll=Entry(Manage_Frame,textvariable=self.roll_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=15,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=15,sticky="w")

        lbl_email=Label(Manage_Frame,text="Email:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=15,sticky="w")
        
        lbl_gender=Label(Manage_Frame,text="Gender:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        #combobox for selection of specific element
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=15,pady=10)

        lbl_contact=Label(Manage_Frame,text="Contact:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=15,sticky="w")

        lbl_DOB=Label(Manage_Frame,text="D.O.B:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_DOB=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=15,sticky="w")

        lbl_address=Label(Manage_Frame,text="Address:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        self.txt_address=Text(Manage_Frame,width=26,height=4,font=("",10))
        self.txt_address.grid(row=7,column=1,pady=10,padx=15,sticky="w")

        #--------------- Button Frame--------------

        Button_Frame=Frame(Manage_Frame,relief=RIDGE,bg="crimson")
        Button_Frame.place(x=15,y=520,width=420)
        
        Addbtn=Button(Button_Frame,text="Add",width=11,height=2,command=self.add_students)
        Addbtn.grid(row=0,column=0,padx=8,pady=10)

        updatebtn=Button(Button_Frame,text="Update",width=11,height=2,command=self.update_data)
        updatebtn.grid(row=0,column=1,padx=8,pady=10)

        deletebtn=Button(Button_Frame,text="Delete",width=11,height=2,command=self.delete_data)
        deletebtn.grid(row=0,column=2,padx=8,pady=10)

        clearbtn=Button(Button_Frame,text="Clear",width=11,height=2,command=self.clear)
        clearbtn.grid(row=0,column=3,padx=8,pady=10)


        # -------- Right Frame Display Frame ---------
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=810,height=590)

        lbl_search=Label(Detail_Frame,text="Search By:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Roll Number","Name","Contact")
        combo_search.grid(row=0,column=1,padx=15,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=15,sticky="w")

        Searchbtn=Button(Detail_Frame,text="Search",width=12,height=2,command=self.search_data)
        Searchbtn.grid(row=0,column=3,padx=8,pady=10) 

        showallbtn=Button(Detail_Frame,text="Show All",width=12,height=2,command=self.fetch_data)
        showallbtn.grid(row=0,column=4,padx=8,pady=10)


# ------------------ Table Frame ----------------
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=15,y=65,width=770,height=500)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_Table=ttk.Treeview(Table_Frame,columns=("Roll No","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)

        self.Student_Table.heading("Roll No",text="Roll No")
        self.Student_Table.heading("Name",text="Name")
        self.Student_Table.heading("Email",text="Email")
        self.Student_Table.heading("Gender",text="Gender")
        self.Student_Table.heading("Contact",text="Contact")
        self.Student_Table.heading("DOB",text="DOB")
        self.Student_Table.heading("Address",text="Address")
        self.Student_Table['show']='headings'
        self.Student_Table.column("Roll No",width=80)
        self.Student_Table.column("Name",width=150)
        self.Student_Table.column("Email",width=150)
        self.Student_Table.column("Gender",width=70)
        self.Student_Table.column("Contact",width=100)
        self.Student_Table.column("DOB",width=80)
        self.Student_Table.column("Address",width=150)
        self.Student_Table.pack(fill=BOTH,expand=1)
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="studentinfo")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s",(self.roll_var.get(),
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get('1.0',END)
                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="studentinfo")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
       self.roll_var.set("") 
       self.name_var.set("")
       self.email_var.set("")
       self.gender_var.set("")
       self.contact_var.set("")
       self.dob_var.set("")
       self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.Student_Table.focus()
        contents=self.Student_Table.item(cursor_row)
        row=contents['values']
        self.roll_var.set(row[0]) 
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
    
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="studentinfo")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),
                                                                                                                  self.email_var.get(),
                                                                                                                  self.gender_var.get(),
                                                                                                                  self.contact_var.get(),
                                                                                                                  self.dob_var.get(),
                                                                                                                  self.txt_address.get('1.0',END),
                                                                                                                  self.roll_var.get()
                                                                                                                  ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="studentinfo")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="studentinfo")
        cur=con.cursor()
        cur.execute("select * from students where"+str(self.search_by.get())+"LIKE %"+str(self.search_txt.get())+"%")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

root=Tk()
ob=Student(root)
root.mainloop()