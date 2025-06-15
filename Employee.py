from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk , messagebox
import sqlite3

class Employee_Module:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1100x550+220+130")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")
        self.rootObject.focus_force()

        #---------------> Employee-Attributes <---------------
        self.search_By = StringVar()
        self.search_Text = StringVar()

        self.employee_Id = StringVar()
        self.employee_Name = StringVar()
        self.employee_Gender = StringVar()
        self.employee_Age = StringVar()
        # self.employee_Address = StringVar()
        self.employee_Date_Of_Birth = StringVar()
        self.employee_Contact = StringVar()
        self.employee_Email = StringVar()
        self.employee_Password = StringVar()
        self.employee_User_Type = StringVar()
        self.employee_Salary = StringVar()
        self.employee_Attendence = StringVar()
        self.employee_Date_Of_Joining = StringVar()
        self.employee_Experience = StringVar()

        #-----------> Search Frame <----------------
        search_Frame = LabelFrame( self.rootObject , text="Search Employee" , font=("goudy old style",12,"bold") , bd = 2 , relief=RIDGE , bg="white" )
        search_Frame.place( x = 250 , y = 20 , width = 600 , height = 70 )

        #--------------> Search Frame Options <-------------------
        search_ComboBox = ttk.Combobox( search_Frame , textvariable=self.search_By , values=("Select","ID","Name","Email","Contact") , state="readonly" , justify=CENTER , font=("goudy old style",15) )
        search_ComboBox.place( x = 10 , y = 7 , width=180 )
        search_ComboBox.current(0)

        textField_Search = Entry( search_Frame , textvariable=self.search_Text , font=("goudy old style",15) , bg="lightyellow" ).place(x=200,y=7,width=220,height=30)

        search_Button = Button( search_Frame , text="Search" , font=("goudy old style",15) , bg="#008000" , fg="white" , cursor="hand2" , command=self.search_Employee ).place(x=430,y=7,width=150,height=30)

        #-----------------> Employee-Details-Title <-----------------------
        employee_Details_Title = Label( self.rootObject , text="Employee Details" , font=("goudy old style",15) , bg="#273746" , fg="white" ).place(x=50,y=100,width=1000)

        #---------------------> Employee-Details Contents <------------------------
        self.employee_Id_Label = Label( self.rootObject , text="Emp ID" , font=("goudy old style",15) , bg="white" ).place(x=50,y=150)
        self.employee_Id_Text_Field = Entry( self.rootObject , textvariable=self.employee_Id , font=("goudy old style",15) , bg="lightyellow" ).place(x=150,y=150,width=180)
        
        self.employee_Name_Label = Label( self.rootObject , text="Name" , font=("goudy old style",15) , bg="white" ).place(x=350,y=150)
        self.employee_Name_Text_Field = Entry( self.rootObject , textvariable=self.employee_Name , font=("goudy old style",15) , bg="lightyellow" ).place(x=500,y=150,width=180)

        self.employee_Gender_Label = Label( self.rootObject , text="Gender" , font=("goudy old style",15) , bg="white" ).place(x=750,y=150)
        # self.employee_Gender_Text_Field = Entry( self.rootObject , textvariable=self.employee_Gender , font=("goudy old style",15) , bg="lightyellow" ).place(x=830,y=150,width=180)
        self.employee_Gender_ComboBox = ttk.Combobox( self.rootObject , textvariable=self.employee_Gender , values=("Select","Male","Female","Other") , state="readonly" , justify=CENTER , font=("goudy old style",15) )
        self.employee_Gender_ComboBox.place(x=850,y=150,width=180)
        self.employee_Gender_ComboBox.current(0)

        self.employee_Age_Label = Label( self.rootObject , text="Age" , font=("goudy old style",15) , bg="white" ).place(x=50,y=190)
        self.employee_Age_Text_Field = Entry( self.rootObject , textvariable=self.employee_Age , font=("goudy old style",15) , bg="lightyellow" ).place(x=150,y=190,width=180)

        self.employee_Email_Label = Label( self.rootObject , text="Email" , font=("goudy old style",15) , bg="white" ).place(x=350,y=190)
        self.employee_Email_Text_Field = Entry( self.rootObject , textvariable=self.employee_Email , font=("goudy old style",15) , bg="lightyellow" ).place(x=500,y=190,width=180)

        self.employee_Date_Of_Birth_Label = Label( self.rootObject , text="D.O.B" , font=("goudy old style",15) , bg="white" ).place(x=750,y=190)
        self.employee_DOB_Text_Field = Entry( self.rootObject , textvariable=self.employee_Date_Of_Birth , font=("goudy old style",15) , bg="lightyellow" ).place(x=850,y=190,width=180)
        
        self.employee_Contact_Label = Label( self.rootObject , text="Contact" , font=("goudy old style",15) , bg="white" ).place(x=50,y=230)
        self.employee_Contact_Text_Field = Entry( self.rootObject , textvariable=self.employee_Contact , font=("goudy old style",15) , bg="lightyellow" ).place(x=150,y=230,width=180)
                
        self.employee_Password_Label = Label( self.rootObject , text="Password" , font=("goudy old style",15) , bg="white" ).place(x=350,y=230)
        self.employee_Password_Text_Field = Entry( self.rootObject , textvariable=self.employee_Password , font=("goudy old style",15) , bg="lightyellow" ).place(x=500,y=230,width=180)

        self.employee_User_Type_Label = Label( self.rootObject , text="User Type" , font=("goudy old style",15) , bg="white" ).place(x=750,y=230)
        # self.employee_User_Type_Text_Field = Entry( self.rootObject , textvariable=self.employee_User_Type , font=("goudy old style",15) , bg="lightyellow" ).place(x=755,y=200,width=100)
        self.employee_User_Type_ComboBox = ttk.Combobox( self.rootObject , textvariable=self.employee_User_Type , values=("Select","Admin","Employee") , state="readonly" , justify=CENTER , font=("goudy old style",15) )
        self.employee_User_Type_ComboBox.place(x=850,y=230,width=180)
        self.employee_User_Type_ComboBox.current(0)

        self.employee_Salary_Label = Label( self.rootObject , text="Salary" , font=("goudy old style",15) , bg="white" ).place(x=50,y=270)
        self.employee_Salary_Text_Field = Entry( self.rootObject , textvariable=self.employee_Salary , font=("goudy old style",15) , bg="lightyellow" ).place(x=150,y=270,width=180)
        
        self.employee_Attendence_Label = Label( self.rootObject , text="Attendence" , font=("goudy old style",15) , bg="white" ).place(x=350,y=270)
        self.employee_Attendence_Text_Field = Entry( self.rootObject , textvariable=self.employee_Attendence , font=("goudy old style",15) , bg="lightyellow" ).place(x=500,y=270,width=180)

        self.employee_Experience_Label = Label( self.rootObject , text="Experience" , font=("goudy old style",15) , bg="white" ).place(x=750,y=270)
        self.employee_Experience_Text_Field = Entry( self.rootObject , textvariable=self.employee_Experience , font=("goudy old style",15) , bg="lightyellow" ).place(x=850,y=270,width=180)

        self.employee_Date_Of_Joining_Label = Label( self.rootObject , text="Joining Date" , font=("goudy old style",15) , bg="white" ).place(x=500,y=310)
        self.employee_Date_Of_Joining_Text_Field = Entry( self.rootObject , textvariable=self.employee_Date_Of_Joining , font=("goudy old style",15) , bg="lightyellow" ).place(x=620,y=310,width=180)

        self.employee_Address_Label = Label( self.rootObject , text="Address" , font=("goudy old style",15) , bg="white" ).place(x=50,y=310)
        self.employee_Address_Text_Field = Text( self.rootObject , font=("goudy old style",15) , bg="lightyellow" )
        self.employee_Address_Text_Field.place(x=150,y=310,width=300,height=60)

        #------------------> Buttons Section <-------------------------------
        save_Button = Button( self.rootObject , text="Save" , font=("goudy old style",15) , bg="#008000" , fg="white" , cursor="hand2" , command=self.save ).place(x=500,y=345,width=110,height=30)
        update_Button = Button( self.rootObject , text="Update" , font=("goudy old style",15) , bg="#2B65EC" , fg="white" , cursor="hand2" , command=self.update ).place(x=620,y=345,width=110,height=30)
        delete_Button = Button( self.rootObject , text="Delete" , font=("goudy old style",15) , bg="#FF0000" , fg="white" , cursor="hand2" , command=self.delete ).place(x=740,y=345,width=110,height=30)
        clear_Button = Button( self.rootObject , text="Clear" , font=("goudy old style",15) , bg="#4E5180" , fg="white" , cursor="hand2" , command=self.clear ).place(x=860,y=345,width=110,height=30)

        #---------------------> Employee-Information-Table <--------------------------
        employee_Table_Frame = Frame( self.rootObject , bd=3 , relief=RIDGE )
        employee_Table_Frame.place( x = 0 , y = 380 , relwidth = 1 , height=150 )

        horizental_Scroll_Bar = Scrollbar( employee_Table_Frame , orient=HORIZONTAL )
        vertical_Scroll_Bar = Scrollbar( employee_Table_Frame , orient=VERTICAL )

        self.employee_Table = ttk.Treeview( employee_Table_Frame , columns=( "employee_id" , "employee_name" , "employee_gender" , "employee_age" , "employee_address" , "employee_dob" , "employee_contact" , "employee_email" , "employee_password" , "employee_user_type" , "employee_salary" , "employee_attendence" , "employee_doj" , "employee_experience" ) , xscrollcommand=horizental_Scroll_Bar.set , yscrollcommand=vertical_Scroll_Bar.set )
        horizental_Scroll_Bar.pack( side=BOTTOM , fill=X )
        vertical_Scroll_Bar.pack( side=RIGHT , fill=Y )
        horizental_Scroll_Bar.config( command=self.employee_Table.xview )
        vertical_Scroll_Bar.config( command=self.employee_Table.yview )

        self.employee_Table.heading( "employee_id" , text="Employee ID" )
        self.employee_Table.heading( "employee_name" , text="Name" )
        self.employee_Table.heading( "employee_gender" , text="Gender" )
        self.employee_Table.heading( "employee_age" , text="Age" )
        self.employee_Table.heading( "employee_address" , text="Address" )
        self.employee_Table.heading( "employee_dob" , text="Date-Of-Birth" )
        self.employee_Table.heading( "employee_contact" , text="Contact" )
        self.employee_Table.heading( "employee_email" , text="Email" )
        self.employee_Table.heading( "employee_password" , text="Password" )
        self.employee_Table.heading( "employee_user_type" , text="User-Type" )
        self.employee_Table.heading( "employee_salary" , text="Salary" )
        self.employee_Table.heading( "employee_attendence" , text="Attendence" )
        self.employee_Table.heading( "employee_doj" , text="Joining Date" )
        self.employee_Table.heading( "employee_experience" , text="Experience" )
        
        self.employee_Table["show"] = "headings"

        self.employee_Table.column( "employee_id" , width=90 )
        self.employee_Table.column( "employee_name" , width=90 )
        self.employee_Table.column( "employee_gender" , width=90 )
        self.employee_Table.column( "employee_age" , width=90 )
        self.employee_Table.column( "employee_address" , width=90 )
        self.employee_Table.column( "employee_dob" , width=90 )
        self.employee_Table.column( "employee_contact" , width=90 )
        self.employee_Table.column( "employee_email" , width=90 )
        self.employee_Table.column( "employee_password" , width=90 )
        self.employee_Table.column( "employee_user_type" , width=90 )
        self.employee_Table.column( "employee_salary" , width=90 )
        self.employee_Table.column( "employee_attendence" , width=90 )
        self.employee_Table.column( "employee_doj" , width=90 )
        self.employee_Table.column( "employee_experience" , width=90 )
        
        self.employee_Table.pack( fill=BOTH , expand=1 )
        self.employee_Table.bind("<ButtonRelease-1>" , self.get_Employee_Data_In_Form)
        
        self.show_Database_Data()

    #------------------> Database Section <-----------------------
    def save( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.employee_Id.get() == "":
                messagebox.showerror("Error" , "Employee-ID Must Be Required" , parent=self.rootObject)
            elif self.employee_Name.get() == '':
                messagebox.showerror("Error" , "Employee-Name Must Be Required" , parent=self.rootObject)
            # elif self.employee_Address.get() == "":
            #     messagebox.showerror("Error" , "Employee-Address Must Be Required" , parent=self.rootObject)
            elif self.employee_Age.get() == '':
                messagebox.showerror("Error" , "Employee-Age Must Be Required" , parent=self.rootObject)
            elif self.employee_Contact.get() == "":
                messagebox.showerror("Error" , "Employee-Contact Must Be Required" , parent=self.rootObject)
            elif self.employee_Date_Of_Joining.get() == '':
                messagebox.showerror("Error" , "Employee-Joining-Date Must Be Required" , parent=self.rootObject)
            elif self.employee_Date_Of_Birth.get() == "":
                messagebox.showerror("Error" , "Employee-Date-Of-Birth Must Be Required" , parent=self.rootObject)
            elif self.employee_Email.get() == '':
                messagebox.showerror("Error" , "Employee-Email Must Be Required" , parent=self.rootObject)
            elif self.employee_Experience.get() == "":
                messagebox.showerror("Error" , "Employee-Experience Must Be Required" , parent=self.rootObject)
            elif self.employee_Salary.get() == '':
                messagebox.showerror("Error" , "Employee-Salary Must Be Required" , parent=self.rootObject)
            # elif self.employee_Gender.get() == "":
            #     messagebox.showerror("Error" , "Employee-Gender Must Be Required" , parent=self.rootObject)
            # elif self.employee_User_Type.get() == '':
            #     messagebox.showerror("Error" , "Employee-User-Type Must Be Required" , parent=self.rootObject)
            elif self.employee_Password.get() == '':
                messagebox.showerror("Error" , "Employee-Password Must Be Required" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Employee where employee_id = ?",( self.employee_Id.get() , ) )
                row = queryCursor.fetchone()
                if row != None:
                    messagebox.showerror("Error" , f"This Employee-ID( {self.employee_Id.get()} ) Is Already Assigned To Someone So,\nPlease Try different Employee-ID" , parent = self.rootObject)
                else:
                    queryCursor.execute("insert into Employee ( employee_id , employee_name , employee_gender , employee_age , employee_address , employee_dob , employee_contact , employee_email , employee_password , employee_user_type , employee_salary , employee_attendence , employee_doj , employee_experience ) values( ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? ) " , ( self.employee_Id.get() , self.employee_Name.get() , self.employee_Gender.get() , self.employee_Age.get() , self.employee_Address_Text_Field.get('1.0',END) , self.employee_Date_Of_Birth.get() , self.employee_Contact.get() , self.employee_Email.get() , self.employee_Password.get() , self.employee_User_Type.get() , self.employee_Salary.get() , self.employee_Attendence.get() , self.employee_Date_Of_Joining.get() , self.employee_Experience.get() ) )
                    database_Connection.commit()
                    messagebox.showinfo("Success" , "Successfully New Employee Added" , parent=self.rootObject)
                    self.show_Database_Data()

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    #------------------> Show Database Data <-------------------------
    def show_Database_Data(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            queryCursor.execute("select * from Employee")
            tabular_Data = queryCursor.fetchall()
            self.employee_Table.delete( * self.employee_Table.get_children())
            for row in tabular_Data:
                self.employee_Table.insert("",END,values=row)
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)
    
    def get_Employee_Data_In_Form(self , employee_Data_In_Form):
        data_Format = self.employee_Table.focus()
        content = ( self.employee_Table.item( data_Format ) )
        row = content["values"]
        # print(row)
        self.employee_Id.set( row[0] )
        self.employee_Name.set( row[1] )
        self.employee_Gender.set( row[2] )
        self.employee_Age.set( row[3] )
        self.employee_Address_Text_Field.delete('1.0',END)
        self.employee_Address_Text_Field.insert(END,row[4])
        self.employee_Date_Of_Birth.set( row[5] )
        self.employee_Contact.set( row[6] )
        self.employee_Email.set( row[7] )
        self.employee_Password.set( row[8] )
        self.employee_User_Type.set( row[9] )
        self.employee_Salary.set( row[10] )
        self.employee_Attendence.set( row[11] )
        self.employee_Date_Of_Joining.set( row[12] )
        self.employee_Experience.set( row[13] )
    
    def update( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.employee_Id.get() == "":
                messagebox.showerror("Error" , "Employee-ID Must Be Required" , parent=self.rootObject)
            elif self.employee_Name.get() == '':
                messagebox.showerror("Error" , "Employee-Name Must Be Required" , parent=self.rootObject)
            # elif self.employee_Address.get() == "":
            #     messagebox.showerror("Error" , "Employee-Address Must Be Required" , parent=self.rootObject)
            elif self.employee_Age.get() == '':
                messagebox.showerror("Error" , "Employee-Age Must Be Required" , parent=self.rootObject)
            elif self.employee_Contact.get() == "":
                messagebox.showerror("Error" , "Employee-Contact Must Be Required" , parent=self.rootObject)
            elif self.employee_Date_Of_Joining.get() == '':
                messagebox.showerror("Error" , "Employee-Joining-Date Must Be Required" , parent=self.rootObject)
            elif self.employee_Date_Of_Birth.get() == "":
                messagebox.showerror("Error" , "Employee-Date-Of-Birth Must Be Required" , parent=self.rootObject)
            elif self.employee_Email.get() == '':
                messagebox.showerror("Error" , "Employee-Email Must Be Required" , parent=self.rootObject)
            elif self.employee_Experience.get() == "":
                messagebox.showerror("Error" , "Employee-Experience Must Be Required" , parent=self.rootObject)
            elif self.employee_Salary.get() == '':
                messagebox.showerror("Error" , "Employee-Salary Must Be Required" , parent=self.rootObject)
            # elif self.employee_Gender.get() == "":
            #     messagebox.showerror("Error" , "Employee-Gender Must Be Required" , parent=self.rootObject)
            # elif self.employee_User_Type.get() == '':
            #     messagebox.showerror("Error" , "Employee-User-Type Must Be Required" , parent=self.rootObject)
            elif self.employee_Password.get() == '':
                messagebox.showerror("Error" , "Employee-Password Must Be Required" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Employee where employee_id = ?",( self.employee_Id.get() , ) )
                row = queryCursor.fetchone()
                if row == None:
                    messagebox.showerror("Error" , "Invalid Employee-ID" , parent = self.rootObject)
                else:
                    queryCursor.execute("update Employee set employee_name = ? , employee_gender = ? , employee_age = ? , employee_address = ? , employee_dob = ? , employee_contact = ? , employee_email = ? , employee_password = ? , employee_user_type = ? , employee_salary = ? , employee_attendence = ? , employee_doj = ? , employee_experience = ? where employee_id = ? " , ( self.employee_Name.get() , self.employee_Gender.get() , self.employee_Age.get() , self.employee_Address_Text_Field.get('1.0',END) , self.employee_Date_Of_Birth.get() , self.employee_Contact.get() , self.employee_Email.get() , self.employee_Password.get() , self.employee_User_Type.get() , self.employee_Salary.get() , self.employee_Attendence.get() , self.employee_Date_Of_Joining.get() , self.employee_Experience.get() , self.employee_Id.get() ) )
                    database_Connection.commit()
                    messagebox.showinfo("Success" , "Successfully Employee Updated" , parent=self.rootObject)
                    self.show_Database_Data()

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    def delete( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.employee_Id.get() == "":
                messagebox.showerror("Error" , "Employee-ID Must Be Required" , parent=self.rootObject)
            elif self.employee_Name.get() == '':
                messagebox.showerror("Error" , "Employee-Name Must Be Required" , parent=self.rootObject)
            # elif self.employee_Address.get() == "":
            #     messagebox.showerror("Error" , "Employee-Address Must Be Required" , parent=self.rootObject)
            elif self.employee_Age.get() == '':
                messagebox.showerror("Error" , "Employee-Age Must Be Required" , parent=self.rootObject)
            elif self.employee_Contact.get() == "":
                messagebox.showerror("Error" , "Employee-Contact Must Be Required" , parent=self.rootObject)
            elif self.employee_Date_Of_Joining.get() == '':
                messagebox.showerror("Error" , "Employee-Joining-Date Must Be Required" , parent=self.rootObject)
            elif self.employee_Date_Of_Birth.get() == "":
                messagebox.showerror("Error" , "Employee-Date-Of-Birth Must Be Required" , parent=self.rootObject)
            elif self.employee_Email.get() == '':
                messagebox.showerror("Error" , "Employee-Email Must Be Required" , parent=self.rootObject)
            elif self.employee_Experience.get() == "":
                messagebox.showerror("Error" , "Employee-Experience Must Be Required" , parent=self.rootObject)
            elif self.employee_Salary.get() == '':
                messagebox.showerror("Error" , "Employee-Salary Must Be Required" , parent=self.rootObject)
            # elif self.employee_Gender.get() == "":
            #     messagebox.showerror("Error" , "Employee-Gender Must Be Required" , parent=self.rootObject)
            # elif self.employee_User_Type.get() == '':
            #     messagebox.showerror("Error" , "Employee-User-Type Must Be Required" , parent=self.rootObject)
            elif self.employee_Password.get() == '':
                messagebox.showerror("Error" , "Employee-Password Must Be Required" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Employee where employee_id = ?",( self.employee_Id.get() , ) )
                row = queryCursor.fetchone()
                if row == None:
                    messagebox.showerror("Error" , "Invalid Employee-ID" , parent = self.rootObject)
                else:
                    confirmation_Message = messagebox.askyesno("Confirm" , "Do you really want to delete ?" , parent = self.rootObject)
                    if confirmation_Message == True:
                        queryCursor.execute("delete from Employee where employee_id = ?" , ( self.employee_Id.get() , ) )
                        database_Connection.commit()
                        messagebox.showinfo("Delete" , "Employeee Delete Successfully" , parent = self.rootObject)
                        self.clear()
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    def clear(self):
        self.employee_Id.set("")
        self.employee_Name.set("")
        self.employee_Gender.set("Select")
        self.employee_Age.set('')
        self.employee_Address_Text_Field.delete('1.0',END)
        self.employee_Date_Of_Birth.set("")
        self.employee_Contact.set("")
        self.employee_Email.set("")
        self.employee_Password.set('')
        self.employee_User_Type.set("Admin")
        self.employee_Salary.set('')
        self.employee_Attendence.set("")
        self.employee_Date_Of_Joining.set('')
        self.employee_Experience.set("")
        self.search_Text.set("")
        self.search_By.set("Select")
        self.show_Database_Data()
    
    def search_Employee(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.search_By.get() == "Select":
                messagebox.showerror("Error" , "Select Search By Option" , parent = self.rootObject)
            elif self.search_Text.get() == "":
                messagebox.showerror("Error" , "Search Input Should Be Required" , parent = self.rootObject)
            else:
                # queryCursor.execute("select * from Employee where "+str( self.search_By.get() )+" LIKE '%"+ str( self.search_Text.get() )+"%'")
                queryCursor.execute("select * from Employee where employee_id LIKE '%"+self.search_Text.get()+"%' or employee_name LIKE '%"+self.search_Text.get()+"%' or employee_contact LIKE '%"+self.search_Text.get()+"%' or employee_email LIKE '%"+self.search_Text.get()+"%'")
                tabular_Data = queryCursor.fetchall()
                if len( tabular_Data ) != 0:
                    self.employee_Table.delete( * self.employee_Table.get_children())
                    for row in tabular_Data:
                        self.employee_Table.insert("",END,values=row)
                else:
                    messagebox.showerror("Error" , "No Record Found :(" , parent = self.rootObject)

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} :)) " , parent = self.rootObject)
    
if __name__ == "__main__":
    root_Object = Tk()
    employee_Module = Employee_Module( root_Object )
    root_Object.resizable( False , False )
    root_Object.mainloop()  # mainloop() use to keep open output-window.