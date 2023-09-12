from tkinter import*
from PIL import Image,ImageTk
from customer import cust_window
from room import roombooking
from details import DetailsRoom
class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')

        #================image1====================
        img1=Image.open(r'C:\Users\Hp\Desktop\background.jpeg')
        img1=img1.resize((1500,140),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lableimg=Label(self.root,image=self.photoimg1,bd=4,relief=RAISED)
        lableimg.place(x=0,y=0,width=1550,height=140)


        #================Logo=======================
        img2=Image.open(r'C:\Users\Hp\Desktop\logo.png')
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lableimg1=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lableimg1.place(x=0,y=0,width=230,height=140)


        #===============Title========================
        title=Label(self.root,text='HOTEL MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),fg='gold',bg='black',bd=4,relief=RIDGE)
        title.place(x=0,y=140,width=1550,height=50)
        
        
        #===============Main Frame===================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        #===============Menu=========================
        label_menu=Label(self.root,text='MENU',font=('times new roman',20,'bold'),fg='gold',bg='black',bd=4,relief=RIDGE)
        label_menu.place(x=0,y=190,width=230)
        
        
        #===============Button Frame===================
        button_frame=Frame(self.root,bd=4,relief=RIDGE)
        button_frame.place(x=0,y=230,width=228,height=190)
        
        #================Button========================
        cust_button=Button(button_frame,text='CUSTOMER',command=self.cust_details,width=22,font=('times new roman',14,'bold'),fg='gold',bg='black',bd=0,cursor='hand1')
        cust_button.grid(row=0,column=0,pady=1)
        
        room_button=Button(button_frame,text='ROOM',command=self.roombooking,width=22,font=('times new roman',14,'bold'),fg='gold',bg='black',bd=0,cursor='hand1')
        room_button.grid(row=1,column=0,pady=1)
        
        details_button=Button(button_frame,text='DETAILS',command=self.details_room,width=22,font=('times new roman',14,'bold'),fg='gold',bg='black',bd=0,cursor='hand1')
        details_button.grid(row=2,column=0,pady=1)
        
        report_button=Button(button_frame,text='REPORT',width=22,font=('times new roman',14,'bold'),fg='gold',bg='black',bd=0,cursor='hand1')
        report_button.grid(row=3,column=0,pady=1)
        
       # logout_button=Button(button_frame,text='LOGOUT',width=22,font=('times new roman',14,'bold'),fg='gold',bg='black',bd=0,cursor='hand1')
       # logout_button.grid(row=4,column=0,pady=1)
        
        #================Right Side Image===============
        img3=Image.open(r'C:\Users\Hp\Desktop\side_image.png')
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lableimg2=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lableimg2.place(x=225,y=0,width=1310,height=590)
        
        #================Down Image===============
        img4=Image.open(r'C:\Users\Hp\Desktop\food_logo.jpg')
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lableimg3=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lableimg3.place(x=0,y=225,width=230,height=210)
        
        #================Down Image===============
        img5=Image.open(r'C:\Users\Hp\Desktop\food1.png')
        img5=img5.resize((230,210),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lableimg4=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lableimg4.place(x=0,y=400,width=230,height=190)
        
        
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_window(self.new_window)
        
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=roombooking(self.new_window)
    
    
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
        
if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()