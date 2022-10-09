from tkinter import *
from tkcalendar import *
from babel.numbers import * 

from dbfread import DBF, FieldParser
from tkinter import filedialog, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas as pd
import sqlite3
from sqlite3 import Error

from PIL import Image, ImageTk
from .queries import query
from .xmlconv import xmlconvert
from .input_data import input_stockitem
import os
from customtkinter import *
import threading


class MyFieldParser(FieldParser):
    def parseN(self, field, data):
        # Had to strip out the other characters first before \x00, as per super function specs.
        data = data.strip().strip(b'*\x00')
        return super(MyFieldParser, self).parseN(field, data)

    def parseD(self, field, data):
        data = data.strip(b'\x00')
        return super(MyFieldParser, self).parseD(field, data)


class Secondwindow:
    def __init__(self, mainwindow):

        # tkintr widgets
        self.root = mainwindow.root
        self.mw = mainwindow
        self.db = self.mw.fpath
        try:
            # db connection
            self.conn = sqlite3.connect(self.db)
            self.cursor = self.conn.cursor()
        except Error as e:
            messagebox.showerror("Error", e)
        # list for saving table name
        self.table_names = []

        self.root.geometry(f"{1300}x{550}")
        self.frame = CTkFrame(self.root, height=600, width=1000)
        self.frame.pack()

        self.tableop = LabelFrame(
            self.frame, text="Table Operations.", bg="#2a2d2e", fg="white")
        self.tableop.grid(row=0, column=1, padx=10, pady=20)
        self.selectTable = CTkLabel(self.tableop, text="Select Table: ")
        self.selectTable.grid(row=3, column=0, pady=10, padx=10)

        self.settablemenue()

        self.view = CTkButton(self.tableop, text="View Table", command=self.showtable, height=2, width=14,
                              borderwidth=4, bg_color="#565b5e", fg_color="#565b5e").grid(row=1, column=3, padx=30, pady=10)
        self.tablelist = CTkButton(self.tableop, text="Table List", command=self.showtablelist, height=2, width=14,
                                   borderwidth=4, bg_color="#565b5e", fg_color="#565b5e").grid(row=3, column=3, padx=30, pady=10)
        self.save = CTkButton(self.tableop, text='Save Table', height=2, width=14, borderwidth=4, command=lambda: threading.Thread(
            target=self.convert_table_to_xls).start(), bg_color="#565b5e", fg_color="#565b5e").grid(row=5, column=3, padx=30, pady=10)
        self.saveall = CTkButton(self.tableop, text='Save All Table', height=2, width=14, borderwidth=4, command=lambda: threading.Thread(
            target=self.savealltable, args=(self.root,)).start(), bg_color="#565b5e", fg_color="#565b5e").grid(row=1, column=5, padx=30, pady=10)
        self.path = ''
        self.breplace = CTkButton(self.tableop, text="Replace Table", command=lambda: threading.Thread(
            target=self.replace).start(), bg_color="#565b5e", fg_color="#565b5e")
        self.breplace.grid(row=6, column=6, padx=10, pady=20)

        self.l3 = CTkLabel(self.tableop, text="Select File:")
        self.l3.grid(row=6, column=0, pady=20)

        self.b = CTkButton(self.tableop, text="Browse",
                           command=self.openex, bg_color="#565b5e", fg_color="#565b5e")
        self.b.grid(row=6, column=5, padx=5, pady=20)

        self.e = CTkEntry(self.tableop, width=350, borderwidth=3)
        self.e.grid(row=6, column=1, columnspan=4, pady=20)

        self.inputdata = LabelFrame(
            self.frame, text="Input Data", bg="#2a2d2e", fg="white")
        self.inputdata.grid(row=0, column=2, pady=10, padx=10)

        self.input_ledger = CTkButton(self.inputdata, text="Input Data In ledger", command=lambda: threading.Thread(
            target=self.insert_ledger).start(), bg_color="#565b5e", fg_color="#565b5e")
        self.input_ledger.grid(row=0, column=0, pady=20, padx=20)

        self.input_stockitem = CTkButton(self.inputdata, text="Input Data In stockitem",
                                         command=self.insert_stockitem, bg_color="#565b5e", fg_color="#565b5e")
        self.input_stockitem.grid(row=1, column=0, pady=20, padx=20)

        self.sales02 = CTkButton(self.inputdata, text="Input Data In 02sales",
                                 command=self.insert_02sales, bg_color="#565b5e", fg_color="#565b5e")
        self.sales02.grid(row=2, column=0, pady=20, padx=20)

        self.purchase02 = CTkButton(self.inputdata, text="Input Data In 02purchase",
                                    command=self.insert_02purchase, bg_color="#565b5e", fg_color="#565b5e")
        self.purchase02.grid(row=3, column=0, pady=20, padx=20)

        self.sale03 = CTkButton(self.inputdata, text="Export Data From ldgr",
                                command=self.export_ldgr, bg_color="#565b5e", fg_color="#565b5e")
        self.sale03.grid(row=4, column=0, pady=20, padx=20)

        self.back_img = ImageTk.PhotoImage(Image.open(
            "src/img/back.png").resize((40, 40), Image.ANTIALIAS))
        self.back_CTkButton = CTkButton(
            self.frame, text="", height=30, width=30, image=self.back_img, command=self.back)
        self.back_CTkButton.configure(bg_color="#2a2d2e", fg_color="#2a2d2e")
        self.back_CTkButton.grid(
            row=0, column=0, padx=10, pady=20, sticky="NE")

        self.xmlcon = LabelFrame(
            self.frame, text="XML Conversion", bg="#2a2d2e", fg="white")
        self.xmlcon.grid(row=1, column=1, padx=10, pady=20)
        x = xmlconvert(self.xmlcon, self.db)

    def set_table_name(self):
        try:
            # db connection
            con2 = sqlite3.connect(self.db)
            cur2 = con2.cursor()
        except Error as e:
            messagebox.showerror("Error", e)

        self.table_names.clear()

        try:
            res = cur2.execute(query['get_tables']).fetchall()
            for i in range(len(res)):
                self.table_names.append(res[i][0])

            self.table_names.remove('companystate')

            if ('sqlite_sequence' in self.table_names):
                self.table_names.remove('sqlite_sequence')

        except Error as e:
            messagebox.showerror("Error", e)
        con2.close()

    # ADD NAME OF TABLE IN OPTION MENUE

    def settablemenue(self):
        self.set_table_name()
        self.clicked = StringVar()
        if len(self.table_names) > 0:
            self.clicked.set(self.table_names[0])
        else:
            self.clicked.set('')
        self.dbox = CTkComboBox(master=self.tableop,
                                variable=self.clicked, values=self.table_names)
        self.dbox.grid(row=3, column=1, pady=10, padx=10)

    def savealltable(self, root):

        try:
            # db connection
            conn = sqlite3.connect(self.db)

            frame = CTkToplevel(self.tableop)
            frame.title("Processing")
            frame.iconbitmap('src/img/logo.ico')

            pb = ttk.Progressbar(frame, orient=HORIZONTAL,
                                 length=500, mode='determinate')
            pb.pack(anchor="c", padx=20, pady=20)
            l = CTkLabel(master=frame)
            l.pack(anchor="c", padx=20, pady=20)
            self.set_table_name()

            step = 100/len(self.table_names)

            # create tables if not exist
            cur = os.getcwd()
            cur = os.path.join(cur, "tables")
            if os.path.exists(cur) == FALSE:
                os.makedirs(cur)
            i = 1
            for tname in self.table_names:
                l.configure(
                    text=f"Saving {tname} ({i}/{len(self.table_names)})")
                df = pd.read_sql_query("select * from [" + tname+"];", conn)
                df = df.applymap(lambda x: x.encode('unicode_escape').decode(
                    'utf-8') if isinstance(x, str) else x)
                df.to_excel('tables/' + tname+'.xlsx', index=False)
                pb['value'] += step
                i += 1

            conn.close()
            frame.destroy()
        except Error as e:
            messagebox.showerror("Error", e)

    # display selected table

    def showtable(self):

        try:
            # db connection
            con = sqlite3.connect(self.db)
            cur = con.cursor()

            tname = self.clicked.get()
            r = con.execute("SELECT * from "+tname+" ;")
            columns = tuple(map(lambda x: x[0], r.description))

            # data
            result = cur.execute("SELECT * from "+tname+" ;").fetchall()

            # Add some style
            style = ttk.Style()

            # Pick a theme
            style.theme_use("default")
            # Configure our treeview colors

            style.configure("Treeview",
                            background="#D3D3D3",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="#D3D3D3"
                            )

            # Change selected color
            style.map('Treeview', background=[('selected', 'blue')])

            # main frame
            frame = CTkToplevel(self.frame)
            frame.title(tname)
            frame.iconbitmap('src/img/logo.ico')
            frame.protocol('wm_delete_window', sys.exit)
            tree = Treeview(frame, columns=columns,
                            show='headings', selectmode="extended")

            scrollv = CTkScrollbar(
                frame, orientation=VERTICAL, command=tree.yview)
            scrollv.pack(side=RIGHT, fill=Y)
            scrollh = CTkScrollbar(
                frame, orientation=HORIZONTAL, command=tree.xview)
            scrollh.pack(side=BOTTOM, fill=X)

            tree.pack(side='left', fill=BOTH)
            tree.configure(yscrollcommand=scrollv.set,
                           xscrollcommand=scrollh.set)
            tree.bind("<Left>", lambda event: tree.xview_scroll(-25, "units"))
            tree.bind("<Right>", lambda event: tree.xview_scroll(25, "units"))
            tree.bind("<Up>", lambda event: tree.yview_scroll(-1, "units"))
            tree.bind("<Down>", lambda event: tree.yview_scroll(1, "units"))

            for col in columns:
                tree.column(col, anchor=CENTER)
                tree.heading(col, text=col)

            # Create striped row tags
            tree.tag_configure('oddrow', background="white")
            tree.tag_configure('evenrow', background="#D8D8D8")

            global count
            count = 0

            for res in result:
                if count % 2 == 0:
                    tree.insert(parent='', index='end', text="",
                                values=res, tags=('evenrow',))
                else:
                    tree.insert(parent='', index='end', text="",
                                values=res, tags=('oddrow',))
                count += 1

            con.close()

        except Error as e:
            messagebox.showerror("Error", e)

    def openex(self):
        filename = filedialog.askopenfilename(title="Select File", filetypes=[(
            "Excel files", "*.xlsx"), ("csv files", "*.csv"), ("dbf files", "*.dbf")])
        self.e.insert(0, filename)
        self.path = filename

    def replace(self):
        try:
            # db connection
            
            con3 = sqlite3.connect(self.db)
            if len(self.path) > 0:
                savewin = CTkToplevel(self.tableop)
                screen_width = savewin.winfo_screenwidth()  # Width of the screen
                screen_height = savewin.winfo_screenheight()  # Height of the screen

                # Calculate Starting X and Y coordinates for Window
                x = (screen_width/2) - (100/2)
                y = (screen_height/2) - (20/2)

                savewin.geometry('%dx%d+%d+%d' % (200, 50, x, y))
                savewin.resizable(False, False)
                savewin.title("Replacing")
                savewin.iconbitmap('src/img/logo.ico')
                savewin.protocol("WM_DELETE_WINDOW", self.disable_event)

                pb = ttk.Progressbar(
                    savewin, orient=HORIZONTAL, mode='indeterminate')
                pb.pack(anchor="c", padx=20, pady=20)
                savewin.after(0, lambda: self.change(pb, savewin))

                filename = self.path.split('/')[len(self.path.split('/'))-1]
                if filename.endswith(".xlsx"):
                    tname = filename[:-5]
                else:
                    tname = filename[:-4]
                self.set_table_name()
                if tname not in self.table_names:
                    messagebox.showerror(
                        "Error", "File name and table name must be same.")
                else:
                    if filename.endswith(".dbf"):
                        table = DBF(self.path, parserclass=MyFieldParser)
                        df = pd.DataFrame.from_dict(table)

                    elif filename.endswith(".csv"):
                        df = pd.read_csv(self.path)
                    else:
                        df = pd.read_excel(self.path)
                    df.to_sql(tname, con3, if_exists='replace', index=False)
                self.e.delete(0, END)
                con3.close()
                savewin.destroy()
            else:
                messagebox.showerror("Error", "select csv files")
        except Error as e:
            messagebox.showerror("Error", e)

    def change(self, p, r):
        if not p.winfo_exists():
            return
        p.step(10)
        r.after(100, lambda: self.change(p, r))

    def disable_event(self):
        pass

    def convert_table_to_xls(self):
        self.f = filedialog.asksaveasfilename(
            filetypes=[("Excel files", "*.xlsx")], defaultextension=".xlsx")
        # asksaveasfile return empty if dialog closed with "cancel".
        if self.f == '':
            return
        try:
            savewin = CTkToplevel(self.tableop)
            screen_width = savewin.winfo_screenwidth()  # Width of the screen
            screen_height = savewin.winfo_screenheight()  # Height of the screen

            # Calculate Starting X and Y coordinates for Window
            x = (screen_width/2) - (100/2)
            y = (screen_height/2) - (20/2)

            savewin.geometry('%dx%d+%d+%d' % (200, 50, x, y))
            savewin.resizable(False, False)
            savewin.title("Saving")
            savewin.iconbitmap('src/img/logo.ico')
            savewin.protocol("WM_DELETE_WINDOW", self.disable_event)

            pb = ttk.Progressbar(
                savewin, orient=HORIZONTAL, mode='indeterminate')
            pb.pack(anchor="c", padx=20, pady=20)
            savewin.after(0, lambda: self.change(pb, savewin))

            con4 = sqlite3.connect(self.db)
            tname = self.clicked.get()
            df = pd.read_sql_query("select * from [" + tname+"];", con4)
            df = df.applymap(lambda x: x.encode('unicode_escape').decode(
                'utf-8') if isinstance(x, str) else x)
            df.to_excel(self.f, index=False)
            con4.close()
            savewin.destroy()
        except:
            messagebox.showerror("error", "Close File "+tname+".xlsx. ")

    def showtablelist(self):
        self.set_table_name()
        tablewin = CTkToplevel(self.tableop)
        tablewin.resizable(False, False)
        tablewin.title("Tables")
        tablewin.iconbitmap('src/img/logo.ico')
        # Add some style
        style = ttk.Style()

        # Pick a theme
        style.theme_use("default")
        # Configure our treeview colors

        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3"
                        )

        # Change selected color
        style.map('Treeview',
                  background=[('selected', 'blue')])

        table = Treeview(tablewin)
        table['column'] = ("S.No.", "Table Name")

        # format our columns
        table.column("#0", width=0, stretch=NO)
        table.column("S.No.", anchor=W, width=35)
        table.column("Table Name", anchor=CENTER, width=150)

        # create headings
        table.heading("S.No.", text="S.No.", anchor=W)
        table.heading("Table Name", text="Table Name", anchor=CENTER)

        # add data
        for i in range(len(self.table_names)):
            table.insert(parent='', index='end', iid=i, text="",
                         values=(i+1, self.table_names[i]))

        table.grid(row=15, column=1, padx=15, pady=20)

    def insert_ledger(self):
        self.set_table_name()
        t_names = [name.lower() for name in self.table_names]
        if 'master' in t_names:
            """names = self.cursor.execute("SELECT NAME FROM MASTER WHERE UPST_NO NOT LIKE '50%' OR UPST_NO IS NULL ;").fetchall()
            gw  = group_input(self.tableop,names,self.conn,self.cursor)
            gw.create_group()"""
            try:
                # db connection
                con = sqlite3.connect(self.db)
                cur = con.cursor()
                cur.execute("DELETE FROM ledger;")
                cur.execute(
                    "UPDATE sqlite_sequence SET seq = 1 WHERE name = 'ledger';")
                cur.execute(query['input_ledger'])
                if 'master' in t_names and 'ldgr' in t_names:
                    cur.execute(
                        "UPDATE ldgr SET LEDGER_NAME = (SELECT name from master where master.code = ldgr.code);")
                con.commit()
                con.close()

            except Error as e:
                messagebox.showerror("Error", e)

        else:
            messagebox.showerror("Error", "Input master first.")

    def insert_stockitem(self):
        self.set_table_name()
        t_names = [name.lower() for name in self.table_names]
        if 'product' in t_names:
            self.cursor.execute("DELETE FROM stockitem;")
            stock_names = self.cursor.execute(
                "SELECT B_DESC FROM PRODUCT WHERE TAX != 14.5").fetchall()
            si = input_stockitem(self.tableop, self.conn,
                                 self.cursor, stock_names)
            si.input_date()
        else:
            messagebox.showerror("Error", "Input Product first.")

    def insert_02sales(self):
        self.set_table_name()
        t_names = [name.lower() for name in self.table_names]
        if 'prodtal' in t_names:
            self.selectwin = CTkToplevel(self.inputdata)
            self.selectwin.resizable(False, False)
            self.selectwin.title("Select")
            self.selectwin.iconbitmap('src/img/logo.ico')

            l1 = CTkLabel(self.selectwin, text="Start Date: ")
            l1.grid(row=1, column=2, padx=20, pady=20)
            self.cal1 = Calendar(
                self.selectwin, selectmode="day", date_pattern='mm/dd/y')
            self.cal1.grid(row=2, column=2, padx=20, pady=20)
            l2 = CTkLabel(self.selectwin, text="End Date: ")
            l2.grid(row=1, column=4, padx=20, pady=20)
            self.cal2 = Calendar(
                self.selectwin, selectmode="day", date_pattern='mm/dd/y')
            self.cal2.grid(row=2, column=4, padx=20, pady=20)

            enter = CTkButton(self.selectwin, text="Enter",
                              command=self.salesEnter)
            enter.grid(row=3, column=5, padx=20, pady=20)

        else:
            messagebox.showerror("Error", "Input Prodtal first.")

    def salesEnter(self):
        self.selectwin.destroy()
        date = self.cal1.get_date().split('/')
        sd = date[2][2:]+date[0]+date[1]
        date = self.cal2.get_date().split('/')
        ed = date[2][2:]+date[0]+date[1]
        self.cursor.execute("drop table if exists temp;")
        self.cursor.execute("create table temp (sd integer,ed integer);")
        self.cursor.execute("insert into temp values("+sd+","+ed+");")
        self.cursor.execute("DELETE FROM sales02;")
        self.cursor.execute(query['insert_02sales'])
        self.conn.commit()

    def insert_02purchase(self):
        self.set_table_name()
        t_names = [name.lower() for name in self.table_names]
        if 'prodtal' in t_names:
            self.selectwin = CTkToplevel(self.inputdata)
            self.selectwin.resizable(False, False)
            self.selectwin.title("Select")
            self.selectwin.iconbitmap('src/img/logo.ico')

            l1 = CTkLabel(self.selectwin, text="Start Date: ")
            l1.grid(row=1, column=2, padx=20, pady=20)
            self.cal1 = Calendar(
                self.selectwin, selectmode="day", date_pattern='mm/dd/y')
            self.cal1.grid(row=2, column=2, padx=20, pady=20)
            l2 = CTkLabel(self.selectwin, text="End Date: ")
            l2.grid(row=1, column=4, padx=20, pady=20)
            self.cal2 = Calendar(
                self.selectwin, selectmode="day", date_pattern='mm/dd/y')
            self.cal2.grid(row=2, column=4, padx=20, pady=20)

            enter = CTkButton(self.selectwin, text="Enter",
                              command=self.purEnter)
            enter.grid(row=3, column=5, padx=20, pady=20)

        else:
            messagebox.showerror("Error", "Input Prodtal first.")

    def purEnter(self):
        self.selectwin.destroy()
        date = self.cal1.get_date().split('/')
        sd = date[2][2:]+date[0]+date[1]
        date = self.cal2.get_date().split('/')
        ed = date[2][2:]+date[0]+date[1]
        self.cursor.execute("drop table if exists temp;")
        self.cursor.execute("create table temp (sd integer,ed integer);")
        self.cursor.execute("insert into temp values("+sd+","+ed+");")
        self.cursor.execute("DELETE FROM purchase02;")
        self.cursor.execute(query['insert_02purchase'])
        self.conn.commit()

    def export_ldgr(self):

        self.set_table_name()
        t_names = [name.lower() for name in self.table_names]

        if 'ldgr' in t_names:

            self.selectwin = CTkToplevel(self.inputdata)
            self.selectwin.resizable(False, False)
            self.selectwin.title("Select")
            self.selectwin.iconbitmap('src/img/logo.ico')

            l1 = CTkLabel(self.selectwin, text="Start Date: ")
            l1.grid(row=1, column=2, padx=20, pady=20)
            self.cal1 = Calendar(
                self.selectwin, selectmode="day", date_pattern='mm/dd/y')
            self.cal1.grid(row=2, column=2, padx=20, pady=20)
            l2 = CTkLabel(self.selectwin, text="End Date: ")
            l2.grid(row=1, column=4, padx=20, pady=20)
            self.cal2 = Calendar(
                self.selectwin, selectmode="day", date_pattern='mm/dd/y')
            self.cal2.grid(row=2, column=4, padx=20, pady=20)

            enter = CTkButton(self.selectwin, text="Enter", command=self.Enter)
            enter.grid(row=3, column=5, padx=20, pady=20)

        else:
            messagebox.showerror("Error", "Input ldgr first.")

    def Enter(self):
        date = self.cal1.get_date().split('/')
        sd = date[2][2:]+date[0]+date[1]
        date = self.cal2.get_date().split('/')
        ed = date[2][2:]+date[0]+date[1]
        self.cursor.execute("drop table if exists temp;")
        self.cursor.execute("create table temp (sd integer,ed integer);")
        self.cursor.execute("insert into temp values("+sd+","+ed+");")
        self.conn.commit()
        for widget in self.selectwin.winfo_children():
            widget.destroy()

        self.s = IntVar()
        self.p = IntVar()
        self.r = IntVar()
        self.cash = IntVar()
        self.check = IntVar()
        self.pay = IntVar()

        l = CTkLabel(master=self.selectwin, text="Select Exporting Style :").grid(
            row=0, column=0, padx=20, pady=10)
        l1 = CTkLabel(master=self.selectwin, text="AccMultipleDaybookStyle").grid(
            row=0, column=1, padx=20, pady=10)
        l2 = CTkLabel(master=self.selectwin, text="AccountingSingleVch").grid(
            row=0, column=2, padx=20, pady=10)

        self.export = CTkButton(master=self.selectwin,
                                text="Export", command=self.ldgr_ex)
        self.export.grid(row=7, column=3, pady=10, padx=10)
        self.export.configure(state='disabled')

        sales = CTkLabel(master=self.selectwin, text="Sales").grid(
            row=1, column=0, padx=20, pady=10)
        sm = CTkRadioButton(master=self.selectwin, text="", variable=self.s, value=1,
                            command=self.change_state).grid(row=1, column=1, padx=20, pady=10)
        ss = CTkRadioButton(master=self.selectwin, text="", variable=self.s, value=2,
                            command=self.change_state).grid(row=1, column=2, padx=20, pady=10)

        pur = CTkLabel(master=self.selectwin, text="Purchase").grid(
            row=2, column=0, padx=20, pady=10)
        pm = CTkRadioButton(master=self.selectwin, text="", variable=self.p, value=1,
                            command=self.change_state).grid(row=2, column=1, padx=20, pady=10)
        ps = CTkRadioButton(master=self.selectwin, text="", variable=self.p, value=2,
                            command=self.change_state).grid(row=2, column=2, padx=20, pady=10)

        cash_l = CTkLabel(master=self.selectwin, text="Cash Deposit").grid(
            row=3, column=0, padx=20, pady=10)
        cam = CTkRadioButton(master=self.selectwin, text="", variable=self.cash,
                             value=1, command=self.change_state).grid(row=3, column=1, padx=20, pady=10)
        cas = CTkRadioButton(master=self.selectwin, text="", variable=self.cash,
                             value=2, command=self.change_state).grid(row=3, column=2, padx=20, pady=10)
        cas = CTkRadioButton(master=self.selectwin, text="", variable=self.cash,
                             value=2, command=self.change_state).grid(row=3, column=2, padx=20, pady=10)

        check_l = CTkLabel(master=self.selectwin, text="Check Deposit").grid(
            row=4, column=0, padx=20, pady=10)
        chm = CTkRadioButton(master=self.selectwin, text="", variable=self.check,
                             value=1, command=self.change_state).grid(row=4, column=1, padx=20, pady=10)
        chs = CTkRadioButton(master=self.selectwin, text="", variable=self.check,
                             value=2, command=self.change_state).grid(row=4, column=2, padx=20, pady=10)

        rec = CTkLabel(master=self.selectwin, text="Receipt").grid(
            row=5, column=0, padx=20, pady=10)
        rm = CTkRadioButton(master=self.selectwin, text="", variable=self.r, value=1,
                            command=self.change_state).grid(row=5, column=1, padx=20, pady=10)
        rs = CTkRadioButton(master=self.selectwin, text="", variable=self.r, value=2,
                            command=self.change_state).grid(row=5, column=2, padx=20, pady=10)

        pay_l = CTkLabel(master=self.selectwin, text="Payment").grid(
            row=6, column=0, padx=20, pady=10)
        pam = CTkRadioButton(master=self.selectwin, text="", variable=self.pay,
                             value=1, command=self.change_state).grid(row=6, column=1, padx=20, pady=10)
        pas = CTkRadioButton(master=self.selectwin, text="", variable=self.pay,
                             value=2, command=self.change_state).grid(row=6, column=2, padx=20, pady=10)

    def change_state(self):

        if (self.s.get() != 0 and self.p.get() != 0 and self.r.get() != 0 and self.cash.get() != 0 and self.check.get() != 0 and self.pay.get() != 0):
            self.export.configure(state='normal')

    def ldgr_ex(self):
        self.cursor.execute("DELETE FROM Sale03Acct;")
        self.cursor.execute("DELETE FROM Pur03Acct;")
        self.cursor.execute("DELETE FROM AccMultipleDaybookStyle;")
        self.cursor.execute("DELETE FROM AccountingSingleVch;")
        self.cursor.execute(query['insert_Sale03Acct'])
        self.cursor.execute(query['insert_Pur03Acct'])

        if self.s.get() == 1:
            self.cursor.execute(query['insert_sales_AccMultipleDaybookStyle'])
        else:
            self.cursor.execute(query['insert_sales_AccountingSingleVch'])

        if self.p.get() == 1:
            self.cursor.execute(query['insert_pur_AccMultipleDaybookStyle'])
        else:
            self.cursor.execute(query['insert_pur_AccountingSingleVch'])

        if self.r.get() == 1:
            self.cursor.execute(
                query['insert_receipt_AccMultipleDaybookStyle'])
        else:
            self.cursor.execute(query['insert_receipt_AccountingSingleVch'])

        self.cursor.execute(query['insert_creceipt_AccMultipleDaybookStyle'])

        self.cursor.execute(
            "CREATE  VIEW cashrec AS SELECT * from AccMultipleDaybookStyle WHERE source_vouchertypename = 'Cash Receipt';")
        self.cursor.execute(
            "CREATE  VIEW discount AS SELECT * from AccMultipleDaybookStyle WHERE source_vouchertypename = 'Discount';")
        self.cursor.execute("""INSERT INTO AccMultipleDaybookStyle SELECT c.voucher_number,c.voucher_date,'Receipt','Receipt',c.narrations,'Cash',
                               c.credit_amount-d.debit_amount,0,'' from cashrec c,discount d WHERE c.voucher_number=d.voucher_number ;""")
        self.cursor.execute("DROP VIEW cashrec")
        self.cursor.execute("DROP VIEW discount")
        self.cursor.execute("""UPDATE AccMultipleDaybookStyle set source_vouchertypename="Receipt",original_vouchertypename="Receipt" 
                               WHERE source_vouchertypename="Discount" or source_vouchertypename="Cash Receipt"; """)

        if self.pay.get() == 1:
            self.cursor.execute(
                query['insert_payment_AccMultipleDaybookStyle'])
        else:
            self.cursor.execute(query['insert_payment_AccountingSingleVch'])

        if self.cash.get() == 1:
            self.cursor.execute(
                query['insert_cashdeposit_AccMultipleDaybookStyle'])
        else:
            self.cursor.execute(
                query['insert_cashdeposit_AccountingSingleVch'])

        if self.check.get() == 1:
            self.cursor.execute(query['insert_contra_AccMultipleDaybookStyle'])
        else:
            self.cursor.execute(query['insert_contra_AccountingSingleVch'])
        self.cursor.execute("drop table if exists temp;")
        self.conn.commit()
        self.selectwin.destroy()

    def back(self):
        self.frame.pack_forget()
        self.mw.home()
