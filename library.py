from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkinter import ttk
import random
import time;
import datetime

def main():
    root = Tk()
    #root.configure(background='black')
    app = Window1(root)
    



     # ==================================================Login System Code Window1===================================================================================#



       


class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Library Management Login System")
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
        

        self.Username = StringVar()
        self.Password = StringVar()
        

        


        self.LabelTitle = Label(self.frame,text="Libraray Management System",font=('arial',50,'bold'),bd=5)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)

        

        self.Loginframe1 = Frame(self.frame,width=1010,height=200,bd=25,relief='ridge')
        self.Loginframe1.grid(row=1,column=0,pady=10)

        self.Loginframe2 = Frame(self.frame,width=1010,height=100,bd=20,relief='ridge')
        self.Loginframe2.grid(row=2,column=0,pady=30)

        self.Loginframe3 = Frame(self.frame,width=1010,height=100,bd=20,relief='ridge')
        self.Loginframe3.grid(row=3,column=0,pady=2)

        self.Loginframe4 = Frame(self.frame,width=1010,height=100,bd=20,relief='ridge')
        self.Loginframe4.grid(row=4,column=0,pady=2)

        

        

        # ===================================================================================================================================================

        self.LabelUsername = Label(self.Loginframe1,text="UserName",font=('arial',20,'bold'),bd=22,)
        self.LabelUsername.grid(row=0,column=0)
        self.TxtUsername = Entry(self.Loginframe1,text="UserName",font=('arial',20,'bold'),bd=22,textvariable=self.Username)
        self.TxtUsername.grid(row=0,column=1)

        self.LabelPass = Label(self.Loginframe1,text="Password",font=('arial',20,'bold'),bd=22,)
        self.LabelPass.grid(row=1,column=0)
        self.TxtPass = Entry(self.Loginframe1,text="Password",font=('arial',20,'bold'),bd=22,show="*",textvariable=self.Password)
        self.TxtPass.grid(row=1,column=1)
        

        # ====================================================================================================================================================


        self.btnLogin = Button(self.Loginframe2,text="LOGIN",width=17,font=('arial',15,'bold'),command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)

        self.btnReset = Button(self.Loginframe2,text="RESET",width=17,font=('arial',15,'bold'),command=self.Reset)
        self.btnReset.grid(row=0,column=1)

        self.btnExit = Button(self.Loginframe2,text="EXIT",width=17,font=('arial',15,'bold'),command=self.Exit)
        self.btnExit.grid(row=0,column=2)

        # ====================================================================================================================================================

     
        

        self.btnStureg = Button(self.Loginframe3,text="Student Registration",state=DISABLED,width=20,font=('arial',20,'bold'),command=self.Stureg_window)
        self.btnStureg.grid(row=0,column=0)

        self.btnbookreg = Button(self.Loginframe3,text="Book Registration",state=DISABLED,width=20,font=('arial',20,'bold'),command=self.bookreg_window)
        self.btnbookreg.grid(row=0,column=1)

        self.btnbillreg = Button(self.Loginframe3,text="Billing System",state=DISABLED,width=20,font=('arial',20,'bold'),command=self.bill_window)
        self.btnbillreg.grid(row=0,column=2)



        self.data = Button(self.Loginframe4,text="File Data",width=20,font=('arial',15,'bold'),command=self.fileData)
        self.data.grid(row=0,column=0)

        
        

        # =====================================================================================================================================================

    def Login_System(self):
            user = (self.Username.get())
            pas = (self.Password.get())

            if (user == str("bce")) and (pas == str("bce")):
                self.btnStureg.config(state = NORMAL)
                self.btnbookreg.config(state = NORMAL)
                self.btnbillreg.config(state = NORMAL)
            else:
                tkinter.messagebox.askyesno("Library Management System","You Have Entered An Invalid Login Details")
                self.btnStureg.config(state = DISABLED)
                self.btnbookreg.config(state = DISABLED)
                self.btnbillreg.config(state = DISABLED)
                self.Username.set("")
                self.Password.set("")
                self.TxtUsername.focus()


    def Reset(self):
            self.btnStureg.config(state = DISABLED)
            self.btnbookreg.config(state = DISABLED)
            self.btnbillreg.config(state = DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.TxtUsername.focus()

    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("Library Management System","Confirm If You Want To Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

         # ================================================Login System Code Window1 Ends here=====================================================================================#
        
        
        
                
                

        # =====================================================================================================================================================

    def Stureg_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def bookreg_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)

    def bill_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)

    def fileData(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window5(self.newWindow)

    def search(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window6(self.newWindow)

         # =====================================================================================================================================#
    

class Window2:
   def __init__(self,root):
        self.root=root
        self.root.title("Student Registration Form")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")

        # =====================================================================================================================================#

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        FirstName=StringVar()
        LastName=StringVar()
        Address=StringVar()
        PhoneNo=StringVar()
        Ref=StringVar()
        Email=StringVar()
        College=StringVar()
        DOB=StringVar()
        pinCode=StringVar()
        Id=StringVar()
        

        Membership=StringVar()
        Membership.set("0")
        # ===========================================Frame===============================================================


        def insert():
            ref=Ref.get()
            fname=FirstName.get()
            lname=LastName.get()
            add=Address.get()
            phno=PhoneNo.get()
            date=DateofOrder.get()
            email=Email.get()
            coll=College.get()
            pincode=pinCode.get()
            dob=DOB.get()
            

            
            file=open("student.txt","a")
            file.write(ref)
            file.write(" ")
            file.write(fname)
            file.write(" ")
            file.write(lname)
            file.write(" ")
            file.write(add)
            file.write(" ")
            file.write(phno)
            file.write(" ")
            file.write(date)
            file.write(" ")
            file.write(email)
            file.write(" ")
            file.write(coll)
            file.write(" ")
            file.write(pincode)
            file.write(" ")
            file.write(dob)
            file.write('\n')
            file.close()
            print("Success")

        def delete():
            ref=Ref.get()
            with open("student.txt", "r") as f:
                file_content=f.readlines()
                for ind, line in enumerate(file_content):
                    if line.startswith(ref):
                        file_content[ind]=""
            with open("student.txt","w") as f:
                f.writelines(file_content)
                print("Delete successfull")


        def iExit():
            iExit=tkinter.messagebox.askyesno("Student Registration Form","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def reset():
            FirstName.set("")
            LastName.set("")
            Address.set("")
            PhoneNo.set("")
            Ref.set("")
            Email.set("")
            College.set("")
            DOB.set("")
            pinCode.set("")
            

            var1.set
            var2.set("")
            var3.set("")
            var4.set("")

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Student Registration System","Confirm if you want to add new student")
            if iResetRecord > 0:
                reset()
            elif iResetRecord <=0:
                reset()
                self.lblTxt.delete("1.0",END)
                return

        def Ref_No():
            x=random.randint(100,1000)
            randomRef = str(x)
            Ref.set(randomRef)


        def submit():
            Ref_No()
            self.lblTxt.insert(END,"\t" + Ref.get() + "\t\t" + FirstName.get() +  "\t\t" + LastName.get()  +  "\t\t" + Address.get() +  "\t\t" + PhoneNo.get() + "\t\t" + DateofOrder.get() + "\t\t" +  College.get() +  "\n")  
            
            
            
            
                
            
            
                                            


        Mainframe=Frame(self.root)
        Mainframe.grid()

        TitleFrame=Frame(Mainframe,bd=18,width=1250,padx=30,relief=RIDGE,)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial','75','bold'),text="Student Registration Form")
        self.lblTitle.grid()


        # ===========================================LowerFrame============================================================

        MemberDetailsFrame = LabelFrame(Mainframe,width=1350,height=500,bd=20,pady=5,relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails=LabelFrame(MemberDetailsFrame,bd=10,width=880,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F=LabelFrame(FrameDetails,bd=10,width=350,height=400,font=('arial',12,'bold'),text='Student Details',relief=RIDGE)
        MembersName_F.grid(row=0,column=0)

        Receipt_ButtonFrame=LabelFrame(MemberDetailsFrame,bd=10,width=1000,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)

        # ================================================================================================================

        self.lblReferanceNo=Label(MembersName_F,font=('arial','15','bold'),text="Reference No",bd=7)
        self.lblReferanceNo.grid(row=0,column=0)

        self.txtReferanceNo=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=Ref,insertwidth=2)
        self.txtReferanceNo.grid(row=0,column=1)

        self.lblFirstName=Label(MembersName_F,font=('arial','15','bold'),text="FirstName     ",bd=7)
        self.lblFirstName.grid(row=1,column=0)

        self.txtFirstName=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=FirstName,insertwidth=2)
        self.txtFirstName.grid(row=1,column=1)


        self.lblLastName=Label(MembersName_F,font=('arial','15','bold'),text="LastName     ",bd=7)
        self.lblLastName.grid(row=2,column=0)

        self.txtLastName=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=LastName,insertwidth=2)
        self.txtLastName.grid(row=2,column=1)

        self.lblAddress=Label(MembersName_F,font=('arial','15','bold'),text="Address       ",bd=7)
        self.lblAddress.grid(row=3,column=0)

        self.txtAddress=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=Address,insertwidth=2)
        self.txtAddress.grid(row=3,column=1)

        self.lblPhoneNo=Label(MembersName_F,font=('arial','15','bold'),text="PhoneNo      ",bd=7)
        self.lblPhoneNo.grid(row=4,column=0)

        self.txtPhoneNo=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=PhoneNo,insertwidth=2)
        self.txtPhoneNo.grid(row=4,column=1)

        self.lblDate=Label(MembersName_F,font=('arial','15','bold'),text="Date            ",bd=7)
        self.lblDate.grid(row=5,column=0)

        self.txtDate=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=DateofOrder,insertwidth=2)
        self.txtDate.grid(row=5,column=1)

        self.lblEmail=Label(MembersName_F,font=('arial','15','bold'),text="Email           ",bd=7)
        self.lblEmail.grid(row=6,column=0)

        self.txtEmail=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=Email,insertwidth=2)
        self.txtEmail.grid(row=6,column=1)

        self.lblCollege=Label(MembersName_F,font=('arial','15','bold'),text="College         ",bd=7)
        self.lblCollege.grid(row=7,column=0)

        self.txtCollege=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=College,insertwidth=2)
        self.txtCollege.grid(row=7,column=1)

        # =============

        self.lblCollege=Label(MembersName_F,font=('arial','15','bold'),text="PinCode         ",bd=7)
        self.lblCollege.grid(row=8,column=0)

        self.txtCollege=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=pinCode,insertwidth=2)
        self.txtCollege.grid(row=8,column=1)

        self.lblCollege=Label(MembersName_F,font=('arial','15','bold'),text="DOB         ",bd=7)
        self.lblCollege.grid(row=9,column=0)

        self.txtCollege=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=DOB,insertwidth=2)
        self.txtCollege.grid(row=9,column=1)

        self.lblCollege=Label(MembersName_F,font=('arial','15','bold'),text="ID            ",bd=7)
        self.lblCollege.grid(row=10,column=0)

        self.txtCollege=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=Id,insertwidth=2)
        self.txtCollege.grid(row=10,column=1)

        

        

        

        

        

        


        # ================================================================================================================


        # ================================================================================================================


        self.lblLabel=Label(Receipt_ButtonFrame,font=('arial','10','bold'),pady=10,text="STUDENT REF\t FIRSTNAME\t LASTNAME\t ADDRESS\t PHONENO\t DATE\t COLLEGE",bd=7)
        self.lblLabel.grid(row=0,column=0,columnspan=4)

        self.lblTxt=Text(Receipt_ButtonFrame,width=115,height=23,font=('arial','10','bold'))
        self.lblTxt.grid(row=1,column=0,columnspan=4)

        



        # ===================================================Buttons========================================================

        self.btn1=Button(Receipt_ButtonFrame,padx=18,bd=5,font=('arial','16','bold'),width=13,text="SUBMIT",command=submit).grid(row=2,column=0)

        self.btn4=Button(Receipt_ButtonFrame,padx=18,bd=5,font=('arial','16','bold'),command=insert,width=13,text="INSERT").grid(row=2,column=1)

        self.btn2=Button(Receipt_ButtonFrame,padx=18,bd=5,font=('arial','16','bold'),command=iResetRecord,width=13,text="RESET").grid(row=2,column=3)

        self.btn3=Button(Receipt_ButtonFrame,padx=18,bd=5,font=('arial','16','bold'),command=delete,width=13,text="Delete").grid(row=2,column=2)


    



        # =====================================================================================================================================#

class Window3:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Registration Form")
        self.root.geometry("1350x590+0+0")
        self.root.configure(background="black")


         # =====================================================================================================================================#

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        FirstName=StringVar()
        LastName=StringVar()
        Address=StringVar()
        PhoneNo=StringVar()
        Ref=StringVar()
        Email=StringVar()
        College=StringVar()
        
        

        Membership=StringVar()
        Membership.set("0")
        # ===========================================Frame===============================================================


        def insert():
            Bookid=Ref.get()
            booktitle=FirstName.get()
            bookuthor=LastName.get()
            pubyear=Address.get()
            bookcatagory=PhoneNo.get()
            date=DateofOrder.get()
            bookprice=Email.get()
            company=College.get()
            
            

            
            file=open("book.txt","a")
            file.write(Bookid)
            file.write(" ")
            file.write(booktitle)
            file.write(" ")
            file.write(bookuthor)
            file.write(" ")
            file.write(pubyear)
            file.write(" ")
            file.write(bookcatagory)
            file.write(" ")
            file.write(date)
            file.write(" ")
            file.write(bookprice)
            file.write(" ")
            file.write(company)
            file.write(" ")
            file.write('\n')
            file.close()
            print("Success")

        def delete():
            ref=Ref.get()
            with open("book.txt", "r") as f:
                file_content=f.readlines()
                for ind, line in enumerate(file_content):
                    if line.startswith(ref):
                        file_content[ind]=""
            with open("book.txt","w") as f:
                f.writelines(file_content)
                print("Delete successfull")


        def iExit():
            iExit=tkinter.messagebox.askyesno("Student Registration Form","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def reset():
            FirstName.set("")
            LastName.set("")
            Address.set("")
            PhoneNo.set("")
            Ref.set("")
            Email.set("")
            College.set("")
            DOB.set("")
            pinCode.set("")
            

            var1.set
            var2.set("")
            var3.set("")
            var4.set("")

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Student Registration System","Confirm if you want to add new student")
            if iResetRecord > 0:
                reset()
            elif iResetRecord <=0:
                reset()
                self.lblTxt.delete("1.0",END)
                return

        def Ref_No():
            x=random.randint(100,1000)
            randomRef = str(x)
            Ref.set(randomRef)


        def submit():
            Ref_No()
            self.lblTxt.insert(END,"\t" + Ref.get() + "\t\t" + FirstName.get() +  "\t\t" + LastName.get()  +  "\t\t" + Address.get() +  "\t\t" + PhoneNo.get() + "\t\t" + DateofOrder.get() + "\t\t" +  College.get() +  "\n")  
            
            
            
            
                
            
            
                                            


        Mainframe=Frame(self.root)
        Mainframe.grid()

        TitleFrame=Frame(Mainframe,bd=18,width=1250,padx=30,relief=RIDGE,)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial','79','bold'),text="Books Registration Form")
        self.lblTitle.grid()


        # ===========================================LowerFrame============================================================

        MemberDetailsFrame = LabelFrame(Mainframe,width=1350,height=500,bd=20,pady=5,relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails=LabelFrame(MemberDetailsFrame,bd=10,width=880,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F=LabelFrame(FrameDetails,bd=10,width=350,height=400,font=('arial',12,'bold'),text='Student Details',relief=RIDGE)
        MembersName_F.grid(row=0,column=0)

        Receipt_ButtonFrame=LabelFrame(MemberDetailsFrame,bd=10,width=1000,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)

        # ================================================================================================================

        self.lblReferanceNo=Label(MembersName_F,font=('arial','15','bold'),text="Book ID           ",bd=7)
        self.lblReferanceNo.grid(row=0,column=0)

        self.txtReferanceNo=Entry(MembersName_F,font=('arial','15','bold'),bd=7,state=DISABLED,textvariable=Ref,insertwidth=2)
        self.txtReferanceNo.grid(row=0,column=1)

        self.lblFirstName=Label(MembersName_F,font=('arial','15','bold'),text="Book Title       ",bd=7)
        self.lblFirstName.grid(row=1,column=0)

        self.txtFirstName=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=FirstName,insertwidth=2)
        self.txtFirstName.grid(row=1,column=1)


        self.lblLastName=Label(MembersName_F,font=('arial','15','bold'),text="Book Author   ",bd=7)
        self.lblLastName.grid(row=2,column=0)

        self.txtLastName=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=LastName,insertwidth=2)
        self.txtLastName.grid(row=2,column=1)

        self.lblAddress=Label(MembersName_F,font=('arial','15','bold'),text="Book Pub Year",bd=7)
        self.lblAddress.grid(row=3,column=0)

        self.txtAddress=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=Address,insertwidth=2)
        self.txtAddress.grid(row=3,column=1)

        self.lblPhoneNo=Label(MembersName_F,font=('arial','15','bold'),text="Book Catagory",bd=7)
        self.lblPhoneNo.grid(row=4,column=0)

        self.txtPhoneNo=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=PhoneNo,insertwidth=2)
        self.txtPhoneNo.grid(row=4,column=1)

        self.lblDate=Label(MembersName_F,font=('arial','15','bold'),text="Date                ",bd=7)
        self.lblDate.grid(row=5,column=0)

        self.txtDate=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=DateofOrder,insertwidth=2)
        self.txtDate.grid(row=5,column=1)

        self.lblEmail=Label(MembersName_F,font=('arial','15','bold'),text="Book Price       ",bd=7)
        self.lblEmail.grid(row=6,column=0)

        self.txtEmail=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=Email,insertwidth=2)
        self.txtEmail.grid(row=6,column=1)

        self.lblCollege=Label(MembersName_F,font=('arial','15','bold'),text="Pub Company  ",bd=7)
        self.lblCollege.grid(row=7,column=0)

        self.txtCollege=Entry(MembersName_F,font=('arial','15','bold'),bd=7,textvariable=College,insertwidth=2)
        self.txtCollege.grid(row=7,column=1)

        

        

        

        

        

        

        


        # ================================================================================================================


        # ================================================================================================================


        self.lblLabel=Label(Receipt_ButtonFrame,font=('arial','10','bold'),pady=10,text="Book IDNO\t Book Title\t Book Author\t Pub Year\t Book Catagory\t DATE\t Book Company",bd=7)
        self.lblLabel.grid(row=0,column=0,columnspan=4)

        self.lblTxt=Text(Receipt_ButtonFrame,width=115,height=16,font=('arial','10','bold'))
        self.lblTxt.grid(row=1,column=0,columnspan=4)

        



        # ===================================================Buttons========================================================

        self.btn1=Button(Receipt_ButtonFrame,padx=18,bd=5,font=('arial','16','bold'),width=13,text="SUBMIT",command=submit).grid(row=2,column=0)

        self.btn4=Button(Receipt_ButtonFrame,padx=18,bd=5,font=('arial','16','bold'),command=insert,width=13,text="INSERT").grid(row=2,column=1)

        self.btn2=Button(Receipt_ButtonFrame,padx=18,bd=5,font=('arial','16','bold'),command=iResetRecord,width=13,text="RESET").grid(row=2,column=3)

        self.btn3=Button(Receipt_ButtonFrame,padx=18,bd=5,font=('arial','16','bold'),command=delete,width=13,text="Delete").grid(row=2,column=2)


        



        # =====================================================================================================================================#



class Window4:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="powder blue")

         # =====================================================================================================================================#

        MType=StringVar()
        Ref=StringVar()
        Title=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Address1=StringVar()
        Address2=StringVar()
        PostalCode=StringVar()
        MobileNo=StringVar()
        Bookid=StringVar()
        Booktitle=StringVar()
        BookType=StringVar()
        Author=StringVar()
        DateBorrowed=StringVar()
        Datedue=StringVar()
        Sellingprice=StringVar()
        LateReturnFine=StringVar()
        DateOverdue=StringVar()
        Daysonloan=StringVar()
        Prescription=StringVar()

        def iExit():
            iExit=tkinter.messagebox.askyesno("Library Billing System","Confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return

        def iResetRecord():
            MType.set("")
            Ref.set("")
            Title.set("")
            Firstname.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            PostalCode.set("")
            MobileNo.set("")
            Bookid.set("")
            Booktitle.set("")
            BookType.set("")
            Author.set("")
            DateBorrowed.set("")
            Datedue.set("")
            Sellingprice.set("")
            LateReturnFine.set("")
            DateOverdue.set("")
            Daysonloan.set("")
            Prescription.set("")
            self.Txtdisplay.delete("1.0",END)

        def idelete():
            iResetRecord()

        def bill():
            
            self.Txtdisplay1.insert(END,"\n"+"TYPE:"+MType.get()+"\n"+"NAME:"+Firstname.get()+"\n"+"TITLE:"+Booktitle.get()+"\n"+"DATE:"+DateBorrowed.get()+"\n"+"DAYS:"+Daysonloan.get()+"\n"+"RETURN:"+Datedue.get()+"\n\n"+"THANK YOU !!!")
            
            

        

        def display():
            self.Txtdisplay.insert(END,"\t"+MType.get()+"\t\t"+Ref.get()+"\t"+Title.get()+"\t"+Firstname.get()+"\t"+Surname.get()+"\t\t"+Address1.get()+"\t\t"+Address2.get()+"\t"+PostalCode.get()+"\t"+DateBorrowed.get()+"\t\t"+Daysonloan.get()+"\n")
                                     
            
            
            

        

            
            
            

        # --------------------------------------------------Frame------------------------------------------------------------------

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,width=1350,padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle = Label (TitleFrame,width=42,font=('arial',40,'bold'),text="Library Billing System" , padx=12)  
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame,bd=10,width=1350,height=89,padx=20,relief=RIDGE)    
        ButtonFrame.pack(side=BOTTOM)

        FrameDetails = Frame(MainFrame,bd=20,width=1350,height=100,padx=120,relief=RIDGE)  
        FrameDetails.pack(side=BOTTOM)

        Dataframe = Frame(MainFrame,bd=20,width=1500,height=400,padx=20,relief=RIDGE)   
        Dataframe.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(Dataframe, bd=10,width=1250,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text='Library Membership Info:')
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(Dataframe, bd=10,width=650,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text='Book Details:')
        DataFrameRight.pack(side=RIGHT)

        # --------------------------------------------------Widget------------------------------------------------------------------

        self.lblMemberType = Label(DataFrameLeft,font=('arial',12,'bold'),text="MemberType:",padx=2,pady=2)
        self.lblMemberType.grid(row=0,column=0,sticky=W)

        self.cboMemberType =ttk.Combobox(DataFrameLeft,font=('arial',12,'bold'),textvariable=MType,state='readonly',width=23,)
        self.cboMemberType['value']=('','Student','Lecture','Others')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0,column=1)

        #============

        

        self.lblRefno = Label(DataFrameLeft,font=('arial',12,'bold'),text="Reference No:",padx=2,pady=2)
        self.lblRefno.grid(row=1,column=0,sticky=W)

        self.TxtRefno = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Ref,width=25,)
        self.TxtRefno.grid(row=1,column=1)

        #=============

        self.lblTitle = Label(DataFrameLeft,font=('arial',12,'bold'),text="Title:",padx=2,pady=2)
        self.lblTitle.grid(row=2,column=0,sticky=W)

        self.cboTitle =ttk.Combobox(DataFrameLeft,font=('arial',12,'bold'),textvariable=Title,state='readonly',width=23,)
        self.cboTitle['value']=('','Student','Lecture','Others')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2,column=1)

        #===========

        self.lblName = Label(DataFrameLeft,font=('arial',12,'bold'),text="FirstName:",padx=2,pady=2)
        self.lblName.grid(row=3,column=0,sticky=W)

        self.TxtName = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Firstname,width=25,)
        self.TxtName.grid(row=3,column=1)

        #=============

        self.lblName = Label(DataFrameLeft,font=('arial',12,'bold'),text="LastName:",padx=2,pady=2)
        self.lblName.grid(row=4,column=0,sticky=W)

        self.TxtName = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Surname,width=25)
        self.TxtName.grid(row=4,column=1)

        #===============

    

        self.lbladd1 = Label(DataFrameLeft,font=('arial',12,'bold'),text="Address 1:",padx=2,pady=2)
        self.lbladd1.grid(row=5,column=0,sticky=W)

        self.Txtadd1 = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Address1,width=25)
        self.Txtadd1.grid(row=5,column=1)

        #=============

        self.lbladd2 = Label(DataFrameLeft,font=('arial',12,'bold'),text="Address 2:",padx=2,pady=2)
        self.lbladd2.grid(row=6,column=0,sticky=W)

        self.Txtadd2 = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Address2,width=25)
        self.Txtadd2.grid(row=6,column=1)

        #===========

        self.lblpost = Label(DataFrameLeft,font=('arial',12,'bold'),text="Post Code:",padx=2,pady=2)
        self.lblpost.grid(row=7,column=0,sticky=W)

        self.Txtpost = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=PostalCode,width=25)
        self.Txtpost.grid(row=7,column=1)

        #=============

        self.lblpost = Label(DataFrameLeft,font=('arial',12,'bold'),text="Mobile No:",padx=2,pady=2)
        self.lblpost.grid(row=8,column=0,sticky=W)

        self.Txtpost = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=MobileNo,width=25)
        self.Txtpost.grid(row=8,column=1)

        #=================================================================================================================================

        self.lblbid = Label(DataFrameLeft,font=('arial',12,'bold'),text="Book Id:",padx=2,pady=2)
        self.lblbid.grid(row=0,column=2,sticky=W)

        self.Txtbid = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Bookid,width=25)
        self.Txtbid.grid(row=0,column=3)

        #=============

        self.lbltitle = Label(DataFrameLeft,font=('arial',12,'bold'),text="Book Title:",padx=2,pady=2)
        self.lbltitle.grid(row=1,column=2,sticky=W)

        self.Txttitle = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25,textvariable=Booktitle)
        self.Txttitle.grid(row=1,column=3)

        #=============

        self.lblauthor = Label(DataFrameLeft,font=('arial',12,'bold'),text="Author:",padx=2,pady=2)
        self.lblauthor.grid(row=2,column=2,sticky=W)

        self.Txtauthor = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Author,width=25)
        self.Txtauthor.grid(row=2,column=3)

         #=============

        self.lbldatebor = Label(DataFrameLeft,font=('arial',12,'bold'),text="Date Borrowed:",padx=2,pady=2)
        self.lbldatebor.grid(row=3,column=2,sticky=W)

        self.Txtdatebor = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=DateBorrowed,width=25)
        self.Txtdatebor.grid(row=3,column=3)

         #=============

        self.lbldatedue = Label(DataFrameLeft,font=('arial',12,'bold'),text="Date Due:",padx=2,pady=2)
        self.lbldatedue.grid(row=4,column=2,sticky=W)

        self.Txtdatedue = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Datedue,width=25)
        self.Txtdatedue.grid(row=4,column=3)

         #=============

        self.lblloan = Label(DataFrameLeft,font=('arial',12,'bold'),text="Days on Loan:",padx=2,pady=2)
        self.lblloan.grid(row=5,column=2,sticky=W)

        self.Txtloan = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Daysonloan,width=25)
        self.Txtloan.grid(row=5,column=3)

          #=============

        self.lblfine = Label(DataFrameLeft,font=('arial',12,'bold'),text="Late Return Fine:",padx=2,pady=2)
        self.lblfine.grid(row=6,column=2,sticky=W)

        self.Txtfine = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=LateReturnFine,width=25)
        self.Txtfine.grid(row=6,column=3)

             #=============

        self.lblfine1 = Label(DataFrameLeft,font=('arial',12,'bold'),text="Date Over Due:",padx=2,pady=2)
        self.lblfine1.grid(row=7,column=2,sticky=W)

        self.Txtfine1 = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=DateOverdue,width=25)
        self.Txtfine1.grid(row=7,column=3)

             #=============

        self.lblprice = Label(DataFrameLeft,font=('arial',12,'bold'),text="Selling Price:",padx=2,pady=2)
        self.lblprice.grid(row=8,column=2,sticky=W)

        self.Txtprice = Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Sellingprice,width=25)
        self.Txtprice.grid(row=8,column=3)


        # ================================================widget1============================================================================

        self.Txtdisplay1 = Text(DataFrameRight,font=('arial',12,'bold'),width=32,height=13,padx=8,pady=20)
        self.Txtdisplay1.grid(row=0,column=2)


        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0,column=1,sticky='ns')

        

                        

        
        #ListBox
        ListOfBooks = ['python','C','C++','HTML','CSS','DJANGO','FLASk','REACT','REACTNATIVE','GO','JAVASCRIPT','ANDROID']

        def SelectedBook(evt):
              value = str(booklists.get(booklists.curselection()))
              w=value
              if(w == "python"):
                  Bookid.set("Book1601")
                  Booktitle.set("Python")
                  Author.set("RAGHU")
                  display()

              if(w == "C"):
                  Bookid.set("Book1602")
                  Booktitle.set("C")
                  Author.set("KIRAN")
                  display()

              if(w == "C++"):
                  Bookid.set("Book1603")
                  Booktitle.set("C++")
                  Author.set("NITHIN")
                  display()

              if(w == "HTML"):
                  Bookid.set("Book1604")
                  Booktitle.set("HTML")
                  Author.set("GOKUL")
                  display()

              if(w == "CSS"):
                  Bookid.set("Book1605")
                  Booktitle.set("CSS")
                  Author.set("Chethan")
                  display()

              if(w == "DJANGO"):
                  Bookid.set("Book1606")
                  Booktitle.set("DJANGO")
                  Author.set("Ajith")
                  display()

              if(w == "FLASk"):
                  Bookid.set("Book1607")
                  Booktitle.set("FLASk")
                  Author.set("NITHIN")
                  display()

              if(w == "REACT"):
                  Bookid.set("Book1608")
                  Booktitle.set("REACT")
                  Author.set("Hithesh Choudhary")
                  display()

              if(w == "REACTNATIVE"):
                  Bookid.set("Book1609")
                  Booktitle.set("REACTNATIVE")
                  Author.set("Chethan")
                  display()

              if(w == "GO"):
                  Bookid.set("Book1610")
                  Booktitle.set("GO")
                  Author.set("Ajith")
                  display()

              if(w == "JAVASCRIPT"):
                  Bookid.set("Book1611")
                  Booktitle.set("JAVASCRIPT")
                  Author.set("NITHIN")
                  display()

              if(w == "ANDROID"):
                  Bookid.set("Book1612")
                  Booktitle.set("ANDROID")
                  Author.set("Hithesh Choudhary")
                  display()


                  
              
          
          

                      
                        
        booklists = Listbox(DataFrameRight,width=20,height=12,font=('arial',12,'bold'))
        booklists.bind('<<ListboxSelect>>',SelectedBook)
        booklists.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklists.yview)

        for items in ListOfBooks:
            booklists.insert(END,items)



        self.label=Label(FrameDetails,font=('arial',10,'bold'),pady=8,text="Member Type\tReference No\tTitle\tFirstName\tSurname\tAddress 1\tAddress 2\tPost Code\t Book Title\t Date Borrowed\t Days On Loan")
        self.label.grid(row=0,column=0)
        self.Txtdisplay = Text(FrameDetails,font=('arial',12,'bold'),width=121,height=4,padx=2,pady=4)
        self.Txtdisplay.grid(row=1,column=0)

        


          
        # =================================================================================================================================



        

        # ================================================Button============================================================================

        self.btnDisplaydata=Button(ButtonFrame,text='Display Data',font=('arial',12,'bold'),command=display,width=33,bd=4)
        self.btnDisplaydata.grid(row=0,column=0)

        self.btnDelete=Button(ButtonFrame,text='BILL',font=('arial',12,'bold'),command=bill,width=33,bd=4)
        self.btnDelete.grid(row=0,column=1)

        self.btnReset=Button(ButtonFrame,text='Reset',font=('arial',12,'bold'),command=iResetRecord,width=33,bd=4)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame,text='Exit',font=('arial',12,'bold'),command=iExit,width=33,bd=4)
        self.btnExit. grid(row=0,column=3)



        # =====================================================================================================================================#






class Window5:


   
   
   def __init__(self,root):
        self.root=root
        self.root.title("FILE DATA")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="powder blue")

       
       

        #============================================================================================================================================

        

      

       
        
        
        

        
       

       

        
        


                

        

        #==============================================================================================================================================



class Window6:
   def __init__(self,root):
        self.root=root
        self.root.title("Library Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="powder blue")

        
        


        #============================================================================================================================================
        
        

       

        
   

        #==============================================================================================================================================




if __name__ == '__main__':
    main()
    



    
