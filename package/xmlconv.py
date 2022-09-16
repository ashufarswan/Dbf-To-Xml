from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sqlite3 import Error
import uuid
from customtkinter import *
from tkinter.filedialog import asksaveasfilename
import threading
import sqlite3

class xmlconvert:
    def __init__(self, frame,db):
        self.frame = frame
        self.db = db
        self.path = ' '

        self.l1 = CTkLabel(self.frame, text="Select Table: ")
        self.l1.grid(row=6, column=3, pady=10, padx=5)

        self.table_names = ['ledger', 'stockitem','groups']
        try:
            self.clicked = StringVar()
            if len(self.table_names) > 0:
                self.clicked.set(self.table_names[0])
            else:
                self.clicked.set('')
            self.op = CTkComboBox( master=self.frame, variable=self.clicked, values=self.table_names)
            self.op.grid(row=6, column=4, pady=10, padx=5)
        except Error as e:
            messagebox.showerror("Error", e)

        self.ex = CTkButton(self.frame, text="Export As XML",command=lambda:threading.Thread(target = self.export).start(), bg_color="#565b5e", fg_color="#565b5e")
        self.ex.grid(row=6, column=5, pady=10, padx=30)


    def change(self,p,r):
        if not p.winfo_exists():
            return
        p.step(10)
        r.after(100, lambda:self.change(p,r))
    
    def disable_event(self):
        pass

    def export(self):
        self.f = asksaveasfilename(filetypes=[("XML files", "*.xml")],defaultextension=".xml")
        if self.f == '':  # asksaveasfile return empty if dialog closed with "cancel".
            return

        exporting = CTkToplevel(self.frame)
        screen_width = exporting.winfo_screenwidth()  # Width of the screen
        screen_height = exporting.winfo_screenheight() # Height of the screen
        x = (screen_width/2) - (100/2)
        y = (screen_height/2) - (20/2)
        
        exporting.geometry('%dx%d+%d+%d' % (200, 50, x, y))
        exporting.resizable(False,False)
        exporting.title("Exporting")
        exporting.iconbitmap('src/img/logo.ico')
        exporting.protocol("WM_DELETE_WINDOW", self.disable_event)
        
        pb = ttk.Progressbar(exporting, orient= HORIZONTAL, mode= 'indeterminate')
        pb.pack(anchor="c",padx=20,pady=20)
        exporting.after(0,lambda:self.change(pb,exporting))
            

        if self.clicked.get() == "ledger":
            self.export_ledger()
        elif self.clicked.get() == "stockitem":
            self.export_stock()
        elif self.clicked.get() == "groups":
            self.export_group()
        
        else:
            messagebox.showerror("Error", "Can't export this table as XML.")
        exporting.destroy()

    def check(self, val):
        if val == None or val == 'None':
            return " "
        if type(val) == str:
            return val.replace('&', '&amp;')
        return val

    def date(self, str):
        return str.replace("-", "")

    def check_group(self,area):
        if area == "Area" :
            return 'Suspense A/c'
        else:
            return area


    def export_group(self):
        master_start = open("src/xml_scripts/master_start.xml", "r", encoding="utf-8")
        master_end = open("src/xml_scripts/master_end.xml","r", encoding="utf-8")

       
        master_xml = open(self.f, "w",encoding="utf-8")
        for line in master_start:
            master_xml.write(line)
        try:
            #db connection
            con = sqlite3.connect(self.db)
            cur = con.cursor()
        except  Error as e:
            messagebox.showerror("Error",e)

        group =  cur.execute("SELECT DISTINCT Ledger_Group FROM ledger;").fetchall()
        
        count = 170
        con.close()
        for area in group:
            if area[0]!="Suspense A/c":
                master_xml.write('    <TALLYMESSAGE xmlns:UDF="TallyUDF">\n')
                master_xml.write('      <GROUP NAME="'+ area[0]+'" RESERVEDNAME= "">' + "\n")
                master_xml.write('      <GUID>'+str(uuid.uuid4())+'</GUID>' + "\n")
                master_xml.write('      <PARENT>Sundry Debtors</PARENT>' + "\n")
                master_xml.write('      <BASICGROUPISCALCULABLE>No</BASICGROUPISCALCULABLE>' + "\n")
                master_xml.write('      <ADDLALLOCTYPE/>' + "\n")
                master_xml.write('      <GRPDEBITPARENT/>' + "\n")
                master_xml.write('      <GRPCREDITPARENT/>' + "\n")
                master_xml.write('      <ISBILLWISEON>Yes</ISBILLWISEON>' + "\n")
                master_xml.write('      <ISCOSTCENTRESON>No</ISCOSTCENTRESON>' + "\n")
                master_xml.write('      <ISADDABLE>No</ISADDABLE>' + "\n")
                master_xml.write('      <ISUPDATINGTARGETID>No</ISUPDATINGTARGETID>' + "\n")
                master_xml.write('      <ISDELETED>No</ISDELETED>' + "\n")
                master_xml.write('      <ISSECURITYONWHENENTERED>No</ISSECURITYONWHENENTERED>' + "\n")
                master_xml.write('      <ASORIGINAL>Yes</ASORIGINAL>' + "\n")
                master_xml.write('      <ISSUBLEDGER>No</ISSUBLEDGER>' + "\n")
                master_xml.write('      <ISREVENUE>No</ISREVENUE>' + "\n")
                master_xml.write('      <AFFECTSGROSSPROFIT>No</AFFECTSGROSSPROFIT>' + "\n")
                master_xml.write('      <ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>' + "\n")
                master_xml.write('      <TRACKNEGATIVEBALANCES>Yes</TRACKNEGATIVEBALANCES>' + "\n")
                master_xml.write('      <ISCONDENSED>No</ISCONDENSED>' + "\n")
                master_xml.write('      <AFFECTSSTOCK>No</AFFECTSSTOCK>' + "\n")
                master_xml.write('      <ISGROUPFORLOANRCPT>No</ISGROUPFORLOANRCPT>' + "\n")
                master_xml.write('      <ISGROUPFORLOANPYMNT>No</ISGROUPFORLOANPYMNT>' + "\n")
                master_xml.write('      <ISRATEINCLUSIVEVAT>No</ISRATEINCLUSIVEVAT>' + "\n")
                master_xml.write('      <ISINVDETAILSENABLE>No</ISINVDETAILSENABLE>' + "\n")
                master_xml.write('      <SORTPOSITION> 500</SORTPOSITION>' + "\n")
                master_xml.write(f'      <ALTERID> {count}</ALTERID>' + "\n")
                master_xml.write('      <SERVICETAXDETAILS.LIST>      </SERVICETAXDETAILS.LIST>' + "\n")
                master_xml.write('      <VATDETAILS.LIST>      </VATDETAILS.LIST>' + "\n")
                master_xml.write('      <SALESTAXCESSDETAILS.LIST>      </SALESTAXCESSDETAILS.LIST>' + "\n")
                master_xml.write('      <GSTDETAILS.LIST>      </GSTDETAILS.LIST>' + "\n")
                master_xml.write('      <LANGUAGENAME.LIST>' + "\n")
                master_xml.write('       <NAME.LIST TYPE="String">' + "\n")
                master_xml.write('        <NAME>'+ area[0] +'</NAME>' + "\n")
                master_xml.write('        <NAME>'+ area[0][4:] +'</NAME>' + "\n")
                master_xml.write('       </NAME.LIST>' + "\n")
                master_xml.write('       <LANGUAGEID> 1033</LANGUAGEID>' + "\n")
                master_xml.write('      </LANGUAGENAME.LIST>' + "\n")
                master_xml.write('      <XBRLDETAIL.LIST>      </XBRLDETAIL.LIST>' + "\n")
                master_xml.write('      <AUDITDETAILS.LIST>      </AUDITDETAILS.LIST>' + "\n")
                master_xml.write('      <SCHVIDETAILS.LIST>      </SCHVIDETAILS.LIST>' + "\n")
                master_xml.write('      <EXCISETARIFFDETAILS.LIST>      </EXCISETARIFFDETAILS.LIST>' + "\n")
                master_xml.write('      <TCSCATEGORYDETAILS.LIST>      </TCSCATEGORYDETAILS.LIST>' + "\n")
                master_xml.write('      <TDSCATEGORYDETAILS.LIST>      </TDSCATEGORYDETAILS.LIST>' + "\n")
                master_xml.write('      <GSTCLASSFNIGSTRATES.LIST>      </GSTCLASSFNIGSTRATES.LIST>' + "\n")
                master_xml.write('      <EXTARIFFDUTYHEADDETAILS.LIST>      </EXTARIFFDUTYHEADDETAILS.LIST>' + "\n")
                master_xml.write('     </GROUP>' + "\n")
                master_xml.write('    </TALLYMESSAGE>' + "\n")
                count += 2
        

    def export_ledger(self):
        master_start = open("src/xml_scripts/master_start.xml", "r", encoding="utf-8")
        master_end = open("src/xml_scripts/master_end.xml","r", encoding="utf-8")

       
        master_xml = open(self.f, "w",encoding="utf-8")
        for line in master_start:
            master_xml.write(line)
        try:
            #db connection
            con = sqlite3.connect(self.db)
            cur = con.cursor()
        except  Error as e:
            messagebox.showerror("Error",e)

        result = cur.execute("SELECT * FROM ledger;").fetchall()
        group =  cur.execute("SELECT DISTINCT Ledger_Group FROM ledger;").fetchall()
        
        count = 170
        con.close()
        for area in group:
            if area[0]!="Area":
                master_xml.write('    <TALLYMESSAGE xmlns:UDF="TallyUDF">\n')
                master_xml.write('      <GROUP NAME="'+ area[0]+'" RESERVEDNAME= "">' + "\n")
                master_xml.write('      <GUID>'+str(uuid.uuid4())+'</GUID>' + "\n")
                master_xml.write('      <PARENT>Sundry Debtors</PARENT>' + "\n")
                master_xml.write('      <BASICGROUPISCALCULABLE>No</BASICGROUPISCALCULABLE>' + "\n")
                master_xml.write('      <ADDLALLOCTYPE/>' + "\n")
                master_xml.write('      <GRPDEBITPARENT/>' + "\n")
                master_xml.write('      <GRPCREDITPARENT/>' + "\n")
                master_xml.write('      <ISBILLWISEON>Yes</ISBILLWISEON>' + "\n")
                master_xml.write('      <ISCOSTCENTRESON>No</ISCOSTCENTRESON>' + "\n")
                master_xml.write('      <ISADDABLE>No</ISADDABLE>' + "\n")
                master_xml.write('      <ISUPDATINGTARGETID>No</ISUPDATINGTARGETID>' + "\n")
                master_xml.write('      <ISDELETED>No</ISDELETED>' + "\n")
                master_xml.write('      <ISSECURITYONWHENENTERED>No</ISSECURITYONWHENENTERED>' + "\n")
                master_xml.write('      <ASORIGINAL>Yes</ASORIGINAL>' + "\n")
                master_xml.write('      <ISSUBLEDGER>No</ISSUBLEDGER>' + "\n")
                master_xml.write('      <ISREVENUE>No</ISREVENUE>' + "\n")
                master_xml.write('      <AFFECTSGROSSPROFIT>No</AFFECTSGROSSPROFIT>' + "\n")
                master_xml.write('      <ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>' + "\n")
                master_xml.write('      <TRACKNEGATIVEBALANCES>Yes</TRACKNEGATIVEBALANCES>' + "\n")
                master_xml.write('      <ISCONDENSED>No</ISCONDENSED>' + "\n")
                master_xml.write('      <AFFECTSSTOCK>No</AFFECTSSTOCK>' + "\n")
                master_xml.write('      <ISGROUPFORLOANRCPT>No</ISGROUPFORLOANRCPT>' + "\n")
                master_xml.write('      <ISGROUPFORLOANPYMNT>No</ISGROUPFORLOANPYMNT>' + "\n")
                master_xml.write('      <ISRATEINCLUSIVEVAT>No</ISRATEINCLUSIVEVAT>' + "\n")
                master_xml.write('      <ISINVDETAILSENABLE>No</ISINVDETAILSENABLE>' + "\n")
                master_xml.write('      <SORTPOSITION> 500</SORTPOSITION>' + "\n")
                master_xml.write(f'      <ALTERID> {count}</ALTERID>' + "\n")
                master_xml.write('      <SERVICETAXDETAILS.LIST>      </SERVICETAXDETAILS.LIST>' + "\n")
                master_xml.write('      <VATDETAILS.LIST>      </VATDETAILS.LIST>' + "\n")
                master_xml.write('      <SALESTAXCESSDETAILS.LIST>      </SALESTAXCESSDETAILS.LIST>' + "\n")
                master_xml.write('      <GSTDETAILS.LIST>      </GSTDETAILS.LIST>' + "\n")
                master_xml.write('      <LANGUAGENAME.LIST>' + "\n")
                master_xml.write('       <NAME.LIST TYPE="String">' + "\n")
                master_xml.write('        <NAME>'+ area[0] +'</NAME>' + "\n")
                master_xml.write('        <NAME>'+ area[0][4:] +'</NAME>' + "\n")
                master_xml.write('       </NAME.LIST>' + "\n")
                master_xml.write('       <LANGUAGEID> 1033</LANGUAGEID>' + "\n")
                master_xml.write('      </LANGUAGENAME.LIST>' + "\n")
                master_xml.write('      <XBRLDETAIL.LIST>      </XBRLDETAIL.LIST>' + "\n")
                master_xml.write('      <AUDITDETAILS.LIST>      </AUDITDETAILS.LIST>' + "\n")
                master_xml.write('      <SCHVIDETAILS.LIST>      </SCHVIDETAILS.LIST>' + "\n")
                master_xml.write('      <EXCISETARIFFDETAILS.LIST>      </EXCISETARIFFDETAILS.LIST>' + "\n")
                master_xml.write('      <TCSCATEGORYDETAILS.LIST>      </TCSCATEGORYDETAILS.LIST>' + "\n")
                master_xml.write('      <TDSCATEGORYDETAILS.LIST>      </TDSCATEGORYDETAILS.LIST>' + "\n")
                master_xml.write('      <GSTCLASSFNIGSTRATES.LIST>      </GSTCLASSFNIGSTRATES.LIST>' + "\n")
                master_xml.write('      <EXTARIFFDUTYHEADDETAILS.LIST>      </EXTARIFFDUTYHEADDETAILS.LIST>' + "\n")
                master_xml.write('     </GROUP>' + "\n")
                master_xml.write('    </TALLYMESSAGE>' + "\n")
                count += 2
            for line in master_end:
                master_xml.write(line)

        master_start.close()
        master_end.close()

        

        
        for res in result:
            master_xml.write('    <TALLYMESSAGE xmlns:UDF="TallyUDF">\n')
            master_xml.write('     <LEDGER NAME= "' + self.check(res[1]) + '" RESERVEDNAME= "" >\n')
            master_xml.write('     <ADDRESS.LIST TYPE="String">' + "\n")
            master_xml.write("     <ADDRESS> " + self.check(res[7])  + " </ADDRESS> " + "\n")
            master_xml.write("     <ADDRESS> " + self.check(res[8])  + " </ADDRESS> " + "\n")
            master_xml.write("     <ADDRESS> " + self.check(res[9])  + " </ADDRESS> " + "\n")
            master_xml.write("     </ADDRESS.LIST> " + "\n")
            master_xml.write('     <MAILINGNAME.LIST TYPE="String"> ' + "\n")
            master_xml.write("     <MAILINGNAME> " + self.check(res[1])  + " </MAILINGNAME> " + "\n")
            master_xml.write("     </MAILINGNAME.LIST> " + "\n")
            master_xml.write('     <OLDAUDITENTRYIDS.LIST TYPE="Number"> ' + "\n")
            master_xml.write("     <OLDAUDITENTRYIDS>-1</OLDAUDITENTRYIDS> " + "\n")
            master_xml.write("     </OLDAUDITENTRYIDS.LIST> " + "\n")
            master_xml.write("     <GUID> " + str(uuid.uuid4()) + "</GUID> " + "\n")
            master_xml.write("     <CURRENCYNAME>₹</CURRENCYNAME> " + "\n")
            master_xml.write("     <EMAIL> " + self.check(res[15])  + " </EMAIL> " + "\n")
            master_xml.write("     <PRIORSTATENAME> " + self.check(res[11])  + " </PRIORSTATENAME> " + "\n")
            master_xml.write("     <PINCODE> " + self.check(res[12])  + " </PINCODE> " + "\n")
            master_xml.write("     <INCOMETAXNUMBER> " + self.check(res[17])  + " </INCOMETAXNUMBER> " + "\n")
            master_xml.write("     <COUNTRYNAME> " + self.check(res[10])  + " </COUNTRYNAME> " + "\n")
            master_xml.write("     <GSTREGISTRATIONTYPE> " + self.check(res[18])  + " </GSTREGISTRATIONTYPE> " + "\n")
            master_xml.write("     <VATDEALERTYPE>Regular</VATDEALERTYPE> " + "\n")
            master_xml.write(f"     <PARENT>  {self.check_group(res[2])}   </PARENT> " + "\n")
            #master_xml.write("     <PARENT> Area50 </PARENT> " + "\n")
            master_xml.write("     <TAXCLASSIFICATIONNAME/> " + "\n")
            master_xml.write("     <TAXTYPE> " + self.check(res[4])  + " </TAXTYPE> " + "\n")
            master_xml.write("     <BILLCREDITPERIOD> " + self.check(res[5])  + " </BILLCREDITPERIOD> " + "\n")
            master_xml.write("     <COUNTRYOFRESIDENCE> " + self.check(res[10])  + " </COUNTRYOFRESIDENCE> " + "\n")
            master_xml.write("     <LEDADDLALLOCTYPE/> " + "\n")
            master_xml.write("     <LEDGERPHONE> " + self.check(res[25])  + " </LEDGERPHONE> " + "\n")
            master_xml.write("     <LEDGERCONTACT> " + self.check(res[13])  + " </LEDGERCONTACT> " + "\n")
            master_xml.write("     <LEDGERMOBILE> " + self.check(res[14])  + " </LEDGERMOBILE> " + "\n")
            master_xml.write("     <GSTTYPE/> " + "\n")
            master_xml.write("     <APPROPRIATEFOR/> " + "\n")
            master_xml.write("     <PARTYGSTIN> " + self.check(res[19])  + " </PARTYGSTIN> " + "\n")
            master_xml.write("     <GSTTYPEOFSUPPLY>Services</GSTTYPEOFSUPPLY> " + "\n")
            master_xml.write("     <LEDSTATENAME> " + self.check(res[11])  + " </LEDSTATENAME> " + "\n")
            master_xml.write("     <SERVICECATEGORY>&#4; Not Applicable</SERVICECATEGORY> " + "\n")
            master_xml.write("     <EXCISELEDGERCLASSIFICATION/> " + "\n")
            master_xml.write("     <EXCISEDUTYTYPE/> " + "\n")
            master_xml.write("     <EXCISENATUREOFPURCHASE/> " + "\n")
            master_xml.write("     <LEDGERFBTCATEGORY/> " + "\n")
            master_xml.write("     <ISBILLWISEON> " + self.check(res[6])  + " </ISBILLWISEON> " + "\n")
            master_xml.write("     <ISCOSTCENTRESON>No</ISCOSTCENTRESON> " + "\n")
            master_xml.write("     <ISINTERESTON>No</ISINTERESTON> " + "\n")
            master_xml.write("     <ALLOWINMOBILE>No</ALLOWINMOBILE> " + "\n")
            master_xml.write("     <ISCOSTTRACKINGON>No</ISCOSTTRACKINGON> " + "\n")
            master_xml.write("     <ISBENEFICIARYCODEON>No</ISBENEFICIARYCODEON> " + "\n")
            master_xml.write("     <ISEXPORTONVCHCREATE>No</ISEXPORTONVCHCREATE> " + "\n")
            master_xml.write("     <PLASINCOMEEXPENSE>No</PLASINCOMEEXPENSE> " + "\n")
            master_xml.write("     <ISUPDATINGTARGETID>No</ISUPDATINGTARGETID> " + "\n")
            master_xml.write("     <ISDELETED>No</ISDELETED> " + "\n")
            master_xml.write("     <ISSECURITYONWHENENTERED>No</ISSECURITYONWHENENTERED> " + "\n")
            master_xml.write("     <ASORIGINAL>Yes</ASORIGINAL> " + "\n")
            master_xml.write("     <ISCONDENSED>No</ISCONDENSED> " + "\n")
            master_xml.write("     <AFFECTSSTOCK>No</AFFECTSSTOCK> " + "\n")
            master_xml.write("     <ISRATEINCLUSIVEVAT>No</ISRATEINCLUSIVEVAT> " + "\n")
            master_xml.write("     <FORPAYROLL>No</FORPAYROLL> " + "\n")
            master_xml.write("     <ISABCENABLED>No</ISABCENABLED> " + "\n")
            master_xml.write("     <ISCREDITDAYSCHKON>No</ISCREDITDAYSCHKON> " + "\n")
            master_xml.write("     <INTERESTONBILLWISE>No</INTERESTONBILLWISE> " + "\n")
            master_xml.write("     <OVERRIDEINTEREST>No</OVERRIDEINTEREST> " + "\n")
            master_xml.write("     <OVERRIDEADVINTEREST>No</OVERRIDEADVINTEREST> " + "\n")
            master_xml.write("     <USEFORVAT>No</USEFORVAT> " + "\n")
            master_xml.write("     <IGNORETDSEXEMPT>No</IGNORETDSEXEMPT> " + "\n")
            master_xml.write("     <ISTCSAPPLICABLE>No</ISTCSAPPLICABLE> " + "\n")
            master_xml.write("     <ISTDSAPPLICABLE>No</ISTDSAPPLICABLE> " + "\n")
            master_xml.write("     <ISFBTAPPLICABLE>No</ISFBTAPPLICABLE> " + "\n")
            master_xml.write("     <ISGSTAPPLICABLE>No</ISGSTAPPLICABLE> " + "\n")
            master_xml.write("     <ISEXCISEAPPLICABLE>No</ISEXCISEAPPLICABLE> " + "\n")
            master_xml.write("     <ISTDSEXPENSE>No</ISTDSEXPENSE> " + "\n")
            master_xml.write("     <ISEDLIAPPLICABLE>No</ISEDLIAPPLICABLE> " + "\n")
            master_xml.write("     <ISRELATEDPARTY>No</ISRELATEDPARTY> " + "\n")
            master_xml.write("     <USEFORESIELIGIBILITY>No</USEFORESIELIGIBILITY> " + "\n")
            master_xml.write("     <ISINTERESTINCLLASTDAY>No</ISINTERESTINCLLASTDAY> " + "\n")
            master_xml.write("     <APPROPRIATETAXVALUE>No</APPROPRIATETAXVALUE> " + "\n")
            master_xml.write("     <ISBEHAVEASDUTY>No</ISBEHAVEASDUTY> " + "\n")
            master_xml.write("     <INTERESTINCLDAYOFADDITION>No</INTERESTINCLDAYOFADDITION> " + "\n")
            master_xml.write("     <INTERESTINCLDAYOFDEDUCTION>No</INTERESTINCLDAYOFDEDUCTION> " + "\n")
            master_xml.write("     <ISOTHTERRITORYASSESSEE>No</ISOTHTERRITORYASSESSEE> " + "\n")
            master_xml.write("     <IGNOREMISMATCHWITHWARNING>No</IGNOREMISMATCHWITHWARNING> " + "\n")
            master_xml.write("     <USEASNOTIONALBANK>No</USEASNOTIONALBANK> " + "\n")
            master_xml.write("     <OVERRIDECREDITLIMIT>No</OVERRIDECREDITLIMIT> " + "\n")
            master_xml.write("     <ISAGAINSTFORMC>No</ISAGAINSTFORMC> " + "\n")
            master_xml.write("     <ISCHEQUEPRINTINGENABLED>Yes</ISCHEQUEPRINTINGENABLED> " + "\n")
            master_xml.write("     <ISPAYUPLOAD>No</ISPAYUPLOAD> " + "\n")
            master_xml.write("     <ISPAYBATCHONLYSAL>No</ISPAYBATCHONLYSAL> " + "\n")
            master_xml.write("     <ISBNFCODESUPPORTED>No</ISBNFCODESUPPORTED> " + "\n")
            master_xml.write("""      <ALLOWEXPORTWITHERRORS>No</ALLOWEXPORTWITHERRORS>           \n""")
            master_xml.write("""      <CONSIDERPURCHASEFOREXPORT>No</CONSIDERPURCHASEFOREXPORT>\n""")
            master_xml.write("""      <ISTRANSPORTER>No</ISTRANSPORTER>\n""")
            master_xml.write("""      <USEFORNOTIONALITC>No</USEFORNOTIONALITC>\n""")
            master_xml.write("""      <ISECOMMOPERATOR>No</ISECOMMOPERATOR>\n""")
            master_xml.write("""      <OVERRIDEBASEDONREALIZATION>No</OVERRIDEBASEDONREALIZATION>\n""")
            master_xml.write("""      <SHOWINPAYSLIP>No</SHOWINPAYSLIP>\n""")
            master_xml.write("""      <USEFORGRATUITY>No</USEFORGRATUITY>\n""")
            master_xml.write("""      <ISTDSPROJECTED>No</ISTDSPROJECTED>\n""")
            master_xml.write("""      <FORSERVICETAX>No</FORSERVICETAX>\n""")
            master_xml.write("""      <ISINPUTCREDIT>No</ISINPUTCREDIT>\n""")
            master_xml.write("""      <ISEXEMPTED>No</ISEXEMPTED>\n""")
            master_xml.write("""      <ISABATEMENTAPPLICABLE>No</ISABATEMENTAPPLICABLE>\n""")
            master_xml.write("""      <ISSTXPARTY>No</ISSTXPARTY>\n""")
            master_xml.write("""      <ISSTXNONREALIZEDTYPE>No</ISSTXNONREALIZEDTYPE>\n""")
            master_xml.write("""      <ISUSEDFORCVD>No</ISUSEDFORCVD>\n""")
            master_xml.write("""      <LEDBELONGSTONONTAXABLE>No</LEDBELONGSTONONTAXABLE>\n""")
            master_xml.write("""      <ISEXCISEMERCHANTEXPORTER>No</ISEXCISEMERCHANTEXPORTER>\n""")
            master_xml.write("""      <ISPARTYEXEMPTED>No</ISPARTYEXEMPTED>\n""")
            master_xml.write("""      <ISSEZPARTY>No</ISSEZPARTY>\n""")
            master_xml.write("""      <TDSDEDUCTEEISSPECIALRATE>No</TDSDEDUCTEEISSPECIALRATE>\n""")
            master_xml.write("""      <ISECHEQUESUPPORTED>No</ISECHEQUESUPPORTED>\n""")
            master_xml.write("""      <ISEDDSUPPORTED>No</ISEDDSUPPORTED>\n""")
            master_xml.write("""      <HASECHEQUEDELIVERYMODE>No</HASECHEQUEDELIVERYMODE>\n""")
            master_xml.write("""      <HASECHEQUEDELIVERYTO>No</HASECHEQUEDELIVERYTO>\n""")
            master_xml.write("""      <HASECHEQUEPRINTLOCATION>No</HASECHEQUEPRINTLOCATION>\n""")
            master_xml.write("""      <HASECHEQUEPAYABLELOCATION>No</HASECHEQUEPAYABLELOCATION>\n""")
            master_xml.write("""      <HASECHEQUEBANKLOCATION>No</HASECHEQUEBANKLOCATION>\n""")
            master_xml.write("""      <HASEDDDELIVERYMODE>No</HASEDDDELIVERYMODE>\n""")
            master_xml.write("""      <HASEDDDELIVERYTO>No</HASEDDDELIVERYTO>\n""")
            master_xml.write("""      <HASEDDPRINTLOCATION>No</HASEDDPRINTLOCATION>\n""")
            master_xml.write("""      <HASEDDPAYABLELOCATION>No</HASEDDPAYABLELOCATION>\n""")
            master_xml.write("""      <HASEDDBANKLOCATION>No</HASEDDBANKLOCATION>\n""")
            master_xml.write("""      <ISEBANKINGENABLED>No</ISEBANKINGENABLED>\n""")
            master_xml.write("""      <ISEXPORTFILEENCRYPTED>No</ISEXPORTFILEENCRYPTED>\n""")
            master_xml.write("""      <ISBATCHENABLED>No</ISBATCHENABLED>\n""")
            master_xml.write("""     <ISPRODUCTCODEBASED>No</ISPRODUCTCODEBASED>\n""")
            master_xml.write("""      <HASEDDCITY>No</HASEDDCITY>\n""")
            master_xml.write("""      <HASECHEQUECITY>No</HASECHEQUECITY>\n""")
            master_xml.write("""      <ISFILENAMEFORMATSUPPORTED>No</ISFILENAMEFORMATSUPPORTED>\n""")
            master_xml.write("""      <HASCLIENTCODE>No</HASCLIENTCODE>\n""")
            master_xml.write("""      <PAYINSISBATCHAPPLICABLE>No</PAYINSISBATCHAPPLICABLE>\n""")
            master_xml.write("""      <PAYINSISFILENUMAPP>No</PAYINSISFILENUMAPP>\n""")
            master_xml.write("""      <ISSALARYTRANSGROUPEDFORBRS>No</ISSALARYTRANSGROUPEDFORBRS>\n""")
            master_xml.write("""      <ISEBANKINGSUPPORTED>No</ISEBANKINGSUPPORTED>\n""")
            master_xml.write("""      <ISSCBUAE>No</ISSCBUAE>\n""")
            master_xml.write("""      <ISBANKSTATUSAPP>No</ISBANKSTATUSAPP>\n""")
            master_xml.write("""      <ISSALARYGROUPED>No</ISSALARYGROUPED>\n""")
            master_xml.write("""      <USEFORPURCHASETAX>No</USEFORPURCHASETAX>\n""")
            master_xml.write("""      <AUDITED>No</AUDITED>\n""")
            master_xml.write("""      <SORTPOSITION> 1000</SORTPOSITION>\n""")
            master_xml.write("""      <ALTERID> 172</ALTERID>\n""")
            master_xml.write("""     <SERVICETAXDETAILS.LIST>      </SERVICETAXDETAILS.LIST>\n""")
            master_xml.write("""     <LBTREGNDETAILS.LIST>      </LBTREGNDETAILS.LIST>\n""")
            master_xml.write("""      <VATDETAILS.LIST>      </VATDETAILS.LIST>\n""")
            master_xml.write("""      <SALESTAXCESSDETAILS.LIST>      </SALESTAXCESSDETAILS.LIST>\n""")
            master_xml.write("""      <GSTDETAILS.LIST>      </GSTDETAILS.LIST>\n""")
            master_xml.write("""      <LANGUAGENAME.LIST>\n""")
            master_xml.write('          <NAME.LIST TYPE="String">\n          <NAME> ' + self.check(res[1])  + '</NAME>\n')
            master_xml.write("""        </NAME.LIST>\n        <LANGUAGEID> 1033</LANGUAGEID>\n""")
            master_xml.write("""      </LANGUAGENAME.LIST>\n""")
            master_xml.write("""      <XBRLDETAIL.LIST>      </XBRLDETAIL.LIST>\n""")
            master_xml.write("""      <AUDITDETAILS.LIST>      </AUDITDETAILS.LIST>\n""")
            master_xml.write("""      <SCHVIDETAILS.LIST>      </SCHVIDETAILS.LIST>\n""")
            master_xml.write("""      <EXCISETARIFFDETAILS.LIST>      </EXCISETARIFFDETAILS.LIST>\n""")
            master_xml.write("""      <TCSCATEGORYDETAILS.LIST>      </TCSCATEGORYDETAILS.LIST>\n""")
            master_xml.write("""      <TDSCATEGORYDETAILS.LIST>      </TDSCATEGORYDETAILS.LIST>\n""")
            master_xml.write("""      <SLABPERIOD.LIST>      </SLABPERIOD.LIST>\n""")
            master_xml.write("""      <GRATUITYPERIOD.LIST>      </GRATUITYPERIOD.LIST>\n""")
            master_xml.write("""      <ADDITIONALCOMPUTATIONS.LIST>      </ADDITIONALCOMPUTATIONS.LIST>\n""")
            master_xml.write("""      <EXCISEJURISDICTIONDETAILS.LIST>      </EXCISEJURISDICTIONDETAILS.LIST>\n""")
            master_xml.write("""      <EXCLUDEDTAXATIONS.LIST>      </EXCLUDEDTAXATIONS.LIST>\n""")
            master_xml.write("""      <BANKALLOCATIONS.LIST>      </BANKALLOCATIONS.LIST>\n""")
            master_xml.write("""      <PAYMENTDETAILS.LIST>      </PAYMENTDETAILS.LIST>\n""")
            master_xml.write("""      <BANKEXPORTFORMATS.LIST>      </BANKEXPORTFORMATS.LIST>\n""")
            master_xml.write("""      <BILLALLOCATIONS.LIST>      </BILLALLOCATIONS.LIST>\n""")
            master_xml.write("""      <INTERESTCOLLECTION.LIST>      </INTERESTCOLLECTION.LIST>\n""")
            master_xml.write("""      <LEDGERCLOSINGVALUES.LIST>      </LEDGERCLOSINGVALUES.LIST>\n""")
            master_xml.write("""      <LEDGERAUDITCLASS.LIST>      </LEDGERAUDITCLASS.LIST>\n""")
            master_xml.write("""      <OLDAUDITENTRIES.LIST>      </OLDAUDITENTRIES.LIST>\n""")
            master_xml.write("""      <TDSEXEMPTIONRULES.LIST>      </TDSEXEMPTIONRULES.LIST>\n""")
            master_xml.write("""      <DEDUCTINSAMEVCHRULES.LIST>      </DEDUCTINSAMEVCHRULES.LIST>\n""")
            master_xml.write("""      <LOWERDEDUCTION.LIST>      </LOWERDEDUCTION.LIST>\n""")
            master_xml.write("""      <STXABATEMENTDETAILS.LIST>      </STXABATEMENTDETAILS.LIST>\n""")
            master_xml.write("""      <LEDMULTIADDRESSLIST.LIST>      </LEDMULTIADDRESSLIST.LIST>\n""")
            master_xml.write("""      <STXTAXDETAILS.LIST>      </STXTAXDETAILS.LIST>\n""")
            master_xml.write("""      <CHEQUERANGE.LIST>      </CHEQUERANGE.LIST>\n""")
            master_xml.write("""      <DEFAULTVCHCHEQUEDETAILS.LIST>      </DEFAULTVCHCHEQUEDETAILS.LIST>\n""")
            master_xml.write("""      <ACCOUNTAUDITENTRIES.LIST>      </ACCOUNTAUDITENTRIES.LIST>\n""")
            master_xml.write("""      <AUDITENTRIES.LIST>      </AUDITENTRIES.LIST>\n""")
            master_xml.write("""      <BRSIMPORTEDINFO.LIST>      </BRSIMPORTEDINFO.LIST>\n""")
            master_xml.write("""      <AUTOBRSCONFIGS.LIST>      </AUTOBRSCONFIGS.LIST>\n""")
            master_xml.write("""      <BANKURENTRIES.LIST>      </BANKURENTRIES.LIST>\n""")
            master_xml.write("""      <DEFAULTCHEQUEDETAILS.LIST>      </DEFAULTCHEQUEDETAILS.LIST>\n""")
            master_xml.write("""      <DEFAULTOPENINGCHEQUEDETAILS.LIST>      </DEFAULTOPENINGCHEQUEDETAILS.LIST>\n""")
            master_xml.write("""      <CANCELLEDPAYALLOCATIONS.LIST>      </CANCELLEDPAYALLOCATIONS.LIST>\n""")
            master_xml.write("""      <ECHEQUEPRINTLOCATION.LIST>      </ECHEQUEPRINTLOCATION.LIST>\n""")
            master_xml.write("""      <ECHEQUEPAYABLELOCATION.LIST>      </ECHEQUEPAYABLELOCATION.LIST>\n""")
            master_xml.write("""      <EDDPRINTLOCATION.LIST>      </EDDPRINTLOCATION.LIST>\n""")
            master_xml.write("""      <EDDPAYABLELOCATION.LIST>      </EDDPAYABLELOCATION.LIST>\n""")
            master_xml.write("""      <AVAILABLETRANSACTIONTYPES.LIST>      </AVAILABLETRANSACTIONTYPES.LIST>\n""")
            master_xml.write("""      <LEDPAYINSCONFIGS.LIST>      </LEDPAYINSCONFIGS.LIST>\n""")
            master_xml.write("""      <TYPECODEDETAILS.LIST>      </TYPECODEDETAILS.LIST>\n""")
            master_xml.write("""      <FIELDVALIDATIONDETAILS.LIST>      </FIELDVALIDATIONDETAILS.LIST>\n""")
            master_xml.write("""      <INPUTCRALLOCS.LIST>      </INPUTCRALLOCS.LIST>\n""")
            master_xml.write("""      <TCSMETHODOFCALCULATION.LIST>      </TCSMETHODOFCALCULATION.LIST>\n""")
            master_xml.write("""      <GSTCLASSFNIGSTRATES.LIST>      </GSTCLASSFNIGSTRATES.LIST>\n""")
            master_xml.write("""      <EXTARIFFDUTYHEADDETAILS.LIST>      </EXTARIFFDUTYHEADDETAILS.LIST>\n""")
            master_xml.write("""      <VOUCHERTYPEPRODUCTCODES.LIST>      </VOUCHERTYPEPRODUCTCODES.LIST>\n""")
            master_xml.write("""     </LEDGER>\n""")

        for line in master_end:
            master_xml.write(line)

        master_start.close()
        master_end.close()


    def taxability(self, val):
        if val == 'taxable':
            return 'Applicable'
        else:
            return 'Not Applicable'

    def export_stock(self):
        stock_start = open("src/xml_scripts/stock_start.xml", "r",encoding="utf-8")
        stock_end = open("src/xml_scripts/stock_end.xml", "r",encoding="utf-8")

        stock_xml  = open(self.f, "w",encoding="utf-8")

        for line in stock_start:
            stock_xml.write(line)
        try:
            #db connection
            con = sqlite3.connect(self.db)
            cur = con.cursor()
        except  Error as e:
            messagebox.showerror("Error",e)

        result = cur.execute("SELECT * FROM  stockitem;").fetchall()
        con.close()
        for res in result:
            stock_xml.write('    <TALLYMESSAGE xmlns:UDF="TallyUDF">\n')
            stock_xml.write('     <STOCKITEM NAME= "' + self.check(res[1]) + '" RESERVEDNAME= ''">' + "\n")
            stock_xml.write('      <OLDAUDITENTRYIDS.LIST TYPE="Number">' + "\n")
            stock_xml.write('       <OLDAUDITENTRYIDS>-1</OLDAUDITENTRYIDS>' + "\n")
            stock_xml.write('      </OLDAUDITENTRYIDS.LIST>' + "\n")
            stock_xml.write('      <GUID>' + str(uuid.uuid4()) + '</GUID>' + "\n")
            stock_xml.write('      <PARENT>Item Group</PARENT>' + "\n")
            stock_xml.write('      <CATEGORY/>' + "\n")
            stock_xml.write(f'      <GSTAPPLICABLE>&#4; { self.taxability(self.check(res[20])) }</GSTAPPLICABLE>' + "\n")
            stock_xml.write('      <TAXCLASSIFICATIONNAME/>' + "\n")
            stock_xml.write('      <GSTTYPEOFSUPPLY>Goods</GSTTYPEOFSUPPLY>' + "\n")
            stock_xml.write('      <EXCISEAPPLICABILITY>&#4; </EXCISEAPPLICABILITY>' + "\n")
            stock_xml.write('      <SALESTAXCESSAPPLICABLE/>' + "\n")
            stock_xml.write('      <VATAPPLICABLE>&#4; Applicable</VATAPPLICABLE>' + "\n")
            stock_xml.write('      <COSTINGMETHOD>Avg. Cost</COSTINGMETHOD>' + "\n")
            stock_xml.write('      <VALUATIONMETHOD>Avg. Price</VALUATIONMETHOD>' + "\n")
            stock_xml.write('      <BASEUNITS>' + self.check(res[6]) + '</BASEUNITS>' + "\n")
            stock_xml.write('      <ADDITIONALUNITS>' + self.check(res[9]) + '</ADDITIONALUNITS>\n')
            stock_xml.write('      <EXCISEITEMCLASSIFICATION/>' + "\n")
            stock_xml.write('      <VATBASEUNIT>pcs</VATBASEUNIT>' + "\n")
            stock_xml.write('      <ISCOSTCENTRESON>No</ISCOSTCENTRESON>' + "\n")
            stock_xml.write('      <ISBATCHWISEON>No</ISBATCHWISEON>' + "\n")
            stock_xml.write('      <ISPERISHABLEON>No</ISPERISHABLEON>' + "\n")
            stock_xml.write('      <ISENTRYTAXAPPLICABLE>No</ISENTRYTAXAPPLICABLE>' + "\n")
            stock_xml.write('      <ISCOSTTRACKINGON>No</ISCOSTTRACKINGON>' + "\n")
            stock_xml.write('      <ISUPDATINGTARGETID>No</ISUPDATINGTARGETID>' + "\n")
            stock_xml.write('      <ISDELETED>No</ISDELETED>' + "\n")
            stock_xml.write('      <ISSECURITYONWHENENTERED>No</ISSECURITYONWHENENTERED>' + "\n")
            stock_xml.write('      <ASORIGINAL>Yes</ASORIGINAL>' + "\n")
            stock_xml.write('      <ISRATEINCLUSIVEVAT>No</ISRATEINCLUSIVEVAT>' + "\n")
            stock_xml.write('      <IGNOREPHYSICALDIFFERENCE>No</IGNOREPHYSICALDIFFERENCE>' + "\n")
            stock_xml.write('      <IGNORENEGATIVESTOCK>No</IGNORENEGATIVESTOCK>' + "\n")
            stock_xml.write('      <TREATSALESASMANUFACTURED>No</TREATSALESASMANUFACTURED>' + "\n")
            stock_xml.write('      <TREATPURCHASESASCONSUMED>No</TREATPURCHASESASCONSUMED>' + "\n")
            stock_xml.write('      <TREATREJECTSASSCRAP>No</TREATREJECTSASSCRAP>' + "\n")
            stock_xml.write('      <HASMFGDATE>No</HASMFGDATE>' + "\n")
            stock_xml.write('      <ALLOWUSEOFEXPIREDITEMS>No</ALLOWUSEOFEXPIREDITEMS>' + "\n")
            stock_xml.write('      <IGNOREBATCHES>No</IGNOREBATCHES>' + "\n")
            stock_xml.write('      <IGNOREGODOWNS>No</IGNOREGODOWNS>' + "\n")
            stock_xml.write('      <ADJDIFFINFIRSTSALELEDGER>No</ADJDIFFINFIRSTSALELEDGER>' + "\n")
            stock_xml.write('      <ADJDIFFINFIRSTPURCLEDGER>No</ADJDIFFINFIRSTPURCLEDGER>' + "\n")
            stock_xml.write('      <CALCONMRP>No</CALCONMRP>' + "\n")
            stock_xml.write('      <EXCLUDEJRNLFORVALUATION>No</EXCLUDEJRNLFORVALUATION>' + "\n")
            stock_xml.write('      <ISMRPINCLOFTAX>No</ISMRPINCLOFTAX>' + "\n")
            stock_xml.write('      <ISADDLTAXEXEMPT>No</ISADDLTAXEXEMPT>' + "\n")
            stock_xml.write('      <ISSUPPLEMENTRYDUTYON>No</ISSUPPLEMENTRYDUTYON>' + "\n")
            stock_xml.write('      <GVATISEXCISEAPPL>No</GVATISEXCISEAPPL>' + "\n")
            stock_xml.write('      <REORDERASHIGHER>No</REORDERASHIGHER>' + "\n")
            stock_xml.write('      <MINORDERASHIGHER>No</MINORDERASHIGHER>' + "\n")
            stock_xml.write('      <ISEXCISECALCULATEONMRP>No</ISEXCISECALCULATEONMRP>' + "\n")
            stock_xml.write('      <INCLUSIVETAX>No</INCLUSIVETAX>' + "\n")
            stock_xml.write('      <GSTCALCSLABONMRP>No</GSTCALCSLABONMRP>' + "\n")
            stock_xml.write('      <MODIFYMRPRATE>No</MODIFYMRPRATE>' + "\n")
            stock_xml.write('      <ALTERID> 169</ALTERID>' + "\n")                                      #check later
            stock_xml.write(f'      <DENOMINATOR> { self.check(res[13])} </DENOMINATOR>' + "\n")
            stock_xml.write(f'      <CONVERSION> { self.check(res[12])} </CONVERSION>' + "\n")
            # stock_xml.write(f'      <BASICRATEOFEXCISE> 10 </BASICRATEOFEXCISE>'+ "\n")
            stock_xml.write('      <RATEOFVAT>0</RATEOFVAT>' + "\n")
            stock_xml.write('      <VATBASENO> 1</VATBASENO>' + "\n")
            stock_xml.write('      <VATTRAILNO> 1</VATTRAILNO>' + "\n")
            stock_xml.write('      <VATACTUALRATIO> 1</VATACTUALRATIO>' + "\n")
            # stock_xml.write(f'      <OPENINGBALANCE>{ 5 pcs =  1 bag}</OPENINGBALANCE>'+ "\n")
            # stock_xml.write(f'      <OPENINGVALUE>{-235.00}</OPENINGVALUE>'+ "\n")
            # stock_xml.write(f'      <OPENINGRATE>{47.00/pcs}</OPENINGRATE>'+ "\n")
            stock_xml.write('      <SERVICETAXDETAILS.LIST>      </SERVICETAXDETAILS.LIST>' + "\n")
            stock_xml.write('      <VATDETAILS.LIST>      </VATDETAILS.LIST>' + "\n")
            stock_xml.write('      <SALESTAXCESSDETAILS.LIST>      </SALESTAXCESSDETAILS.LIST>' + "\n")
            stock_xml.write('      <GSTDETAILS.LIST>      </GSTDETAILS.LIST>' + "\n")
            stock_xml.write('      <LANGUAGENAME.LIST>' + "\n")
            stock_xml.write('       <NAME.LIST TYPE="String">' + "\n")
            stock_xml.write('        <NAME>' + self.check(res[1]) + '</NAME>' + "\n")
            stock_xml.write('       </NAME.LIST>' + "\n")
            stock_xml.write('       <LANGUAGEID> 1033</LANGUAGEID>' + "\n")
            stock_xml.write('      </LANGUAGENAME.LIST>' + "\n")
            stock_xml.write('      <SCHVIDETAILS.LIST>      </SCHVIDETAILS.LIST>' + "\n")
            stock_xml.write('      <EXCISETARIFFDETAILS.LIST>      </EXCISETARIFFDETAILS.LIST>' + "\n")
            stock_xml.write('      <TCSCATEGORYDETAILS.LIST>      </TCSCATEGORYDETAILS.LIST>' + "\n")
            stock_xml.write('      <TDSCATEGORYDETAILS.LIST>      </TDSCATEGORYDETAILS.LIST>' + "\n")
            stock_xml.write('      <EXCLUDEDTAXATIONS.LIST>      </EXCLUDEDTAXATIONS.LIST>' + "\n")
            stock_xml.write('      <OLDAUDITENTRIES.LIST>      </OLDAUDITENTRIES.LIST>' + "\n")
            stock_xml.write('      <ACCOUNTAUDITENTRIES.LIST>      </ACCOUNTAUDITENTRIES.LIST>' + "\n")
            stock_xml.write('      <AUDITENTRIES.LIST>      </AUDITENTRIES.LIST>' + "\n")
            stock_xml.write('      <MRPDETAILS.LIST>' + "\n")
            stock_xml.write('       <FROMDATE>' + self.date(self.check(res[19])) + '</FROMDATE>' + "\n")
            stock_xml.write('       <MRPRATEDETAILS.LIST>' + "\n")
            stock_xml.write('       <STATENAME>&#4; Any</STATENAME>' + "\n")
            stock_xml.write(f'       <MRPRATE>{ self.check(res[18])} </MRPRATE>' + "\n")
            stock_xml.write('           </MRPRATEDETAILS.LIST>' + "\n")
            stock_xml.write('      </MRPDETAILS.LIST>' + "\n")
            stock_xml.write('      <VATCLASSIFICATIONDETAILS.LIST>      </VATCLASSIFICATIONDETAILS.LIST>' + "\n")
            stock_xml.write('      <COMPONENTLIST.LIST>      </COMPONENTLIST.LIST>' + "\n")
            stock_xml.write('      <ADDITIONALLEDGERS.LIST>      </ADDITIONALLEDGERS.LIST>' + "\n")
            stock_xml.write('      <SALESLIST.LIST>      </SALESLIST.LIST>' + "\n")
            stock_xml.write('      <PURCHASELIST.LIST>      </PURCHASELIST.LIST>' + "\n")
            stock_xml.write('      <FULLPRICELIST.LIST>      </FULLPRICELIST.LIST>' + "\n")
            stock_xml.write('      <BATCHALLOCATIONS.LIST>      </BATCHALLOCATIONS.LIST>' + "\n")
            stock_xml.write('      <TRADEREXCISEDUTIES.LIST>      </TRADEREXCISEDUTIES.LIST>' + "\n")
            stock_xml.write('      <STANDARDCOSTLIST.LIST>' + "\n")
            stock_xml.write('       <DATE>' + self.date(self.check(res[17])) + '</DATE>' + "\n")
            stock_xml.write(f'       <RATE> {self.check(res[16]) }</RATE>' + "\n")
            stock_xml.write('      </STANDARDCOSTLIST.LIST>' + "\n")
            stock_xml.write('      <STANDARDPRICELIST.LIST>' + "\n")
            stock_xml.write('       <DATE>' + self.date(self.check(res[15])) + '</DATE>' + "\n")
            stock_xml.write(f'       <RATE>{self.check(res[14])}</RATE>' + "\n")
            stock_xml.write('      </STANDARDPRICELIST.LIST>' + "\n")
            stock_xml.write('      <EXCISEITEMGODOWN.LIST>      </EXCISEITEMGODOWN.LIST>' + "\n")
            stock_xml.write('      <MULTICOMPONENTLIST.LIST>      </MULTICOMPONENTLIST.LIST>' + "\n")
            stock_xml.write('      <LBTDETAILS.LIST>      </LBTDETAILS.LIST>' + "\n")
            stock_xml.write('      <PRICELEVELLIST.LIST>      </PRICELEVELLIST.LIST>' + "\n")
            stock_xml.write('      <GSTCLASSFNIGSTRATES.LIST>      </GSTCLASSFNIGSTRATES.LIST>' + "\n")
            stock_xml.write('      <EXTARIFFDUTYHEADDETAILS.LIST>      </EXTARIFFDUTYHEADDETAILS.LIST>' + "\n")
            stock_xml.write('      <TEMPGSTITEMSLABRATES.LIST>      </TEMPGSTITEMSLABRATES.LIST>' + "\n")
            stock_xml.write('     </STOCKITEM>' + "\n")
            stock_xml.write('     </TALLYMESSAGE>\n')

        for line in stock_end:
            stock_xml.write(line)

        stock_start.close()
        stock_end.close()
        stock_xml.close()
