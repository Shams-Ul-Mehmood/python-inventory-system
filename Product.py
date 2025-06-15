from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk , messagebox
import sqlite3

class Product_Module:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1100x550+220+130")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")
        self.rootObject.focus_force()

        ############################ Variable ######################
        self.search_By = StringVar()
        self.search_Text = StringVar()
        self.productId = StringVar()
        self.productCategory = StringVar()
        self.productCategoryList = []
        self.productName = StringVar()
        self.productSupplier = StringVar()
        self.productSupplierList = list()
        self.fetch_Category_Supplier()
        self.productPrice = StringVar()
        self.productQuantity = StringVar()
        self.productStatus = StringVar()

        ############################# Product Frame ##########################
        productFrame = Frame( self.rootObject , bg="white" , bd=2, relief=RIDGE )
        productFrame.place( x=10 , y=10, width=450, height=480 )

        productTitle = Label( productFrame , text="Product Details" , font=("goudy old style",20) , bg="#273746" , fg="white" ).pack( side=TOP , fill=X )

        productCategoryTitle = Label( productFrame , text="Category" , font=("goudy old style",20) , bg="white" ).place( x=30 , y=60 )
        productNameTitle = Label( productFrame , text="Name" , font=("goudy old style",20) , bg="white" ).place( x=30 , y=110 )
        productSupplierTitle = Label( productFrame , text="Supplier" , font=("goudy old style",20) , bg="white" ).place( x=30 , y=160 )
        productPriceTitle = Label( productFrame , text="Price" , font=("goudy old style",20) , bg="white" ).place( x=30 , y=210 )
        productQuantityTitle = Label( productFrame , text="Quantity" , font=("goudy old style",20) , bg="white" ).place( x=30 , y=260 )
        productStatusTitle = Label( productFrame , text="Status" , font=("goudy old style",20) , bg="white" ).place( x=30 , y=310 )
        
        #--------------> Search Frame Options <-------------------
        productCategory_ComboBox = ttk.Combobox( productFrame , textvariable=self.productCategory , values=self.productCategoryList , state="readonly" , justify=CENTER , font=("goudy old style",15) )
        productCategory_ComboBox.place( x = 150 , y = 65 , width=200 )
        productCategory_ComboBox.current(0)

        productName_ComboBox = Entry( productFrame , textvariable=self.productName , font=("goudy old style",15) , bg="lightyellow" ).place( x = 150 , y = 115 , width=200 )

        productSupplier_ComboBox = ttk.Combobox( productFrame , textvariable=self.productSupplier , values=self.productSupplierList , state="readonly" , justify=CENTER , font=("goudy old style",15) )
        productSupplier_ComboBox.place( x = 150 , y = 165 , width=200 )
        productSupplier_ComboBox.current(0)

        productPrice_ComboBox = Entry( productFrame , textvariable=self.productPrice , font=("goudy old style",15) , bg="lightyellow" ).place( x = 150 , y = 215 , width=200 )

        productQuantity_ComboBox = Entry( productFrame , textvariable=self.productQuantity , font=("goudy old style",15) , bg="lightyellow" ).place( x = 150 , y = 265 , width=200 )

        productStatus_ComboBox = ttk.Combobox( productFrame , textvariable=self.productStatus , values=("Active",'Inactive') , state="readonly" , justify=CENTER , font=("goudy old style",15) )
        productStatus_ComboBox.place( x = 150 , y = 315 , width=200 )
        productStatus_ComboBox.current(0)


        #------------------> Buttons Section <-------------------------------
        save_Button = Button( productFrame , text="Save" , command=self.save , font=("goudy old style",15) , bg="#008000" , fg="white" , cursor="hand2" ).place(x=10,y=400,width=100,height=40)
        update_Button = Button( productFrame , text="Update" , command=self.update , font=("goudy old style",15) , bg="#2B65EC" , fg="white" , cursor="hand2" ).place(x=120,y=400,width=100,height=40)
        delete_Button = Button( productFrame , text="Delete" , command=self.delete , font=("goudy old style",15) , bg="#FF0000" , fg="white" , cursor="hand2" ).place(x=230,y=400,width=100,height=40)
        clear_Button = Button( productFrame , text="Clear" , command=self.clear , font=("goudy old style",15) , bg="#4E5180" , fg="white" , cursor="hand2" ).place(x=340,y=400,width=100,height=40)

        #-----------> Search Frame <----------------
        searchFrame = LabelFrame( self.rootObject , text="Search Product" , font=("goudy old style",12,"bold") , bd = 2 , relief=RIDGE , bg="white" )
        searchFrame.place( x = 490 , y = 10 , width = 600 , height = 80 )

        #--------------> Search Frame Options <-------------------
        search_ComboBox = ttk.Combobox( searchFrame , textvariable=self.search_By , values=("Select","Name","Category","Supplier") , state="readonly" , justify=CENTER , font=("goudy old style",15) )
        search_ComboBox.place( x = 10 , y = 7 , width=180 )
        search_ComboBox.current(0)

        textField_Search = Entry( searchFrame , textvariable=self.search_Text , font=("goudy old style",15) , bg="lightyellow" ).place(x=200,y=7,width=220,height=30)

        search_Button = Button( searchFrame , text="Search" , command=self.search_Product , font=("goudy old style",15) , bg="#008000" , fg="white" , cursor="hand2"  ).place(x=430,y=7,width=150,height=30)

        #---------------------> Product-Information-Table <--------------------------
        product_Table_Frame = Frame( self.rootObject , bd=3 , relief=RIDGE )
        product_Table_Frame.place( x = 488 , y = 100 , width = 600 , height=390 )

        horizental_Scroll_Bar = Scrollbar( product_Table_Frame , orient=HORIZONTAL )
        vertical_Scroll_Bar = Scrollbar( product_Table_Frame , orient=VERTICAL )

        self.product_Table = ttk.Treeview( product_Table_Frame , columns=( "product_id" , "category" , "supplier" , "name" , "price" , "quantity" , "status" ) , xscrollcommand=horizental_Scroll_Bar.set , yscrollcommand=vertical_Scroll_Bar.set )
        horizental_Scroll_Bar.pack( side=BOTTOM , fill=X )
        vertical_Scroll_Bar.pack( side=RIGHT , fill=Y )
        horizental_Scroll_Bar.config( command=self.product_Table.xview )
        vertical_Scroll_Bar.config( command=self.product_Table.yview )

        self.product_Table.heading( "product_id" , text="Product ID" )
        self.product_Table.heading( "category" , text="Category" )
        self.product_Table.heading( "supplier" , text="Supplier" )
        self.product_Table.heading( "name" , text="Name" )
        self.product_Table.heading( "price" , text="Price" )
        self.product_Table.heading( "quantity" , text="Quantity" )
        self.product_Table.heading( "status" , text="Status" )
        
        self.product_Table["show"] = "headings"

        self.product_Table.column( "product_id" , width=90 )
        self.product_Table.column( "category" , width=90 )
        self.product_Table.column( "supplier" , width=90 )
        self.product_Table.column( "name" , width=90 )
        self.product_Table.column( "price" , width=90 )
        self.product_Table.column( "quantity" , width=90 )
        self.product_Table.column( "status" , width=90 )
        
        self.product_Table.pack( fill=BOTH , expand=1 )
        self.product_Table.bind("<ButtonRelease-1>" , self.get_Supplier_Data_In_Form)
        
        self.show_Database_Data()
        

        #------------------> Database Section <-----------------------
    
    def fetch_Category_Supplier(self):
        self.productCategoryList.append("Empty")
        self.productSupplierList.append("Empty")
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            queryCursor.execute("select category_name from Category")
            category = queryCursor.fetchall()
            # print(category)
            # category_List = list()
            
            if len(category) > 0:
                del self.productCategoryList[:]
                self.productCategoryList.append("Select")
                for i in category:
                    # category_List.append(i[0])
                    self.productCategoryList.append(i[0])

            queryCursor.execute("select supplier_name from Supplier")
            supplier = queryCursor.fetchall()
            # print(supplier)
            if len(supplier) > 0:
                del self.productSupplierList[:]
                self.productSupplierList.append("Select")
                for i in supplier:
                    # supplier_List.append(i[0])
                    self.productSupplierList.append(i[0])

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)


    def save( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.productCategory.get() == "Select" or self.productCategory.get() == "Empty" or self.productSupplier.get() == "Select" or self.productName.get() == "":
                messagebox.showerror("Error" , "All fields are required" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Product where name = ?",( self.productName.get() , ) )
                row = queryCursor.fetchone()
                if row != None:
                    messagebox.showerror("Error" , "Product is already present, please try different" , parent = self.rootObject)
                else:
                    queryCursor.execute("insert into Product ( supplier , category , name , price , quantity , status ) values( ? , ? , ? , ? , ? , ? ) " , ( self.productSupplier.get() , self.productCategory.get() , self.productName.get() , self.productPrice.get() , self.productQuantity.get() , self.productStatus.get() ) )
                    database_Connection.commit()
                    messagebox.showinfo("Success" , "New Product Added Successfully" , parent=self.rootObject)
                    self.show_Database_Data()

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    #------------------> Show Database Data <-------------------------
    def show_Database_Data(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            queryCursor.execute("select * from Product")
            tabular_Data = queryCursor.fetchall()
            self.product_Table.delete( * self.product_Table.get_children())
            for row in tabular_Data:
                self.product_Table.insert("",END,values=row)
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)
    
    def get_Supplier_Data_In_Form(self , employee_Data_In_Form):
        data_Format = self.product_Table.focus()
        content = ( self.product_Table.item( data_Format ) )
        row = content["values"]
        self.productId.set(row[0])
        self.productSupplier.set(row[2])
        self.productCategory.set(row[1])
        self.productName.set(row[3])
        self.productPrice.set(row[4])
        self.productQuantity.set(row[5])
        self.productStatus.set(row[6])
    
    def update( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.productId.get() == "":
                messagebox.showerror("Error" , "Please select product from list" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Product where product_id = ?",( self.productId.get() , ) )
                row = queryCursor.fetchone()
                if row == None:
                    messagebox.showerror("Error" , "Invalid Product-ID" , parent = self.rootObject)
                else:
                    queryCursor.execute("update Product set Supplier = ? , Category = ? , name = ? , price = ? , quantity = ? , status = ? where product_id = ? " , ( self.productSupplier.get() , self.productCategory.get() , self.productName.get() , self.productPrice.get() , self.productQuantity.get() , self.productStatus.get() , self.productId.get() ) )
                    database_Connection.commit()
                    messagebox.showinfo("Success" , "Successfully Product Updated" , parent=self.rootObject)
                    self.show_Database_Data()

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    def delete( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.productId.get() == "":
                messagebox.showerror("Error" , "Select product from the list" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Product where product_id = ?",( self.productId.get() , ) )
                row = queryCursor.fetchone()
                if row == None:
                    messagebox.showerror("Error" , "Invalid Product" , parent = self.rootObject)
                else:
                    confirmation_Message = messagebox.askyesno("Confirm" , "Do you really want to delete ?" , parent = self.rootObject)
                    if confirmation_Message == True:
                        queryCursor.execute("delete from Product where product_id = ?" , ( self.productId.get() , ) )
                        database_Connection.commit()
                        messagebox.showinfo("Delete" , "Product Delete Successfully" , parent = self.rootObject)
                        self.clear()
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    def clear(self):
        self.productCategory.set("Select")
        self.productSupplier.set("Select")
        self.productName.set("")
        self.productPrice.set("")
        self.productQuantity.set("")
        self.productStatus.set("Active")
        self.productId.set("")
        self.search_Text.set("")
        self.search_By.set("Select")
        self.show_Database_Data()
    
    def search_Product(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.search_By.get() == "Select":
                messagebox.showerror("Error" , "Select Search By Option" , parent = self.rootObject)
            elif self.search_Text.get() == "":
                messagebox.showerror("Error" , "Search Input Should Be Required" , parent = self.rootObject)
            else:
                # queryCursor.execute("select * from Product where "+str( self.search_By.get() )+" LIKE '%"+ str( self.search_Text.get() )+"%'")
                queryCursor.execute("select * from Product where product_id LIKE '%"+self.search_Text.get()+"%' or name LIKE '%"+self.search_Text.get()+"%' or price LIKE '%"+self.search_Text.get()+"%' or quantity LIKE '%"+self.search_Text.get()+"%'")
                tabular_Data = queryCursor.fetchall()
                if len( tabular_Data ) != 0:
                    self.product_Table.delete( * self.product_Table.get_children())
                    for row in tabular_Data:
                        self.product_Table.insert("",END,values=row)
                else:
                    messagebox.showerror("Error" , "No Record Found :(" , parent = self.rootObject)

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} :)) " , parent = self.rootObject)



if __name__ == "__main__":
    root_Object = Tk()
    product_Module = Product_Module( root_Object )
    root_Object.resizable( False , False )
    root_Object.mainloop()  # mainloop() use to keep open output-window.