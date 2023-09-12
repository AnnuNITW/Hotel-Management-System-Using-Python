from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class cust_window:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')
    
    
        #==================variables================
        
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        
        self.var_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar() 
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


        #===============Title========================
        title=Label(self.root,text='ADD CUSTOMER',font=('times new roman',18,'bold'),fg='gold',bg='black',bd=4,relief=RIDGE)
        title.place(x=0,y=0,width=1295,height=50)
        
        #================Logo=======================
       
        img2=Image.open(r'C:\Users\Hp\Desktop\logo.png')
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lableimg1=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lableimg1.place(x=5,y=2,width=100,height=40)
        
        
        #===============Label========================
        
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',padx=2,font=('times new roman',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=490)   

        #================Label and Entry=======================
        
        #cust ref
        
        st_ref=Label(labelframeleft,text='Customer Ref',padx=2,pady=6,font=('times new roman',12,'bold'))
        st_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=('times new roman',13,'bold'),state='readonly')
        entry_ref.grid(row=0,column=1)
        
        #cust name
        
        cname=Label(labelframeleft,text='Customer Name:',padx=2,pady=6,font=('times new roman',12,'bold'))
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_name,width=29,font=('times new roman',13,'bold'))
        txtcname.grid(row=1,column=1)
        
        # mother name
        
        mname=Label(labelframeleft,text='Mother Name:',padx=2,pady=6,font=('times new roman',12,'bold'))
        mname.grid(row=2,column=0,sticky=W)

        txt_mname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=('times new roman',13,'bold'))
        txt_mname.grid(row=2,column=1)
        
        #gender combobox
        
        gender=Label(labelframeleft,text='Gender:',padx=2,pady=6,font=('times new roman',12,'bold'))
        gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=('times new roman',13,'bold'),width=27,state='readonly')
        combo_gender['value']=('Male','Female','Other')
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        # postcode
        
        postcode=Label(labelframeleft,text='PostCode:',padx=2,pady=6,font=('times new roman',12,'bold'))
        postcode.grid(row=4,column=0,sticky=W)

        txt_postcode=ttk.Entry(labelframeleft,width=29,textvariable=self.var_post,font=('times new roman',13,'bold'))
        txt_postcode.grid(row=4,column=1)
        
        # Mobile number
        
        mobile=Label(labelframeleft,text='Mobile Number:',padx=2,pady=6,font=('times new roman',12,'bold'))
        mobile.grid(row=5,column=0,sticky=W)

        txt_mobile=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=('times new roman',13,'bold'))
        txt_mobile.grid(row=5,column=1)
        
        
        # Email
        email=Label(labelframeleft,text='Email:',padx=2,pady=6,font=('times new roman',12,'bold'))
        email.grid(row=6,column=0,sticky=W)

        txt_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=('times new roman',13,'bold'))
        txt_email.grid(row=6,column=1)
        
        #Nationlity
        
        nationality=Label(labelframeleft,text='Nationality:',padx=2,pady=6,font=('times new roman',12,'bold'))
        nationality.grid(row=7,column=0,sticky=W)
        
        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=('times new roman',13,'bold'),width=27,state='readonly')
        combo_nationality['value']=('Indian','American','British')
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
        
        # ID proof cobobox
        
        id_proof=Label(labelframeleft,text='ID Proof Type:',padx=2,pady=6,font=('times new roman',12,'bold'))
        id_proof.grid(row=8,column=0,sticky=W)
        
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=('times new roman',13,'bold'),width=27,state='readonly')
        combo_id['value']=('AadharCard','DrivingLicence','Passport')
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
        
        #id number
        
        idnumber=Label(labelframeleft,text='ID Number:',padx=2,pady=6,font=('times new roman',12,'bold'))
        idnumber.grid(row=9,column=0,sticky=W)

        txt_idnumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=('times new roman',13,'bold'))
        txt_idnumber.grid(row=9,column=1)
        
        # address
        
        address=Label(labelframeleft,text='Address:',padx=2,pady=6,font=('times new roman',12,'bold'))
        address.grid(row=10,column=0,sticky=W)

        txt_address=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=('times new roman',13,'bold'))
        txt_address.grid(row=10,column=1)
        
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
        table_frame.place(x=435,y=50,width=860,height=490)
        
        #=================Search System====================
        
        lbl_search=Label(table_frame,text='Search By:',font=('times new roman',12,'bold'),bg='red',fg='white')
        lbl_search.grid(row=0,column=0,sticky=W)
        
        # Search cobobox
        
        self.search_var=StringVar() 
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=('times new roman',12,'bold'),width=24,state='readonly')
        combo_search['value']=('Mobile','Ref')
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
        
        #==================Show Data Table==================
        
        detail_frame=Frame(table_frame,bd=2,relief=RIDGE)
        detail_frame.place(x=0,y=50,width=860,height=350)
        
        #scrool bar
        
        scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
        
        self.cust_details_table=ttk.Treeview(detail_frame,column=('Ref','Name','Mother','Gender','PostCode','Mobile','Email','Nationality','Idproof','Idnumber','Address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)
        
        # table column heading
        
        self.cust_details_table.heading('Ref',text='Refer No')
        self.cust_details_table.heading('Name',text='Name')
        self.cust_details_table.heading('Mother',text='Mother')
        self.cust_details_table.heading('Gender',text='Gender')
        self.cust_details_table.heading('PostCode',text='PostCode')
        self.cust_details_table.heading('Mobile',text='Mobile No')
        self.cust_details_table.heading('Email',text='Email')
        self.cust_details_table.heading('Nationality',text='Nationality')
        self.cust_details_table.heading('Idproof',text='ID Proof')
        self.cust_details_table.heading('Idnumber',text='ID Number')
        self.cust_details_table.heading('Address',text='Address')
        
        self.cust_details_table['show']='headings'
      
        self.cust_details_table.column('Ref',width=100)
        self.cust_details_table.column('Name',width=100)
        self.cust_details_table.column('Mother',width=100)
        self.cust_details_table.column('Gender',width=100)
        self.cust_details_table.column('PostCode',width=100)
        self.cust_details_table.column('Mobile',width=100)
        self.cust_details_table.column('Email',width=100)
        self.cust_details_table.column('Nationality',width=100)
        self.cust_details_table.column('Idproof',width=100)
        self.cust_details_table.column('Idnumber',width=100)
        self.cust_details_table.column('Address',width=100)
        
        self.cust_details_table.pack(fill=BOTH,expand=1) 
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor) 
        self.fetch_data()
     #Function to add data
        
    def add_data(self):
        if self.var_mobile.get()=='' or self.var_mother.get()=='':
            messagebox.showerror('Error','All fields are required to be filled',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
                con_cursor=conn.cursor()
                con_cursor.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                self.var_ref.get(),
                                                                                self.var_name.get(),
                                                                                self.var_mother.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_post.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_id_proof.get(),
                                                                                self.var_id_number.get(),
                                                                                self.var_address.get()
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Customer has been added',parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning',f'Some thing went wrong:{str(es)}',parent=self.root)
    #Function to fetch data
    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
        con_cursor=conn.cursor()
        con_cursor.execute('select * from customer')
        rows=con_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #Get function
    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])
    
    #Update function
    
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
            con_cursor=conn.cursor()           
            con_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                
                                                                                                                    
                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                    self.var_mother.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_post.get(),
                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_nationality.get(),
                                                                                                                                                                    self.var_id_proof.get(),
                                                                                                                                                                    self.var_id_number.get(),
                                                                                                                                                                    self.var_address.get(),                                                   
                                                                                                                                                                    self.var_ref.get()
                                                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)
            
    #Delete function
    
    def Delete(self):
        try:
            delete_confirmation = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
            if delete_confirmation:
                conn = mysql.connector.connect(host='localhost', user='root', password='mysql123', database='worksheet', auth_plugin='mysql_native_password')
                con_cursor = conn.cursor()
                query = "DELETE FROM customer WHERE Ref = %s"
                value = (self.var_ref.get(),)
                con_cursor.execute(query, value)
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Deleted", "Customer has been deleted successfully", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
        
    # Reset function
    
    def reset(self):
        #self.var_ref.set(""),
        self.var_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
    
    #Search function
    
    def search(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
        con_cursor=conn.cursor()
        
        con_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE'%"+str(self.txt_search.get())+"%'")
        rows=con_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=cust_window(root)
    root.mainloop()