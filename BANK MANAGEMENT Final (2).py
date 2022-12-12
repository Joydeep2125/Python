 #imports
from tkinter import*
import tkinter.messagebox
import os
import mysql.connector

#databse_connection
db=mysql.connector.connect(host="localhost", user="root",password="Mysql@123")
cur=db.cursor()
cur.execute(f"create database if not exists BANK")

db=mysql.connector.connect(host="localhost", user="root",password="Mysql@123",database='BANK')
cur=db.cursor()

cur.execute(f"create table if not exists entry(name varchar(20),mob varchar(10),password varchar(15), aadhaarno varchar(20),dob varchar(10), opb varchar(10))")
db.commit()   

#Main Screen
root=Tk()
root.title('Banking Management')
root.geometry("1222x800+40+5")
root.config(bg="black",padx=10,pady=10)
root.resizable(False,False)

framehome=Frame(root,bg="white")
framehome.pack(fill=BOTH,expand=True)

logo=PhotoImage(file='bank1.gif')
wl=Label(root,image=logo).place(x=0,y=0)

import time


#Funtions
def register():
    #Variables
    global temp_name
    global temp_mob
    global temp_password
    global temp_aadhaarno
    global temp_dob
    global temp_opb
    global alert1
    global v0
    temp_name=StringVar()
    temp_mob=StringVar()
    temp_password=StringVar()
    temp_aadhaarno=StringVar()
    temp_dob=StringVar()
    temp_opb=StringVar()
    v0=IntVar()
    v0.set(1)

            
    #Register Screen
    register_screen=Toplevel(root)
    register_screen.title('Register')
    register_screen.geometry("500x600")
    register_screen.config(bg="sky blue")
    
    #Labels
    Label(register_screen,font=('Times New Roman',15,"bold"),text="PLEASE ENTER YOUR DETAILS BELOW",padx=20,fg='white',anchor='w',relief=RIDGE,borderwidth=5,width=32,bg="black").place(x=35,y=10)
    Label(register_screen,text='USERNAME ',bg='yellow',font=('Footlight MT Light',15),relief=GROOVE,borderwidth=3,width=10,anchor='w').place(x=90,y=60)
    Label(register_screen,text='MOBILE',bg='yellow',font=('Footlight MT Light',15),relief=GROOVE,borderwidth=3,width=10,anchor='w').place(x=90,y=110)
    Label(register_screen,text='PASSWORD. ',bg='yellow',font=('Footlight MT Light',15),relief=GROOVE,borderwidth=3,width=10,anchor='w').place(x=90,y=160)
    Label(register_screen,text='AADHAAR',bg='yellow',font=('Footlight MT Light',15),relief=GROOVE,borderwidth=3,width=10,anchor='w').place(x=90,y=210)
    Label(register_screen,text='DOB ',bg='yellow',font=('Footlight MT Light',15),relief=GROOVE,borderwidth=3,width=10,anchor='w').place(x=90,y=260)
    Radiobutton(register_screen,text="Male",font=('Bookman Old Style',15),relief=GROOVE,bd=3,bg="pink",variable=v0,value=1).place(x=90,y=300)
    Radiobutton(register_screen,text="Female",font=('Bookman Old Style',15),relief=GROOVE,bd=3,bg="pink",variable=v0,value=2).place(x=200,y=300)
    Radiobutton(register_screen,text="Others",font=('Bookman Old Style',15),relief=GROOVE,bd=3,bg="pink",variable=v0,value=3).place(x=330,y=300)
    Label(register_screen,text='ENTER OPENEING BALANCE ',bg='yellow',font=('Times New Roman',13,"bold"),relief=GROOVE,borderwidth=3,width=24,anchor='w').place(x=10,y=370)
    alert1=Label(register_screen,font=('Calisto MT',15))
    alert1.place(x=50,y=500)

    #Entries
    Entry(register_screen,textvariable=temp_name,font=('Footlight MT Light',12),bd=5).place(x=230,y=60)
    Entry(register_screen,textvariable=temp_mob,font=('Footlight MT Light',12),bd=5).place(x=230,y=110)
    Entry(register_screen,textvariable=temp_password,show="*",font=('Footlight MT Light',12),bd=5).place(x=230,y=160)
    Entry(register_screen,textvariable=temp_aadhaarno,font=('Footlight MT Light',12),bd=5).place(x=230,y=210)
    Entry(register_screen,textvariable=temp_dob,font=('Footlight MT Light',12),bd=5).place(x=230,y=260)
    Entry(register_screen,textvariable=temp_opb,font=('Footlight MT Light',10),bd=5).place(x=270,y=370)
    

    #Buttons
    Button(register_screen,text='Register',font=('times',15,'bold'),bg='red',bd=5,width=10,activebackground='blue',activeforeground='white',command=finish_reg).place(x=90,y=450)                    
    Button(register_screen,text='Back',font=('times',15,'bold'),bg='red',bd=5,width=10,activebackground='blue',activeforeground='white',command=back_screen).place(x=260,y=450)                    
    

def back_screen():
    iback=tkinter.messagebox.askyesno("Register","do you want to go back?")
    if iback==0:
        root.destroy()
        return
    
    
def finish_reg():
    global name
    global mob
    global password
    global aadhaarno
    global dob
    global opb
    name=temp_name.get()
    mob=temp_mob.get()
    password=temp_password.get()
    aadhaarno=temp_aadhaarno.get()
    dob=temp_dob.get()
    opb=temp_opb.get()
    all_accounts=os.listdir()

    if name=="" or mob=="" or password=="" or aadhaarno=="" or dob=="" or opb=="":
        alert1.config(text="All credentials are required",fg="red")
        alert1.place(x=139,y=412)
        return
    cur.execute(f"select name from entry where name='{name}'")
    rec=cur.fetchone()
    try:
        for i in rec:
            if i==name:
                alert1.config(fg='red',text="Accounts already exists")
                alert1.place(x=139,y=412)
                return
    except:
         cur.execute(f"insert into entry values('{name}','{mob}','{password}','{aadhaarno}','{dob}','{opb}')")
         db.commit()
         alert1.config(fg="green",text="Account has been created successfully")
         alert1.place(x=90,y=412)

def login():
    #Variables
    global temp_login_name
    global temp_login_password
    global alert2
    global login_screen
    temp_login_name=StringVar()
    temp_login_password=StringVar()
    

    
    #Login Screen
    login_screen=Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("650x400")
    login_screen.config(bg="pink")
    
    #Labels
    Label(login_screen,font=('Calisto MT',20),text="LOGIN TO YOUR ACCOUNT",padx=20,fg='white',anchor='w',relief=RIDGE,borderwidth=5,width=24,bg="black").place(x=99,y=10)
    Label(login_screen,text='USERNAME :',bg='yellow',font=('Times New Roman',17),relief=GROOVE,borderwidth=3,width=11,anchor='w').place(x=142,y=90)
    Label(login_screen,text='PASSWORD :',bg='yellow',font=('Times New Roman',17),relief=GROOVE,borderwidth=3,width=11,anchor='w').place(x=142,y=140)
    alert2=Label(login_screen,font=('Calisto MT',15))
    alert2.place(x=235,y=180)

    #Entry
    Entry(login_screen,textvariable=temp_login_name,font=('times',12),bd=5).place(x=315,y=90)
    Entry(login_screen,textvariable=temp_login_password,show="*",font=('times',12),bd=5).place(x=315,y=140)

    #Button
    Button(login_screen,text='Login',font=('times',15,'bold'),bg='red',bd=5,width=10,activebackground='blue',activeforeground='white',command=login_session).place(x=250,y=220)
    
def login_session():
    global login_name
    global login_password
    all_accounts=os.listdir()
    login_name=temp_login_name.get()
    login_password=temp_login_password.get()
    cur.execute(f"select name from entry where name='{login_name}' and password='{login_password}'")
    rec=cur.fetchone()
    print(rec)
    if rec!=None:
        for i in rec:
            print(i)
        if i==login_name:
            print(i)
            login_screen.destroy()
            account_screen=Toplevel(root)
            account_screen.title("Account")
            account_screen.geometry("405x500")
            #Labels
            Label(account_screen,font=('Times New Roman',15,"bold"),text="WELCOME TO YOUR ACCOUNT",padx=20,fg='white',anchor='w',relief=RIDGE,borderwidth=5,width=25,bg="black").place(x=30,y=10)
            #Buttons
            Button(account_screen,text="Account Details",font=('Calisto MT',15,"bold"),relief=RIDGE,bg="red",fg="white",borderwidth=10,width=15,command=account_details).place(x=100,y=100)
            Button(account_screen,text="Deposit",font=('Calisto MT',15,"bold"),relief=RIDGE,bg="blue",fg="white",borderwidth=10,width=15,command=deposit).place(x=100,y=190)
            Button(account_screen,text="Withdraw",font=('Calisto MT',15,"bold"),relief=RIDGE,bg="green",fg="white",borderwidth=10,width=15,command=withdraw).place(x=100,y=280)
            Button(account_screen,text="Update",font=('Calisto MT',15,"bold"),relief=RIDGE,bg="grey",fg="white",borderwidth=10,width=15,command=update).place(x=100,y=370)
            return
        else:
            alert2.config(fg="red",text="Password or user incorrect ")
            return

    alert2.config(fg="red",text="No account found")

def account_details():
    #variables
    cur.execute(f"select* from entry where name='{login_name}' and password='{login_password}'")
    rec=cur.fetchone()
    print(rec)
    detail_name=rec[0]
    detail_mob=rec[2]
    detail_aadhaarno=rec[3]
    detail_dob=rec[4]
    detail_balance=rec[5]

    #Personal_screen
    personal_screen=Toplevel(root)
    personal_screen.title("Personal Details")
    personal_screen.geometry("470x300")

    #Labels
    Label(personal_screen,font=('Times New Roman',15,"bold"),text="YOUR PERSONAL DETAILS",padx=20,fg='white',anchor='w',relief=RIDGE,borderwidth=5,width=22,bg="black").place(x=60,y=10)
    Label(personal_screen,text="Name :  "+detail_name,font=('Footlight MT Light',14)).place(x=54,y=60)
    Label(personal_screen,text="Mobile :  "+detail_mob,font=('Footlight MT Light',14)).place(x=54,y=90)
    Label(personal_screen,text="AadhaarNo. :  "+detail_aadhaarno,font=('Footlight MT Light',14)).place(x=54,y=120)
    Label(personal_screen,text="DOB :  "+detail_dob,font=('Footlight MT Light',14)).place(x=54,y=150)
    Label(personal_screen,text="Balance : Rs.  "+detail_balance,font=('Footlight MT Light',14)).place(x=54,y=180)





def deposit():
    #Variables
    global deposit_amount
    global deposit_noti
    global current_balance_label
    deposit_amount=StringVar()
    cur.execute(f"select opb from entry where name='{login_name}' and password='{login_password}'")
    rec=cur.fetchone()
    for i in rec:
        print(i)
        detail_balance=i

    #Deposit screen
    deposit_screen=Toplevel(root)
    deposit_screen.title("Deposit")
    deposit_screen.geometry("400x400")

    #Label
    Label(deposit_screen,font=('Times New Roman',15,"bold"),text="DEPOSIT HERE",padx=20,fg='white',anchor='w',relief=RIDGE,borderwidth=5,width=12,bg="black").place(x=100,y=10)
    current_balance_label=Label(deposit_screen,text="CURRENT BALANCE : Rs. "+detail_balance,font=("Footlight MT Light",15))
    current_balance_label.place(x=50,y=100)
    Label(deposit_screen,text="AMOUNT : ",font=("Footlight MT Light",15)).place(x=50,y=150)
    deposit_noti=Label(deposit_screen,font=("Footlight MT Light",15))
    deposit_noti.place(x=50,y=200)

    #Entry
    Entry(deposit_screen,textvariable=deposit_amount,font=('Footlight MT Light',12),bd=5).place(x=160,y=150)

    #Buttons
    Button(deposit_screen,text='Deposit',font=('times',15,'bold'),bg='red',bd=5,width=10,activebackground='blue',activeforeground='white',command=finish_deposit).place(x=120,y=250)
def finish_deposit():
    if deposit_amount.get()=="":
        deposit_noti.config(text="Amount is required!",fg="red")
        return
    if float(deposit_amount.get())<=0:
        deposit_noti.config(text="Negative currency is not accepted",fg="red")
        return
    cur.execute(f"select opb from entry where name='{login_name}' and password='{login_password}'")
    rec=cur.fetchone()
    for i in rec:
        print(i)
    current_balance_label=i
    updated_balance=current_balance_label
    updated_balance=float(updated_balance) + float(deposit_amount.get())
    cur.execute(f"update entry set opb='{updated_balance}' where name='{login_name}' and password='{login_password}'")
    deposit_noti.config(text="Balance Updated",fg="green")
    db.commit()
    print('done')

    
def withdraw():
    #Variables
    global withdraw_amount
    global withdraw_noti
    global current_balance_label
    withdraw_amount=StringVar()
    cur.execute(f"select opb from entry where name='{login_name}' and password='{login_password}'")
    rec=cur.fetchone()
    for i in rec:
        print(i)
    detail_balance=i    

    #Withdraw screen
    withdraw_screen=Toplevel(root)
    withdraw_screen.title("Withdraw")
    withdraw_screen.geometry("400x500")

    #Label
    Label(withdraw_screen,font=('Times New Roman',15,"bold"),text="WITHDRAW HERE",padx=20,fg='white',anchor='w',relief=RIDGE,borderwidth=5,width=14,bg="black").place(x=100,y=10)
    current_balance_label=Label(withdraw_screen,text="CURRENT BALANCE : Rs. "+detail_balance,font=("Footlight MT Light",15))
    current_balance_label.place(x=50,y=100)
    Label(withdraw_screen,text="AMOUNT : ",font=("Footlight MT Light",15)).place(x=50,y=150)
    withdraw_noti=Label(withdraw_screen,font=("Footlight MT Light",15))
    withdraw_noti.place(x=50,y=200)

    #Entry
    Entry(withdraw_screen,textvariable=withdraw_amount,font=('Footlight MT Light',12),bd=5).place(x=170,y=150)

    #Buttons
    Button(withdraw_screen,text='Withdraw',font=('times',15,'bold'),bg='red',bd=5,width=10,activebackground='blue',activeforeground='white',command=finish_withdraw).place(x=120,y=250)

def finish_withdraw():
     if withdraw_amount.get()=="":
        withdraw_noti.config(text="Amount is required!",fg="red")
        return
     if float(withdraw_amount.get())<=0:
         withdraw_noti.config(text="Negative currency is not accepted",fg="red")
         return
     cur.execute(f"select opb from entry where name='{login_name}' and password='{login_password}'")
     rec=cur.fetchone()
     for i in rec:
         print(i)
     current_balance_label=i     
     if float(withdraw_amount.get())>float(current_balance_label):
         withdraw_noti.config(text="Insufficient Amount")
         return   
     updated_balance=current_balance_label
     updated_balance=float(updated_balance) - float(withdraw_amount.get())
     print(login_name)
     cur.execute(f"update entry set opb='{updated_balance}' where name='{login_name}' and password='{login_password}'")
     db.commit()
     withdraw_noti.config(text="Balance Updated",fg="green")

def update():
    #Variables
    global updated_mob
    global update_noti
    global updated_aadhaar
    global current_mob
    global current_aadhaar
    updated_aadhaar=StringVar()
    updated_mob=StringVar()
    cur.execute(f"select aadhaarno,mob from entry where name='{login_name}' and password='{login_password}'")
    rec=cur.fetchone()
    detail_mob=rec[0]
    detail_aadhaar=rec[1]    

    #Update screen
    update_screen=Toplevel(root)
    update_screen.title("Update")
    update_screen.geometry("500x500")

    #Label
    Label(update_screen,font=('Times New Roman',18,"bold"),text="UPDATE YOUR ACCOUNT",padx=20,fg='white',anchor='w',relief=RIDGE,borderwidth=5,width=20,bg="black").place(x=87,y=10)
    Label(update_screen,text="Mobile No. :" +detail_mob,font=("Footlight MT Light",18)).place(x=50,y=100)
    Label(update_screen,text="Aadhaar No. : "+detail_aadhaar,font=("Footlight MT Light",18)).place(x=50,y=250)
    Label(update_screen,text="Mobile No. : ",font=("Footlight MT Light",18)).place(x=50,y=150)
    Label(update_screen,text="Aadhaar No. : ",font=("Footlight MT Light",18)).place(x=50,y=300)
    update_noti=Label(update_screen,font=("Footlight MT Light",15))
    update_noti.place(x=120,y=450)

    #Entry
    Entry(update_screen,textvariable=updated_mob,font=('Footlight MT Light',12),bd=5).place(x=180,y=150)
    Entry(update_screen,textvariable=updated_aadhaar,font=('Footlight MT Light',12),bd=5).place(x=180,y=300)

    #Buttons
    Button(update_screen,text='Update',font=('times',15,'bold'),bg='red',bd=5,width=10,activebackground='blue',activeforeground='white',command=finish_update).place(x=150,y=370)

def finish_update():
     if updated_aadhaar.get()=="" or updated_mob.get()=="":
        update_noti.config(text="Amount is required!",fg="red")
        return
     if float(updated_mob.get())<=0:
         update_noti.config(text="Negative currency is not accepted",fg="red")
         return
     cur.execute(f"select aadhaarno,mob from entry where name='{login_name}' and password='{login_password}'")
     rec=cur.fetchone()
     current_mob=rec[0]
     current_aadhaar=rec[1]
     cur.execute(f"update entry set aadhaarno='{updated_aadhaar}' , mob='{current_mob}' where name='{login_name}' and password='{login_password}'")
     rec= cur.fetchall()
     db.commit()
     update_noti.config(text="Record Updated",fg="green")

def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)

def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200,IntroLabelTick)

def Exit_screen():
    iexit=tkinter.messagebox.askyesnocancel("Bank Management","Do you want to exit ?")
    if iexit>0:
        root.destroy()
        return
    
####SLIDER
ss = 'Welcome To AEES BANK'
count = 0
text = ''

####Welcome To Management System(up n down)
SliderLabel = Label(root,text=ss,font=('times',42,'bold'),foreground='blue',relief=RIDGE,borderwidth=10,width=20,bg='cyan')
SliderLabel.place(x=280,y=20)
IntroLabelTick()

Label(font=('Footlight MT Light',38),text="Select your choice",padx=20,fg='black',anchor='w',relief=RIDGE,borderwidth=10,width=14,bg="white").place(x=397,y=150)

#Buttons
Button(root,text="Register",font=('Calisto MT',20),relief=RIDGE,bg="red",fg="black",borderwidth=10,width=15,command=register).place(x=475,y=300)
Button(root,text="Login",font=('Calisto MT',20),relief=RIDGE,bg="yellow",fg="black",borderwidth=10,width=15,command=login).place(x=475,y=400)
Button(root,text="Exit",font=('Calisto MT',20),relief=RIDGE,bg="blue",fg="black",borderwidth=10,width=15,command=Exit_screen).place(x=475,y=500)

####Clock
clock = Label(root,font=('times',18,'bold'),relief=RIDGE,borderwidth=8,bg='black',fg="white")
clock.place(x=8,y=25)
tick()   
        
root.mainloop()
