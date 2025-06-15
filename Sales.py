from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk , messagebox
import sqlite3
import os

class Sales_Module:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1100x550+220+130")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")
        self.rootObject.focus_force()

        self.bill_List = list()
        self.invoiceTextField = StringVar()

        ################### Title #####################
        title_Label = Label( self.rootObject , text="View Customer Bills" , font=("goudy old style" , 30) , bg="#343123" , fg="white" , bd=2 , relief=RIDGE ).pack(side=TOP , fill=X , padx=12 , pady=4)

        invoice_Label = Label( self.rootObject , text="Invoice No." , font=("times new roman",15) , bg="white" ).place(x=50,y=80)

        invoice_TextField = Entry( self.rootObject , text = self.invoiceTextField , font=("times new roman",15) , bg="lightyellow" ).place(x=160,y=80,width=180,height=28)

        searchButton = Button( self.rootObject , text="Search" , command=self.search, font=("times new roman",15,"bold"), bg="#2196f3" , fg="white" , cursor="hand2" ).place(x=360,y=80,width=120,height=28)

        clearButton = Button( self.rootObject , text="Clear" , command=self.clear, font=("times new roman",15,"bold"), bg="lightgray" , fg="black" , cursor="hand2" ).place(x=490,y=80,width=120,height=28)

        ################### Bill List #####################
        sales_Frame = Frame( self.rootObject , bd=3 , relief=RIDGE )
        sales_Frame.place( x = 50 , y = 140 , width = 200 , height = 390 )

        bill_List_Scroll_Y = Scrollbar(sales_Frame , orient=VERTICAL)
        self.sales_List = Listbox( sales_Frame , font=("goudy old style" , 15) , bg="white" , yscrollcommand=bill_List_Scroll_Y.set )
        bill_List_Scroll_Y.pack(side=RIGHT , fill=Y)
        bill_List_Scroll_Y.config(command=self.sales_List.yview)
        self.sales_List.pack(fill=BOTH , expand=1)
        self.sales_List.bind("<ButtonRelease-1>", self.get_Data)

        ################### Bill Area #####################
        bill_Frame = Frame( self.rootObject , bd=3 , relief=RIDGE )
        bill_Frame.place( x = 260 , y = 140 , width = 410 , height = 390 )

        customer_Bill_Area_Title = Label( bill_Frame , text="Customer Bill Area" , font=("goudy old style" , 20) , bg="orange" ).pack(side=TOP , fill=X)

        bill_Area_Scroll_Y = Scrollbar(bill_Frame , orient=VERTICAL)
        self.bill_Area = Text( bill_Frame , font=("goudy old style" ,7) , bg="lightyellow" , yscrollcommand=bill_Area_Scroll_Y.set )
        bill_Area_Scroll_Y.pack(side=RIGHT , fill=Y)
        bill_Area_Scroll_Y.config(command=self.bill_Area.yview)
        self.bill_Area.pack(fill=BOTH , expand=1)

        ################### Image #####################
        self.bill_Image = Image.open("./pictures/category_13.jpg")
        self.bill_Image = self.bill_Image.resize((440,300) ,Image.BICUBIC)
        self.bill_Image = ImageTk.PhotoImage( self.bill_Image )

        bill_Image_Label = Label(self.rootObject , image=self.bill_Image , bd=0)
        bill_Image_Label.place(x=680, y=170)

        self.show()

    def show(self):
        del self.bill_List[:]
        self.sales_List.delete(0,END)
        # print(os.listdir('bill'))
        for i in os.listdir('bill'):
            if i.split('.')[-1] == "txt":
                self.sales_List.insert(END,i)
                self.bill_List.append(i.split(".")[0])

    def get_Data(self, event):
        index_ = self.sales_List.curselection()
        file_name = self.sales_List.get(index_)
        # print(file_name)
        self.bill_Area.delete('1.0',END)
        openFile = open(f"bill/{file_name}" , "r")
        for i in openFile:
            self.bill_Area.insert(END,i)
        openFile.close()
    
    def search(self):
        if self.invoiceTextField.get() == "":
            messagebox.showerror("Error","Invoice no. should be required",parent = self.rootObject)
        else:
            if self.invoiceTextField.get() in self.bill_List:
                openFile = open(f"bill/{self.invoiceTextField.get()}.txt" , "r")
                self.bill_Area.delete("1.0",END)
                for i in openFile:
                    self.bill_Area.insert(END,i)
                openFile.close()
            else:
                messagebox.showerror("Error","Invalid Invoice Number", parent = self.rootObject)

    def clear(self):
        self.show()
        self.bill_Area.delete("1.0",END)

if __name__ == "__main__":
    root_Object = Tk()
    product_Module = Sales_Module( root_Object )
    root_Object.resizable( False , False )
    root_Object.mainloop()  # mainloop() use to keep open output-window.