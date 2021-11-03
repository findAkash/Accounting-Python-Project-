from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from back_end.dbconnection import *
from model.connector import *



class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        # title & screen
        self.title('ACCOUNT')
        self.configure(background='#dce9fa')
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry('%dx%d+0+0' % (width, height))
        self.frame_main = Frame(self, width=width, height=height, bg='#dce9fa')
        self.frame_main.pack()

        # background
        # self.background = ImageTk.PhotoImage(file='bg4.jpg')

        # resizing the background image
        back_image = Image.open('bg5.jpg')
        resized_image = back_image.resize((960, 590))
        resized_image.save('resized_960x590.ppm', 'ppm')

        self.background = ImageTk.PhotoImage(file='resized_960x590.ppm')
        use_background = Label(self.frame_main, image=self.background, bd=0).place(x=0, y=230)

        self.logo = ImageTk.PhotoImage(file='alphalogor.jpg')
        use_logo = Label(self.frame_main, image=self.logo, bd=0).place(x=595, y=4)
        welcome = Label(self.frame_main, text='ACCOUNTING PACKAGE', fg='#0170c1', bd=10, relief=GROOVE,
                        font=('Broadway', 40, 'bold'), bg='#dce9fa').place(x=730, y=28)

        # Frame for add company
        self.frame_company = Frame(self.frame_main, width=880, height=780, bg='#479be4', bd=10, relief=GROOVE)
        self.frame_company.place(x=1000, y=150)
        # heading
        registration_title = Label(self.frame_company, text='REGISTRATION', bd=10, relief=GROOVE,
                                   font=('arial', 30, 'bold'), bg='#479be4', fg='white')
        registration_title.grid(columnspan=3, pady=40)

        # input company details========================================================================================================
        # ------------------------------------------registration no.
        lbl_registration = Label(self.frame_company, text='Registration No.', font=('arial', 20, 'bold'), bg='#479be4',
                                 fg='black').grid(
            row=1, column=0, pady=10, padx=(20, 10), sticky=W)
        self.address_entry = Entry(self.frame_company, font=('arial', 20), width=13, fg='black')
        self.address_entry.grid(row=1, column=1, columnspan=2, pady=15, padx=10, sticky=W)

        # ------------------------------------------Name

        # -----------------------function for click event to remove the default value on clicking-------------------
        def click_event_first_name(event):
            self.firstName_entry.delete(0, END)

        def click_event_last_name(event):
            self.lastName_entry.delete(0, END)

        lbl_name = Label(self.frame_company, text='Name', font=('arial', 20, 'bold'), bg='#479be4', fg='black').grid(
            row=2, column=0, pady=10, padx=20, sticky=W)
        self.firstName_entry = Entry(self.frame_company, width=13, font=('arial', 20), fg='light grey')
        self.firstName_entry.insert(0, 'First Name')
        self.firstName_entry.grid(row=2, column=1, pady=15, padx=10, sticky=W)
        self.firstName_entry.bind('<Button-1>', click_event_first_name)

        self.lastName_entry = Entry(self.frame_company, width=13, font=('arial', 20), fg='light grey')
        self.lastName_entry.insert(0, 'Last Name')
        self.lastName_entry.bind('<Button-1>', click_event_last_name)
        self.lastName_entry.grid(row=2, column=2, pady=15, padx=10, sticky=W)
        # -------------------------------------------company name
        lbl_comapanyName = Label(self.frame_company, text='Company Name', font=('arial', 20, 'bold'), bg='#479be4',
                                 fg='black').grid(
            row=3, column=0, pady=15, padx=(20, 10), sticky=W)
        self.companyName_entry = Entry(self.frame_company, font=('arial', 20), width=30, fg='black')
        self.companyName_entry.grid(row=3, column=1, columnspan=2, pady=15, padx=10, sticky=W)
        # -------------------------------------------email
        lbl_email = Label(self.frame_company, text='Email', font=('arial', 20, 'bold'), bg='#479be4',
                          fg='black').grid(
            row=4, column=0, pady=15, padx=(20, 10), sticky=W)
        self.email_entry = Entry(self.frame_company, font=('arial', 20), width=30, fg='black')
        self.email_entry.grid(row=4, column=1, columnspan=2, pady=15, padx=10, sticky=W)
        # ------------------------------------------contact
        lbl_contact = Label(self.frame_company, text='Contact No.', font=('arial', 20, 'bold'), bg='#479be4',
                            fg='black').grid(
            row=5, column=0, pady=15, padx=(20, 10), sticky=W)
        self.contact_entry = Entry(self.frame_company, font=('arial', 20), width=30, fg='black')
        self.contact_entry.grid(row=5, column=1, columnspan=2, pady=15, padx=10, sticky=W)
        # -----------------------------------------address
        lbl_address = Label(self.frame_company, text='Address', font=('arial', 20, 'bold'), bg='#479be4',
                            fg='black').grid(
            row=6, column=0, pady=15, padx=(20, 10), sticky=W)
        self.address_entry = Entry(self.frame_company, font=('arial', 20), width=30, fg='black')
        self.address_entry.grid(row=6, column=1, columnspan=2, pady=15, padx=10, sticky=W)

        # -----------------------------------------pan & vat
        # ----------------------------------function for click event to remove the default entry data -------------------
        def click_event_pan(event):
            self.pan_entry.delete(0, END)

        def click_event_vat(event):
            self.vat_entry.delete(0, END)

        lbl_pan = Label(self.frame_company, text='PAN & VAT', font=('arial', 20, 'bold'), bg='#479be4',
                        fg='black').grid(
            row=7, column=0, pady=15, padx=(20, 10), sticky=W)
        self.pan_entry = Entry(self.frame_company, font=('arial', 20), width=10, fg='light grey')
        self.pan_entry.insert(0, 'PAN')
        self.pan_entry.grid(row=7, column=1, pady=15, padx=10, sticky=W)
        self.pan_entry.bind('<Button-1>', click_event_pan)

        self.vat_entry = Entry(self.frame_company, font=('arial', 20), width=10, fg='light grey')
        self.vat_entry.insert(0, ' VAT no.')
        self.vat_entry.grid(row=7, column=2, pady=15, padx=10, sticky=W)
        self.vat_entry.bind('<Button-1>', click_event_vat)

        # -----------------------------------------fiscal year
        # ----------------------------------------click_event for eg:2074/75---------------------
        def click_event_fiscalyr(event):
            self.fiscal_entry.delete(0, END)

        lbl_Fiscal_Year = Label(self.frame_company, text='Fiscal Year', font=('arial', 20, 'bold'), bg='#479be4',
                                fg='black').grid(
            row=8, column=0, pady=15, padx=(20, 10), sticky=W)
        self.fiscal_entry = Entry(self.frame_company, font=('arial', 20), fg='light grey', width=10)
        self.fiscal_entry.insert(0, 'eg: 2074/75')
        self.fiscal_entry.grid(row=8, column=1, pady=15, padx=10, sticky=W)
        self.fiscal_entry.bind('<Button>', click_event_fiscalyr)
        # ---------------------------------------button
        self.btn_register = Button(self.frame_company, text='Register', cursor='hand2', bg='blue',
                                   font=('arial', 15, 'bold'),
                                   command=self.create_account, fg='white')
        self.btn_register.grid(row=9, columnspan=3, pady=20)

    # ------------------------------------------------END-------------------------------------------------------------------

    # ==========================================to set username and password================================================
    def create_account(self):
        # Frame for create account
        self.frame_company.destroy()
        self.frame_setUser = Frame(self.frame_main, width=880, height=780, bg='#479be4', bd=10, relief=GROOVE)
        self.frame_setUser.place(x=1100, y=220)
        # heading
        account_title = Label(self.frame_setUser, text='Create Account', bd=10, relief=GROOVE,
                              font=('arial', 30, 'bold'), bg='#479be4', fg='white')
        account_title.grid(row=0, columnspan=2, pady=40)

        # set login account ===========================================================================================
        # ------------------------------------------user type
        lbl_userType = Label(self.frame_setUser, text='User Type', font=('Helvetica', 25, 'bold'), bg='#479be4',
                             fg='white').grid(
            row=1, column=0, pady=10, padx=(20, 0), sticky=W)

        # ----------------------optionMenu for user type-------------------------------------
        self.userType = StringVar()
        self.userType.set('Admin')
        self.option_userType = OptionMenu(self.frame_setUser, self.userType, 'Admin', 'User')
        self.option_userType.grid(row=1, column=1, pady=15, padx=(0, 20), sticky=W)
        self.option_userType.config(font=('arial', 20), width=10)

        # ----------------------username and password-----------------------------------------
        # Username
        def click_event_username(event):  # function for click event to remove the default value on clicking
            self.username_entry.delete(0, END)
            self.username_entry.config(fg='Black')

        self.username_entry = Entry(self.frame_setUser, width=30, font=('arial', 20), fg='light grey')
        self.username_entry.insert(0, 'Username')
        self.username_entry.grid(row=2, columnspan=2, pady=15, padx=10, ipady=12, sticky=W)
        self.username_entry.bind('<Button-1>', click_event_username)

        # Password
        def click_event_password(event):  # function for click event to remove the default value on clicking
            self.password_entry.delete(0, END)
            self.password_entry.config(fg='black')

        self.password_entry = Entry(self.frame_setUser, width=30, font=('arial', 20), fg='light grey')
        self.password_entry.insert(0, 'Password')
        self.password_entry.grid(row=3, columnspan=2, pady=15, padx=10, ipady=13, sticky=W)
        self.password_entry.bind('<Button-1>', click_event_password)
        self.password_entry.bind('<Tab>', click_event_password)

        # Confirm  Password
        def click_event_confirm_password(event):  # function for click event to remove the default value on clicking
            self.confirmPassword_entry.delete(0, END)
            self.confirmPassword_entry.config(fg='black')

        self.confirmPassword_entry = Entry(self.frame_setUser, width=30, font=('arial', 20), fg='light grey')
        self.confirmPassword_entry.insert(0, 'Confirm Password')
        self.confirmPassword_entry.grid(row=4, columnspan=2, pady=15, padx=10, ipady=13, sticky=W)
        self.confirmPassword_entry.bind('<Button-1>', click_event_confirm_password)

        # button

        btn_set_login = Button(self.frame_setUser, text='Create', width=23, height=1, font=('arial', 20, 'bold'),
                               command=self.login, bg='royal blue', fg='white')
        btn_set_login.grid(row=5, columnspan=2, pady=20)

    # -----------------------------------------------------END-------------------------------------------------------------

    # Frame for login
    def login(self):
        self.frame_setUser.destroy()
        self.frame_login = Frame(self.frame_main, width=880, height=780, bg='#479be4', bd=10, relief=GROOVE)
        self.frame_login.place(x=1100, y=220)
        # heading
        login_title = Label(self.frame_login, text='LogIn', bd=10, relief=GROOVE,
                            font=('arial', 30, 'bold'), bg='#479be4', fg='white')
        login_title.grid(row=0, columnspan=2, pady=40)

        # set login account ===========================================================================================
        # ------------------------------------------user type
        lbl_userType = Label(self.frame_login, text='User Type', font=('Helvetica', 25, 'bold'), bg='#479be4',
                             fg='Black').grid(
            row=1, column=0, pady=10, padx=(20, 0), sticky=W)

        # ----------------------optionMenu for user type-------------------------------------
        self.userType = StringVar()
        self.userType.set('Admin')
        self.option_userType = OptionMenu(self.frame_login, self.userType, 'Admin', 'User')
        self.option_userType.grid(row=1, column=1, pady=15, padx=(5, 20), sticky=W)
        self.option_userType.config(font=('arial', 20), width=10)

        # ----------------------username and password-----------------------------------------
        # ------------set user and password icon--------------------------------------
        self.user_icon = ImageTk.PhotoImage(file='images/user.png')
        lbl_user_icon = Label(self.frame_login, image=self.user_icon, bg='#479be4').grid(row=2)

        self.password_icon = ImageTk.PhotoImage(file='images/password.png')
        lbl_password_icon = Label(self.frame_login, image=self.password_icon, bg='#479be4').grid(row=3)

        # Username
        def click_event_username(event):  # function for click event to remove the default value on clicking
            self.username_entry.delete(0, END)
            self.username_entry.config(fg='Black')

        self.username_entry = Entry(self.frame_login, width=30, font=('arial', 20), fg='light grey')
        self.username_entry.insert(0, 'Username')
        self.username_entry.grid(row=2, column=1, columnspan=2, pady=15, padx=(0, 10), ipady=12, sticky=W)
        self.username_entry.bind('<Button-1>', click_event_username)

        # Password
        def click_event_password(event):  # function for click event to remove the default value on clicking
            self.password_entry.delete(0, END)
            self.password_entry.config(fg='black')

        self.password_entry = Entry(self.frame_login, width=30, font=('arial', 20), fg='light grey')
        self.password_entry.insert(0, 'Password')
        self.password_entry.grid(row=3, column=1, columnspan=2, pady=15, padx=(0, 10), ipady=13, sticky=W)
        self.password_entry.bind('<Button-1>', click_event_password)
        self.password_entry.bind('<Tab>', click_event_password)

        # button
        btn_set_login = Button(self.frame_login, text='LogIn', width=23, height=1, command=self.dashboard,
                               font=('arial', 20, 'bold'), bg='royal blue', fg='white')
        btn_set_login.grid(row=4, column=1, pady=20)

        # ----------------------------------------------------END----------------------------------------------------------------
        self._frame = None

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place()
        # DASHBOARD

    def dashboard(self):
        self.frame_main.destroy()
        self.switch_frame(Dashboard)

class Functions:

    @classmethod
    def search_method_function(cls, data,index, b):
        rows = []
        for i in range(len(data)):
            if str(data[i][index]) == b:
                rows.append(data[i])
                return rows
        return rows


    @classmethod
    def sort_method(cls, data, index):
        swap = True
        while swap:
            swap = False
            for i in range(len(data) - 1):
                if (data[i][index]) > (data[i + 1][index]):
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swap = True
        return data


class Dashboard(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.configure(background='')
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.window.configure(width=width,height=height)
        my_canvas = Canvas(self.window, width=width, height=height)
        my_canvas.place(x=0, y=0)
        # my_canvas.create_line(0, 110, width, 100, fill='grey')
        my_canvas.create_line(0, 50, width, 50, fill='grey')

        #----------------------frame for dashboard--------------------------------
        self.frame_dashboard = Frame(self.window,height=height,width=width, bg='#dce9fa')
        self.frame_dashboard.place(x=0,y=0)

        self.frame_menubar = Frame(self.window, bg='white', width=width, height=48)
        self.frame_menubar.place(x=0, y=1)

        #-------------------------------logo------------------------------------------
        self.logo = ImageTk.PhotoImage(file='alphalogor.jpg')
        use_logo = Label(self.window, image=self.logo, bd=0).place(x=(width/2-50), y= (height/2-80))
        # welcome = Label(self.window, text='ACCOUNTING PACKAGE', fg='#0170c1', bd=10, relief=GROOVE,
        #                 font=('Broadway', 40, 'bold'), bg='#dce9fa').place(x=730, y=28)

        # ----------------------------menu hover effect -------------------------------

        #------for group---------------
        def enter_hover(event):
            menu_group.config(fg='white',font=('arial',15))
            menu_group['bg'] = '#479be4'

        def leave_hover(event):
            menu_group['bg'] = 'white'
            menu_group.config(font=('arial', 15), fg='black')
        menu_group = Button(self.window, text='Group',command=self.group, bg='white',width=10, font=('arial', 15), relief='flat')
        menu_group.grid(padx=0, pady=5)
        menu_group.bind('<Leave>', leave_hover)
        menu_group.bind('<Enter>', enter_hover)


        #-------for add product-----------
        def enter_hover(event):
            menu_addproduct.config(fg='white',font=('arial',15))
            menu_addproduct['bg'] = '#479be4'

        def leave_hover(event):
            menu_addproduct['bg'] = 'white'
            menu_addproduct.config(font=('arial', 15), fg='black')
        menu_addproduct = Button(self.window, text='Add Product',command=self.add_product,width=10, bg='white', font=('arial', 15), relief='flat')
        menu_addproduct.grid(column=1,row=0,padx=0, pady=5)
        menu_addproduct.bind('<Leave>', leave_hover)
        menu_addproduct.bind('<Enter>', enter_hover)

        def enter_hover(event):
            menu_addledger.config(fg='white',font=('arial',15))
            menu_addledger['bg'] = '#479be4'
        def leave_hover(event):
            menu_addledger['bg'] = 'white'
            menu_addledger.config(font=('arial', 15), fg='black')
        menu_addledger = Button(self.window, text='Ledger',command=self.add_product,width=10, bg='white', font=('arial', 15), relief='flat')
        menu_addledger.grid(column=2,row=0,padx=0, pady=5)
        menu_addledger.bind('<Leave>', leave_hover)
        menu_addledger.bind('<Enter>', enter_hover)

        def enter_hover(event):
            menu_sales.config(fg='white',font=('arial',15))
            menu_sales['bg'] = '#479be4'
        def leave_hover(event):
            menu_sales['bg'] = 'white'
            menu_sales.config(font=('arial', 15), fg='black')
        menu_sales = Button(self.window, text='Sales',command=lambda :self.window.switch_frame(Sales),width=10, bg='white', font=('arial', 15), relief='flat')
        menu_sales.grid(column=3,row=0,padx=0, pady=5)
        menu_sales.bind('<Leave>', leave_hover)
        menu_sales.bind('<Enter>', enter_hover)

        def enter_hover(event):
            menu_purchases.config(fg='white',font=('arial',15))
            menu_purchases['bg'] = '#479be4'
        def leave_hover(event):
            menu_purchases['bg'] = 'white'
            menu_purchases.config(font=('arial', 15), fg='black')
        menu_purchases = Button(self.window, text='Purchase',command=lambda :self.window.switch_frame(Purchase),width=10, bg='white', font=('arial', 15), relief='flat')
        menu_purchases.grid(column=4,row=0,padx=0, pady=5)
        menu_purchases.bind('<Leave>', leave_hover)
        menu_purchases.bind('<Enter>', enter_hover)

        def enter_hover(event):
            menu_payment.config(fg='white',font=('arial',15))
            menu_payment['bg'] = '#479be4'
        def leave_hover(event):
            menu_payment['bg'] = 'white'
            menu_payment.config(font=('arial', 15), fg='black')
        menu_payment = Button(self.window, text='Payment',command=self.add_product,width=10, bg='white', font=('arial', 15), relief='flat')
        menu_payment.grid(column=5,row=0,padx=0, pady=5)
        menu_payment.bind('<Leave>', leave_hover)
        menu_payment.bind('<Enter>', enter_hover)

        def enter_hover(event):
            menu_receipt .config(fg='white',font=('arial',15))
            menu_receipt['bg'] = '#479be4'
        def leave_hover(event):
            menu_receipt['bg'] = 'white'
            menu_receipt.config(font=('arial', 15), fg='black')
        menu_receipt = Button(self.window, text='Receipt',command=self.add_product,width=10, bg='white', font=('arial', 15), relief='flat')
        menu_receipt.grid(column=6,row=0,padx=0, pady=5)
        menu_receipt .bind('<Leave>', leave_hover)
        menu_receipt.bind('<Enter>', enter_hover)

        def enter_hover(event):
            menu_daybook.config(fg='white',font=('arial',15))
            menu_daybook['bg'] = '#479be4'
        def leave_hover(event):
            menu_daybook['bg'] = 'white'
            menu_daybook.config(font=('arial', 15), fg='black')
        menu_daybook = Button(self.window, text='Daybook',command=self.add_product,width=10, bg='white', font=('arial', 15), relief='flat')
        menu_daybook.grid(column=7,row=0,padx=0, pady=5)
        menu_daybook.bind('<Leave>', leave_hover)
        menu_daybook.bind('<Enter>', enter_hover)

        def enter_hover(event):
            menu_stock.config(fg='white',font=('arial',15))
            menu_stock['bg'] = '#479be4'
        def leave_hover(event):
            menu_stock['bg'] = 'white'
            menu_stock.config(font=('arial', 15), fg='black')
        menu_stock = Button(self.window, text='Stock',command=self.add_product,width=10, bg='white', font=('arial', 15), relief='flat')
        menu_stock.grid(column=8,row=0,padx=0, pady=5)
        menu_stock.bind('<Leave>', leave_hover)
        menu_stock.bind('<Enter>', enter_hover)

        def enter_hover(event):
            menu_logout.config(fg='white',font=('arial',15))
            menu_logout['bg'] = '#479be4'
        def leave_hover(event):
            menu_logout['bg'] = 'white'
            menu_logout.config(font=('arial', 15), fg='black')
        menu_logout = Button(self.window, text='Logout',command=self.add_product,width=10, bg='white', font=('arial', 15), relief='flat')
        menu_logout.grid(column=9,row=0,padx=0, pady=5)
        menu_logout.bind('<Leave>', leave_hover)
        menu_logout.bind('<Enter>', enter_hover)

        frame_bottom = Frame(self.window, height = 50, width = width, bg= 'white')
        frame_bottom.place(x=0, y=(height-60))

    def group(self):
        self.window.switch_frame(Group)

    def add_product(self):
        self.window.switch_frame(AddProduct)

    def sale(self):
        pass

#-----------------------------------------------------------Group-------------------------------------------------------


class Group(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        self.window = window
        self.window = Toplevel()
        self.window.title('Accounting Package')
        self.window.geometry('500x700+200+200')
        self.window.config(bg='#dce9fa')

        self.dbconnect = Curd()
        self.heading = Label(self.window, text = 'Groups', font = ('arial', 15, 'bold'), bd=1, fg = 'black', bg='white')
        self.heading.place(x=0, y=0, relwidth=1)

        self.Id_var = StringVar()
        self.group_name_var = StringVar()
        #---------frame for entry---------

        self.frame_entry = Frame(self.window, bg='#dce9fa')
        self.frame_entry.place(x=0,y=50)

        #--------Label and Entry form for group----
        group_id = Label(self.frame_entry, text = 'Group Id', fg='black', font=('arial, 13'), bg='#dce9fa').grid(row=0, column = 0, padx=(0,5))
        self.entry_group_id = Entry(self.frame_entry,width=10,textvariable=self.Id_var, font=('arial, 13'))
        self.entry_group_id.grid(row=0, column=1,padx=(5,0) )

        group_name = Label(self.frame_entry, text='Group Name', fg='black', font=('arial, 13'), bg='#dce9fa').grid(row=0,column=2, padx=(15,0))
        self.entry_group_name = Entry(self.frame_entry,textvariable=self.group_name_var, width=10, font='arial, 13')
        self.entry_group_name.grid(row=0, column=3)

        #---------------------------button to add group-----------------------------------------
        self.add_group = Button(self.frame_entry,command=self.insert, text='Add',width=10, font=('arial', 13 ), bg='#195e83', fg='white')
        self.add_group.grid(row=0, column=4, padx=10)
# --------------------------------------------------------------------------------------------------------

        #---------------output frame-------------------
        self.output_frame = Frame(self.window, bg= '#dce9fa', bd =4, relief=RIDGE)
        self.output_frame.place(x=5, y=100, width=490, height=540)

        scroll_x=Scrollbar(self.output_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(self.output_frame, orient=VERTICAL)
        self.group_table = ttk.Treeview(self.output_frame,columns=('group_id', 'group_name'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.group_table.xview)
        scroll_y.config(command=self.group_table.yview)
        self.group_table.heading('group_id', text='Group Id')
        self.group_table.heading('group_name', text='Group Name')
        self.group_table.column('group_id', width=100)
        self.group_table.column('group_name', width=100)
        self.group_table['show']='headings'
        self.group_table.pack(fill=BOTH, expand=1)
        self.group_table.bind("<ButtonRelease-1>", self.get_cursor)

        #-------------------button for update and delete--------------------------------
        self.button_frame = Frame(self.window, bd=4, relief=RIDGE, bg='#dce9fa')
        self.button_frame.place(x=5, y=600, width=490, height=90)
        self.update_group = Button(self.button_frame,command=self.update_data, text ='Update', bg='#195e83',font=('arial', 13 ),width=10, fg='white').grid(column=0,pady=10,padx=40)
        self.delete_group = Button(self.button_frame,command=self.delete_data, text='Delete', bg='#195e83',font=('arial', 13 ),width=10, fg='white').grid(row=0,column=1,pady=10,padx=40)
        self.fetch_data()

    def get_cursor(self, ev):
        cursor_row = self.group_table.focus()
        contents = self.group_table.item(cursor_row)
        row = contents['values']
        self.Id_var.set(row[0])
        self.group_name_var.set(row[1])


    def fetch_data(self):
        query = 'select * from tbl_group;'
        rows = self.dbconnect.fetch_data(query)
        print(rows)
        if len(rows) != 0:
            self.group_table.delete(*self.group_table.get_children())
            for row in rows:
                self.group_table.insert('', END, values=row)
                self.dbconnect.connection.commit()

    def insert(self):
        group_ref = Group_c(self.entry_group_id.get(), self.entry_group_name.get())
        query = 'insert into tbl_group values(%s,%s)'
        values = (group_ref.get_group_id(), group_ref.get_group_name())
        self.dbconnect.add_data(query, values)
        self.fetch_data()
        self.clear_data()

    def update_data(self):
        group_ref = Group_c(self.entry_group_id.get(), self.entry_group_name.get())
        query = 'update tbl_group set group_name=%s where group_id=%s;'
        values =(group_ref.get_group_name(),int(group_ref.get_group_id()))
        self.dbconnect.add_data(query,values)
        self.fetch_data()
        self.clear_data()

    def clear_data(self):
        self.Id_var.set('')
        self.group_name_var.set('')

    def delete_data(self):
        group_ref = Group_c(self.entry_group_id.get(), self.entry_group_name.get())
        query = 'delete from tbl_group where group_id=%s;'
        values = (group_ref.get_group_id(),)
        self.dbconnect.delete_data(query, values)
        self.clear_data()
        self.fetch_data()



class AddProduct(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        self.window = window
        self.window = Toplevel()
        self.window.title('Add Product')
        self.window.geometry('800x900+510+90')
        self.window.configure(bg='#dce9fa')

        self.heading = Label(self.window, text = 'Product', font = ('arial', 15, 'bold'), bd=1, fg = 'black', bg='white')
        self.heading.place(x=0, y=0, relwidth=1)

        self.product_id_var = StringVar()
        self.group_id_var = StringVar()
        self.product_name_var = StringVar()
        self.market_price_var = StringVar()
        self.min_stock_var = StringVar()
        self.max_stock_var = StringVar()

        self.dbconnect = Curd()
        #---------frame for entry---------

        self.frame_entry = Frame(self.window, bg='#dce9fa')
        self.frame_entry.place(x=0,y=50)

        #--------Label and Entry form for product----
        product_id = Label(self.frame_entry, text = 'Product Id', fg='black', font=('arial, 13'),width=15, bg='#dce9fa').grid(row=0, column = 0, padx=(15,5), sticky=W)
        self.entry_product_id = Entry(self.frame_entry,width=20,textvariable=self.product_id_var, font=('arial, 13'))
        self.entry_product_id.grid(row=0, column=1,padx=(5,0) , sticky=W)


        group_id = Label(self.frame_entry, text = 'Group Id', fg='black', font=('arial, 13'), bg='#dce9fa').grid(row=0, column = 2, padx=(15,5), sticky=W)
        self.entry_group_id = Entry(self.frame_entry,width=20,textvariable=self.group_id_var, font=('arial, 13'))
        self.entry_group_id.grid(row=0, column=3,padx=(0,15), pady=10 , sticky=W)

        product_name = Label(self.frame_entry, text='Product Name', fg='black', font=('arial, 13'), bg='#dce9fa').grid(row=1,column=0, padx=(15,5), sticky=W)
        self.entry_product_name = Entry(self.frame_entry, width=20,textvariable=self.product_name_var, font='arial, 13')
        self.entry_product_name.grid(row=1, column=1, padx=(0,15), pady=10, sticky=W)

        market_price = Label(self.frame_entry, text='Market Price', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=1, column=2, padx=(15, 5), sticky=W)
        self.entry_market_price = Entry(self.frame_entry,textvariable=self.market_price_var, width=20, font='arial, 13')
        self.entry_market_price.grid(row=1, column=3, padx=(0,15), pady=10, sticky=W)

        stock_minwarning = Label(self.frame_entry, text='Minimum Stock', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=2, column=0, padx=(15, 5), sticky=W)
        self.entry_stock_minwarning = Entry(self.frame_entry,textvariable=self.min_stock_var, width=20, font='arial, 13')
        self.entry_stock_minwarning.grid(row=2, column=1, padx=(0,15), sticky=W)

        stock_maxwarning = Label(self.frame_entry, text='Maximum Stock', fg='black', font=('arial, 13'),
                              bg='#dce9fa').grid(
            row=2, column=2, padx=(15, 5), sticky=W)
        self.entry_stock_maxwarning = Entry(self.frame_entry,textvariable=self.max_stock_var, width=20, font='arial, 13')
        self.entry_stock_maxwarning.grid(row=2, column=3, padx=(0,15), pady=10, sticky=W)


        #---------------------------button to add group-----------------------------------------
        self.add_product = Button(self.frame_entry,command=self.insert, text='Add',width=10, font=('arial', 13 ), bg='#195e83', fg='white')
        self.add_product.grid(row=3, columnspan=4, padx=10)

        #new frame
        self.detail_frame = Frame(self.window, bd=4, relief=RIDGE, bg='#dce9fa')
        self.detail_frame.place(x=10, y=220)
        # -----------------------------------------searching--------------------------------------------------------------------
        search_method = Label(self.detail_frame, text='Search by ', font=('times new roman', 13, 'bold'), fg='white',
                              bg='#195e83')
        search_method.grid(row=0, column=0, pady=10, padx=10, sticky='w')
        self.combo_search = ttk.Combobox(self.detail_frame,
                                         font=('times new roman', 13, 'bold'), width=10, state='readonly')
        self.combo_search['values'] = ('product_name', 'group')
        self.combo_search.grid(row=0, column=1, sticky='w', pady=10, padx=10)

        self.entry_search = Entry(self.detail_frame, font=('times new roman', 13))
        self.entry_search.grid(row=0, column=2, sticky='w', pady=10, padx=10)

        search_btn = Button(self.detail_frame, text='Search', command=self.search_data, width=10,
                            font=('times new roman', 13, 'bold'))
        search_btn.grid(row=0, column=3, padx=10, pady=10, sticky='w')
        AllShow_btn = Button(self.detail_frame, command=self.fetch_data, text='Available Shows', width=15,
                             font=('times new roman', 13, 'bold'))
        AllShow_btn.grid(row=0, column=4, padx=20, pady=10, sticky='w')
        # --------------------------------------------sorting--------------------------------------------------------------------
        sort_method = Label(self.detail_frame, text='Sort by ', font=('times new roman', 13, 'bold'), fg='white',
                            bg='#195e83')
        sort_method.grid(row=1, column=0, pady=10, padx=10, sticky='w')
        self.combo_sort = ttk.Combobox(self.detail_frame,
                                       font=('times new roman', 13, 'bold'), width=10, state='readonly')
        self.combo_sort['values'] = ('product_name', 'price')
        self.combo_sort.grid(row=1, column=1, sticky='w', pady=10, padx=10)
        sort_btn = Button(self.detail_frame, text='Sort', command=self.sorting, width=10,
                          font=('times new roman', 13, 'bold'))
        sort_btn.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        #---------------output frame-------------------
        self.output_frame = Frame(self.window, bg= '#dce9fa', bd =4, relief=RIDGE)
        self.output_frame.place(x=5, y=360, width=790, height=500)

        scroll_x=Scrollbar(self.output_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(self.output_frame, orient=VERTICAL)
        self.group_table = ttk.Treeview(self.output_frame,columns=('product_id', 'group_id', 'product_name',
                                                                   'market_price','stock_minwarning', 'stock_maxwarning'), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.group_table.xview)
        scroll_y.config(command=self.group_table.yview)
        self.group_table.heading('product_id', text='Product Id')
        self.group_table.heading('group_id', text='Group Id')
        self.group_table.heading('product_name', text='Product Name')
        self.group_table.heading('market_price', text='MRP')
        self.group_table.heading('stock_minwarning', text='Min Stock')
        self.group_table.heading('stock_maxwarning', text='Max Stock')
        # self.group_table.column('group_id', width=100)
        # self.group_table.column('group_name', width=100)
        self.group_table['show'] = 'headings'
        self.group_table.pack(fill=BOTH, expand=1)
        self.group_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        #-------------------button for update and delete--------------------------------
        self.button_frame = Frame(self.window, bd=4, relief=RIDGE, bg='#dce9fa')
        self.button_frame.place(x=5, y=840, width=790, height=50)
        self.update_group = Button(self.button_frame, text ='Update',command=self.update_data, bg='#195e83',font=('arial', 13 ),width=10, fg='white').grid(column=0,pady=5,padx=40)
        self.delete_group = Button(self.button_frame, text='Delete',command=self.delete_data, bg='#195e83',font=('arial', 13 ),width=10, fg='white').grid(row=0,column=1,pady=5,padx=40)

    def get_cursor(self, ev):
        cursor_row = self.group_table.focus()
        contents = self.group_table.item(cursor_row)
        row = contents['values']
        self.product_id_var.set(row[0])
        self.group_id_var.set(row[1])
        self.product_name_var.set(row[2])
        self.market_price_var.set(row[3])
        self.min_stock_var.set(row[4])
        self.max_stock_var.set(row[5])

    def fetch_data(self):
        query = 'select * from tbl_product;'
        rows = self.dbconnect.fetch_data(query)
        print(rows)
        if len(rows) != 0:
            self.group_table.delete(*self.group_table.get_children())
            for row in rows:
                self.group_table.insert('', END, values=row)
                self.dbconnect.connection.commit()

    def update_data(self):
        product_ref = Product_c(int(self.entry_product_id.get()), self.entry_product_name.get(), self.entry_market_price.get(),
                  self.entry_stock_minwarning.get(), self.entry_stock_maxwarning.get(), self.entry_group_id.get())
        query = 'update tbl_product set group_id=%s, product_name=%s, price=%s, min_stock=%s, max_stock=%s where product_id=%s;'
        values = (int(product_ref.get_group_id()), product_ref.get_product_name(),product_ref.get_price(),product_ref.get_min_stock(),product_ref.max_stock,int(product_ref.get_product_Id()))
        self.dbconnect.add_data(query, values)
        self.fetch_data()
        self.clear_data()

    def clear_data(self):
        self.product_id_var.set('')
        self.group_id_var.set('')
        self.product_name_var.set('')
        self.market_price_var.set('')
        self.min_stock_var.set('')
        self.max_stock_var.set('')

    def delete_data(self):
        product_ref = Product_c(int(self.entry_product_id.get()), self.entry_product_name.get(),
                                self.entry_market_price.get(),
                                self.entry_stock_minwarning.get(), self.entry_stock_maxwarning.get(),
                                self.entry_group_id.get())
        query = 'delete from tbl_product where group_id=%s;'

        values = (product_ref.get_product_Id(),)
        self.dbconnect.delete_data(query, values)
        self.clear_data()
        self.fetch_data()

    def insert(self):
        query = 'insert into tbl_product values(%s,%s,%s,%s,%s,%s)'
        values = (int(self.entry_product_id.get()), self.entry_product_name.get(), self.entry_market_price.get(),
                  self.entry_stock_minwarning.get(), self.entry_stock_maxwarning.get(), self.entry_group_id.get())
        self.dbconnect.add_data(query, values)
        self.fetch_data()


    def search_data(self):
        query = 'select * from tbl_product;'
        self.dbconnect.fetch_data(query)
        data = self.dbconnect.rows
        a = self.combo_search.get()
        b = self.entry_search.get()

        if a == 'product_name':
            rows = Functions.search_method_function(data, 2, b)
            print(rows)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)
                    self.dbconnect.connection.commit()

        elif a == 'group':
            rows = Functions.search_method_function(data, 1, b)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)
                    self.dbconnect.connection.commit()


    def sorting(self):
        query = 'select * from tbl_product;'
        self.dbconnect.fetch_data(query)
        data = self.dbconnect.rows
        sort_by = self.combo_sort.get()

        if sort_by == 'product_name':
            Functions.sort_method(data, 2)
            rows = data
            print(rows)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)

        if sort_by == 'price':
            rows = Functions.sort_method(data, 3)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)


class Customer(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        self.window = window
        self.window = Toplevel()
        self.window.title('Add Product')
        self.window.geometry('800x900+510+90')
        self.window.configure(bg='#dce9fa')

        self.heading = Label(self.window, text = 'Customer', font = ('arial', 15, 'bold'), bd=1, fg = 'black', bg='white')
        self.heading.place(x=0, y=0, relwidth=1)

        self.customer_id_var = StringVar()
        self.customer_name_var = StringVar()
        self.customer_address_var = StringVar()
        self.customer_contact = StringVar()

        self.dbconnect = Curd()
        #---------frame for entry---------

        self.frame_entry = Frame(self.window, bg='#dce9fa')
        self.frame_entry.place(x=0,y=50)

        #--------Label and Entry form for product----
        customer_id = Label(self.frame_entry, text = 'Customer Id', fg='black', font=('arial, 13'),width=15, bg='#dce9fa').grid(row=0, column = 0, padx=(15,5), sticky=W)
        self.entry_customer_id = Entry(self.frame_entry, width=20, textvariable=self.customer_id_var, font=('arial, 13'))
        self.entry_customer_id.grid(row=0, column=1, padx=(5, 0), sticky=W)


        customer_name = Label(self.frame_entry, text = 'Group Id', fg='black', font=('arial, 13'), bg='#dce9fa').grid(row=0, column = 2, padx=(15,5), sticky=W)
        self.entry_customer_name = Entry(self.frame_entry, width=20, textvariable=self.customer_name_var, font=('arial, 13'))
        self.entry_customer_name.grid(row=0, column=3, padx=(0, 15), pady=10, sticky=W)

        customer_address = Label(self.frame_entry, text='Product Name', fg='black', font=('arial, 13'), bg='#dce9fa').grid(row=1,column=0, padx=(15,5), sticky=W)
        self.entry_customer_address = Entry(self.frame_entry, width=20, textvariable=self.customer_address_var, font='arial, 13')
        self.entry_customer_address.grid(row=1, column=1, padx=(0, 15), pady=10, sticky=W)

        customer_contact = Label(self.frame_entry, text='Market Price', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=1, column=2, padx=(15, 5), sticky=W)
        self.customer_contact = Entry(self.frame_entry, textvariable=self.customer_contact, width=20, font='arial, 13')
        self.customer_contact.grid(row=1, column=3, padx=(0, 15), pady=10, sticky=W)


        #---------------------------button to add group-----------------------------------------
        self.add_customer = Button(self.frame_entry,command=self.insert, text='Add',width=10, font=('arial', 13 ), bg='#195e83', fg='white')
        self.add_customer.grid(row=3, columnspan=4, padx=10)

        #new frame
        self.detail_frame = Frame(self.window, bd=4, relief=RIDGE, bg='#dce9fa')
        self.detail_frame.place(x=10, y=220)
        # -----------------------------------------searching--------------------------------------------------------------------
        search_method = Label(self.detail_frame, text='Search by ', font=('times new roman', 13, 'bold'), fg='white',
                              bg='#195e83')
        search_method.grid(row=0, column=0, pady=10, padx=10, sticky='w')
        self.combo_search = ttk.Combobox(self.detail_frame,
                                         font=('times new roman', 13, 'bold'), width=10, state='readonly')
        self.combo_search['values'] = ('customer_id','customer_name')
        self.combo_search.grid(row=0, column=1, sticky='w', pady=10, padx=10)

        self.entry_search = Entry(self.detail_frame, font=('times new roman', 13))
        self.entry_search.grid(row=0, column=2, sticky='w', pady=10, padx=10)

        search_btn = Button(self.detail_frame, text='Search', command=self.search_data, width=10,
                            font=('times new roman', 13, 'bold'))
        search_btn.grid(row=0, column=3, padx=10, pady=10, sticky='w')
        AllShow_btn = Button(self.detail_frame, command=self.fetch_data, text='Available Shows', width=15,
                             font=('times new roman', 13, 'bold'))
        AllShow_btn.grid(row=0, column=4, padx=20, pady=10, sticky='w')
        # --------------------------------------------sorting--------------------------------------------------------------------
        sort_method = Label(self.detail_frame, text='Sort by ', font=('times new roman', 13, 'bold'), fg='white',
                            bg='#195e83')
        sort_method.grid(row=1, column=0, pady=10, padx=10, sticky='w')
        self.combo_sort = ttk.Combobox(self.detail_frame,
                                       font=('times new roman', 13, 'bold'), width=10, state='readonly')
        self.combo_sort['values'] = ('customer_id', 'customer_name')
        self.combo_sort.grid(row=1, column=1, sticky='w', pady=10, padx=10)
        sort_btn = Button(self.detail_frame, text='Sort', command=self.sorting, width=10,
                          font=('times new roman', 13, 'bold'))
        sort_btn.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        #---------------output frame-------------------
        self.output_frame = Frame(self.window, bg= '#dce9fa', bd =4, relief=RIDGE)
        self.output_frame.place(x=5, y=360, width=790, height=500)

        scroll_x=Scrollbar(self.output_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(self.output_frame, orient=VERTICAL)
        self.group_table = ttk.Treeview(self.output_frame,columns=('customer_id', 'customer_name', 'customer_address'), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.group_table.xview)
        scroll_y.config(command=self.group_table.yview)
        self.group_table.heading('product_id', text='Product Id')
        self.group_table.heading('group_id', text='Group Id')
        self.group_table.heading('product_name', text='Product Name')
        self.group_table.heading('market_price', text='MRP')
        self.group_table.heading('stock_minwarning', text='Min Stock')
        self.group_table.heading('stock_maxwarning', text='Max Stock')
        # self.group_table.column('group_id', width=100)
        # self.group_table.column('group_name', width=100)
        self.group_table['show'] = 'headings'
        self.group_table.pack(fill=BOTH, expand=1)
        self.group_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        #-------------------button for update and delete--------------------------------
        self.button_frame = Frame(self.window, bd=4, relief=RIDGE, bg='#dce9fa')
        self.button_frame.place(x=5, y=840, width=790, height=50)
        self.update_group = Button(self.button_frame, text ='Update',command=self.update_data, bg='#195e83',font=('arial', 13 ),width=10, fg='white').grid(column=0,pady=5,padx=40)
        self.delete_group = Button(self.button_frame, text='Delete',command=self.delete_data, bg='#195e83',font=('arial', 13 ),width=10, fg='white').grid(row=0,column=1,pady=5,padx=40)

    def get_cursor(self, ev):
        cursor_row = self.group_table.focus()
        contents = self.group_table.item(cursor_row)
        row = contents['values']
        self.customer_id_var.set(row[0])
        self.customer_name_var.set(row[1])
        self.customer_address_var.set(row[2])
        self.customer_contact.set(row[3])
        self.min_stock_var.set(row[4])
        self.max_stock_var.set(row[5])

    def fetch_data(self):
        query = 'select * from tbl_product;'
        rows = self.dbconnect.fetch_data(query)
        print(rows)
        if len(rows) != 0:
            self.group_table.delete(*self.group_table.get_children())
            for row in rows:
                self.group_table.insert('', END, values=row)
                self.dbconnect.connection.commit()

    def update_data(self):
        product_ref = Product_c(int(self.entry_customer_id.get()), self.entry_customer_address.get(), self.customer_contact.get(),
                                self.entry_stock_minwarning.get(), self.entry_stock_maxwarning.get(), self.entry_customer_name.get())
        query = 'update tbl_product set group_id=%s, product_name=%s, price=%s, min_stock=%s, max_stock=%s where product_id=%s;'
        values = (int(product_ref.get_group_id()), product_ref.get_product_name(),product_ref.get_price(),product_ref.get_min_stock(),product_ref.max_stock,int(product_ref.get_product_Id()))
        self.dbconnect.add_data(query, values)
        self.fetch_data()
        self.clear_data()

    def clear_data(self):
        self.customer_id_var.set('')
        self.customer_name_var.set('')
        self.customer_address_var.set('')
        self.customer_contact.set('')
        self.min_stock_var.set('')
        self.max_stock_var.set('')

    def delete_data(self):
        product_ref = Product_c(int(self.entry_customer_id.get()), self.entry_customer_address.get(),
                                self.customer_contact.get(),
                                self.entry_stock_minwarning.get(), self.entry_stock_maxwarning.get(),
                                self.entry_customer_name.get())
        query = 'delete from tbl_product where group_id=%s;'

        values = (product_ref.get_product_Id(),)
        self.dbconnect.delete_data(query, values)
        self.clear_data()
        self.fetch_data()

    def insert(self):
        query = 'insert into tbl_product values(%s,%s,%s,%s,%s,%s)'
        values = (int(self.entry_customer_id.get()), self.entry_customer_address.get(), self.customer_contact.get(),
                  self.entry_stock_minwarning.get(), self.entry_stock_maxwarning.get(), self.entry_customer_name.get())
        self.dbconnect.add_data(query, values)
        self.fetch_data()


    def search_data(self):
        query = 'select * from tbl_product;'
        self.dbconnect.fetch_data(query)
        data = self.dbconnect.rows
        a = self.combo_search.get()
        b = self.entry_search.get()

        if a == 'product_name':
            rows = Functions.search_method_function(data, 2, b)
            print(rows)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)
                    self.dbconnect.connection.commit()

        elif a == 'group':
            rows = Functions.search_method_function(data, 1, b)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)
                    self.dbconnect.connection.commit()


    def sorting(self):
        query = 'select * from tbl_product;'
        self.dbconnect.fetch_data(query)
        data = self.dbconnect.rows
        sort_by = self.combo_sort.get()

        if sort_by == 'product_name':
            Functions.sort_method(data, 2)
            rows = data
            print(rows)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)

        if sort_by == 'price':
            rows = Functions.sort_method(data, 3)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)


class Customer(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        self.window = window
        self.window = Toplevel()
        self.window.title('Add Product')
        self.window.geometry('800x900+510+90')
        self.window.configure(bg='#dce9fa')

        self.heading = Label(self.window, text = 'Product', font = ('arial', 15, 'bold'), bd=1, fg = 'black', bg='white')
        self.heading.place(x=0, y=0, relwidth=1)

        self.product_id_var = StringVar()
        self.group_id_var = StringVar()
        self.product_name_var = StringVar()
        self.market_price_var = StringVar()
        self.min_stock_var = StringVar()
        self.max_stock_var = StringVar()

        self.dbconnect = Curd()
        #---------frame for entry---------

        self.frame_entry = Frame(self.window, bg='#dce9fa')
        self.frame_entry.place(x=0,y=50)

        #--------Label and Entry form for product----
        product_id = Label(self.frame_entry, text = 'Product Id', fg='black', font=('arial, 13'),width=15, bg='#dce9fa').grid(row=0, column = 0, padx=(15,5), sticky=W)
        self.entry_product_id = Entry(self.frame_entry,width=20,textvariable=self.product_id_var, font=('arial, 13'))
        self.entry_product_id.grid(row=0, column=1,padx=(5,0) , sticky=W)


        group_id = Label(self.frame_entry, text = 'Group Id', fg='black', font=('arial, 13'), bg='#dce9fa').grid(row=0, column = 2, padx=(15,5), sticky=W)
        self.entry_group_id = Entry(self.frame_entry,width=20,textvariable=self.group_id_var, font=('arial, 13'))
        self.entry_group_id.grid(row=0, column=3,padx=(0,15), pady=10 , sticky=W)

        product_name = Label(self.frame_entry, text='Product Name', fg='black', font=('arial, 13'), bg='#dce9fa').grid(row=1,column=0, padx=(15,5), sticky=W)
        self.entry_product_name = Entry(self.frame_entry, width=20,textvariable=self.product_name_var, font='arial, 13')
        self.entry_product_name.grid(row=1, column=1, padx=(0,15), pady=10, sticky=W)

        market_price = Label(self.frame_entry, text='Market Price', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=1, column=2, padx=(15, 5), sticky=W)
        self.entry_market_price = Entry(self.frame_entry,textvariable=self.market_price_var, width=20, font='arial, 13')
        self.entry_market_price.grid(row=1, column=3, padx=(0,15), pady=10, sticky=W)

        stock_minwarning = Label(self.frame_entry, text='Minimum Stock', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=2, column=0, padx=(15, 5), sticky=W)
        self.entry_stock_minwarning = Entry(self.frame_entry,textvariable=self.min_stock_var, width=20, font='arial, 13')
        self.entry_stock_minwarning.grid(row=2, column=1, padx=(0,15), sticky=W)

        stock_maxwarning = Label(self.frame_entry, text='Maximum Stock', fg='black', font=('arial, 13'),
                              bg='#dce9fa').grid(
            row=2, column=2, padx=(15, 5), sticky=W)
        self.entry_stock_maxwarning = Entry(self.frame_entry,textvariable=self.max_stock_var, width=20, font='arial, 13')
        self.entry_stock_maxwarning.grid(row=2, column=3, padx=(0,15), pady=10, sticky=W)


        #---------------------------button to add group-----------------------------------------
        self.add_product = Button(self.frame_entry,command=self.insert, text='Add',width=10, font=('arial', 13 ), bg='#195e83', fg='white')
        self.add_product.grid(row=3, columnspan=4, padx=10)

        #new frame
        self.detail_frame = Frame(self.window, bd=4, relief=RIDGE, bg='#dce9fa')
        self.detail_frame.place(x=10, y=220)
        # -----------------------------------------searching--------------------------------------------------------------------
        search_method = Label(self.detail_frame, text='Search by ', font=('times new roman', 13, 'bold'), fg='white',
                              bg='#195e83')
        search_method.grid(row=0, column=0, pady=10, padx=10, sticky='w')
        self.combo_search = ttk.Combobox(self.detail_frame,
                                         font=('times new roman', 13, 'bold'), width=10, state='readonly')
        self.combo_search['values'] = ('product_name', 'group')
        self.combo_search.grid(row=0, column=1, sticky='w', pady=10, padx=10)

        self.entry_search = Entry(self.detail_frame, font=('times new roman', 13))
        self.entry_search.grid(row=0, column=2, sticky='w', pady=10, padx=10)

        search_btn = Button(self.detail_frame, text='Search', command=self.search_data, width=10,
                            font=('times new roman', 13, 'bold'))
        search_btn.grid(row=0, column=3, padx=10, pady=10, sticky='w')
        AllShow_btn = Button(self.detail_frame, command=self.fetch_data, text='Available Shows', width=15,
                             font=('times new roman', 13, 'bold'))
        AllShow_btn.grid(row=0, column=4, padx=20, pady=10, sticky='w')
        # --------------------------------------------sorting--------------------------------------------------------------------
        sort_method = Label(self.detail_frame, text='Sort by ', font=('times new roman', 13, 'bold'), fg='white',
                            bg='#195e83')
        sort_method.grid(row=1, column=0, pady=10, padx=10, sticky='w')
        self.combo_sort = ttk.Combobox(self.detail_frame,
                                       font=('times new roman', 13, 'bold'), width=10, state='readonly')
        self.combo_sort['values'] = ('product_name', 'price')
        self.combo_sort.grid(row=1, column=1, sticky='w', pady=10, padx=10)
        sort_btn = Button(self.detail_frame, text='Sort', command=self.sorting, width=10,
                          font=('times new roman', 13, 'bold'))
        sort_btn.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        #---------------output frame-------------------
        self.output_frame = Frame(self.window, bg= '#dce9fa', bd =4, relief=RIDGE)
        self.output_frame.place(x=5, y=360, width=790, height=500)

        scroll_x=Scrollbar(self.output_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(self.output_frame, orient=VERTICAL)
        self.group_table = ttk.Treeview(self.output_frame,columns=('product_id', 'group_id', 'product_name',
                                                                   'market_price','stock_minwarning', 'stock_maxwarning'), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.group_table.xview)
        scroll_y.config(command=self.group_table.yview)
        self.group_table.heading('product_id', text='Product Id')
        self.group_table.heading('group_id', text='Group Id')
        self.group_table.heading('product_name', text='Product Name')
        self.group_table.heading('market_price', text='MRP')
        self.group_table.heading('stock_minwarning', text='Min Stock')
        self.group_table.heading('stock_maxwarning', text='Max Stock')
        # self.group_table.column('group_id', width=100)
        # self.group_table.column('group_name', width=100)
        self.group_table['show'] = 'headings'
        self.group_table.pack(fill=BOTH, expand=1)
        self.group_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        #-------------------button for update and delete--------------------------------
        self.button_frame = Frame(self.window, bd=4, relief=RIDGE, bg='#dce9fa')
        self.button_frame.place(x=5, y=840, width=790, height=50)
        self.update_group = Button(self.button_frame, text ='Update',command=self.update_data, bg='#195e83',font=('arial', 13 ),width=10, fg='white').grid(column=0,pady=5,padx=40)
        self.delete_group = Button(self.button_frame, text='Delete',command=self.delete_data, bg='#195e83',font=('arial', 13 ),width=10, fg='white').grid(row=0,column=1,pady=5,padx=40)

    def get_cursor(self, ev):
        cursor_row = self.group_table.focus()
        contents = self.group_table.item(cursor_row)
        row = contents['values']
        self.product_id_var.set(row[0])
        self.group_id_var.set(row[1])
        self.product_name_var.set(row[2])
        self.market_price_var.set(row[3])
        self.min_stock_var.set(row[4])
        self.max_stock_var.set(row[5])

    def fetch_data(self):
        query = 'select * from tbl_product;'
        rows = self.dbconnect.fetch_data(query)
        print(rows)
        if len(rows) != 0:
            self.group_table.delete(*self.group_table.get_children())
            for row in rows:
                self.group_table.insert('', END, values=row)
                self.dbconnect.connection.commit()

    def update_data(self):
        product_ref = Product_c(int(self.entry_product_id.get()), self.entry_product_name.get(), self.entry_market_price.get(),
                  self.entry_stock_minwarning.get(), self.entry_stock_maxwarning.get(), self.entry_group_id.get())
        query = 'update tbl_product set group_id=%s, product_name=%s, price=%s, min_stock=%s, max_stock=%s where product_id=%s;'
        values = (int(product_ref.get_group_id()), product_ref.get_product_name(),product_ref.get_price(),product_ref.get_min_stock(),product_ref.max_stock,int(product_ref.get_product_Id()))
        self.dbconnect.add_data(query, values)
        self.fetch_data()
        self.clear_data()

    def clear_data(self):
        self.product_id_var.set('')
        self.group_id_var.set('')
        self.product_name_var.set('')
        self.market_price_var.set('')
        self.min_stock_var.set('')
        self.max_stock_var.set('')

    def delete_data(self):
        product_ref = Product_c(int(self.entry_product_id.get()), self.entry_product_name.get(),
                                self.entry_market_price.get(),
                                self.entry_stock_minwarning.get(), self.entry_stock_maxwarning.get(),
                                self.entry_group_id.get())
        query = 'delete from tbl_product where group_id=%s;'

        values = (product_ref.get_product_Id(),)
        self.dbconnect.delete_data(query, values)
        self.clear_data()
        self.fetch_data()

    def insert(self):
        query = 'insert into tbl_product values(%s,%s,%s,%s,%s,%s)'
        values = (int(self.entry_product_id.get()), self.entry_product_name.get(), self.entry_market_price.get(),
                  self.entry_stock_minwarning.get(), self.entry_stock_maxwarning.get(), self.entry_group_id.get())
        self.dbconnect.add_data(query, values)
        self.fetch_data()


    def search_data(self):
        query = 'select * from tbl_product;'
        self.dbconnect.fetch_data(query)
        data = self.dbconnect.rows
        a = self.combo_search.get()
        b = self.entry_search.get()

        if a == 'product_name':
            rows = Functions.search_method_function(data, 2, b)
            print(rows)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)
                    self.dbconnect.connection.commit()

        elif a == 'group':
            rows = Functions.search_method_function(data, 1, b)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)
                    self.dbconnect.connection.commit()


    def sorting(self):
        query = 'select * from tbl_product;'
        self.dbconnect.fetch_data(query)
        data = self.dbconnect.rows
        sort_by = self.combo_sort.get()

        if sort_by == 'product_name':
            Functions.sort_method(data, 2)
            rows = data
            print(rows)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)

        if sort_by == 'price':
            rows = Functions.sort_method(data, 3)
            if len(rows) != 0:
                self.group_table.delete(*self.group_table.get_children())
                for row in rows:
                    self.group_table.insert('', END, values=row)




class Sales(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        self.window = window
        self.window = Toplevel()
        self.window.title('Sales')
        self.window.geometry('900x900+510+90')
        self.window.configure(bg='#dce9fa')

        self.heading = Label(self.window, text='Sales', font=('arial', 15, 'bold'), bd=1, fg='black', bg='white')
        self.heading.place(x=0, y=0, relwidth=1)

        self.sales_id_var = StringVar()
        self.customer_name_var = StringVar()
        self.vendor_contact_var = StringVar()
        self.product_var = StringVar()
        self.quantity_var = StringVar()
        self.rate_var = StringVar()
        self.grand_total_var = StringVar()
        self.discount_var = StringVar()

        self.dbconnect = Curd()
        # self.screen_frame = Frame(self.window, width=900,height=900)
        # self.screen_frame.place(x=0,y=0, width=900, height=900)
        # ---------frame for entry---------


        self.frame_entry = Frame(self.window, bg='#dce9fa', bd=4, relief=GROOVE)
        self.frame_entry.place(x=0, y=30)

        # --------Label and Entry form for product----
        purchase_code = Label(self.frame_entry, text='Bill No.', fg='black', font=('arial, 13'),
                           bg='#dce9fa').grid(row=0, column=0, padx=(15, 5), sticky=W)
        self.entry_sales_id = Entry(self.frame_entry, width=20, textvariable=self.sales_id_var,
                                        font='arial, 13')
        self.entry_sales_id.grid(row=0, column=1, padx=(5, 0))

        customer = Label(self.frame_entry, text='Customer Name', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=1, column=0, padx=(15, 5), sticky=W)
        self.entry_customer_name = Entry(self.frame_entry, width=20, textvariable=self.customer_name_var,
                                        font='arial, 13')
        self.entry_customer_name.grid(row=1, column=1, pady=10, sticky=W)
        Button(self.frame_entry, text='New Customer', relief="flat", bg='#dce9fa', fg='dark blue',
               cursor="hand2", font=('Arial', 10, 'bold', 'underline', 'italic'),
               bd=1, padx=16).grid(
            row=2, column=1, pady=2)

        # customer_con = Label(self.frame_entry, text='Customer Contact', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
        #     row=3, column=0, padx=(15, 5), sticky=W)
        # self.customer_con = Entry(self.frame_entry, textvariable=self.vendor_contact_var, width=20,
        #                                 font='arial, 13')
        # self.customer_con.grid(row=3, column=3, padx=(0, 15), pady=10, sticky=W)

        #-----------------------------------------------------------------------------------------------
        product = Label(self.frame_entry, text='Product', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=3, column=0, padx=(15, 5), sticky=W)
        self.entry_product = Entry(self.frame_entry, width=20, textvariable=self.product_var, font=('arial, 13'))
        self.entry_product.grid(row=3, column=1, padx=(0, 15), pady=10, sticky=W)

        qty = Label(self.frame_entry, text='Quantity', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=4, column=0, padx=(15, 5), sticky=W)
        self.entry_quantity = Entry(self.frame_entry, width=20, textvariable=self.quantity_var,
                                        font='arial, 13')
        self.entry_quantity.grid(row=4, column=1, padx=(0, 15), pady=10, sticky=W)

        market_price = Label(self.frame_entry, text='Rate', fg='black', font=('arial, 13'),
                             bg='#dce9fa').grid(
            row=5, column=0, padx=(15, 5), sticky=W)
        self.entry_market_price = Entry(self.frame_entry, textvariable=self.rate_var, width=20,
                                        font='arial, 13')
        self.entry_market_price.grid(row=5, column=1, padx=(0, 15), pady=10, sticky=W)
        self.add_product = Button(self.frame_entry, command=self.insert, text='Add', width=10, font=('arial', 13),
                                  bg='#195e83', fg='white')
        self.add_product.grid(row=6, column=1, padx=10)

        # --------------------------------for product list---------------------------------------
        self.product_frame = Frame(self.window, bd = 1, relief=GROOVE, bg='#dce9fa')
        self.product_frame.place(x=400, y=30, width=450, height=250)
        self.entry_search_product = Entry(self.product_frame, font=('arial',15))
        self.entry_search_product.grid(row=0, column=0,pady=5, padx=5)
        Button(self.product_frame, text='Search').grid(row=0,column=1)

        self.output_frame = Frame(self.product_frame, bg='#dce9fa', bd=4, relief=RIDGE)
        self.output_frame.place(x=10, y=60, width=450, height=150)
        scroll_x = Scrollbar(self.output_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.output_frame, orient=VERTICAL)
        self.list_product_table = ttk.Treeview(self.output_frame, columns=('product_id', 'product_name', 'price'
                                                                           ), xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.list_product_table.xview)
        scroll_y.config(command=self.list_product_table.yview)
        self.list_product_table.heading('product_id', text='SN')
        self.list_product_table.heading('product_name', text='Product Name')
        self.list_product_table.heading('price', text='Price')
        self.list_product_table['show'] = 'headings'
        self.list_product_table.column('product_id', width=60)
        self.list_product_table.pack(fill=BOTH, expand=1)
        self.list_product_table.bind("<ButtonRelease-1>", self.get_cursor_product)
        self.fetch_data_product()



        # ---------------------------button to add group-----------------------------------------

        # ---------------output frame-------------------
        Label(self.window, text='Bill', font=('times new roman', 40, 'bold'),bg='#dce9fa').place(x=400, y=300)
        self.output_frame = Frame(self.window, bg='#dce9fa', bd=4, relief=RIDGE)
        self.output_frame.place(x=5, y=360, width=790, height=500)

        scroll_x = Scrollbar(self.output_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.output_frame, orient=VERTICAL)
        self.bill_table = ttk.Treeview(self.output_frame, columns=('Bill_no','product_name', 'quantity', 'price',
                                                                    'amount'), xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.bill_table.xview)
        scroll_y.config(command=self.bill_table.yview)
        self.bill_table.heading('Bill_no', text='Bill No.')
        self.bill_table.heading('product_name', text='Product Name')
        self.bill_table.heading('quantity', text='QTY')
        self.bill_table.heading('price', text='Price')
        self.bill_table.heading('amount', text='Amount')
        self.bill_table['show'] = 'headings'
        self.bill_table.pack(fill=BOTH, expand=1)
        self.bill_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        # -------------------button for update and delete--------------------------------


        self.button_frame = Frame(self.window, bd=4, relief=RIDGE, bg='#dce9fa')
        self.button_frame.place(x=5, y=840, width=790, height=50)
        Label(self.button_frame, text='Discount', font=('arial', '15', 'bold')).grid(row=0, column=0)
        self.entry_discount=Entry(self.button_frame, font=('arial', '15', 'bold'),width=10,textvariable=self.discount_var)
        self.entry_discount.grid(row=0, column=1, padx=2,pady=2)

        Label(self.button_frame,font=('arial', '15', 'bold'), text='Grand Total').grid(row=0, column=2)
        self.entry_grand_total = Entry(self.button_frame,font=('arial', '15', 'bold'),width=15, textvariable=self.grand_total_var)
        self.entry_grand_total.grid(row=0, column=3, padx=2, pady=2)

        Button(self.button_frame, text='Sale',font=('arial', '15', 'bold'),width=10, bg='Green').grid(row=0, column=4, padx=50, pady=2)
        self.data = []
        self.list1=[]

    def grand_total(self):
        sum=0
        for i in range(len(self.data)):
            sum =+ self.data[i][4]
        return sum-int(self.entry_discount.get())

    def set_list(self):
        a = self.entry_market_price.get()
        b = self.entry_quantity.get()
        c = int(a) * int(b)
        a = [self.entry_product.get(), self.entry_product.get(),self.entry_quantity.get(),self.entry_market_price.get(), c]
        self.data.append(a)


    def get_cursor(self, ev):
        cursor_row = self.bill_table.focus()
        contents = self.bill_table.item(cursor_row)
        row = contents['values']
        self.sales_id_var.set(row[0])

        self.customer_name_var.set(row[2])
        self.vendor_contact_var.set(row[3])
        self.product_var .set(row[4])
        self.quantity_var.set(row[5])
        self.rate_var.set(row[6])

    def get_cursor_product(self, ev):
        cursor_row = self.list_product_table.focus()
        contents = self.list_product_table.item(cursor_row)
        row = contents['values']
        self.product_var .set(row[1])

    def fetch_data_product(self):
        query = 'select product_id, product_name, price from tbl_product;'
        rows = self.dbconnect.fetch_data(query)
        print(rows)
        if len(rows) != 0:
            self.list_product_table.delete(*self.list_product_table.get_children())
            for row in rows:
                self.list_product_table.insert('', END, values=row)
                self.dbconnect.connection.commit()

    def fetch_data(self):
        query = 'select product_name, quantity, rate, amount from tbl_sales;'
        rows = self.dbconnect.fetch_data(query)
        print(rows)
        if len(rows) != 0:
            self.bill_table.delete(*self.bill_table.get_children())
            for row in rows:
                self.bill_table.insert('', END, values=row)
                self.dbconnect.connection.commit()


    def clear_data(self):
        self.sales_id_var.set('')
        self.customer_name_var.set('')
        self.vendor_contact_var.set('')
        self.product_var.set('')
        self.quantity_var.set('')
        self.rate_var.set('')


    def insert(self):
        # bookissue_ref = BookIssue(self.entry_book_Id.get(), self.entry_book_name.get(), self.entry_student_id.get(), self.entry_student_name.get())
        query = 'insert into tbl_sales values(%s,%s,%s,%s,%s,%s,%s)'
        self.amount = int(self.entry_quantity.get())*int(self.entry_market_price.get())
        values = (self.entry_sales_id.get(), self.entry_customer_name.get(),
                  self.customer_con.get(), self.entry_product.get(), self.entry_quantity.get(), self.entry_market_price.get(),int(self.amount))
        self.dbconnect.add_data(query, values)
        self.fetch_data()


class Purchase(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        self.window = window
        self.window = Toplevel()
        self.window.title('Purchase')
        self.window.geometry('800x900+510+90')
        self.window.configure(bg='#dce9fa')

        self.heading = Label(self.window, text='Purchase', font=('arial', 15, 'bold'), bd=1, fg='black', bg='white')
        self.heading.place(x=0, y=0, relwidth=1)

        self.purchase_id_var = StringVar()
        self.vat_id_var = StringVar()
        self.vendor_name_var = StringVar()
        self.vendor_contact_var = StringVar()
        self.product_var = StringVar()
        self.quantity_var = StringVar()
        self.rate_var = StringVar()

        self.dbconnect = Curd()
        # ---------frame for entry---------

        self.frame_entry = Frame(self.window, bg='#dce9fa')
        self.frame_entry.place(x=0, y=50)

        # --------Label and Entry form for product----
        purchase_code = Label(self.frame_entry, text='Purchase Code', fg='black', font=('arial, 13'), width=15,
                           bg='#dce9fa').grid(row=0, column=0, padx=(15, 5), sticky=W)
        self.entry_purchase_code = Entry(self.frame_entry, width=20, textvariable=self.purchase_id_var, font=('arial, 13'))
        self.entry_purchase_code.grid(row=0, column=1, padx=(5, 0), sticky=W)

        vat_no = Label(self.frame_entry, text='VAT No.', fg='black', font=('arial, 13'), bg='#dce9fa').grid(row=0,
                                                                                                               column=2,
                                                                                                               padx=(
                                                                                                               15, 5),
                                                                                                               sticky=W)
        self.entry_vat_no = Entry(self.frame_entry, width=20, textvariable=self.vat_id_var, font=('arial, 13'))
        self.entry_vat_no.grid(row=0, column=3, padx=(0, 15), pady=10, sticky=W)

        vendor = Label(self.frame_entry, text='Vendor Name', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=1, column=0, padx=(15, 5), sticky=W)
        self.entry_vendor_name = Entry(self.frame_entry, width=20, textvariable=self.vendor_name_var,
                                        font='arial, 13')
        self.entry_vendor_name.grid(row=1, column=1, padx=(0, 15), pady=10, sticky=W)

        vendor_con = Label(self.frame_entry, text='Vendor Contact', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=1, column=2, padx=(15, 5), sticky=W)
        self.entry_vendor_con = Entry(self.frame_entry, textvariable=self.vendor_contact_var, width=20,
                                        font='arial, 13')
        self.entry_vendor_con.grid(row=1, column=3, padx=(0, 15), pady=10, sticky=W)

        #-----------------------------------------------------------------------------------------------
        product = Label(self.frame_entry, text='Product', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=2, column=0, padx=(15, 5), sticky=W)
        self.entry_product = Entry(self.frame_entry, width=20, textvariable=self.product_var, font=('arial, 13'))
        self.entry_product.grid(row=2, column=1, padx=(0, 15), pady=10, sticky=W)

        qty = Label(self.frame_entry, text='Quantity', fg='black', font=('arial, 13'), bg='#dce9fa').grid(
            row=3, column=0, padx=(15, 5), sticky=W)
        self.entry_quantity = Entry(self.frame_entry, width=20, textvariable=self.quantity_var,
                                        font='arial, 13')
        self.entry_quantity.grid(row=3, column=1, padx=(0, 15), pady=10, sticky=W)

        market_price = Label(self.frame_entry, text='Rate', fg='black', font=('arial, 13'),
                             bg='#dce9fa').grid(
            row=4, column=0, padx=(15, 5), sticky=W)
        self.entry_market_price = Entry(self.frame_entry, textvariable=self.rate_var, width=20,
                                        font='arial, 13')
        self.entry_market_price.grid(row=4, column=1, padx=(0, 15), pady=10, sticky=W)
        self.add_product = Button(self.frame_entry, command=self.insert, text='Add', width=10, font=('arial', 13),
                                  bg='#195e83', fg='white')
        self.add_product.grid(row=5, columnspan=4, padx=10)


        # ---------------------------button to add group-----------------------------------------

        # ---------------output frame-------------------
        self.output_frame = Frame(self.window, bg='#dce9fa', bd=4, relief=RIDGE)
        self.output_frame.place(x=5, y=360, width=790, height=500)

        scroll_x = Scrollbar(self.output_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.output_frame, orient=VERTICAL)
        self.group_table = ttk.Treeview(self.output_frame, columns=('product_name', 'quantity', 'price',
                                                                    'amount'), xscrollcommand=scroll_x.set,
                                        yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.group_table.xview)
        scroll_y.config(command=self.group_table.yview)
        self.group_table.heading('product_name', text='Product Name')
        self.group_table.heading('quantity', text='QTY')
        self.group_table.heading('price', text='Price')
        self.group_table.heading('amount', text='Amount')
        self.group_table['show'] = 'headings'
        self.group_table.pack(fill=BOTH, expand=1)
        self.group_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        # -------------------button for update and delete--------------------------------
        self.button_frame = Frame(self.window, bd=4, relief=RIDGE, bg='#dce9fa')
        self.button_frame.place(x=5, y=840, width=790, height=50)


    def get_cursor(self, ev):
        cursor_row = self.group_table.focus()
        contents = self.group_table.item(cursor_row)
        row = contents['values']
        self.purchase_id_var.set(row[0])
        self.vat_id_var.set(row[1])
        self.vendor_name_var.set(row[2])
        self.vendor_contact_var.set(row[3])
        self.product_var .set(row[4])
        self.quantity_var.set(row[5])
        self.rate_var.set(row[6])


    def fetch_data(self):
        query = 'select product_name, quantity, rate, amount from tbl_purchase;'
        rows = self.dbconnect.fetch_data(query)
        print(rows)
        if len(rows) != 0:
            self.group_table.delete(*self.group_table.get_children())
            for row in rows:
                self.group_table.insert('', END, values=row)
                self.dbconnect.connection.commit()


    def clear_data(self):
        self.purchase_id_var.set('')
        self.vat_id_var.set('')
        self.vendor_name_var.set('')
        self.vendor_contact_var.set('')
        self.product_var.set('')
        self.quantity_var.set('')
        self.rate_var.set('')


    def insert(self):
        query = 'insert into tbl_purchase values(%s,%s,%s,%s,%s,%s,%s,%s)'
        self.amount = int(self.entry_quantity.get())*int(self.entry_market_price.get())
        values = (self.entry_purchase_code.get(), self.entry_vat_no.get(), self.entry_vendor_name.get(),
                  self.entry_vendor_con.get(), self.entry_product.get(), self.entry_quantity.get(), self.entry_market_price.get(),int(self.amount))
        self.dbconnect.add_data(query, values)
        self.fetch_data()


if __name__=='__main__':
    start = Main()
    start.mainloop()
