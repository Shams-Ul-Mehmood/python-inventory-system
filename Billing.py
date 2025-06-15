from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import time
import os
import tempfile

class Billing:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1550x900+0+0")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")
        self.cart_List = list()
        self.check_Print = 0

        # ---------> Inventory Management System Title <--------------
        self.title_icon = PhotoImage(file="./pictures/cart_logo_2.png")
        Billing_Title = Label( self.rootObject , text="Inventory Management System" , font=("times new roman", 40, "bold") , bg="#273746" ,fg="white" , anchor="w" , padx=20 , image=self.title_icon , compound=LEFT ).place(x=0 , y=0 , relwidth=1 , height=70 )

        # -----> Logout-Button <--------
        logout_button = Button( self.rootObject , text="Logout" , command=self.logout, font=("times new roman",15,"bold") , bg="white" , fg="black" , cursor="hand2" ).place(x=1350 , y=5 , height=60 , width=150 )

        # --------> clock <---------
        self.label_clock = Label( self.rootObject , text="Welcome To Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS" , font=("times new roman", 15) , bg="#616A6B" , fg="white" )
        self.label_clock.place(x=0 , y=70 , relwidth=1 , height=30 )

        # -------------> Product Frame <-------------
        self.product_Name_Search = StringVar()
        ProductFrame = Frame(self.rootObject, bd=4, relief=RIDGE, bg="white")
        ProductFrame.place(x=6, y=110, width=410, height=650)

        productTitle = Label(ProductFrame, text="All Products", font=("goudy old style", 20, "bold"), bg="#262626", fg="white").pack(side=TOP, fill=X)

        SearchAreaFrame = Frame(ProductFrame, bd=2, relief=RIDGE, bg="white")
        SearchAreaFrame.place(x=2, y=42, width=398, height=90)

        product_Search_Label = Label(SearchAreaFrame, text="Search Product | By Name", font=("times new roman", 15,"bold"), bg="white", fg="green").place(x=2, y=5)

        product_Name_Label = Label(SearchAreaFrame, text="Product Name", font=("times new roman", 15,"bold"), bg="white").place(x=2, y=45)
        product_Name_TextField = Entry(SearchAreaFrame, textvariable=self.product_Name_Search, font=("times new roman", 15), bg="lightyellow").place(x=135, y=47, width=150, height=22)

        product_Search_Button = Button(SearchAreaFrame, text="Search", command=self.search_Product, font=("goudy old style",15), fg="white", bg="#2196f3", cursor="hand2").place(x=290, y=45, width=100, height=25)

        show_All_Product_Button = Button(SearchAreaFrame, text="Show All", command=self.show_Database_Data, font=("goudy old style",15), fg="white", bg="#083531", cursor="hand2").place(x=290, y=10, width=100, height=25)

        Product_Area_Frame = Frame( ProductFrame , bd=3 , relief=RIDGE )
        Product_Area_Frame.place( x = 2 , y = 140 , width = 398 , height=475 )

        horizental_Scroll_Bar = Scrollbar( Product_Area_Frame , orient=HORIZONTAL )
        vertical_Scroll_Bar = Scrollbar( Product_Area_Frame , orient=VERTICAL )

        self.product_Table = ttk.Treeview( Product_Area_Frame , columns=( "product_id" , "product_name" , "product_price" , "product_quantity", "product_status" ) , xscrollcommand=horizental_Scroll_Bar.set , yscrollcommand=vertical_Scroll_Bar.set )
        horizental_Scroll_Bar.pack( side=BOTTOM , fill=X )
        vertical_Scroll_Bar.pack( side=RIGHT , fill=Y )
        horizental_Scroll_Bar.config( command=self.product_Table.xview )
        vertical_Scroll_Bar.config( command=self.product_Table.yview )

        self.product_Table.heading( "product_id" , text="PID" )
        self.product_Table.heading( "product_name" , text="Name" )
        self.product_Table.heading( "product_price" , text="Price" )
        self.product_Table.heading( "product_quantity" , text="QTY" )
        self.product_Table.heading( "product_status" , text="Status" )
        
        self.product_Table["show"] = "headings"

        self.product_Table.column( "product_id" , width=40 )
        self.product_Table.column( "product_name" , width=90 )
        self.product_Table.column( "product_price" , width=90 )
        self.product_Table.column( "product_quantity" , width=40 )
        self.product_Table.column( "product_status" , width=90 )
        
        self.product_Table.pack( fill=BOTH , expand=1 )
        self.product_Table.bind("<ButtonRelease-1>" , self.get_Product_Bill_Data_In_Form)

        product_Note_Label = Label(ProductFrame, text="Note: 'Enter 0 QTY to Remove the Product from Cart'", font=("goudy old style", 12), anchor="w", fg="red", bg="white").pack(side=BOTTOM, fill=X)

        # -------------> Customer Frame <-------------
        self.customerName = StringVar()
        self.customerContact = StringVar()
        CustomerFrame = Frame(self.rootObject, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=420, y=110, width=530, height=70)

        customerFrameTitle = Label(CustomerFrame, text="Customer Details", font=("goudy old style", 15), bg="lightgray").pack(side=TOP, fill=X)

        customer_Name_Label = Label(CustomerFrame, text="Name", font=("times new roman", 15), bg="white").place(x=5, y=35)
        customer_Name_TextField = Entry(CustomerFrame, textvariable=self.customerName, font=("times new roman", 13), bg="lightyellow").place(x=60, y=35, width=180)

        customer_Contact_Label = Label(CustomerFrame, text="Contact No.", font=("times new roman", 15), bg="white").place(x=250, y=35)
        customer_Contact_TextField = Entry(CustomerFrame, textvariable=self.customerContact, font=("times new roman", 13), bg="lightyellow").place(x=355, y=35, width=160)

        Calculator_Cart_Frame = Frame(self.rootObject, bd=2, relief=RIDGE, bg="white")
        Calculator_Cart_Frame.place(x=420, y=190, width=530, height=440)

        self.calculator_Input = StringVar()
        Calculator_Frame = Frame(Calculator_Cart_Frame, bd=9, relief=RIDGE, bg="white")
        Calculator_Frame.place(x=5, y=7, width=268, height=420)

        text_Calculator_InputField = Entry(Calculator_Frame, textvariable=self.calculator_Input, font=("arial",15,"bold"), width=21, bd=10, relief=GROOVE, state="readonly", justify=RIGHT)
        text_Calculator_InputField.grid(row=0, columnspan=4)

        button_7 = Button(Calculator_Frame, text='7', command=lambda:self.get_InputData(7), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=1, column=0)
        button_8 = Button(Calculator_Frame, text='8', command=lambda:self.get_InputData(8), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=1, column=1)
        button_9 = Button(Calculator_Frame, text='9', command=lambda:self.get_InputData(9), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=1, column=2)
        button_Plus = Button(Calculator_Frame, text="+", command=lambda:self.get_InputData("+"), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=1, column=3)
        
        button_4 = Button(Calculator_Frame, text='4', command=lambda:self.get_InputData(4), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=2, column=0)
        button_5 = Button(Calculator_Frame, text='5', command=lambda:self.get_InputData(5), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=2, column=1)
        button_6 = Button(Calculator_Frame, text='6', command=lambda:self.get_InputData(6), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=2, column=2)
        button_Minus = Button(Calculator_Frame, text="-", command=lambda:self.get_InputData("-"), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=2, column=3)
        
        button_1 = Button(Calculator_Frame, text='1', command=lambda:self.get_InputData(1), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=3, column=0)
        button_2 = Button(Calculator_Frame, text='2', command=lambda:self.get_InputData(2), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=3, column=1)
        button_3 = Button(Calculator_Frame, text='3', command=lambda:self.get_InputData(3), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=3, column=2)
        button_Product = Button(Calculator_Frame, text="*", command=lambda:self.get_InputData("*"), font=("arial",15,"bold"), width=4, bd=5, pady=22, cursor="hand2").grid(row=3, column=3)
        
        button_Clear = Button(Calculator_Frame, text='C', command=self.clear_Calculator, font=("arial",15,"bold"), width=4, bd=5, pady=21, cursor="hand2").grid(row=4, column=0)
        button_0 = Button(Calculator_Frame, text='0', command=lambda:self.get_InputData(0), font=("arial",15,"bold"), width=4, bd=5, pady=21, cursor="hand2").grid(row=4, column=1)
        button_Equal = Button(Calculator_Frame, text='=', command=self.equal_Operation, font=("arial",15,"bold"), width=4, bd=5, pady=21, cursor="hand2").grid(row=4, column=2)
        button_Divide = Button(Calculator_Frame, text="/", command=lambda:self.get_InputData("/"), font=("arial",15,"bold"), width=4, bd=5, pady=21, cursor="hand2").grid(row=4, column=3)
        

        Cart_Frame = Frame( Calculator_Cart_Frame , bd=3 , relief=RIDGE )
        Cart_Frame.place( x = 275 , y = 6 , width = 245 , height=420 )

        self.cartFrameTitle = Label(Cart_Frame, text="Cart \t Total Product: [0]", font=("goudy old style", 15), bg="lightgray")
        self.cartFrameTitle.pack(side=TOP, fill=X)

        horizental_Scroll_Bar = Scrollbar( Cart_Frame , orient=HORIZONTAL )
        vertical_Scroll_Bar = Scrollbar( Cart_Frame , orient=VERTICAL )

        self.cart_Table = ttk.Treeview( Cart_Frame , columns=( "product_id" , "product_name" , "product_price" , "product_quantity") , xscrollcommand=horizental_Scroll_Bar.set , yscrollcommand=vertical_Scroll_Bar.set )
        horizental_Scroll_Bar.pack( side=BOTTOM , fill=X )
        vertical_Scroll_Bar.pack( side=RIGHT , fill=Y )
        horizental_Scroll_Bar.config( command=self.cart_Table.xview )
        vertical_Scroll_Bar.config( command=self.cart_Table.yview )

        self.cart_Table.heading( "product_id" , text="PID" )
        self.cart_Table.heading( "product_name" , text="Name" )
        self.cart_Table.heading( "product_price" , text="Price" )
        self.cart_Table.heading( "product_quantity" , text="QTY" )
        # self.cart_Table.heading( "product_status" , text="Status" )
        
        self.cart_Table["show"] = "headings"

        self.cart_Table.column( "product_id" , width=30 )
        self.cart_Table.column( "product_name" , width=100 )
        self.cart_Table.column( "product_price" , width=90 )
        self.cart_Table.column( "product_quantity" , width=40 )
        # self.cart_Table.column( "product_status" , width=90 )
        
        self.cart_Table.pack( fill=BOTH , expand=1 )
        self.cart_Table.bind("<ButtonRelease-1>" , self.get_Cart_Data)
        
        self.productID = StringVar()
        self.productName = StringVar()
        self.productPrice = StringVar()
        self.productQuantity = StringVar()
        self.productStock = StringVar()
        Cart_Buttons_Frame = Frame(self.rootObject, bd=2, relief=RIDGE, bg="white")
        Cart_Buttons_Frame.place(x=420, y=635, width=530, height=125)

        productNameLabel = Label(Cart_Buttons_Frame, text="Product Name", font=("times new roman",15), bg="white").place(x=5, y=5)
        productNameTextField = Entry(Cart_Buttons_Frame, textvariable=self.productName, font=("times new roman",15), bg="lightyellow", state="readonly").place(x=5, y=35, width=190, height=22)

        productPriceLabel = Label(Cart_Buttons_Frame, text="Price Per Qty", font=("times new roman",15), bg="white").place(x=230, y=5)
        productPriceTextField = Entry(Cart_Buttons_Frame, textvariable=self.productPrice, font=("times new roman",15), bg="lightyellow", state="readonly").place(x=230, y=35, width=130, height=22)
        
        productQuantityLabel = Label(Cart_Buttons_Frame, text="Quantity", font=("times new roman",15), bg="white").place(x=390, y=5)
        productQuantityTextField = Entry(Cart_Buttons_Frame, textvariable=self.productQuantity, font=("times new roman",15), bg="lightyellow").place(x=390, y=35, width=130, height=22)
        
        self.productInStockLabel = Label(Cart_Buttons_Frame, text="In Stock", font=("times new roman",15), bg="white")
        self.productInStockLabel.place(x=5, y=70)

        cart_Clear_Button = Button( Cart_Buttons_Frame, text="Clear", command=self.clear_Cart, font=("times new roman",15), bg="lightgray", cursor="hand2").place(x=180, y=70, width=150, height=30)
        cart_Add_Button = Button( Cart_Buttons_Frame, text="Add | Update Cart", command=self.add_Update_Cart, font=("times new roman",15), bg="orange", cursor="hand2").place(x=340, y=70, width=180, height=30)
        
        Billing_Frame = Frame(self.rootObject, bg="white", bd=2, relief=RIDGE)
        Billing_Frame.place(x=953, y=110, width=570, height=440)

        billingTitle = Label(Billing_Frame, text="Customer Bill", font=("goudy old style", 20, "bold"), bg="#f44336", fg="white").pack(side=TOP, fill=X)
        scroll_Y = Scrollbar(Billing_Frame, orient=VERTICAL)
        scroll_Y.pack(side=RIGHT, fill=Y)
        self.bill_TextArea = Text(Billing_Frame, yscrollcommand=scroll_Y.set)
        self.bill_TextArea.pack(fill=BOTH, expand=1)
        scroll_Y.config(command=self.bill_TextArea.yview)

        Billing_Buttons_Menu_Frame = Frame(self.rootObject, bg="white", bd=2, relief=RIDGE)
        Billing_Buttons_Menu_Frame.place(x=953, y=555, width=570, height=205)

        self.amount_Label = Label(Billing_Buttons_Menu_Frame, text="Bill Amount\n[0]", font=("goudy old style",15,"bold"), fg="white", bg="#3f51b5")
        self.amount_Label.place(x=2, y=2, width=200, height=99)

        self.discount_Label = Label(Billing_Buttons_Menu_Frame, text="Discount\n[5%]", font=("goudy old style",15,"bold"), fg="white", bg="#8bc34a")
        self.discount_Label.place(x=204, y=2, width=200, height=99)

        self.netPay_Label = Label(Billing_Buttons_Menu_Frame, text="Net-Pay\n[0]", font=("goudy old style",15,"bold"), fg="white", bg="#607d8b")
        self.netPay_Label.place(x=405, y=2, width=160, height=99)

        bill_Print_Button = Button(Billing_Buttons_Menu_Frame, text="Print", command=self.print_Bill, cursor="hand2", font=("goudy old style",15,"bold"), fg="white", bg="lightgreen")
        bill_Print_Button.place(x=2, y=100, width=200, height=100)

        clear_All_Button = Button(Billing_Buttons_Menu_Frame, text="Clear All", command=self.clear_All, cursor="hand2", font=("goudy old style",15,"bold"), fg="white", bg="gray")
        clear_All_Button.place(x=204, y=100, width=200, height=100)

        generate_Bill_Button = Button(Billing_Buttons_Menu_Frame, text="Generate & Save Bill", command=self.generate_Bill, cursor="hand2", font=("goudy old style",13,"bold"), fg="white", bg="#009688")
        generate_Bill_Button.place(x=405, y=100, width=160, height=100)

        #=================== Footer ======================
        footer = Label(self.rootObject, text="IMS-Inventory Management System | Developed By Shams Afridi\nFor any Techincal Issue Contact: +923109726643", font=("times new roman",4), bg="#4d636d", fg="white").pack(fill=X, side=BOTTOM)

        self.show_Database_Data()
        self.dynamic_Date_And_Time()

    def get_InputData(self, number):
        value = self.calculator_Input.get()+str(number)
        self.calculator_Input.set(value)
    
    def clear_Calculator(self):
        self.calculator_Input.set("")

    def equal_Operation(self):
        output = self.calculator_Input.get()
        self.calculator_Input.set(eval(output))

    #------------------> Show Database Data <-------------------------
    def show_Database_Data(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            queryCursor.execute("select product_id , name , price , quantity , status from Product where status='Active'")
            tabular_Data = queryCursor.fetchall()
            self.product_Table.delete( * self.product_Table.get_children())
            for row in tabular_Data:
                self.product_Table.insert("",END,values=row)
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    def search_Product(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.product_Name_Search.get() == "":
                messagebox.showerror("Error" , "Search Input Should Be Required" , parent = self.rootObject)
            else:
                # queryCursor.execute("select * from Product where "+str( self.search_By.get() )+" LIKE '%"+ str( self.search_Text.get() )+"%'")
                queryCursor.execute("select product_id , name , price , quantity , status from Product where name LIKE '%"+self.product_Name_Search.get()+"%' and status='Active'")
                tabular_Data = queryCursor.fetchall()
                if len( tabular_Data ) != 0:
                    self.product_Table.delete( * self.product_Table.get_children())
                    for row in tabular_Data:
                        self.product_Table.insert("",END,values=row)
                else:
                    messagebox.showerror("Error" , "No Record Found :(" , parent = self.rootObject)

        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} :)) " , parent = self.rootObject)

    def get_Product_Bill_Data_In_Form(self , product_Bill_Data_In_Form):
        data_Format = self.product_Table.focus()
        content = ( self.product_Table.item( data_Format ) )
        row = content["values"]
        self.productID.set(row[0])
        self.productName.set(row[1])
        self.productPrice.set(row[2])
        self.productInStockLabel.config(text=f"In Stock [{str(row[3])}]")
        self.productStock.set(row[3])
        self.productQuantity.set("1")
    

    def get_Cart_Data(self , cart_Data):
        data_Format = self.cart_Table.focus()
        content = ( self.cart_Table.item( data_Format ) )
        row = content["values"]
        self.productID.set(row[0])
        self.productName.set(row[1])
        self.productPrice.set(row[2])
        self.productQuantity.set(row[3])
        self.productInStockLabel.config(text=f"In Stock [{str(row[4])}]")
        self.productStock.set(row[4])

    def add_Update_Cart(self):
        if self.productID.get() == "":
            messagebox.showerror("Error","Please select product from the list",parent=self.rootObject)
        elif self.productQuantity.get() == "":
            messagebox.showerror("Error","Quantity is Required",parent=self.rootObject)
        elif int(self.productQuantity.get()) > int(self.productStock.get()) or int(self.productQuantity.get()) < 0:
            messagebox.showerror("Error","Invalid Quantity",parent=self.rootObject)
        else:
            # calculate_Product_Price = float(int(self.productQuantity.get()) * float( self.productPrice.get() ))
            calculate_Product_Price = self.productPrice.get()
            cart_Items_List = [ self.productID.get(), self.productName.get(), calculate_Product_Price, self.productQuantity.get(), self.productStock.get() ]

            #================ Update-Cart List =================
            present = "no"
            index = 0
            for row in self.cart_List:
                if self.productID.get() == row[0]:
                    present = "yes"
                    break
                index += 1
            if present == "yes":
                option = messagebox.askyesno("Confirm","Product already exist.\nDo you want to Update | Remove Item from the Cart List", parent=self.rootObject)
                if option == True:
                    if self.productQuantity.get() == "0":
                        self.cart_List.pop(index)
                    else:
                        # self.cart_List[index][2] = calculate_Product_Price
                        self.cart_List[index][3] = self.productQuantity.get()
            else:
                self.cart_List.append(cart_Items_List)
            self.show_Cart()
            self.update_Bill()
    
    def update_Bill(self):
        self.bill_Amount = 0
        self.net_Pay_Amount = 0
        self.discount = 0
        for row in self.cart_List:
            self.bill_Amount = self.bill_Amount + (float(row[2]) * int(row[3]))
        self.discount = (self.bill_Amount * 5)/100
        self.net_Pay_Amount = self.bill_Amount - self.discount
        self.amount_Label.config(text=f"Bill Amount\n{str(self.bill_Amount)}")
        self.netPay_Label.config(text=f"Net Amount\n{str(self.net_Pay_Amount)}")
        self.cartFrameTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_List))}]")

    def show_Cart(self):
        try:
            self.cart_Table.delete( * self.cart_Table.get_children())
            for row in self.cart_List:
                self.cart_Table.insert("",END,values=row)
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    def generate_Bill(self):
        if self.customerName.get() == "" or self.customerContact.get() == "":
            messagebox.showerror("Error","Customer details are required",parent = self.rootObject)
        elif len( self.cart_List ) == 0:
            messagebox.showerror("Error","Please add product to the Cart",parent = self.rootObject)
        else:
            #---------------> Top Customer Bill Area <---------------------
            self.top_Customer_Bill_Area()
            #---------------> Middle Customer Bill Area <---------------------
            self.middle_Customer_Bill_Area()
            #---------------> Bottom Customer Bill Area <---------------------
            self.bottom_Customer_Bill_Area()

            saveOpenFile = open(f"bill/{str(self.invoice)}.txt","w")
            saveOpenFile.write(self.bill_TextArea.get("1.0",END))
            saveOpenFile.close()
            messagebox.showinfo("Saved","Bill has been save in application",parent=self.rootObject)
            self.check_Print = 1
    
    def top_Customer_Bill_Area(self):
        self.invoice = int( time.strftime("%H%M%S") ) + int( time.strftime("%d%m%Y") )
        bill_Top_Area_Template = f"""
\t\tSultan Mahmood-Inventory
\t Phone No. +923*******3 , Kuala Lumpur-40215
{str("="*67)}
 Customer Name: {self.customerName.get()}
 Phone No: {self.customerContact.get()}
 Bill No: {str(self.invoice)}\t\t\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*67)}
 Product Name\t\t\t\t\tQTY\tPrice
{str("="*67)}
        """
        self.bill_TextArea.delete("1.0",END)
        self.bill_TextArea.insert("1.0",bill_Top_Area_Template)
    
    def middle_Customer_Bill_Area(self):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
        queryCursor = database_Connection.cursor()
        try:
            for row in self.cart_List:
                productID = row[0]
                productName = row[1]
                productQuantity = int(row[4]) - int( row[3] )
                if int(row[3]) == int(row[4]):
                    productStatus = "Inactive"
                
                if int(row[3]) != int(row[4]):
                    productStatus = "Active"
                productPrice = str(float(row[2]*int(row[3])))
                self.bill_TextArea.insert(END,"\n "+productName+"\t\t\t\t\t"+row[3]+"\tRs. "+productPrice)

                #-----------------> Update product-quantity in product-table <-------------------------
                queryCursor.execute("update Product set quantity = ? , status = ? where product_id = ? " , (productQuantity, productStatus, productID ))
                database_Connection.commit()
            database_Connection.close()
            self.show_Database_Data()
        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)

    def bottom_Customer_Bill_Area(self):
        bill_Bottom_Area_Template = f'''
{str("="*67)}
 Bill Amount:\t\t\t\t\tRs.{self.bill_Amount}
 Discount:\t\t\t\t\tRs.{self.discount}
 Total Amount:\t\t\t\t\tRs.{self.net_Pay_Amount}
{str("="*67)}\n
        '''
        self.bill_TextArea.insert(END,bill_Bottom_Area_Template)

    def clear_Cart(self):
        self.productID.set("")
        self.productName.set("")
        self.productPrice.set("")
        self.productQuantity.set("")
        self.productInStockLabel.config(text=f"In Stock")
        self.productStock.set("")

    def clear_All(self):
        self.check_Print = 0
        self.bill_TextArea.delete("1.0",END)
        self.clear_Cart()
        self.customerName.set("")
        self.customerContact.set("")
        self.product_Name_Search.set("")
        del self.cart_List[:]
        self.show_Cart()
        self.show_Database_Data()
        self.cartFrameTitle.config(text=f"Cart \t Total Product: [0]")

    def dynamic_Date_And_Time(self):
        dynamic_Time = time.strftime("%I:%M:%S")
        dynamic_Date = time.strftime("%d-%m-%Y")
        self.label_clock.config(text=f"Welcome To Inventory Management System\t\t Date: {str(dynamic_Date)}\t\t Time: {str(dynamic_Time)}")
        self.label_clock.after(200,self.dynamic_Date_And_Time)

    def print_Bill(self):
        if self.check_Print == 1:
            messagebox.showinfo("Print","Please wait while printing",parent = self.rootObject)
            new_Print_File = tempfile.mktemp(".txt")
            open(new_Print_File,"w").write(self.bill_TextArea.get("1.0",END))
            os.startfile(new_Print_File,"print")
        else:
            messagebox.showerror("Print","Please generate bill to print the receipt",parent = self.rootObject)

    def logout(self):
        self.rootObject.destroy()
        os.system("python Login.py")
    


if __name__ == "__main__":
    root_Object = Tk()
    Billing = Billing( root_Object )
    root_Object.mainloop()  # mainloop() use to keep open output-window.