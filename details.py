from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')
        
                
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
        
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='New Room Add',padx=2,font=('times new roman',12,'bold'))
        labelframeleft.place(x=5,y=50,width=540,height=350) 
        
         #Floor
        
        lbl_floor=Label(labelframeleft,text='Floor:',padx=2,pady=6,font=('times new roman',12,'bold'))
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=('times new roman',13,'bold'))
        entry_floor.grid(row=0,column=1,sticky=W)
        
        #Room no
        
        lbl_roomno=Label(labelframeleft,text='Room No:',padx=2,pady=6,font=('times new roman',12,'bold'))
        lbl_roomno.grid(row=1,column=0,sticky=W)
        
        self.var_RoomNo=StringVar()

        entry_roomno=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=('times new roman',13,'bold'))
        entry_roomno.grid(row=1,column=1,sticky=W)
        
        #Room Type
        
        lbl_roomtype=Label(labelframeleft,text='Room Type:',padx=2,pady=6,font=('times new roman',12,'bold'))
        lbl_roomtype.grid(row=2,column=0,sticky=W)
        
        self.var_roomtype=StringVar()

        entry_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=20,font=('times new roman',13,'bold'))
        entry_roomtype.grid(row=2,column=1,sticky=W)
        
           #==================btn fame===================
        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)
        
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
        
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='Show Room Details:',padx=2,font=('times new roman',12,'bold'))
        table_frame.place(x=600,y=55,width=600,height=350)
        
        #scrool bar
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(table_frame,column=('floor','roomno','roomtype'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
         # table column heading
        
        self.room_table.heading('floor',text='Floor')
        self.room_table.heading('roomno',text='Room No')
        self.room_table.heading('roomtype',text='Room Type')

       
        
        self.room_table['show']='headings'
      
        self.room_table.column('floor',width=100)
        self.room_table.column('roomno',width=100)
        self.room_table.column('roomtype',width=100)
    
        
        self.room_table.pack(fill=BOTH,expand=1) 
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor) 
        self.fetch_data()
        
 #Function to add data
        
    def add_data(self):
        if self.var_floor.get()=='' or self.var_roomtype.get()=='':
            messagebox.showerror('Error','All fields are required to be filled',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
                con_cursor=conn.cursor()
                con_cursor.execute('insert into details values(%s,%s,%s)',(
                                                                                self.var_floor.get(),
                                                                                self.var_RoomNo.get(),
                                                                                self.var_roomtype.get()
                                                                                
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','New Room Added Successfully',parent=self.root)
            except Exception as es:
                messagebox.showwarning('Warning',f'Some thing went wrong:{str(es)}',parent=self.root)
                
    #get_cursor
        
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        
        self.var_floor.set(row[0]),
        self.var_RoomNo.set(row[1]),
        self.var_roomtype.set(row[2])
        
        
     #Update function
    
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter Floor number", parent=self.root)
        else:
            try:
                print("Update button clicked")
                conn = mysql.connector.connect(host='localhost', user='root', password='mysql123', database='worksheet', auth_plugin='mysql_native_password')
                con_cursor = conn.cursor()

                update_query = "update details set Floor=%s, RoomType=%s where Floor=%s and RoomNo=%s"
                query_data = (
                self.var_floor.get(),
                self.var_roomtype.get(),
                self.var_floor.get(),
                self.var_RoomNo.get()
                            )
                print("Update query:", update_query % query_data)  
                con_cursor.execute(update_query, query_data)

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

            
     #Delete function
    
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want to delete this room details",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
    # Reset function
    
    def reset(self):
        self.var_floor.set(""),
        self.var_RoomNo.set(""),
        self.var_roomtype.set(""),
        
        
        
   #Function to fetch data
    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='mysql123',database='worksheet',auth_plugin='mysql_native_password')
        con_cursor=conn.cursor()
        con_cursor.execute('select * from details')
        rows=con_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()   
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()