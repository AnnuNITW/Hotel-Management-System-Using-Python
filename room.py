from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')
        
        #   Variable
        
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailables=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        #===============Title========================
        title=Label(self.root,text='ROOM BOOKING DETAILS',font=('times new roman',18,'bold'),fg='gold',bg='black',bd=4,relief=RIDGE)
        title.place(x=0,y=0,width=1295,height=50)
        
        #================Logo=======================
       
        img2=Image.open(r'C:\Users\Hp\Desktop\logo.png')
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lableimg1=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lableimg1.place(x=5,y=2,width=100,height=40)
        #===============Label========================
        
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Roombooking Detail',padx=2,font=('times new roman',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=490) 
        #================Label and Entry=======================
        
        #cust contact
        
        st_contact=Label(labelframeleft,text='Customer Contact:',padx=2,pady=6,font=('times new roman',12,'bold'))
        st_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=('times new roman',13,'bold'))
        entry_contact.grid(row=0,column=1,sticky=W)
        
        #fetch data button
        
        btn_Fetchbutton=Button(labelframeleft,text='Fetch Button',command=self.fetch_contact,font=('times new roman',8,'bold'),bg='black',fg='gold',width=9)
        btn_Fetchbutton.place(x=345,y=4)
        
        # Check in Date
        
        Check_in_Date=Label(labelframeleft,text='Check_in Date:',padx=2,pady=6,font=('times new roman',12,'bold'))
        Check_in_Date.grid(row=1,column=0,sticky=W)

        txt_Check_in_Date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=('times new roman',13,'bold'))
        txt_Check_in_Date.grid(row=1,column=1)
        
        # Check out Date
        
        Check_out_Date=Label(labelframeleft,text='Check_out Date:',padx=2,pady=6,font=('times new roman',12,'bold'))
        Check_out_Date.grid(row=2,column=0,sticky=W)

        txt_Check_out_Date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=('times new roman',13,'bold'))
        txt_Check_out_Date.grid(row=2,column=1)
        
        #roomtype combobox
        
        roomtype=Label(labelframeleft,text='Room Type:',padx=2,pady=6,font=('times new roman',12,'bold'))
        roomtype.grid(row=3,column=0,sticky=W)
        
        #To fetch data 
        conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
        con_cursor=conn.cursor()
        con_cursor.execute('select RoomType from details')
        ide=con_cursor.fetchall()
        

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=('times new roman',13,'bold'),width=27,state='readonly')
        combo_roomtype['value']=ide
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)
        
        #Room available 
              
        Avaialableroom=Label(labelframeleft,text='Available Room:',padx=2,pady=6,font=('times new roman',12,'bold'))
        Avaialableroom.grid(row=4,column=0,sticky=W)

        #txt_Avaialableroom=ttk.Entry(labelframeleft,textvariable=self.var_roomavailables,width=29,font=('times new roman',13,'bold'))
        #txt_Avaialableroom.grid(row=4,column=1)
      
       #To fetch data 
        conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
        con_cursor=conn.cursor()
        con_cursor.execute('select RoomNo from details')
        rows=con_cursor.fetchall()
        
        combo_roomno=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailables,font=('times new roman',13,'bold'),width=27,state='readonly')
        combo_roomno['value']=rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4,column=1)
        
        # Meal
        
        Meal=Label(labelframeleft,text='Meal:',padx=2,pady=6,font=('times new roman',12,'bold'))
        Meal.grid(row=5,column=0,sticky=W)

        txt_Meal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=29,font=('times new roman',13,'bold'))
        txt_Meal.grid(row=5,column=1)
        
        # No of days
        
        NoOfDays=Label(labelframeleft,text='No Of Days:',padx=2,pady=6,font=('times new roman',12,'bold'))
        NoOfDays.grid(row=6,column=0,sticky=W)

        txt_NoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=('times new roman',13,'bold'))
        txt_NoOfDays.grid(row=6,column=1)
        
        # Paid Tax
        
        PaidTax=Label(labelframeleft,text='Paid Tax:',padx=2,pady=6,font=('times new roman',12,'bold'))
        PaidTax.grid(row=7,column=0,sticky=W)

        txt_PaidTax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=('times new roman',13,'bold'))
        txt_PaidTax.grid(row=7,column=1)
        
        # Sub total
        
        subtatal=Label(labelframeleft,text='Sub Tota:',padx=2,pady=6,font=('times new roman',12,'bold'))
        subtatal.grid(row=8,column=0,sticky=W)

        txt_subtatal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=('times new roman',13,'bold'))
        txt_subtatal.grid(row=8,column=1)
        
        # Total Cost
        
        totalcost=Label(labelframeleft,text='Total Cost:',padx=2,pady=6,font=('times new roman',12,'bold'))
        totalcost.grid(row=9,column=0,sticky=W)

        txt_totalcost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=('times new roman',13,'bold'))
        txt_totalcost.grid(row=9,column=1)
        
        # Bill button
        btn_Bill=Button(labelframeleft,text='Bill',command=self.total,font=('times new roman',11,'bold'),bg='black',fg='gold',width=10)
        btn_Bill.grid(row=100,column=0,padx=1,sticky=W)
        
         #==================btn fame===================
        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        # add button

        btn_add=Button(btn_frame,text='Add',command=self.add_data,font=('times new roman',11,'bold'),bg='black',fg='gold',width=10)
        btn_add.grid(row=0,column=0,padx=1)
        
        # update button

        btn_update=Button(btn_frame,text='Update',command=self.update,font=('times new roman',11,'bold'),bg='black',fg='gold',width=10)
        btn_update.grid(row=0,column=1,padx=1)
        
        # delete button

        btn_delete=Button(btn_frame,text='Delete',command=self.Delete,font=('times new roman',11,'bold'),bg='black',fg='gold',width=10)
        btn_delete.grid(row=0,column=2,padx=1)
        
        # reset button

        btn_reset=Button(btn_frame,text='Reset',command=self.reset,font=('times new roman',11,'bold'),bg='black',fg='gold',width=10)
        btn_reset.grid(row=0,column=3,padx=1)
        
        #====================Table Frame==================
        
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details And Search System',padx=2,font=('times new roman',12,'bold'))
        table_frame.place(x=435,y=280,width=860,height=260)
        
        #=================Search System====================
        
        lbl_search=Label(table_frame,text='Search By:',font=('times new roman',12,'bold'),bg='red',fg='white')
        lbl_search.grid(row=0,column=0,sticky=W)
        
        # Search cobobox
        
        self.search_var=StringVar() 
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=('times new roman',12,'bold'),width=24,state='readonly')
        combo_search['value']=('Contact','Room')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        # search entry
        
        self.txt_search=StringVar()
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=('times new roman',13,'bold'))
        txt_search.grid(row=0,column=2,padx=2)
        
        # search button

        btn_search=Button(table_frame,text='Search',command=self.search,font=('times new roman',11,'bold'),bg='black',fg='gold',width=10)
        btn_search.grid(row=0,column=3,padx=1)
        
        # show all button

        btn_showall=Button(table_frame,text='Show All',command=self.fetch_data,font=('times new roman',11,'bold'),bg='black',fg='gold',width=10)
        btn_showall.grid(row=0,column=4,padx=1)
        
        # Right side image
       
        img3=Image.open(r'C:\Users\Hp\Desktop\bed.jpg')
        img3=img3.resize((520,300),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lableimg2=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lableimg2.place(x=760,y=55,width=520,height=200)
        
        
        #==================Show Data Table==================
        
        detail_frame=Frame(table_frame,bd=2,relief=RIDGE)
        detail_frame.place(x=0,y=50,width=860,height=180)
        
        #scrool bar
        
        scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(detail_frame,column=('contact','checkin','checkout','roomtype','roomavailable','meal','noofdays'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        # table column heading
        
        self.room_table.heading('contact',text='Contact')
        self.room_table.heading('checkin',text='Check-in')
        self.room_table.heading('checkout',text='Check-out')
        self.room_table.heading('roomtype',text='Room Type')
        self.room_table.heading('roomavailable',text='Room No')
        self.room_table.heading('meal',text='Meal')
        self.room_table.heading('noofdays',text='NoOfDays')
       
        
        self.room_table['show']='headings'
      
        self.room_table.column('contact',width=100)
        self.room_table.column('checkin',width=100)
        self.room_table.column('checkout',width=100)
        self.room_table.column('roomtype',width=100)
        self.room_table.column('roomavailable',width=100)
        self.room_table.column('meal',width=100)
        self.room_table.column('noofdays',width=100)
        
        self.room_table.pack(fill=BOTH,expand=1) 
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor) 
        
        self.fetch_data()
        
        #Function to add data
        
    def add_data(self):
        if self.var_contact.get()=='' or self.var_checkin.get()=='':
            messagebox.showerror('Error','All fields are required to be filled',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
                con_cursor=conn.cursor()
                con_cursor.execute('insert into room values(%s,%s,%s,%s,%s,%s,%s)',(
                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailables.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_noofdays.get()
                                                                                
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Room Booked',parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning',f'Some thing went wrong:{str(es)}',parent=self.root)
        #Function to fetch data
    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
        con_cursor=conn.cursor()
        con_cursor.execute('select * from room')
        rows=con_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
       #get_cursor
        
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailables.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
        
    #Update function
    
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
            con_cursor=conn.cursor()           
            con_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                
                                                                                                                    
                                                                                                                                                                    
                                                                                                                                                                    self.var_checkin.get(),
                                                                                                                                                                    self.var_checkout.get(),
                                                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                                                    self.var_roomavailables.get(),
                                                                                                                                                                    self.var_meal.get(),
                                                                                                                                                                    self.var_noofdays.get(),
                                                                                                                                                                    self.var_contact.get()       ))                                                                 
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)
     #Delete function
    
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
           
     # Reset function
    
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailables.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        
     #Search function
    
    def search(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
        con_cursor=conn.cursor()
        
        con_cursor.execute("select * from room where "+str(self.search_var.get())+"LIKE '%"+str(self.txt_search.get())+"%'")
        rows=con_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
  #===============all data fetch=======================
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            #==========name============
            conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                
                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)
                
                lblname=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                lblname.place(x=0,y=0)
                
                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                
                
                #========================gender==================
                
                conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblgender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                lblgender.place(x=0,y=30)
                
                lbl1=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl1.place(x=90,y=30)
                
                
                #=====================email===================
                conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblEmail=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)
                
                lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)
                
                #=======================Nationality=====================
                
                conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblNationality=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)
                
                lbl3=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=90)
                
                #========================Address==================
                
                conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblAddress=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)
                
                lbl4=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=120)
                
    
    def total(self):
        in_date=self.var_checkin.get()
        out_date=self.var_checkout.get()
        in_date=datetime.strptime(in_date,"%d/%m/%y")
        out_date=datetime.strptime(out_date,"%d/%m/%y")
        self.var_noofdays.set(abs(out_date-in_date).days)

        if(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Triple"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+Tax))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
if __name__ == "__main__":
    root=Tk()
    obj=roombooking(root)
    root.mainloop()