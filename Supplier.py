from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk , messagebox
import sqlite3

class Supplier_Module:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1100x550+220+130")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")
        self.rootObject.focus_force()

        #---------------> Employee-Attributes <---------------
        self.search_By = StringVar()
        self.search_Text = StringVar()

        self.supplier_Invoice_Id = StringVar()
        self.supplier_Name = StringVar()
        self.supplier_Contact = StringVar()

        #-----------> Search Frame <----------------
        # search_Frame = LabelFrame( self.rootObject , text="Search" , font=("goudy old style",12,"bold") , bd = 2 , relief=RIDGE , bg="white" )
        # search_Frame.place( x = 250 , y = 20 , width = 600 , height = 70 )
        
        #--------------> Search Frame Options <-------------------
        search_Label = Label( self.rootObject , text="Invoice ID" , bg="white" , font=("goudy old style",15) )
        search_Label.place( x = 660 , y = 87 )

        textField_Search = Entry( self.rootObject , textvariable=self.search_Text , font=("goudy old style",15) , bg="lightyellow" ).place(x=755,y=87,width=163,height=30)

        search_Button = Button( self.rootObject , text="Search" , font=("goudy old style",15) , bg="#008000" , fg="white" , cursor="hand2" , command=self.search_Employee ).place(x=931,y=87,width=127,height=30)

        #-----------------> Supplier-Details-Title <-----------------------
        supplier_Details_Title = Label( self.rootObject , text="Supplier Details" , font=("goudy old style",22,"bold") , bg="#273746" , fg="white" ).place(x=50,y=10,width=1015,height=45)

        #---------------------> Supplier-Details Contents <------------------------
        self.supplier_Invoice_Id_Label = Label( self.rootObject , text="Invoice ID" , font=("goudy old style",15) , bg="white" ).place(x=50,y=80)
        self.supplier_Invoice_Id_Text_Field = Entry( self.rootObject , textvariable=self.supplier_Invoice_Id , font=("goudy old style",15) , bg="lightyellow" ).place(x=180,y=80,width=180)
        
        self.supplier_Name_Label = Label( self.rootObject , text="Name" , font=("goudy old style",15) , bg="white" ).place(x=50,y=120)
        self.supplier_Name_Text_Field = Entry( self.rootObject , textvariable=self.supplier_Name , font=("goudy old style",15) , bg="lightyellow" ).place(x=180,y=120,width=180)

        self.supplier_Contact_Label = Label( self.rootObject , text="Contact" , font=("goudy old style",15) , bg="white" ).place(x=50,y=160)
        self.supplier_Contact_Text_Field = Entry( self.rootObject , textvariable=self.supplier_Contact , font=("goudy old style",15) , bg="lightyellow" ).place(x=180,y=160,width=180)
                
        self.supplier_Description_Label = Label( self.rootObject , text="Description" , font=("goudy old style",15) , bg="white" ).place(x=50,y=200)
        self.supplier_Description_Text_Field = Text( self.rootObject , font=("goudy old style",15) , bg="lightyellow" )
        self.supplier_Description_Text_Field.place(x=180,y=200,width=450,height=255)

        #------------------> Buttons Section <-------------------------------
        save_Button = Button( self.rootObject , text="Save" , font=("goudy old style",15) , bg="#008000" , fg="white" , cursor="hand2" , command=self.save ).place(x=180,y=480,width=110,height=40)
        update_Button = Button( self.rootObject , text="Update" , font=("goudy old style",15) , bg="#2B65EC" , fg="white" , cursor="hand2" , command=self.update ).place(x=300,y=480,width=110,height=40)
        delete_Button = Button( self.rootObject , text="Delete" , font=("goudy old style",15) , bg="#FF0000" , fg="white" , cursor="hand2" , command=self.delete ).place(x=420,y=480,width=110,height=40)
        clear_Button = Button( self.rootObject , text="Clear" , font=("goudy old style",15) , bg="#4E5180" , fg="white" , cursor="hand2" , command=self.clear ).place(x=540,y=480,width=110,height=40)

        #---------------------> Employee-Information-Table <--------------------------
        supplier_Table_Frame = Frame( self.rootObject , bd=3 , relief=RIDGE )
        supplier_Table_Frame.place( x = 660 , y = 120 , width = 400 , height=400 )

        horizental_Scroll_Bar = Scrollbar( supplier_Table_Frame , orient=HORIZONTAL )
        vertical_Scroll_Bar = Scrollbar( supplier_Table_Frame , orient=VERTICAL )

        self.supplier_Table = ttk.Treeview( supplier_Table_Frame , columns=( "supplier_invoice_id" , "supplier_name" , "supplier_description" , "supplier_contact" ) , xscrollcommand=horizental_Scroll_Bar.set , yscrollcommand=vertical_Scroll_Bar.set )
        horizental_Scroll_Bar.pack( side=BOTTOM , fill=X )
        vertical_Scroll_Bar.pack( side=RIGHT , fill=Y )
        horizental_Scroll_Bar.config( command=self.supplier_Table.xview )
        vertical_Scroll_Bar.config( command=self.supplier_Table.yview )

        self.supplier_Table.heading( "supplier_invoice_id" , text="Invoice ID" )
        self.supplier_Table.heading( "supplier_name" , text="Name" )
        self.supplier_Table.heading( "supplier_description" , text="Description" )
        self.supplier_Table.heading( "supplier_contact" , text="Contact" )
        
        self.supplier_Table["show"] = "headings"

        self.supplier_Table.column( "supplier_invoice_id" , width=90 )
        self.supplier_Table.column( "supplier_name" , width=90 )
        self.supplier_Table.column( "supplier_description" , width=90 )
        self.supplier_Table.column( "supplier_contact" , width=90 )
        
        self.supplier_Table.pack( fill=BOTH , expand=1 )
        self.supplier_Table.bind("<ButtonRelease-1>" , self.get_Supplier_Data_In_Form)
        
        self.show_Database_Data()

    #------------------> Database Section <-----------------------
    def save( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.supplier_Invoice_Id.get() == "":
                messagebox.showerror("Error" , "Invoice-ID Must Be Required" , parent=self.rootObject)
            elif self.supplier_Name.get() == '':
                messagebox.showerror("Error" , "Supplier-Name Must Be Required" , parent=self.rootObject)
            elif self.supplier_Contact.get() == "":
                messagebox.showerror("Error" , "Supplier-Contact Must Be Required" , parent=self.rootObject)
            #elif self.supplier_Description_Text_Field.get() == '':
            #    messagebox.showerror("Error" , "Supplier-Description Must Be Required" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Supplier where supplier_invoice_id = ?",( self.supplier_Invoice_Id.get() , ) )
                row = queryCursor.fetchone()
                if row != None:
                    messagebox.showerror("Error" , f"This Invoice-ID( {self.supplier_Invoice_Id.get()} ) Is Already Assigned To Someone So,\nPlease Try different Invoice-ID" , parent = self.rootObject)
                else:
                    queryCursor.execute("insert into Supplier ( supplier_invoice_id , supplier_name , supplier_description , supplier_contact ) values( ? , ? , ? , ? ) " , ( self.supplier_Invoice_Id.get() , self.supplier_Name.get() , self.supplier_Description_Text_Field.get('1.0',END) , self.supplier_Contact.get() ) )
                    database_Connection.commit()
                    messagebox.showinfo("Success" , "Successfully New Supplier Added" , parent=self.rootObject)
                    self.show_Database_Data()

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    #------------------> Show Database Data <-------------------------
    def show_Database_Data(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            queryCursor.execute("select * from Supplier")
            tabular_Data = queryCursor.fetchall()
            self.supplier_Table.delete( * self.supplier_Table.get_children())
            for row in tabular_Data:
                self.supplier_Table.insert("",END,values=row)
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error caused due to : {str(exception_error)} " , parent = self.rootObject)
    
    def get_Supplier_Data_In_Form(self , supplier_Data_In_Form):
        data_Format = self.supplier_Table.focus()
        content = ( self.supplier_Table.item( data_Format ) )
        row = content["values"]
        # print(row)
        self.supplier_Invoice_Id.set( row[0] )
        self.supplier_Name.set( row[1] )
        self.supplier_Description_Text_Field.delete('1.0',END)
        self.supplier_Description_Text_Field.insert(END , row[2])
        self.supplier_Contact.set( row[3] )
    
    def update( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.supplier_Invoice_Id.get() == "":
                messagebox.showerror("Error" , "Supplier Invoice-ID Must Be Required" , parent=self.rootObject)
            elif self.supplier_Name.get() == '':
                messagebox.showerror("Error" , "Supplier-Name Must Be Required" , parent=self.rootObject)
            #elif self.supplier_Description_Text_Field.get() == "":
            #    messagebox.showerror("Error" , "Supplier-Description Must Be Required" , parent=self.rootObject)
            elif self.supplier_Contact.get() == "":
                messagebox.showerror("Error" , "Supplier-Contact Must Be Required" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Supplier where supplier_invoice_id = ?",( self.supplier_Invoice_Id.get() , ) )
                row = queryCursor.fetchone()
                if row == None:
                    messagebox.showerror("Error" , "Invalid Supplier Invoice-ID" , parent = self.rootObject)
                else:
                    queryCursor.execute("update Supplier set supplier_name = ? , supplier_description = ? , supplier_contact = ? where supplier_invoice_id = ? " , ( self.supplier_Name.get() , self.supplier_Description_Text_Field.get('1.0',END) , self.supplier_Contact.get() , self.supplier_Invoice_Id.get() ) )
                    database_Connection.commit()
                    messagebox.showinfo("Success" , "Successfully Supplier Updated" , parent=self.rootObject)
                    self.show_Database_Data()

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error produced due to : {str(exception_error)} " , parent = self.rootObject)

    def delete( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.supplier_Invoice_Id.get() == "":
                messagebox.showerror("Error" , "Supplier Invoice-ID Must Be Required" , parent=self.rootObject)
            elif self.supplier_Name.get() == '':
                messagebox.showerror("Error" , "Supplier-Name Must Be Required" , parent=self.rootObject)
            # elif self.supplier_Description_Text_Field.get() == "":
            #     messagebox.showerror("Error" , "Supplier-Description Must Be Required" , parent=self.rootObject)
            elif self.supplier_Contact.get() == "":
                messagebox.showerror("Error" , "Supplier-Contact Must Be Required" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Supplier where supplier_invoice_id = ?",( self.supplier_Invoice_Id.get() , ) )
                row = queryCursor.fetchone()
                if row == None:
                    messagebox.showerror("Error" , "Invalid Supplier Invoice-ID" , parent = self.rootObject)
                else:
                    confirmation_Message = messagebox.askyesno("Confirm" , "Do you really want to delete ?" , parent = self.rootObject)
                    if confirmation_Message == True:
                        queryCursor.execute("delete from Supplier where supplier_invoice_id = ?" , ( self.supplier_Invoice_Id.get() , ) )
                        database_Connection.commit()
                        messagebox.showinfo("Delete" , "Supplier Delete Successfully" , parent = self.rootObject)
                        self.clear()
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    def clear(self):
        self.supplier_Invoice_Id.set("")
        self.supplier_Name.set("")
        self.supplier_Description_Text_Field.delete('1.0',END)
        self.supplier_Contact.set("")
        self.search_Text.set("")
        self.show_Database_Data()
    
    def search_Employee(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.search_Text.get() == "":
                messagebox.showerror("Error" , "Supplier Invoice-ID Should Be Required" , parent = self.rootObject)
            else:
                # queryCursor.execute("select * from Supplier where "+str( self.search_By.get() )+" LIKE '%"+ str( self.search_Text.get() )+"%'")
                queryCursor.execute("select * from Supplier where supplier_invoice_id = ?",(self.search_Text.get() , ) )
                row = queryCursor.fetchone()
                if row != None:
                    self.supplier_Table.delete( * self.supplier_Table.get_children())
                    self.supplier_Table.insert("",END,values=row)
                else:
                    messagebox.showerror("Error" , "No Record Found :(" , parent = self.rootObject)

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} :)) " , parent = self.rootObject)
    
if __name__ == "__main__":
    root_Object = Tk()
    supplier_Module = Supplier_Module( root_Object )
    root_Object.resizable( False , False )
    root_Object.mainloop()  # mainloop() use to keep open output-window.