from tkinter import *
from back_end.dbconnection import *

class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Billing')

        self.geometry('1000x500+500+300')

        self.bill_var= StringVar()
        self.product_name_var=StringVar()
        self.qty_var =StringVar()
        self.rate_var = StringVar()
        self.amount_var =StringVar()



        self.dbonnect = Curd()

        self.entry_frame = Frame(self,bd=4, relief=GROOVE, width=500, height=500)
        self.entry_frame.place(x=0,y=0)

        Label(self.entry_frame, text = 'Bill no', font=('arial', 15,)).grid(row=0, column=0, padx=10, pady=(20, 10))
        Label(self.entry_frame, text='Product name', font=('arial', 15,)).grid(row=1, column=0, padx=10, pady=(20, 10))
        Label(self.entry_frame, text='Quantity', font=('arial', 15,)).grid(row=2, column=0, padx=10, pady=(20, 10))
        Label(self.entry_frame, text='Rate', font=('arial', 15,)).grid(row=3, column=0, padx=10, pady=(20, 10))
        Label(self.entry_frame, text='Amount', font=('arial', 15,)).grid(row=4, column=0, padx=10, pady=(20, 10))

        self.Bill=Entry(self.entry_frame,textvariable=self.bill_var, font=('arial', 15,))
        self.Bill.grid(row=0, column=1, padx=10, pady=(20, 10))
        self.product_name=Entry(self.entry_frame,textvariable=self.product_name_var, font=('arial', 15,))
        self.product_name.grid(row=1, column=1,padx=10, pady=(20, 10))

        self.quantity=Entry(self.entry_frame,textvariable=self.qty_var , font=('arial', 15,))
        self.quantity.grid(row=2, column=1, padx=10, pady=(20, 10))
        self.rate=Entry(self.entry_frame,textvariable=self.rate_var , font=('arial', 15,))
        self.rate.grid(row=3, column=1, padx=10, pady=(20, 10))

        # self.amount=Entry(self.entry_frame,textvariable=self.qty_var, font=('arial', 15,))
        # self.amount.grid(row=4, column=1, padx=10, pady=(20, 10))
        # self.amount.bind('<Enter>', self.amount_ev)
        # self.amount.bind('<Tab>', amount_ev)

        #-----------------------button---------------------
        Button(self.entry_frame,text='Add', font=('arial', 15,), command=self.set_bill).grid(row=5,column=0, padx=10, pady=(20, 10))
        Button(self.entry_frame, text='Reset').grid(row=5, column=1, padx=10, pady=(20, 10))
        Button(self.entry_frame, text='Save', font=('arial', 15,), command=self.save_bill).grid(row=6, column=0, padx=10, pady=(20, 10))

        self.bill_frame =Frame(self,bd=4, relief=GROOVE,bg='white', width=460, height=460)
        self.bill_frame.place(x=520,y=20, width=460, height =460)

        #bill headings
        Label(self.bill_frame, text='Bill no',bg='white', font=('arial', 15,)).grid(row=0, column=0, padx=10, pady=(20, 10))
        Label(self.bill_frame, text='Product name',bg='white', font=('arial', 15,)).grid(row=0, column=1, padx=10, pady=(20, 10))
        Label(self.bill_frame, text='Quantity',bg='white', font=('arial', 15,)).grid(row=0, column=2, padx=10, pady=(20, 10))
        Label(self.bill_frame, text='Rate',bg='white', font=('arial', 15,)).grid(row=0, column=0, padx=3, pady=(20, 10))
        Label(self.bill_frame, text='Amount',bg='white', font=('arial', 15,)).grid(row=0, column=4, padx=10, pady=(20, 10))
        self.data = []
        self.list1=[]

    def set_list(self):
        a = self.rate.get()
        b = self.quantity.get()
        c = int(a) * int(b)
        a = [self.Bill.get(), self.product_name.get(),self.quantity.get(),self.rate.get(), c]
        self.data.append(a)

    def set_bill(self):
        self.set_list()
        for i in range(len(self.data)):
            Label(self.bill_frame, text=self.data[i][0], bg='white', font=('arial', 15,)).grid(row=1+i, column=0, padx=10,
                                                                                         pady=(20, 10)) #for bill no
            Label(self.bill_frame, text=self.data[i][1], bg='white', font=('arial', 15,)).grid(row=1+i, column=1, padx=10,
                                                                                              pady=(20, 10)) #for product name
            Label(self.bill_frame, text=self.data[i][2], bg='white', font=('arial', 15,)).grid(row=1+i, column=2, padx=10,
                                                                                          pady=(20, 10))
            Label(self.bill_frame, text=self.data[i][3], bg='white', font=('arial', 15,)).grid(row=1+i, column=0, padx=3,
                                                                                      pady=(20, 10))
            Label(self.bill_frame, text=self.data[i][4], bg='white', font=('arial', 15,)).grid(row=1+i, column=4, padx=10,
                                                                                        pady=(20, 10))

    def save_bill(self):
        query = 'insert into tbl_sales_bill (bill_no,product_name,qty,rate,amount) value(%s,%s,%s,%s,%s)'

        for i in range(len(self.data)):
            values = (self.data[i][0], self.data[i][1], self.data[i][2], self.data[i][3], self.data[i][4])
            self.dbonnect.add_data(query,values)


if __name__ == '__main__':
    a=Main()
    a.mainloop()