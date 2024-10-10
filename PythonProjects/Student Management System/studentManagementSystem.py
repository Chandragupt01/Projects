def addstudent():
    def submitadd():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addedtime=time.strftime("%H:%M:%S")
        addeddate=time.strftime("%d/%m/%y")
        try:
            strr='insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res=messagebox.askyesnocancel('Notification','ID {} Name {} added successfully.Do you want to clean the form?'.format(id,name),parent=addroot)
            if res==True:
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notification','Id already exists try with another id',parent=addroot)
        strr="select * from studentdata"
        mycursor.execute(strr)
        datas= mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('490x490+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='tan')
    # addroot.iconbitmap('smsicon.ico')
    addroot.resizable(False,False)
    #----------------------------------------------add student labels
    idlabel=Label(addroot,text='Enter Id: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(addroot,text='Enter Name: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(addroot,text='Enter Mobile: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(addroot,text='Enter Email: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(addroot,text='Enter Address: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(addroot,text='Enter Gender: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(addroot,text='Enter D.O.B.: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
    #----------------------------------------------add student entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()

    identry=Entry(addroot,font=('Helvetica',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(addroot,font=('Helvetica',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(addroot,font=('Helvetica',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry=Entry(addroot,font=('Helvetica',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry=Entry(addroot,font=('Helvetica',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry=Entry(addroot,font=('Helvetica',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry=Entry(addroot,font=('Helvetica',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    #############-------------------add button
    submitbtn=Button(addroot,text='Submit',font=('roman',15,'bold'),bg='teal',bd=4,width=20,activebackground='brown',activeforeground='white',command=submitadd)
    submitbtn.place(x=150,y=420)
    addroot.mainloop()

def searchstudent():
    def search():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addeddate=time.strftime("%d/%m/%y")
        if id!=' ':
            strr='Select * from studentdata where id=%s'
            mycursor.execute(strr,(id))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif name!=' ':
            strr='Select * from studentdata where name=%s'
            mycursor.execute(strr,(name))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif mobile!=' ':
            strr='Select * from studentdata where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif email!=' ':
            strr='Select * from studentdata where email=%s'
            mycursor.execute(strr,(email))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif address!=' ':
            strr='Select * from studentdata where address=%s'
            mycursor.execute(strr,(address))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif gender!=' ':
            strr='Select * from studentdata where gender=%s'
            mycursor.execute(strr,(gender))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif dob!=' ':
            strr='Select * from studentdata where dob=%s'
            mycursor.execute(strr,(dob))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif addeddate!=' ':
            strr='Select * from studentdata where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('490x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='tan')
    # searchroot.iconbitmap('smsicon.ico')
    searchroot.resizable(False,False)
    #----------------------------------------------add student labels
    idlabel=Label(searchroot,text='Enter Id: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(searchroot,text='Enter Name: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(searchroot,text='Enter Mobile: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(searchroot,text='Enter Email: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(searchroot,text='Enter Address: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(searchroot,text='Enter Gender: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(searchroot,text='Enter D.O.B.: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
    
    datelabel=Label(searchroot,text='Enter Date: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
    #----------------------------------------------add student entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()

    identry=Entry(searchroot,font=('Helvetica',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(searchroot,font=('Helvetica',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(searchroot,font=('Helvetica',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry=Entry(searchroot,font=('Helvetica',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry=Entry(searchroot,font=('Helvetica',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry=Entry(searchroot,font=('Helvetica',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry=Entry(searchroot,font=('Helvetica',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    dateentry=Entry(searchroot,font=('Helvetica',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    #############-------------------add button
    submitbtn=Button(searchroot,text='Submit',font=('roman',15,'bold'),bg='teal',bd=4,width=20,activebackground='brown',activeforeground='white',command=search)
    submitbtn.place(x=150,y=480)
    searchroot.mainloop()

def deletestudent():
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values'][0]
    strr='delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','Id {} deleted successfully'.format(pp))
    strr='Select * from studentdata'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vv)

def updatestudent():
    def update():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        date=dateval.get()
        time=timeval.get()

        strr="update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s"
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifiaction','Id {} updated successfully'.format(id),parent=updateroot)
        strr='Select * from studentdata'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('490x585+220+200')
    updateroot.title('Student Management System')
    updateroot.config(bg='tan')
    # updateroot.iconbitmap('smsicon.ico')
    updateroot.resizable(False,False)
    #----------------------------------------------add student labels
    idlabel=Label(updateroot,text='Update Id: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(updateroot,text='Update Name: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(updateroot,text='Update Mobile: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(updateroot,text='Update Email: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(updateroot,text='Update Address: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(updateroot,text='Update Gender: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(updateroot,text='Update D.O.B.: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
    
    datelabel=Label(updateroot,text='Update Date: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
    
    timelabel=Label(updateroot,text='Update time: ',bg='teal',font=('Helvetica',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)
    #----------------------------------------------add student entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    timeval=StringVar()

    identry=Entry(updateroot,font=('Helvetica',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(updateroot,font=('Helvetica',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(updateroot,font=('Helvetica',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry=Entry(updateroot,font=('Helvetica',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry=Entry(updateroot,font=('Helvetica',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry=Entry(updateroot,font=('Helvetica',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry=Entry(updateroot,font=('Helvetica',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    dateentry=Entry(updateroot,font=('Helvetica',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    
    timeentry=Entry(updateroot,font=('Helvetica',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=490)

    #############-------------------add button
    submitbtn=Button(updateroot,text='Update',font=('roman',15,'bold'),bg='teal',bd=4,width=20,activebackground='brown',activeforeground='white',command=update)
    submitbtn.place(x=150,y=540)
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values']
    if len(pp)!=0:
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    updateroot.mainloop()

def showstudent():
    strr='Select * from studentdata'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vv)

def exportstudent():
    pass
    ff=filedialog.asksaveasfilename()
    gg=studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=studenttable.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifiaction','Student data is saved {}'.format(paths))

def exitstudent():
    res=messagebox.askyesnocancel('Notification','Do you want to exit?')
    if res == True:
        root.destroy()
############################################ConnectDatabase######################################

def Connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
        # host='localhost'
        # user='root'
        # password='ryuadkins2001'
        
        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr='create database studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int, name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr='alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr='alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database created and now you are connected to the database.',parent=dbroot)

        except:
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database.',parent=dbroot)
        dbroot.destroy


    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    # dbroot.iconbitmap('smsicon.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='tan')
    #-----------------------------------connectdbLabels-----------------------------
    hostlabel=Label(dbroot,text="Enter Host : ",bg='beige',font=('Helvetica',15,'bold'),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    hostlabel.place(x=10,y=10)
    userlabel=Label(dbroot,text="Enter User: ",bg='beige',font=('Helvetica',15,'bold'),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    userlabel.place(x=10,y=70)
    passwordlabel=Label(dbroot,text="Enter Password: ",bg='beige',font=('Helvetica',15,'bold'),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    passwordlabel.place(x=10,y=130)
    #-----------------------------------connectdbEntry-----------------------------
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    hostentry =Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)
    userentry =Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)
    passwordentry =Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)
    passwordentry.config(show='*')
    #-----------------------------------connectdbButton-----------------------------
    submitButton=Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='teal',bd=4,width=20,activebackground='brown',activeforeground='white',command=submitdb)
    submitButton.place(x=150,y=190)
    dbroot.mainloop()
#################################################################################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date : '+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)
#################################IntroSlider#########################################################

def IntroLabelTick():
    global count,text
    if count>=len(ss):
        count=0
        text=''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
        count+=1
    SliderLabel.after(150,IntroLabelTick)

from tkinter import *
from tkinter import ttk
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
import time
import pymysql
import pandas


root = Tk()
root.title("Student Management System")
root.config(bg="teal")
root.geometry("1174x700+200+50")
# root.iconbitmap('smsicon.ico')
root.resizable(False, False)
################################Frames#######################################
###--------------------dataentryframe-------------------------------------------
DataEntryFrame = Frame(root, bg="tan", relief=GROOVE, borderwidth=2)
DataEntryFrame.place(x=10, y=80, width=500, height=600)

frontlabel = Label(DataEntryFrame,text='----------Welcome----------',width=30,font=("Helvetica", 22, "italic bold"),bg='tan')
frontlabel.pack(side=TOP,expand=True)

addbtn=Button(DataEntryFrame,text='1. Add Student', width=25,font=("Helvetica", 22, "italic bold"),bd=6,bg='teal',activebackground='brown',activeforeground='white',relief=GROOVE,command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame,text='2. Search Student', width=25,font=("Helvetica", 22, "italic bold"),bd=6,bg='teal',activebackground='brown',activeforeground='white',relief=GROOVE,command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame,text='3. Delete Student', width=25,font=("Helvetica", 22, "italic bold"),bd=6,bg='teal',activebackground='brown',activeforeground='white',relief=GROOVE,command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='4. Update Student', width=25,font=("Helvetica", 22, "italic bold"),bd=6,bg='teal',activebackground='brown',activeforeground='white',relief=GROOVE,command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn=Button(DataEntryFrame,text='5. Show All', width=25,font=("Helvetica", 22, "italic bold"),bd=6,bg='teal',activebackground='brown',activeforeground='white',relief=GROOVE,command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame,text='6. Export', width=25,font=("Helvetica", 22, "italic bold"),bd=6,bg='teal',activebackground='brown',activeforeground='white',relief=GROOVE,command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='7. Exit', width=25,font=("Helvetica", 22, "italic bold"),bd=6,bg='teal',activebackground='brown',activeforeground='white',relief=GROOVE,command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

###--------------------ShowDataframe-------------------------------------------

ShowDataFrame = Frame(root, bg="tan", relief=GROOVE, borderwidth=2)
ShowDataFrame.place(x=550, y=80, width=620, height=600)

##----------------------showdataframe
style = ttk.Style()
style.configure('Treeview.Heading',font=("Helvetica", 15, "italic bold"),foreground='teal')
style.configure('Treeview',font=("Helvetica", 12, "italic"),foreground='teal',background='tan')

scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable=Treeview(ShowDataFrame,columns=('Id', 'Name', 'Mobile No.', 'Email', 'Address', 'Gender','D.O.B', 'Added Date', 'Added Time'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No.',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)
################################Slider#######################################
ss = "Welcome To Student Management System"
count=0
text=''
SliderLabel = Label(
    root,
    text=ss,
    relief=GROOVE,
    borderwidth=5,
    font=("Helvetica", 22, "italic bold"),
    width=35,
    bg="tan",
)
SliderLabel.place(x=260, y=0)
IntroLabelTick()
################################clock#######################################
clock=Label(root,font=("Helvetica",14, "bold"),relief=GROOVE,borderwidth=5,bg='tan')
clock.place(x=0,y=0)
tick()

################################connecDatabase#######################################
connectbutton= Button(root,text="Connect To Database",width=23,font=("Helvetica",12, "bold"),relief=GROOVE,borderwidth=5,bg='tan',activebackground='brown',activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()
