from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import Email_Password
import smtplib
import time

class Login_Form:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form | Developed By Shams Afridi")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.original_OTP = ""

        #--------------> Login Form Images <--------------
        self.mobile_Image = ImageTk.PhotoImage(file="pictures/login_page.jpg")
        self.mobile_Image_Label = Label(self.root, image=self.mobile_Image, bd=0).place(x=50, y=50)
        self.phone_Image = ImageTk.PhotoImage(file="pictures/login.jpg")
        self.phone_Image_Label = Label(self.root, image=self.phone_Image, bd=0).place(x=200, y=50)

        #-------------> Login Frame <----------------
        self.employee_ID = StringVar()
        self.employee_Password = StringVar()
        login_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_Frame.place(x=650, y=50, width=350, height=460)

        title = Label(login_Frame, text="Login Form", font=("Elephant",30,"bold"), bg="white").place(x=0, y=20, relwidth=1)

        employee_ID_Label = Label(login_Frame, text="Employee ID", font=("Andalus",15),bg="white", fg="#566573").place(x=40, y=95)
        employee_ID_TextField = Entry(login_Frame, textvariable=self.employee_ID, font=("times new roman",15), bd=2, bg="#eaeded").place(x=40,y=135, width=260, height=35)

        employee_Password_Label = Label(login_Frame, text="Password", font=("Andalus",15),bg="white", fg="#566573").place(x=40, y=187)
        employee_Password_TextField = Entry(login_Frame, textvariable=self.employee_Password, show="*", font=("times new roman",15), bd=2, bg="#eaeded").place(x=40, y=225, width=260, height=35)

        login_Button = Button(login_Frame, text="Log In", command=self.login, font=("Arial Rounded MT Bold",15), cursor="hand2", bd=2, bg="#3498db", fg="white" ).place(x=40, y=290, width=260)

        breakLine = Label(login_Frame, bg="lightgray").place(x=40, y=370, width=260, height=2)
        Or = Label(login_Frame, text="OR", bg="white", fg="lightgray", font=("times new roman",15)).place(x=150, y=355)

        forget_Password_Button = Button(login_Frame, text="Forget Password?", state=DISABLED, command=self.forget_Password_Window, font=("times new roman",13), bg="white", cursor="hand2", fg="#3498db", bd=0, activebackground="white", activeforeground="#3498db" ).place(x=40, y=390, width=260)

        registeration_Frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        registeration_Frame.place(x=650, y=540, width=350, height=60)

        registeration_Label = Label(registeration_Frame, text="Don't have an account ?", font=("times new roman",13), bg="white").place(x=60, y=15)

        signup_Button = Button(registeration_Frame, text="Sign Up", state=DISABLED, font=("times new roman",13,"bold"), bg="white", fg="#3498db", bd=0, cursor="hand2", activebackground="white", activeforeground="#3498db" ).place(x=220, y=12)

        #------------------> Animation <-----------------------
        self.image1 = ImageTk.PhotoImage(file="pictures/loginform.jpg")
        self.image2 = ImageTk.PhotoImage(file="pictures/logins.jpg")
        # self.image3 = ImageTk.PhotoImage(file="pictures/logon.jpg")
        # self.image4 = ImageTk.PhotoImage(file="pictures/phone_login.jpg")
        # self.image5 = ImageTk.PhotoImage(file="pictures/logon_form1.jpg")
        # self.image6 = ImageTk.PhotoImage(file="pictures/login.jpg")
        # self.image7 = ImageTk.PhotoImage(file="pictures/login_page.jpg")
        # self.image8 = ImageTk.PhotoImage(file="pictures/login_mobile.jpg")
        # self.image9 = ImageTk.PhotoImage(file="pictures/login_form.jpg")

        self.change_Image_Label = Label(self.root, bg="white")
        self.change_Image_Label.place(x=215, y=65, width=240, height=482)

        self.animation()
    
    def animation(self):
        self.picture1 = self.image1
        self.picture2 = self.image2
        # self.picture3 = self.image3
        # self.picture4 = self.image4
        # self.picture5 = self.image5
        # self.picture6 = self.image6
        # self.picture7 = self.image7
        # self.picture8 = self.image8
        # self.picture9 = self.image9
        self.change_Image_Label.config(image=self.picture1)
        self.change_Image_Label.after(200,self.animation)


    def login(self):
        # if self.employee_ID.get() == "" or self.employee_Password.get() == "":
        #     messagebox.showerror("Error","All fields are required")
        # elif self.employee_ID.get() != "Shams" or self.employee_Password.get() != "1234":
        #     messagebox.showerror("Error","Invalid Employee-ID Or Password\nTry again with correct credentials")
        # else:
        #     messagebox.showinfo("Information", f"Welcome : {self.employee_ID.get()}\nYour Password : {self.employee_Password.get()}")
        
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.employee_ID.get() == "" or self.employee_Password.get() == "":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                queryCursor.execute("select employee_user_type from Employee where employee_id=? AND employee_password=?",(self.employee_ID.get(), self.employee_Password.get()))
                user = queryCursor.fetchone()
                if user == None:
                    messagebox.showerror("Error","Invalid Employee-ID Or Password\nTry again with correct credentials",parent=self.root)
                else:
                    # print(user)
                    if user[0] == "Admin":
                        self.root.destroy()
                        os.system("python Dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python Billing.py")
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)


    def forget_Password_Window(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.employee_ID.get() == "":
                messagebox.showerror("Error", "Employee ID must be required",parent=self.root)
            else:
                queryCursor.execute("select employee_email from Employee where employee_id=?",(self.employee_ID.get(), ))
                user_Email = queryCursor.fetchone()
                if user_Email == None:
                    messagebox.showerror("Error","Invalid Employee-ID try again",parent=self.root)
                else:
                    self.otp = StringVar()
                    self.new_Password = StringVar()
                    self.confirm_Password = StringVar()
                    print(user_Email[0])
                    check = self.send_Email(user_Email[0])
                    if check == "Fail":
                        messagebox.showerror("Error","Connection Error, try again",parent=self.root)
                    else:
                        self.forget_Password_Form = Toplevel(self.root)
                        self.forget_Password_Form.title("RESET PASSWORD")
                        self.forget_Password_Form.geometry("400x350+500+100")
                        self.forget_Password_Form.focus_force()
                        title = Label(self.forget_Password_Form, text="Reset Password", font=("goudy old style",15,"bold"), bg="purple", fg="white").pack(side=TOP, fill=X)
                        reset_Label = Label(self.forget_Password_Form, text="Enter OTP Send on Registered Email", font=("times new roman",12)).place(x=20, y=60)
                        reset_TextField = Entry(self.forget_Password_Form, textvariable=self.otp, font=("times new roman",12), bg="lightyellow").place(x=20, y=90, width=250, height=25)
                        self.send_Button = Button(self.forget_Password_Form, text="SEND", command=self.validate_OTP, font=("times new roman",15), bg="lightblue", fg="white")
                        self.send_Button.place(x=290, y=75, width=100, height=40)

                        new_Password_Label = Label(self.forget_Password_Form, text="New Password", font=("times new roman",12)).place(x=20, y=130)
                        new_Password_TextField = Entry(self.forget_Password_Form, textvariable=self.new_Password, font=("times new roman",12), bg="lightyellow").place(x=20, y=160, width=250, height=25)

                        confirm_Password_Label = Label(self.forget_Password_Form, text="Confirm Password", font=("times new roman",12)).place(x=20, y=210)
                        confirm_Password_TextField = Entry(self.forget_Password_Form, textvariable=self.confirm_Password, font=("times new roman",12), bg="lightyellow").place(x=20, y=240, width=250, height=25)

                        self.update_Button = Button(self.forget_Password_Form, text="UPDATE", command=self.update_Password, state=DISABLED, font=("times new roman",15), bg="lightblue", fg="white")
                        self.update_Button.place(x=150, y=280, width=100, height=40)

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)


    def send_Email(self, to_):
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls() # add security layer mean encryption
        user_email = Email_Password.email
        user_password = Email_Password.password
        s.login(user_email, user_password)
        self.original_OTP = int( time.strftime("%H%S%M") ) + int(time.strftime("%S"))
        # print(self.original_OTP)
        email_Subject = "Inventory Management System Reset Password OTP"
        message = f"Dear User,\n\nYour Reset OTP is {str(self.original_OTP)}.\n\nWith Regards,\nInventory Management System Team"
        message = "Subject: {}\n\n{}".format(email_Subject,message)
        s.sendmail(user_email, to_, message)
        check = s.ehlo()
        if check[0] == 250:
            return "Success"
        else:
            return "Fail"

    def validate_OTP(self):
        if int(self.original_OTP) == int(self.otp.get()):
            self.update_Button.config(state=NORMAL)
            self.send_Button.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP, Try Again",parent=self.forget_Password_Form)
        
    def update_Password(self):
        if self.new_Password.get() == "" or self.confirm_Password.get() == "":
            messagebox.showerror("Error","Password is required",parent=self.forget_Password_Form)
        elif self.new_Password.get() != self.confirm_Password.get():
            messagebox.showerror("Error","new password & confirm password must be same",parent=self.forget_Password_Form)
        else:
            database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
            queryCursor = database_Connection.cursor()
            try:
                queryCursor.execute("Update Employee SET employee_password=? where employee_id=?",(self.new_Password.get(), self.employee_ID.get()))
                database_Connection.commit()
                messagebox.showinfo("Success","Password Updated Successfully",parent=self.forget_Password_Form)
                self.forget_Password_Form.destroy()
        
            except Exception as exception_error:
                messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)
                


root = Tk()
login = Login_Form(root)
root.mainloop()