"""
    Contain all the function realted to fornt window.

"""
from .secondwin import Secondwindow
from tkinter import *
from tkinter import filedialog,messagebox
from customtkinter import *
import sqlite3
from dbfread import DBF,FieldParser
from tkinter import ttk
from .queries import query
import threading
import pandas as pd

class MyFieldParser(FieldParser):
    def parseN(self, field, data):
        data = data.strip().strip(b'*\x00')  # Had to strip out the other characters first before \x00, as per super function specs.
        return super(MyFieldParser, self).parseN(field, data)

    def parseD(self, field, data):
        data = data.strip(b'\x00')
        return super(MyFieldParser, self).parseD(field, data)


class Mainwindow:
    def __init__(self, root):
        self.root = root
        root.iconbitmap('src/img/logo.ico')
        root.geometry(f"{600}x{300}")
        root.resizable(False,False)
        self.root.title("DBF to XML")
        self.mframe = CTkFrame(self.root,height=300,width=600)
        

        self.l1 = CTkLabel(self.mframe,text="DBF to XML",padx=40,pady=20,width=20,height=4)
        self.l1.grid(row=0,column=1,columnspan=4)

        self.l2 = CTkLabel(self.mframe,text = "Select File:")
        self.l2.grid(row = 1,column = 0,pady=15)

        self.b = CTkButton(self.mframe,text = "Browse",command= self.open,bg_color="#565b5e",text_font=('Comic Sans MS',12))
        self.b.grid(row = 1,column = 5,pady=15,padx=5)

        self.e = CTkEntry(self.mframe,width = 250,borderwidth=3)
        self.e.grid(row=1,column=1,columnspan=4,pady=15)
        
        self.exit  = CTkButton(self.mframe,width = 50,text="Exit",command=self.root.destroy,bg_color="#565b5e",text_font=('Comic Sans MS',12))
        self.exit.grid(row = 2,column=1,padx = 20,pady = 20)

        self.bn = CTkButton(self.mframe,width=50,text="Next",command=self.next,bg_color="#565b5e",text_font=('Comic Sans MS',12))
        self.bn.grid(row=2,column=4,padx = 20,pady = 20)        
        
        self.mframe.pack(padx = 30,pady=30)
        self.paths=''
        self.input_state = CTkToplevel(self.root)
        self.input_state.geometry("600x80")
        self.input_state.title("DBF to XML")
        self.input_state.iconbitmap('src/img/logo.ico')
        self.root.eval(f'tk::PlaceWindow {str(self.input_state)} center')
        self.option = ''
        self.proj_menu()    

    def disable_event(self):
        pass
    
    def proj_menu(self):
        for child in self.mframe.winfo_children():
            child.configure(state='disabled')
        self.input_state.protocol("WM_DELETE_WINDOW", self.disable_event)
        self.input_state.resizable(False,False)
        CTkButton(master=self.input_state,text = "New Project",command= self.new_proj).grid(row=0,column=1,padx = 100,pady = 20)
        CTkButton(master=self.input_state,text = "Open Project",command= self.open_proj).grid(row=0,column=2,padx = 30,pady = 20)
        

    def new_proj(self):
        self.option = 'new'
        self.fpath = filedialog.asksaveasfilename(filetypes=[("Database File", "*.db")],defaultextension=".db")
        if self.fpath != '':
            for widget in self.input_state.winfo_children():
                widget.destroy()
            self.input_company_state()
        else:
            self.proj_menu()
        
    def open_proj(self):
        self.fpath = filedialog.askopenfilename(title="Select File",filetypes=[("database files","*.db")])
        if self.fpath != '':
            for widget in self.input_state.winfo_children():
                widget.destroy()
            self.input_company_state()
        else:
            self.proj_menu()
        

    def input_company_state(self):        
        self.clicked = StringVar()
        states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 
                  'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 
                  'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal']
        self.clicked.set('Uttarakhand')
        CTkLabel(master=self.input_state,text="Select Company State.").grid(row=0,column=0,padx = 30,pady = 20)
        CTkComboBox(master=self.input_state,variable=self.clicked,values = states).grid(row=0,column=1,padx = 5,pady = 20)
        CTkButton(master=self.input_state,text = "OK",command= self.ok).grid(row=0,column=2,padx = 30,pady = 20)
    
    def ok(self):
        self.input_state.destroy()
        for child in self.mframe.winfo_children():
            child.configure(state='normal')
        
        self.c_state = self.clicked.get()


    def open(self):
        filename = filedialog.askopenfilenames(title="Select File",filetypes=[("dbf files","*.dbf")])
        self.e.insert(0,filename)
        self.paths = filename

    def next(self):
        #if len(self.paths)>0:
        self.e.delete(0,END)
        self.t1 = threading.Thread(target = self.make_connection)    
        self.t1.start()
        self.monitor(self.t1)
                 
        #else:
        #    messagebox.showerror("Error", "select dbf files")
    
    def home(self):
        self.root.geometry(f"{600}x{300}")
        self.mframe.pack(padx = 30,pady=30)
    

    def make_connection(self):
        
        #try:
        self.conn = sqlite3.connect(self.fpath)
        self.cursor = self.conn.cursor()
        if self.option == 'new':
            res = self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type IS 'table'" +" AND name NOT IN ('sqlite_master', 'sqlite_sequence')").fetchall()
            for i in range(len(res)):
                self.cursor.execute("DROP TABLE "+res[i][0])
        self.cursor.execute("DROP TABLE IF EXISTS companystate;")  
        self.cursor.execute("create table  companystate (c_state VARCHAR(30));")
        self.cursor.execute(f"INSERT INTO companystate values('{self.c_state}');")
        if(len(self.paths)>0):
            frame =  CTkToplevel(self.mframe)
            frame.title("Processing")
            frame.iconbitmap('src/img/logo.ico')
            pb = ttk.Progressbar(frame, orient= HORIZONTAL, length= 500, mode= 'determinate')
            pb.pack(anchor="c",padx=20,pady=20)
            l = CTkLabel(master=frame)
            l.pack(anchor="c",padx=20,pady=20)
            
            step = 100/ len(self.paths)
            i=1
            for path in self.paths:
                tablename = path.split('/')[len(path.split('/'))-1]
                l.configure(text=f"Uploading {tablename} ({i}/{len(self.paths)})")
                table = DBF(path, parserclass=MyFieldParser )
                df = pd.DataFrame.from_dict(table)
                tablename = tablename[:-4]
                if tablename.lower() == 'ldgr':
                    self.cursor.execute(query['create_ldgr'])
                    df.to_sql('temp',self.conn,if_exists='replace',index=False)
                    self.cursor.execute(query['insert_ldgr'])
                    self.cursor.execute('drop table temp;')
                else:
                    df.to_sql(tablename,self.conn,if_exists='replace',index=False)
                pb['value'] +=step
                i+=1
                
            #create table ledger & stockitem
            self.cursor.execute(query['create_ledger'])
            self.cursor.execute(query['create_stockitem'])
            self.cursor.execute(query['create_02sales'])
            self.cursor.execute(query['create_02purchase'])
            self.cursor.execute(query['create_03SaleAcct'])
            self.cursor.execute(query['create_03PurAcct'])
            self.cursor.execute(query['AccMultipleDaybookStyle'])
            self.cursor.execute(query['AccountingSingleVch'])
            frame.destroy()
            self.conn.commit()
            self.conn.close()
        
        elif self.option == 'new':
            self.conn.commit()
            self.conn.close()
            messagebox.showerror("Error", "Select DBF files")

        else:
            self.conn.commit()
            self.conn.close()
        """except :
            messagebox.showerror("Error", "Error Importing DBF")
            self.home()"""
    
        
    def monitor(self, thread):
        if thread.is_alive():
            self.root.after(100, lambda: self.monitor(thread))
        
        else:
            conn = sqlite3.connect(self.fpath)
            cursor = conn.cursor()
            res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT IN ('sqlite_master', 'sqlite_sequence');").fetchall()
            conn.close()    
            if len(res)>1:
                self.paths=[]
                self.option=''
                self.mframe.pack_forget()
                q = Secondwindow(self)       
                
    
        

                
