#  ------------------------------------------mehran ommani------------------------------------------
#  ------------------------------------------982403453----------------------------------------------
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, ttk, Label, Frame, Entry, Button
import sqlite3 as db
from sqlite3 import Error
from datetime import date

class Bill_App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1024x768")
        self.master.title("shop management system")

        title = Label(self.master, text="SHOP MANAGEMENT", bd=12, relief=GROOVE, bg="red",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # define tabs
        self.tabs = ttk.Notebook(self.master)
        self.sell = Frame(self.tabs)
        self.sellreport = Frame(self.tabs)
        self.stockManagment = Frame(self.tabs)
        self.tabs.add(self.sell, text='Sell')
        self.tabs.add(self.sellreport, text='Sell Report')
        self.tabs.add(self.stockManagment, text='Stock Management')
        self.tabs.pack(expand=1, fil='both')
        #Database variable
        self.dbName = 'shopManagement.db'
        self.sqlite_insert_sell = ''' INSERT INTO sell(date,item_id,quantity,order_type)
                                                VALUES(?,?,?,?) '''
        # grocery  quantity variable
        self.maggie = IntVar()
        self.rice = IntVar()
        self.wheat = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.sugar = IntVar()
        #grocery quantity for stock variable
        self.maggieQ = IntVar()
        self.riceQ = IntVar()
        self.wheatQ = IntVar()
        self.food_oilQ = IntVar()
        self.daalQ = IntVar()
        self.sugarQ = IntVar()
        # grocery price variable
        self.maggieP = IntVar()
        self.riceP = IntVar()
        self.wheatP = IntVar()
        self.food_oilP = IntVar()
        self.daalP = IntVar()
        self.sugarP = IntVar()

        self.g_mg = 0
        self.g_rc = 0
        self.g_wh = 0
        self.g_sg = 0
        self.g_fol = 0
        self.g_dl = 0

        # product price varible
        self.grocery_price = StringVar()
        # ----------------->>>>> Groccery frame <<<----------------
        F3 = LabelFrame(self.sell, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),
                        fg="gold", bg="sky blue")
        F3.place(x=0, y=0, width=220, height=393)

        g1_label = Label(F3, text="Meggie", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g1_txt = Entry(F3, width=4, textvariable=self.maggie, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10, sticky=W)

        g2_label = Label(F3, text="Rice", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=1,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g2_txt = Entry(F3, width=4, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10, sticky=W)

        g3_label = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g3_txt = Entry(F3, width=4, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10, sticky=W)

        g4_label = Label(F3, text="Food oil", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=4, textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10, sticky=W)

        g5_label = Label(F3, text="Daal", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=4,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g5_txt = Entry(F3, width=4, textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10, sticky=W)

        g6_label = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=5,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g6_txt = Entry(F3, width=4, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10, sticky=W)

        # bill Area ....................................
        F6 = LabelFrame(self.sell, bd=10, relief=GROOVE)
        F6.place(x=220, y=0, width=380, height=393)
        bill_title = Label(F6, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)

        scrol_y = Scrollbar(F6, orient=VERTICAL)
        self.txtarea = Text(F6, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #  bottom button frame----------------------------------

        F7 = LabelFrame(self.sell, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg="sky blue")
        F7.place(x=0, y=393, relwidth=1, height=180)


        m2 = Label(F7, text="Total Grocery Price", bg="sky blue", fg="black",
                   font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky=W)
        m2_txt = Entry(F7, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)
        btn_frame = Frame(F7, bd=7, relief=GROOVE)
        btn_frame.place(x=0, y=40, width=785, height=90)

        total_btn = Button(btn_frame, command=self.total, text="Total", bg="cyan", bd=5, fg="black", pady=15, width=14,
                           font="arial 12 bold").grid(row=0, column=0, padx=5, pady=5)

        genbill_btn = Button(btn_frame, text="Generate Bill", command=self.bill_area, bg="cyan", bd=5, fg="black",
                             pady=15, width=14, font="arial 12 bold").grid(row=0, column=1, padx=5, pady=5)

        finalizebill_btn = Button(btn_frame, text="Finalize Bill", command=self.purchase, bg="cyan", bd=5, fg="black",
                             pady=15, width=14, font="arial 12 bold").grid(row=0, column=2, padx=5, pady=5)

        clear_btn = Button(btn_frame, text="Clear", command=self.clear_data, bg="cyan", bd=5, fg="black", pady=15,
                           width=11, font="arial 12 bold").grid(row=0, column=3, padx=5, pady=5)

        returned_btn = Button(btn_frame, text="return", command=self.returnedItem, bg="cyan", bd=5, fg="black", pady=15,
                           width=11, font="arial 12 bold").grid(row=0, column=4, padx=5, pady=5)
        # return Area ....................................
        F9 = LabelFrame(self.sell, bd=10, relief=GROOVE)
        F9.place(x=600, y=0, width=380, height=393)
        bill_title = Label(F9, text="Return Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)

        scrol_y1 = Scrollbar(F9, orient=VERTICAL)
        self.txtarea_rt = Text(F9, yscrollcommand=scrol_y1.set)
        scrol_y1.pack(side=RIGHT, fill=Y)
        scrol_y1.config(command=self.txtarea.yview)
        self.txtarea_rt.pack(fill=BOTH, expand=1)


        # sell report area----------------------------------------------------------
        F8 = LabelFrame(self.sellreport, bd=10, relief=GROOVE)
        F8.place(x=0, y=0, width=380, height=393)
        sell_report_title = Label(F8, text="Sell Report", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F8, orient=VERTICAL)
        self.txtarea_sr = Text(F8, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea_sr.yview)
        self.txtarea_sr.pack(fill=BOTH, expand=1)
        ###
        F10 = LabelFrame(self.sellreport, bd=10, relief=GROOVE)
        F10.place(x=380, y=0, width=380, height=393)
        return_report_title = Label(F10, text="Return Report", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y_2 = Scrollbar(F10, orient=VERTICAL)
        self.txtarea_rt_r = Text(F10, yscrollcommand=scrol_y_2.set)
        scrol_y_2.pack(side=RIGHT, fill=Y)
        scrol_y_2.config(command=self.txtarea_rt_r.yview)
        self.txtarea_rt_r.pack(fill=BOTH, expand=1)

        #stock management
        F11 = LabelFrame(self.stockManagment, bd=10, relief=GROOVE, text="grocery inventory", font=("times new roman", 15, "bold"),
                        fg="gold", bg="sky blue")
        F11.place(x=0, y=0, width=300, height=450)

        q_label = Label(F11, text="Quantity", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=0,
                                                                                                                  column=1,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")

        p_label = Label(F11, text="Price", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=0,
                                                                                                                  column=2,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g1_label = Label(F11, text="Meggie", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=1,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g1_txt = Entry(F11, width=4, textvariable=self.maggieQ, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10, sticky=W)
        g11_txt = Entry(F11, width=4, textvariable=self.maggieP, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=2, padx=10, pady=10, sticky=W)
        g2_label = Label(F11, text="Rice", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=2,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g2_txt = Entry(F11, width=4, textvariable=self.riceQ, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10, sticky=W)
        g22_txt = Entry(F11, width=4, textvariable=self.riceP, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=2, padx=10, pady=10, sticky=W)
        g3_label = Label(F11, text="Wheat", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=3,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g3_txt = Entry(F11, width=4, textvariable=self.wheatQ, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10, sticky=W)
        g33_txt = Entry(F11, width=4, textvariable=self.wheatP, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=2, padx=10, pady=10, sticky=W)
        g4_label = Label(F11, text="Food oil", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F11, width=4, textvariable=self.food_oilQ, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10, sticky=W)
        g44_txt = Entry(F11, width=4, textvariable=self.food_oilP, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=2, padx=10, pady=10, sticky=W)
        g5_label = Label(F11, text="Daal", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g5_txt = Entry(F11, width=4, textvariable=self.daalQ, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10, sticky=W)
        g55_txt = Entry(F11, width=4, textvariable=self.daalP, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=2, padx=10, pady=10, sticky=W)
        g6_label = Label(F11, text="Sugar", font=("times new roman", 16, "bold"), fg="black", bg="sky blue").grid(row=6,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g6_txt = Entry(F11, width=4, textvariable=self.sugarQ, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10, sticky=W)
        g66_txt = Entry(F11, width=4, textvariable=self.sugarP, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=6, column=2, padx=10, pady=10, sticky=W)
        F12 = LabelFrame(self.stockManagment, bd=10, relief=GROOVE, text="Update Price and Stock", font=("times new roman", 15, "bold"),
                        fg="gold", bg="sky blue")
        F12.place(x=0, y=450, relwidth=1, height=150)
        stock_btn_frame = Frame(F12, bd=7, relief=GROOVE)
        stock_btn_frame.place(x=10, y=5, width=200, height=100)
        stock_btn_update = Button(stock_btn_frame, command=self.updateStockPrice, text="Update", bg="cyan", bd=5, fg="black", pady=15, width=14,
                           font="arial 12 bold").grid(row=0, column=0, padx=5, pady=5)

        F13 = LabelFrame(self.stockManagment, bd=10, relief=GROOVE, text="List of goods with zero inventory", font=("times new roman", 15, "bold"),
                        fg="gold", bg="sky blue")
        F13.place(x=300, y=0, width=400, height=450)
        zero_inventory_title = Label(F13, text="Zero Inventory Report", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y_3 = Scrollbar(F13, orient=VERTICAL)
        self.txtarea_zeroInventory = Text(F13, yscrollcommand=scrol_y_3.set)
        scrol_y_3.pack(side=RIGHT, fill=Y)
        scrol_y_3.config(command=self.txtarea_zeroInventory.yview)
        self.txtarea_zeroInventory.pack(fill=BOTH, expand=1)


        self.welcome_bill()
        self.welcome_self_report()
        self.welcome_updateStock()
        self.welcome_zero_inventory_report()

    def welcome_zero_inventory_report(self):
        self.txtarea_zeroInventory.delete('1.0', END)
        self.txtarea_zeroInventory.insert(END, "\t\t|| Ommani SHOP ||")
        self.txtarea_zeroInventory.insert(END, "\n==========================================")
        self.txtarea_zeroInventory.insert(END, "\n\tProducts\t\t\tQTY")
        self.txtarea_zeroInventory.insert(END, "\n==========================================")
        sqlcon = self.connection()
        cursor = sqlcon.cursor()
        cursor.execute('''select name from item where stock=0''')
        rows = cursor.fetchall()
        for row in rows:
            self.txtarea_zeroInventory.insert(END, f"\n\t{row[0]}\t\t\t0")
        cursor.close()
        sqlcon.commit()

    def welcome_updateStock(self):
        self.setPrice()
        self.maggieQ.set(self.getStock(1))
        self.riceQ.set(self.getStock(2))
        self.wheatQ.set(self.getStock(3))
        self.food_oilQ.set(self.getStock(4))
        self.daalQ.set(self.getStock(5))
        self.sugarQ.set(self.getStock(6))

    def updateStockPrice(self):
        sqlcon = self.connection()
        cursor = sqlcon.cursor()
        if self.maggieQ.get() != 0:
            stock = self.getStock(1) + self.maggieQ.get()
            value = (self.maggieP.get(), stock, 1)
            cursor.execute('''UPDATE item
                              SET price = ? ,
                              stock = ? 
                              WHERE id = ?;''', value)
        if self.riceQ.get() != 0:
            stock = self.getStock(2) + self.riceQ.get()
            value = (self.riceP.get(), stock, 2)
            cursor.execute('''UPDATE item
                              SET price = ? ,
                              stock = ? 
                              WHERE id = ?;''', value)
        if self.wheatQ.get() != 0:
            stock = self.getStock(3) + self.wheatQ.get()
            value = (self.wheatP.get(), stock, 3)
            cursor.execute('''UPDATE item
                              SET price = ? ,
                              stock = ? 
                              WHERE id = ?;''', value)
        if self.food_oilQ.get() != 0:
            stock = self.getStock(4) + self.food_oilQ.get()
            value = (self.food_oilP.get(), stock, 4)
            cursor.execute('''UPDATE item
                              SET price = ? ,
                              stock = ? 
                              WHERE id = ?;''', value)
        if self.daalQ.get() != 0:
            stock = self.getStock(5) + self.daalQ.get()
            value = (self.daalP.get(), stock, 5)
            cursor.execute('''UPDATE item
                              SET price = ? ,
                              stock = ? 
                              WHERE id = ?;''', value)
        if self.sugarQ.get() != 0:
            stock = self.getStock(6) + self.sugarQ.get()
            value = (self.sugarP.get(), stock, 6)
            cursor.execute('''UPDATE item
                              SET price = ? ,
                              stock = ? 
                              WHERE id = ?;''', value)
        sqlcon.commit()
        cursor.close()

    def getPrice(self, sqlcon, itemID):
        """
        report price of item
        :param sqlcon: sqlite connection
        :return: iterative over price
        """
        try:
            sqlcon.commit()
            cursor = sqlcon.cursor()
            cursor.execute('''select price from item where id = ?''', (itemID,))
            return cursor.fetchall()[0][0]

        except Error as error:
            print(error)
            return -1
        cursor.close()
    def connection(self):
        """
        create connection to sqlite3 Database
        :return: connection
        """
        sqliteConnection = ''
        try:
            sqliteConnection = db.connect(self.dbName)
            print("Successfully Connected to SQLite")
            return sqliteConnection
        except Error as error:
            print("Error while executing sqlite script", error)

    def setPrice(self):
        sqlcon = self.connection()
        sqlcon.commit()
        self.maggieP.set(self.getPrice(sqlcon, 1))
        self.riceP.set(self.getPrice(sqlcon, 2))
        self.wheatP.set(self.getPrice(sqlcon, 3))
        self.food_oilP.set(self.getPrice(sqlcon, 4))
        self.daalP.set(self.getPrice(sqlcon, 5))
        self.sugarP.set(self.getPrice(sqlcon, 6))

    def insertPurchase(self, sqlCon, insert_table_query, value):
        """
        insert data to table
        :param sqlCon: sqlite3 connection
        :param insert_table_query: insert query
        :param value: the tuple contain value for insert
        :return: result of sql command
        """
        try:
            cursor = sqlCon.cursor()
            cursor.execute(insert_table_query, value)
            sqlCon.commit()
            return cursor.lastrowid
        except Error as error:
            print('Error while executing insert query', error)
            return 0
        cursor.close()

    def purchase(self):
        if self.maggie.get() != 0:
            value = (date.today(), 1, self.maggie.get(), 1)
            stock = self.getStock(1)
            if stock >= self.maggie.get():
                sqlcon = self.connection()
                self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
                stock = stock-self.maggie.get()
                self.updateStock(1, stock)
                sqlcon.commit()
        if self.rice.get() != 0:
            value = (date.today(), 2, self.rice.get(), 1)
            stock = self.getStock(2)
            if stock >= self.rice.get():
                sqlcon = self.connection()
                self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
                stock = stock-self.rice.get()
                self.updateStock(2, stock)
                sqlcon.commit()
        if self.wheat.get() != 0:
            value = (date.today(), 3, self.wheat.get(), 1)
            stock = self.getStock(3)
            if stock >= self.wheat.get():
                sqlcon = self.connection()
                self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
                stock = stock-self.wheat.get()
                self.updateStock(3, stock)
                sqlcon.commit()
        if self.food_oil.get() != 0:
            value = (date.today(), 4, self.food_oil.get(), 1)
            stock = self.getStock(4)
            if stock >= self.food_oil.get():
                sqlcon = self.connection()
                self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
                stock = stock-self.food_oil.get()
                self.updateStock(4, stock)
                sqlcon.commit()
        if self.daal.get() != 0:
            value = (date.today(), 5, self.daal.get(), 1)
            stock = self.getStock(5)
            if stock >= self.daal.get():
                sqlcon = self.connection()
                self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
                stock = stock-self.daal.get()
                self.updateStock(5, stock)
                sqlcon.commit()
        if self.sugar.get() != 0:
            value = (date.today(), 6, self.sugar.get(), 1)
            stock = self.getStock(6)
            if stock >= self.sugar.get():
                sqlcon = self.connection()
                self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
                stock = stock-self.sugar.get()
                self.updateStock(6, stock)
                sqlcon.commit()

    def total(self):
        self.setPrice()
        self.g_mg = self.maggie.get() * self.maggieP.get()
        self.g_rc = self.rice.get() * self.riceP.get()
        self.g_wh = self.wheat.get() * self.wheatP.get()
        self.g_sg = self.sugar.get() * self.sugarP.get()
        self.g_fol = self.food_oil.get() * self.food_oilP.get()
        self.g_dl = self.daal.get() * self.daalP.get()

        self.total_grocery_price = float(
            self.g_dl +
            self.g_fol +
            self.g_mg +
            self.g_rc +
            self.g_sg +
            self.g_wh
        )
        self.grocery_price.set(str(self.total_grocery_price))
        self.total_bill = float(self.total_grocery_price)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t\t|| Ommani SHOP ||")
        self.txtarea.insert(END, "\n_________________________________________\n")
        self.txtarea.insert(END, f"\nBill No. : ")
        self.txtarea.insert(END, f"\nCustomer Name :")
        self.txtarea.insert(END, f"\nPhone no.:")
        self.txtarea.insert(END, "\n==========================================")
        self.txtarea.insert(END, "\nProducts\t\t\tQTY\t   Price")
        self.txtarea.insert(END, "\n==========================================")
        self.txtarea_rt.delete('1.0', END)
        self.txtarea_rt.insert(END, "\t\t|| Ommani SHOP ||")
        self.txtarea_rt.insert(END, "\n_________________________________________\n")
        self.txtarea_rt.insert(END, f"\nBill No. : ")
        self.txtarea_rt.insert(END, f"\nCustomer Name :")
        self.txtarea_rt.insert(END, f"\nPhone no.:")
        self.txtarea_rt.insert(END, "\n==========================================")
        self.txtarea_rt.insert(END, "\nProducts\t\t\tQTY\t   Price")
        self.txtarea_rt.insert(END, "\n==========================================")
        self.txtarea_rt_r.delete('1.0', END)
        self.txtarea_rt_r.insert(END, "\t\t|| Ommani SHOP ||")
        self.txtarea_rt_r.insert(END, "\n_________________________________________\n")
        self.txtarea_rt_r.insert(END, f"\nBill No. : ")
        self.txtarea_rt_r.insert(END, f"\nCustomer Name :")
        self.txtarea_rt_r.insert(END, f"\nPhone no.:")
        self.txtarea_rt_r.insert(END, "\n==========================================")
        self.txtarea_rt_r.insert(END, "\nProducts\t\t\tQTY\t   Price")
        self.txtarea_rt_r.insert(END, "\n==========================================")

    def bill_area(self):
        self.welcome_bill()
        # Grocery print
        if self.maggie.get() != 0:
            self.txtarea.insert(END, f"\nMaggie   \t\t\t{self.maggie.get()}\t    {self.g_mg}")
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\nRice     \t\t\t{self.rice.get()}\t    {self.g_rc}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\nWheat    \t\t\t{self.wheat.get()}\t    {self.g_wh}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\nFood oil \t\t\t{self.food_oil.get()}\t    {self.g_fol}")
        if self.sugar.get() != 0:
            self.txtarea.insert(END, f"\nSugar    \t\t\t{self.sugar.get()}\t    {self.g_sg}")
        if self.daal.get() != 0:
            self.txtarea.insert(END, f"\nDaal     \t\t\t{self.daal.get()}\t    {self.g_dl}")
        self.txtarea.insert(END, "\n`````````````````````````````````````````")
        self.txtarea.insert(END, f"\nTotal Bill :\t\t\t      Rs. {str(self.total_bill)}")
        self.txtarea.insert(END, "\n`````````````````````````````````````````")

    def clear_data(self):
        op = messagebox.askyesno("Exit", "Do you want to Exit")
        if op > 0:
            self.maggie.set(0)
            self.rice.set(0)
            self.wheat.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.sugar.set(0)
            self.grocery_price.set(0)
            self.welcome_bill()
        else:
            return

    def getStock(self, item_id):
        sqlcon = self.connection()
        sqlcon.commit()
        try:
            cursor = sqlcon.cursor()
            cursor.execute('''select stock from item where id = ?''', (item_id,))
            return cursor.fetchall()[0][0]
            sqlcon.commit()
            cursor.close()
        except Error as error:
            print(error)
            return -1

    def updateStock(self, item_id, stock):
        sqlcon = self.connection()
        sqlcon.commit()
        try:
            value = (stock, item_id)
            cursor = sqlcon.cursor()
            cursor.execute(''' UPDATE item SET stock = ? WHERE id == ?''', value)
            sqlcon.commit()
            return cursor.lastrowid
        except Error as error:
            print(error)
            return -1

        cursor.close()
    def welcome_self_report(self):
        self.setPrice()
        self.txtarea_sr.delete('1.0', END)
        self.txtarea_sr.insert(END, "\t\t|| Ommani SHOP ||")
        self.txtarea_sr.insert(END, "\n_________________________________________\n")
        self.txtarea_sr.insert(END, f"\nDate : {date.today()} ")
        self.txtarea_sr.insert(END, "\n==========================================")
        self.txtarea_sr.insert(END, "\nProducts\t\t\t\tQTY")
        self.txtarea_sr.insert(END, "\n==========================================")
        self.txtarea_rt_r.delete('1.0', END)
        self.txtarea_rt_r.insert(END, "\t\t|| Ommani SHOP ||")
        self.txtarea_rt_r.insert(END, "\n_________________________________________\n")
        self.txtarea_rt_r.insert(END, f"\nDate : {date.today()} ")
        self.txtarea_rt_r.insert(END, "\n==========================================")
        self.txtarea_rt_r.insert(END, "\nProducts\t\t\t\tQTY")
        self.txtarea_rt_r.insert(END, "\n==========================================")
        sqlcon = self.connection()
        cursor = sqlcon.cursor()
        cursor.execute('''select item_id, quantity, order_type 
                            from sell 
                            where date= ?''',
                       (date.today(),))
        rows = cursor.fetchall()
        cursor.close()
        self.total_sell_today = 0
        self.total_item_sold_today = 0
        self.total_return_today = 0
        self.total_item_return_today = 0
        for row in rows:
            if row[2] == 1:
                self.total_item_sold_today += row[1]
                if row[0] == 1:
                    self.txtarea_sr.insert(END, f"\nMaggie   \t\t\t\t{row[1]}")
                    self.total_sell_today += row[1] * self.maggieP.get()
                    continue
                if row[0] == 2:
                    self.txtarea_sr.insert(END, f"\nRice   \t\t\t\t{row[1]}")
                    self.total_sell_today += row[1] * self.riceP.get()
                    continue
                if row[0] == 3:
                    self.txtarea_sr.insert(END, f"\nWheat   \t\t\t\t{row[1]}")
                    self.total_sell_today += row[1] * self.wheatP.get()
                    continue
                if row[0] == 4:
                    self.txtarea_sr.insert(END, f"\nFood Oil   \t\t\t\t{row[1]}")
                    self.total_sell_today += row[1] * self.food_oilP.get()
                    continue
                if row[0] == 5:
                    self.txtarea_sr.insert(END, f"\nDaal   \t\t\t\t{row[1]}")
                    self.total_sell_today += row[1] * self.daalP.get()
                    continue
                if row[0] == 6:
                    self.txtarea_sr.insert(END, f"\nSuger   \t\t\t\t{row[1]}")
                    self.total_sell_today += row[1] * self.sugarP.get()
                    continue
            else:
                self.total_item_return_today += row[1]
                if row[0] == 1:
                    self.txtarea_rt_r.insert(END, f"\nMaggie   \t\t\t\t{row[1]}")
                    self.total_return_today += row[1] * self.maggieP.get()
                    continue
                if row[0] == 2:
                    self.txtarea_rt_r.insert(END, f"\nRice   \t\t\t\t{row[1]}")
                    self.total_return_today += row[1] * self.riceP.get()
                    continue
                if row[0] == 3:
                    self.txtarea_rt_r.insert(END, f"\nWheat   \t\t\t\t{row[1]}")
                    self.total_return_today += row[1] * self.wheatP.get()
                    continue
                if row[0] == 4:
                    self.txtarea_rt_r.insert(END, f"\nFood Oil   \t\t\t\t{row[1]}")
                    self.total_return_today += row[1] * self.food_oilP.get()
                    continue
                if row[0] == 5:
                    self.txtarea_rt_r.insert(END, f"\nDaal   \t\t\t\t{row[1]}")
                    self.total_return_today += row[1] * self.daalP.get()
                    continue
                if row[0] == 6:
                    self.txtarea_rt_r.insert(END, f"\nSuger   \t\t\t\t{row[1]}")
                    self.total_return_today += row[1] * self.sugarP.get()
                    continue

        self.txtarea_sr.insert(END, "\n`````````````````````````````````````````")
        self.txtarea_sr.insert(END, f"\nTotal sold :\t\t\t       {str(self.total_sell_today)}")
        self.txtarea_sr.insert(END, "\n`````````````````````````````````````````")
        self.txtarea_sr.insert(END, f"\nNumber of items sold :\t\t\t       {str(self.total_item_sold_today)}")
        self.txtarea_sr.insert(END, "\n`````````````````````````````````````````")
        self.txtarea_rt_r.insert(END, "\n`````````````````````````````````````````")
        self.txtarea_rt_r.insert(END, f"\nTotal return :\t\t\t       {str(self.total_return_today)}")
        self.txtarea_rt_r.insert(END, "\n`````````````````````````````````````````")
        self.txtarea_rt_r.insert(END, f"\nNumber of items return :\t\t\t       {str(self.total_item_return_today)}")
        self.txtarea_rt_r.insert(END, "\n`````````````````````````````````````````")

    def returnedItem(self):
        self.welcome_bill()
        self.total()
        # Grocery print
        if self.maggie.get() != 0:
            self.txtarea_rt.insert(END, f"\nMaggie   \t\t\t{self.maggie.get()}\t    {self.g_mg}")
            self.submitRetrunedItem()
        if self.rice.get() != 0:
            self.txtarea_rt.insert(END, f"\nRice     \t\t\t{self.rice.get()}\t    {self.g_rc}")
            self.submitRetrunedItem()
        if self.wheat.get() != 0:
            self.txtarea_rt.insert(END, f"\nWheat    \t\t\t{self.wheat.get()}\t    {self.g_wh}")
            self.submitRetrunedItem()
        if self.food_oil.get() != 0:
            self.txtarea_rt.insert(END, f"\nFood oil \t\t\t{self.food_oil.get()}\t    {self.g_fol}")
            self.submitRetrunedItem()
        if self.sugar.get() != 0:
            self.txtarea_rt.insert(END, f"\nSugar    \t\t\t{self.sugar.get()}\t    {self.g_sg}")
            self.submitRetrunedItem()
        if self.daal.get() != 0:
            self.txtarea_rt.insert(END, f"\nDaal     \t\t\t{self.daal.get()}\t    {self.g_dl}")
            self.submitRetrunedItem()
        self.txtarea_rt.insert(END, "\n`````````````````````````````````````````")
        self.txtarea_rt.insert(END, f"\nTotal Bill :\t\t\t      Rs. {str(self.total_bill)}")
        self.txtarea_rt.insert(END, "\n`````````````````````````````````````````")

    def submitRetrunedItem(self):
        if self.maggie.get() != 0:
            stock = self.getStock(1)
            stock = stock + self.maggie.get()
            value = (date.today(), 1, self.maggie.get(), 0)
            sqlcon = self.connection()
            self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
            self.updateStock(1, stock)
            sqlcon.commit()
        if self.rice.get() != 0:
            stock = self.getStock(2)
            stock = stock + self.rice.get()
            value = (date.today(), 2, self.rice.get(), 0)
            sqlcon = self.connection()
            self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
            self.updateStock(2, stock)
            sqlcon.commit()
        if self.wheat.get() != 0:
            stock = self.getStock(3)
            stock = stock + self.wheat.get()
            value = (date.today(), 3, self.wheat.get(), 0)
            sqlcon = self.connection()
            self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
            self.updateStock(3, stock)
            sqlcon.commit()
        if self.food_oil.get() != 0:
            stock = self.getStock(4)
            stock = stock + self.food_oil.get()
            value = (date.today(), 4, self.food_oil.get(), 0)
            sqlcon = self.connection()
            self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
            self.updateStock(4, stock)
            sqlcon.commit()
        if self.daal.get() != 0:
            stock = self.getStock(5)
            stock = stock + self.daal.get()
            value = (date.today(), 5, self.daal.get(), 0)
            sqlcon = self.connection()
            self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
            self.updateStock(5, stock)
            sqlcon.commit()
        if self.sugar.get() != 0:
            stock = self.getStock(6)
            stock = stock + self.sugar.get()
            value = (date.today(), 6, self.sugar.get(), 0)
            sqlcon = self.connection()
            self.insertPurchase(sqlcon, self.sqlite_insert_sell, value)
            self.updateStock(6, stock)
            sqlcon.commit()

global root
root = Tk()

obj = Bill_App(root)
root.mainloop()
