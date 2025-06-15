from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk , messagebox
import sqlite3

class Category_Module:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1100x550+220+130")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")
        self.rootObject.focus_force()

        #---------------> Category-Attributes <---------------
        self.category_Id = StringVar()
        self.category_Name = StringVar()

        ################### Title #####################
        title_Label = Label( self.rootObject , text="Manage Product Category" , font=("goudy old style" , 30) , bg="#343123" , fg="white" , bd=2 , relief=RIDGE ).pack(side=TOP , fill=X , padx=12 , pady=4)

        category_Name_Label = Label( self.rootObject , text="Enter Category Name" , font=("goudy old style" , 30) , bg="white" ).place( x = 50 , y = 100 )

        category_Name = Entry( self.rootObject , textvariable=self.category_Name , font=("goudy old style" , 20) , bg="lightyellow" ).place( x = 50 , y = 170 , width=300 )

        add_Button = Button( self.rootObject , command=self.add , text="Add" , font=("goudy old style" , 20) , bg="#4caf50" , fg="white" , cursor="hand2" ).place( x = 360 , y = 170 , width=150 , height=35 )
        delete_Button = Button( self.rootObject , command=self.delete , text="Delete" , font=("goudy old style" , 20) , bg="red" , fg="white" , cursor="hand2" ).place( x = 520 , y = 170 , width=150 , height=35 )

        #---------------------> Category-Information-Table <--------------------------
        category_Table_Frame = Frame( self.rootObject , bd=3 , relief=RIDGE )
        category_Table_Frame.place( x = 685 , y = 100 , width = 400 , height=105 )

        horizental_Scroll_Bar = Scrollbar( category_Table_Frame , orient=HORIZONTAL )
        vertical_Scroll_Bar = Scrollbar( category_Table_Frame , orient=VERTICAL )

        self.category_Table = ttk.Treeview( category_Table_Frame , columns=( "category_id" , "category_name" ) , xscrollcommand=horizental_Scroll_Bar.set , yscrollcommand=vertical_Scroll_Bar.set )
        horizental_Scroll_Bar.pack( side=BOTTOM , fill=X )
        vertical_Scroll_Bar.pack( side=RIGHT , fill=Y )
        horizental_Scroll_Bar.config( command=self.category_Table.xview )
        vertical_Scroll_Bar.config( command=self.category_Table.yview )

        self.category_Table.heading( "category_id" , text="Category ID" )
        self.category_Table.heading( "category_name" , text="Category Name" )
        
        self.category_Table["show"] = "headings"

        self.category_Table.column( "category_id" , width=90 )
        self.category_Table.column( "category_name" , width=90 )
        
        self.category_Table.pack( fill=BOTH , expand=1 )
        self.category_Table.bind("<ButtonRelease-1>" , self.get_Supplier_Data_In_Form)

        ################ Images ######################
        self.category_Image = Image.open("./pictures/category_5.jpg")
        self.category_Image = self.category_Image.resize( ( 500 , 315 ) , Image.BICUBIC )
        self.category_Image = ImageTk.PhotoImage( self.category_Image )

        self.category_Image_Label = Label( self.rootObject , image=self.category_Image , bd=2 , relief=RAISED )
        self.category_Image_Label.place( x=50 , y=220 )

        self.categoryImage = Image.open("./pictures/category_2.jpg")
        self.categoryImage = self.categoryImage.resize( ( 510 , 315 ) , Image.BICUBIC )
        self.categoryImage = ImageTk.PhotoImage( self.categoryImage )

        self.categoryImageLabel = Label( self.rootObject , image=self.categoryImage , bd=2 , relief=RAISED )
        self.categoryImageLabel.place( x=570 , y=220 )

        self.show_Database_Data()
    #------------------> Database Section <-----------------------
    def add( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.category_Name.get() == '':
                messagebox.showerror("Error" , "Category-Name Must Be Required" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Category where category_name = ?",( self.category_Name.get() , ) )
                row = queryCursor.fetchone()
                if row != None:
                    messagebox.showerror("Error" , "Please try unique category-id" , parent = self.rootObject)
                else:
                    queryCursor.execute("insert into Category ( category_name ) values( ? ) " , ( self.category_Name.get(), ) )
                    database_Connection.commit()
                    messagebox.showinfo("Success" , "Successfully New Category Added" , parent=self.rootObject)
                    self.show_Database_Data()
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    #------------------> Show Database Data <-------------------------
    def show_Database_Data(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            queryCursor.execute("select * from Category")
            tabular_Data = queryCursor.fetchall()
            self.category_Table.delete( * self.category_Table.get_children())
            for row in tabular_Data:
                self.category_Table.insert("",END,values=row)
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error caused due to : {str(exception_error)} " , parent = self.rootObject)

    def get_Supplier_Data_In_Form(self , category_Data_In_Form):
        data_Format = self.category_Table.focus()
        content = ( self.category_Table.item( data_Format ) )
        row = content["values"]
        # print(row)
        self.category_Id.set( row[0] )
        self.category_Name.set( row[1] )
    
    def delete( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.category_Id.get() == "":
                messagebox.showerror("Error" , "Please select category from the list" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Category where category_id = ?",( self.category_Id.get() , ) )
                row = queryCursor.fetchone()
                if row == None:
                    messagebox.showerror("Error" , "Error, Please try again" , parent = self.rootObject)
                else:
                    confirmation_Message = messagebox.askyesno("Confirm" , "Do you really want to delete ?" , parent = self.rootObject)
                    if confirmation_Message == True:
                        queryCursor.execute("delete from Category where category_id = ?" , ( self.category_Id.get() , ) )
                        database_Connection.commit()
                        messagebox.showinfo("Delete" , "Category Deleted Successfully" , parent = self.rootObject)
                        self.show_Database_Data()
                        self.category_Id.set("")
                        self.category_Name.set('')

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)


if __name__ == "__main__":
    root_Object = Tk()
    category_Module = Category_Module( root_Object )
    root_Object.resizable( False , False )
    root_Object.mainloop()  # mainloop() use to keep open output-window.