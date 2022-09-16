import pandas as pd
from .queries import query
from tkinter import *
from tkcalendar import *
from customtkinter import *


"""
class group_input:
    
    l_dict = {}
    

    def __init__(self,root,names,conn,cursor):
        self.root = root
        self.names = names
        self.i = 0
        self.clicked = []
        self.label = []
        self.op = []
        self.conn = conn
        self.cursor = cursor

        for n in names:
            self.l_dict[n[0]] = 'Bank Accounts'

        # main frame
        self.frame =  CTkToplevel(self.root)

        self.frame.geometry("550x800")
        self.frame.resizable(False, False)
        #canvas
        canvas = Canvas(self.frame,height=800,bg = "#2a2d2e")
        canvas.pack(side=LEFT,fill=BOTH,expand=1)

        #scorll bar
        scroll  = CTkScrollbar(self.frame,orientation=VERTICAL)
        scroll.pack(side=RIGHT,fill=Y)

        canvas.configure(yscrollcommand=scroll.set)
        scroll.configure(command=canvas.yview)
        canvas.bind("<1>",     lambda event: canvas.focus_set())
        canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Up>",    lambda event: canvas.yview_scroll(-1, "units"))
        canvas.bind("<Down>",  lambda event: canvas.yview_scroll( 1, "units"))

        self.frame2  = CTkFrame(canvas,height=800,width=600)
        canvas.create_window((0,0),window=self.frame2,anchor="nw")

        

    def create_group(self):
        
        ledger_group = ['Bank Accounts','Bank OD A/c','Bank OD A/c','Branch / Divisions','Capital Account','Cash-in-Hand',
                        'Current Assets','Current Liabilities','Deposits (Asset)','Direct Expenses','Direct Incomes',
                        'Duties & Taxes','Direct Expenses','Indirect Expenses','Fixed Assets','Direct Incomes','Indirect Incomes',
                        'Indirect Expenses','Indirect Incomes','Investments','Loans & Advances (Asset)','Loans (Liability)',
                        'Misc. Expenses (ASSET)','Provisions','Purchase Accounts','Reserves & Surplus','Reserves & Surplus',
                        'Sales Accounts','Secured Loans','Stock-in-Hand','Sundry Creditors','Sundry Debtors','Suspense A/c','Unsecured Loans']


        if self.i+10 > len(self.names):
            ledger = self.names[self.i:len(self.names)]
            next = CTkButton(self.frame2,text="Save",command=lambda:self.save(ledger),height=2,width=15,borderwidth=4)
        

        else:
            ledger = self.names[self.i:self.i+10]
            next = CTkButton(self.frame2,text="next",command=lambda:self.next(ledger),height=2,width=15,borderwidth=4)
            
        if self.i>9:
            back = CTkButton(self.frame2,text="back",command=lambda:self.back(ledger),height=2,width=15,borderwidth=4)
            back.grid(row = 13,column = 1,padx = 10,pady =20)
        
        for j in range(len(ledger)):
            self.clicked.append(StringVar())
            self.clicked[j].set(self.l_dict[ledger[j][0]])

            self.label.append(CTkLabel(self.frame2,text=ledger[j][0]))
            self.op.append(CTkComboBox(master = self.frame2,variable = self.clicked[j],values=ledger_group))

            self.label[j].grid(row = j,column = 1,padx = 20,pady =20)
            self.op[j].grid(row = j,column = 3,padx = 10,pady =20)
        
        
        next.grid(row = 13,column = 4,padx = 10,pady =20)


    def save(self,ledger):
        for i in range(len(ledger)):
            self.l_dict[ledger[i][0]] =  self.clicked[i].get() 

        l_group = { 'Ledger_Name' : list(self.l_dict.keys()),
                    'Ledger_Group' : list(self.l_dict.values()) }
       


        df = pd.DataFrame(l_group)
        df.to_sql('l_group',self.conn,if_exists='replace')
        self.conn.commit()        

        self.cursor.execute(query['input_ledger'])
        self.conn.commit()
        
        self.frame.destroy()


    def next(self,ledger):

        for i in range(len(ledger)):
            self.l_dict[ledger[i][0]] =  self.clicked[i].get() 
         
        self.clicked.clear()
        self.label.clear()
        self.op.clear()
        for widget in self.frame2.winfo_children():
            widget.destroy()
        self.frame2.pack_forget()
        self.i  = self.i + 10
        self.create_group()
    

    def back(self,ledger):
        for i in range(len(ledger)):
            self.l_dict[ledger[i][0]] =  self.clicked[i].get() 
        self.clicked.clear()
        self.label.clear()
        self.op.clear()
        for widget in self.frame2.winfo_children():
            widget.destroy()
        self.frame2.pack_forget()
        self.i = self.i - 10
        self.create_group()

"""

class input_stockitem:
    
    u_dict = {}
    

    def __init__(self,root,conn,cursor,stock_name):
        self.root = root
        self.conn = conn
        self.cursor = cursor
        self.stock_name = stock_name
        self.clicked_base = []
        self.clicked_alt = []
        self.label = []
        self.op1 = []
        self.op2 = []
        self.i = 0
        for n in stock_name:
            self.u_dict[n[0]] = ['PCS','','PIECES',''] 

        
        
    
    def input_date(self):
        self.frame = CTkToplevel(self.root)
        self.frame.title("Tables")
        self.frame.iconbitmap('src/img/logo.ico')
        
        self.frame.resizable(False, False)
        l = CTkLabel(self.frame,text="Select Selling Date: ")
        l.grid(row=1,column=2,padx=20,pady=20)
        self.cal = Calendar(self.frame,selectmode="day",date_pattern='mm/dd/y')
        self.cal.grid(row=1,column=4,padx=20,pady=20)
        enter  = CTkButton(self.frame,text="Enter",command=self.Enter)
        enter.grid(row=2,column=3,padx=20,pady=20)
        
    def Enter(self):    
        date = self.cal.get_date().split('/')
        d = date[2]+"-"+date[0]+"-"+date[1]
        self.cursor.execute("drop table if exists temp;")
        self.cursor.execute("create table temp (d VARCHAR(100));")
        self.cursor.execute("insert into temp values('"+d+"');")
        self.conn.commit()
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.create_scroll()

    def create_scroll(self):
        #canvas
        self.frame.geometry("750x750")
        self.frame.resizable(False, False)
        canvas = Canvas(self.frame,height=700,bg="#2a2d2e")
        canvas.pack(side=LEFT,fill=BOTH,expand=1)

        #scorll bar
        scrollv  = CTkScrollbar(self.frame,orientation=VERTICAL)
        scrollv.pack(side=RIGHT,fill=Y)

        canvas.configure(yscrollcommand=scrollv.set)
        scrollv.configure(command=canvas.yview)

        
        canvas.bind("<1>",     lambda event: canvas.focus_set())
        canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Up>",    lambda event: canvas.yview_scroll(-1, "units"))
        canvas.bind("<Down>",  lambda event: canvas.yview_scroll( 1, "units"))
        canvas.bind("<Left>",    lambda event: canvas.xview_scroll(-1, "units"))
        canvas.bind("<Right>",  lambda event: canvas.xview_scroll( 1, "units"))


        self.frame2  = CTkFrame(canvas,height=600,width=800)

        canvas.create_window((0,0),window=self.frame2,anchor="nw")  
        self.input_base_unit()



    def input_base_unit(self):        
        
        
        self.units = {'':'','BAG': 'BAGS', 'BAL': 'BALE', 'BDL': 'BUNDLES', 'BKL': 'BUCKLES', 'BOU': 'BILLIONS OF UNITS', 'BOX': 'BOX', 'BTL': 'BOTTLES', 
                 'BUN': 'BUNCHES', 'CAN': 'CANS', 'CBM': 'CUBIC METER', 'CCM': 'CUBIC CENTIMETER', 'CMS': 'CENTIMETER', 'CTN': 'CARTONS', 
                 'DOZ': 'DOZEN', 'DRM': 'DRUM', 'GGR': 'GREAT GROSS', 'GMS': 'GRAMS', 'GRS': 'GROSS', 'GYD': 'GROSS YARDS', 'KGS': 'KILOGRAMS', 
                 'KLR': 'KILOLITRE','KME': 'KILOMETRE', 'MLT': 'MILLILITRE', 'MTR': 'METERS', 'MTS': 'METRIC TON', 'NOS': 'NUMBERS', 'PAC':'PACKS',
                 'PCS': 'PIECES','PRS': 'PAIRS', 'QTL': 'QUINTAL','ROL': 'ROLLS', 'SET': 'SETS', 'SQF': 'SQFSQUARE FEET', 'SQM': 'SQUARE METERS', 
                 'SQY': 'SQUARE YARDS','TBS': 'TABLETS', 'TGM': 'TEN GRAMS', 'THD': 'THOUSANDS', 'TON':'TONNES','TUB':'TUBES', 'UGS': 'US GALLONS', 'UNT': 'UNITS', 'YDS': 
                 'YARDS', 'OTH': 'OTHERS'}
        
        
        if self.i+10 > len(self.stock_name):
            names = self.stock_name[self.i:len(self.stock_name)]
            next = CTkButton(self.frame2,text="Save",command=lambda:self.save(names),height=2,width=15,borderwidth=4)

        else:
            names = self.stock_name[self.i:self.i+10]
            next = CTkButton(self.frame2,text="next",command=lambda:self.next(names),height=2,width=15,borderwidth=4)

        if self.i>9:
            back = CTkButton(self.frame2,text="back",command=lambda:self.back(names),height=2,width=15,borderwidth=4)
            back.grid(row = 13,column = 1,padx = 10,pady =20)
        

        
        stock_name =CTkLabel(self.frame2,text="Stock Name",text_font=('Helvetica', 16))
        base_u = CTkLabel(self.frame2,text="Base Unit",text_font=('Helvetica', 16))
        alt_u = CTkLabel(self.frame2,text="Alternate Unit",text_font=('Helvetica', 16))

        stock_name.grid(row=0,column = 0,padx = 10,pady =20)
        base_u.grid(row=0,column = 2,padx = 10,pady =20)
        alt_u.grid(row=0,column = 4,padx = 10,pady =20)

        for j in range(len(names)):
            self.clicked_base.append(StringVar())
            self.clicked_base[j].set(self.u_dict[names[j][0]][0])
            self.clicked_alt.append(StringVar())
            self.clicked_alt[j].set(self.u_dict[names[j][0]][1])
            self.label.append(CTkLabel(self.frame2,text=names[j][0]))
            self.op1.append(CTkComboBox(master=self.frame2,variable=self.clicked_base[j],values = list(self.units.keys())))
    
            self.op2.append(CTkComboBox(master = self.frame2,variable = self.clicked_alt[j],values =list(self.units.keys())))
    
            
            self.label[j].grid(row = j+1,column = 0,padx = 10,pady =20)
            self.op1[j].grid(row = j+1,column = 2,padx = 10,pady =20)
            self.op2[j].grid(row = j+1,column = 4,padx = 10,pady =20)
        
            next.grid(row = 13,column = 4,padx = 5,pady =20)
    
    
    def save(self,names):
        for i in range(len(names)):
            self.u_dict[names[i][0]][0] = self.clicked_base[i].get() 
            self.u_dict[names[i][0]][1] =  self.clicked_alt[i].get()
            self.u_dict[names[i][0]][2] =  self.units[self.clicked_base[i].get()]
            self.u_dict[names[i][0]][3] = self.units[self.clicked_alt[i].get()] 

        n = []
        bu = []
        au = []
        bfn = []
        afn =  []
        
        for key in self.u_dict:
            n.append(key)
            bu.append(self.u_dict[key][0])
            au.append(self.u_dict[key][1])
            bfn.append(self.u_dict[key][2])
            afn.append(self.u_dict[key][3])
        
        self.unit = {'Stock_name': n,
                     'base_unit': bu,
                     'alt_unit' : au,
                     'base_formal': bfn,
                     'alt_formal': afn
                    }
        


        df = pd.DataFrame(self.unit)
        df.to_sql('units',self.conn,if_exists='replace')
        self.conn.commit()        

        self.cursor.execute(query['insert_stockitem'])
        self.cursor.execute("drop table temp;")
        self.cursor.execute("drop table units;")
        self.conn.commit()  
        
        self.frame.destroy()


    def next(self,names):

        for i in range(len(names)):
            self.u_dict[names[i][0]][0] = self.clicked_base[i].get() 
            self.u_dict[names[i][0]][1] =  self.clicked_alt[i].get()
            self.u_dict[names[i][0]][2] =  self.units[self.clicked_base[i].get()]
            self.u_dict[names[i][0]][3] = self.units[self.clicked_alt[i].get()]

        self.clicked_base.clear()
        self.clicked_alt.clear()
        self.label.clear()
        self.op1.clear()
        self.op2.clear()
        for widget in self.frame2.winfo_children():
            widget.destroy()
        self.frame2.pack_forget()
        self.i  = self.i + 10
        self.input_base_unit()


    def back(self,names):

        for i in range(len(names)):
            self.u_dict[names[i][0]][0] = self.clicked_base[i].get() 
            self.u_dict[names[i][0]][1] =  self.clicked_alt[i].get()
            self.u_dict[names[i][0]][2] =  self.units[self.clicked_base[i].get()]
            self.u_dict[names[i][0]][3] = self.units[self.clicked_alt[i].get()]

        self.clicked_base.clear()
        self.clicked_alt.clear()
        self.label.clear()
        self.op1.clear()
        self.op2.clear()
        for widget in self.frame2.winfo_children():
            widget.destroy()
        self.frame2.pack_forget()
        self.i  = self.i -10
        self.input_base_unit()
        
 



