"""
    Contain all the quries used in program as dictionary.

"""
query = {

    'get_tables' : """SELECT name FROM sqlite_master 
                      WHERE type='table';""",

    'create_ledger' : """   CREATE TABLE IF NOT EXISTS ledger(
                            SR_NO INTEGER PRIMARY KEY AUTOINCREMENT,         
                            Ledger_Name VARCHAR(100),
                            Ledger_Group VARCHAR(100),
                            Opening_BALANCE DOUBLE,                                          
                            Op_Type_Dr_Cr VARCHAR(100),
                            Credit_Days VARCHAR(100),
                            Bill_Wise_On VARCHAR(100),
                            Ledger_Add1 VARCHAR(100),
                            Ledger_Add2 VARCHAR(100),
                            Ledger_Add3 VARCHAR(100),
                            Country VARCHAR(100),
                            State VARCHAR(100),
                            Pin_Code integer,
                            Contact_Person VARCHAR(100),
                            Mobile VARCHAR(100),
                            Email VARCHAR(100),
                            Website VARCHAR(100),
                            Pan_No VARCHAR(100),
                            GST_Registration_Type VARCHAR(100),
                            GSTIN_Number VARCHAR(100),
                            Transfer_Type VARCHAR(100),
                            Favouring_Name VARCHAR(100),
                            Ac_no VARCHAR(100),
                            Ifsc_Code VARCHAR(100),
                            Bank VARCHAR(100),
                            TELEPHONE_NO VARCHAR(100),
                            FAX VARCHAR(100),
                            CC_email VARCHAR(100),
                            ALIAS1 VARCHAR(100)
                             );   """,

    'create_02sales' :      """ CREATE TABLE IF NOT EXISTS sales02(
                                INVOICE_NUMBER VARCHAR(30),
                                INVOICE_DATE  VARCHAR(30),
                                COMPANY_STATE VARCHAR(30),
                                PARTY_NAME VARCHAR(30),
                                PARTY_GSTIN VARCHAR(30),
                                PARTY_GST_TYPE VARCHAR(30),
                                PARTY_STATE VARCHAR(30),
                                VOUCHER_TYPENAME VARCHAR(30),
                                VOUCHER_NARRATION VARCHAR(30),
                                SALES_LEDGER VARCHAR(30),
                                PRODUCT_NAME VARCHAR(30),
                                PRODUCT_TAXABILITY VARCHAR(30),
                                GST_RATE DOUBLE,
                                HSN_CODE INTEGER,
                                HSN_DES VARCHAR(30),
                                ITEM_GROUP VARCHAR(30),
                                ITEM_MRP DOUBLE,
                                GODOWN_NAME VARCHAR(30),
                                BIILED_QTY DOUBLE,
                                ACTUAL_QTY DOUBLE,
                                ITEM_RATE DOUBLE,
                                BASE_UNIT VARCHAR(30),
                                TRADE_DISC DOUBLE,
                                TAXABLE_VALUE DOUBLE,
                                CGST_AMT DOUBLE,
                                SGST_AMT DOUBLE,
                                IGST_AMT DOUBLE,
                                ADDITIONAL_LEDGER_1 VARCHAR(30),
                                ADDITIONAL_LEDGER_2 VARCHAR(30),
                                ADDITIONAL_LEDGER_3 VARCHAR(30),
                                BASIC_BUYERNAME VARCHAR(30),
                                CONSIGNEE_NAME VARCHAR(30),
                                CONSIGNEE_STATE VARCHAR(30),
                                CONSIGNEE_GSTIN VARCHAR(30),
                                PARTY_GROUP VARCHAR(30),
                                PARTY_ADDRESS_1 VARCHAR(30),
                                PARTY_ADDRESS_2 VARCHAR(30),
                                ORIGINAL_INVOICE_NO VARCHAR(30),
                                ITEM_DESCRIPTION VARCHAR(30),
                                ORIGINAL_INVOICE_DATE VARCHAR(30)
                            );
                            """,
    'create_02purchase' :      """ CREATE TABLE IF NOT EXISTS purchase02(
                                INVOICE_NUMBER VARCHAR(30),
                                INVOICE_DATE  VARCHAR(30),
                                COMPANY_STATE VARCHAR(30),
                                PARTY_NAME VARCHAR(30),
                                PARTY_GSTIN VARCHAR(30),
                                PARTY_GST_TYPE VARCHAR(30),
                                PARTY_STATE VARCHAR(30),
                                VOUCHER_TYPENAME VARCHAR(30),
                                VOUCHER_NARRATION VARCHAR(30),
                                SALES_LEDGER VARCHAR(30),
                                PRODUCT_NAME VARCHAR(30),
                                PRODUCT_TAXABILITY VARCHAR(30),
                                GST_RATE DOUBLE,
                                HSN_CODE INTEGER,
                                HSN_DES VARCHAR(30),
                                ITEM_GROUP VARCHAR(30),
                                ITEM_MRP DOUBLE,
                                GODOWN_NAME VARCHAR(30),
                                BIILED_QTY DOUBLE,
                                ACTUAL_QTY DOUBLE,
                                ITEM_RATE DOUBLE,
                                BASE_UNIT VARCHAR(30),
                                TRADE_DISC DOUBLE,
                                TAXABLE_VALUE DOUBLE,
                                CGST_AMT DOUBLE,
                                SGST_AMT DOUBLE,
                                IGST_AMT DOUBLE,
                                ADDITIONAL_LEDGER_1 VARCHAR(30),
                                ADDITIONAL_LEDGER_2 VARCHAR(30),
                                ADDITIONAL_LEDGER_3 VARCHAR(30),
                                BASIC_BUYERNAME VARCHAR(30),
                                CONSIGNEE_NAME VARCHAR(30),
                                CONSIGNEE_STATE VARCHAR(30),
                                CONSIGNEE_GSTIN VARCHAR(30),
                                PARTY_GROUP VARCHAR(30),
                                PARTY_ADDRESS_1 VARCHAR(30),
                                PARTY_ADDRESS_2 VARCHAR(30),
                                ORIGINAL_INVOICE_NO VARCHAR(30),
                                ITEM_DESCRIPTION VARCHAR(30),
                                ORIGINAL_INVOICE_DATE VARCHAR(30)
                            );
                            """,
    
    
    'create_stockitem'  :   """ CREATE TABLE IF NOT EXISTS stockitem(
                                B_CODE VARCHAR(100),
                                STOCK_ITEM_NAME VARCHAR(100),
                                ALIAS_NAME VARCHAR(100),
                                PART_NO INTEGER,
                                GROUP_NAME VARCHAR(100),
                                CATEGORY_NAME VARCHAR(100),
                                BASE_UNITS VARCHAR(100),
                                BASE_UNITS_FORMAL_NAME VARCHAR(100),
                                BASE_DECIMAL_PLACES INTEGER,
                                ALTERNATE_UNITS VARCHAR(100),
                                ALTERNATE_UNITS_FORMAL_NAMES VARCHAR(100),
                                ALTERNATE_DECIMAL_PLACES INTEGER,
                                CONVERSION_NUMBER INTEGER,
                                DENOMINATOR_NUMBER INTEGER,
                                STANDARD_SELLING_RATE DOUBLE,
                                STANDARD_SELLING_DATE VARCHAR(100),
                                STANDARD_PURCHASE_RATE DOUBLE,
                                STANDARD_PURCHASE_DATE VARCHAR(100),
                                MRP_RATE DOUBLE,
                                MRP_DATE VARCHAR(100),
                                GST_TAXABILITY VARCHAR(20),
                                GST_HSN_DESCRIPTION VARCHAR(20),
                                GST_HSN INTEGER,
                                GST_IGST DOUBLE,
                                GST_CGST DOUBLE,
                                GST_SGST DOUBLE,
                                CESS_PER_UNIT INTEGER,
                                CESS_PERCENTAGE_ON_VALUE DOUBLE,
                                PRICE_LIST_LABEL VARCHAR(20),
                                PRICE_LIST_APPL_DATE DATE,
                                PRICE_LIST_RATE DOUBLE,
                                PRICE_LIST_DISCOUNT DOUBLE,
                                OPENING_GODOWN VARCHAR(100),
                                OPENING_QUANTITY INTEGER,
                                OPENING_RATE DOUBLE,
                                OPENING_VALUE DOUBLE,
                                ITEM_REMARK VARCHAR(100),
                                ITEM_DESCRIPTION VARCHAR(100),
                                ITEM_BATCH_NAME VARCHAR(100),
                                ITEM_BATCH_EXP VARCHAR(100)) ;
                            """,
    'create_ldgr':  """ CREATE TABLE IF NOT EXISTS ldgr(
                    TRN_TYPE VARCHAR(5),
                    TYPE_NAR VARCHAR(5),
                    CENT DOUBLE,
                    TRNDATE VARCHAR(30),
                    CODE VARCHAR(30),
                    LEDGER_NAME VARCHAR(50),
                    TRNAMT DOUBLE,
                    AMTTYPE VARCHAR(5),
                    DEBITED_AMT DOUBLE,
                    CREDITED_AMT DOUBLE,
                    DISC VARCHAR(50),
                    BILL_NO VARCHAR(20),
                    NARRATION VARCHAR(50),
                    VR_NO VARCHAR(20),
                    VR_TYPE VARCHAR(5),
                    CAS_CRE INTEGER,
                    TAX_PER DOUBLE,
                    SALE_TYPE VARCHAR(20),
                    PRO_CODE VARCHAR(20),
                    FRGHT VARCHAR(20),
                    FRGH_CODE VARCHAR(20),
                    LP_NO VARCHAR(20),
                    POST_YN VARCHAR(20),
                    OBILL_NO VARCHAR(20),
                    POSTED DOUBLE,
                    BALAMT DOUBLE,
                    BALTYPE VARCHAR(20),
                    COMP_NO VARCHAR(20),
                    POST_DATE VARCHAR(20),
                    VEH_NO VARCHAR(20)
                ) """,
    
    'create_03SaleAcct' : """ CREATE TABLE IF NOT EXISTS Sale03Acct(
                        INVOICE_NUMBER VARCHAR(30),
                        INVOICE_DATE  VARCHAR(30),
                        COMPANY_STATE VARCHAR(20),
                        PARTY_NAME VARCHAR(20),
                        PARTY_GSTIN VARCHAR(30),
                        PARTY_GST_TYPE VARCHAR(20),
                        PARTY_STATE VARCHAR(20),
                        VOUCHER_TYPENAME VARCHAR(20),
                        VOUCHER_NARRATION VARCHAR(30),

                        SALES_GST_28 DOUBLE,
                        SALES_GST_18 DOUBLE,
                        SALES_GST_12 DOUBLE,
                        SALES_GST_5 DOUBLE,
                        SALES_GST_NIL DOUBLE,
                        SALES_GST_EXEMPT DOUBLE,

                        CGST_14 DOUBLE,
                        SGST_14 DOUBLE,
                        IGST_28 DOUBLE,

                        CGST_9 DOUBLE,
                        SGST_9 DOUBLE,
                        IGST_18 DOUBLE,

                        CGST_6 DOUBLE,
                        SGST_6 DOUBLE,
                        IGST_12 DOUBLE,

                        CGST_2_5 DOUBLE,
                        SGST_2_5 DOUBLE,
                        IGST_5 DOUBLE,

                        ADD_LED1 DOUBLE,
                        ADD_LED2 DOUBLE,
                        ADD_LED3 DOUBLE,

                        BASIC_BUYERNAME VARCHAR(30),
                        CONSIGNEE_NAME VARCHAR(30),
                        CONSIGNEE_STATE VARCHAR(30),
                        CONSIGNEE_GSTIN VARCHAR(30),
                        PARTY_GROUP VARCHAR(30),
                        PARTY_ADDRESS1 VARCHAR(30),
                        PARTY_ADDRESS2 VARCHAR(30),
                        BILL_NEW_REF VARCHAR(30)
                    )    
                """,

    'create_03PurAcct' : """ CREATE TABLE IF NOT EXISTS Pur03Acct(
                            INVOICE_NUMBER VARCHAR(30),
                            INVOICE_DATE  VARCHAR(30),
                            COMPANY_STATE VARCHAR(20),
                            PARTY_NAME VARCHAR(20),
                            PARTY_GSTIN VARCHAR(30),
                            PARTY_GST_TYPE VARCHAR(20),
                            PARTY_STATE VARCHAR(20),
                            VOUCHER_TYPENAME VARCHAR(20),
                            VOUCHER_NARRATION VARCHAR(30),

                            PURCHASE_GST_28 DOUBLE,
                            PURCHASE_GST_18 DOUBLE,
                            PURCHASE_GST_12 DOUBLE,
                            PURCHASE_GST_5 DOUBLE,
                            PURCHASE_GST_NIL DOUBLE,
                            PURCHASE_GST_EXEMPT DOUBLE,

                            CGST_14 DOUBLE,
                            SGST_14 DOUBLE,
                            IGST_28 DOUBLE,

                            CGST_9 DOUBLE,
                            SGST_9 DOUBLE,
                            IGST_18 DOUBLE,

                            CGST_6 DOUBLE,
                            SGST_6 DOUBLE,
                            IGST_12 DOUBLE,

                            CGST_2_5 DOUBLE,
                            SGST_2_5 DOUBLE,
                            IGST_5 DOUBLE,

                            ADD_LED1 DOUBLE,
                            ADD_LED2 DOUBLE,
                            ADD_LED3 DOUBLE,

                            BASIC_BUYERNAME VARCHAR(30),
                            CONSIGNEE_NAME VARCHAR(30),
                            CONSIGNEE_STATE VARCHAR(30),
                            CONSIGNEE_GSTIN VARCHAR(30),
                            PARTY_GROUP VARCHAR(30),
                            PARTY_ADDRESS1 VARCHAR(30),
                            PARTY_ADDRESS2 VARCHAR(30),

                            ORIGINAL_INVOICE_NUMBER VARCHAR(30),
                            ORIGINAL_INVOICE_DATE VARCHAR(30)
                            )

                        """,

    'AccMultipleDaybookStyle' : """ CREATE TABLE IF NOT EXISTS AccMultipleDaybookStyle(
                                    VOUCHER_NUMBER INTEGER,
                                    VOUCHER_DATE  VARCHAR(30),
                                    SOURCE_VOUCHERTYPENAME VARCHAR(30),
                                    ORIGINAL_VOUCHERTYPENAME VARCHAR(30),
                                    NARRATIONS VARCHAR(30),
                                    DEBITorCREDIT_LEDGER VARCHAR(30),
                                    DEBIT_AMOUNT DOUBLE,
                                    CREDIT_AMOUNT DOUBLE,
                                    DEBIT_LEDGER_GROUP VARCHAR(30)
                                    )
                                """,

    
    'AccountingSingleVch' : """ CREATE TABLE IF NOT EXISTS AccountingSingleVch(
                                    VOUCHER_NUMBER INTEGER,
                                    VOUCHER_DATE  VARCHAR(30),
                                    SOURCE_VOUCHERTYPENAME VARCHAR(30),
                                    ORIGINAL_VOUCHERTYPENAME VARCHAR(30),
                                    NARRATIONS VARCHAR(30),
                                    DEBIT_LEDGER VARCHAR(30),
                                    DEBIT_AMOUNT DOUBLE,
                                    CREDIT_LEDGER VARCHAR(30),
                                    CREDIT_AMOUNT DOUBLE,
                                    DEBIT_LEDGER_GROUP VARCHAR(30),
                                    CREDIT_LEDGER_GROUP VARCHAR(30)
                                    )
                                """ ,   

    #ledger_group removed

    'input_ledger'  : f"""    
                            INSERT INTO ledger (Ledger_Name,Ledger_Group,Opening_BALANCE , Op_Type_Dr_Cr ,Credit_Days,Bill_Wise_On,Ledger_Add1 ,
                            Ledger_Add2 ,Ledger_Add3 ,
                            Country ,State ,Pin_Code,Contact_Person,Mobile ,Email ,Website,Pan_No,GST_Registration_Type , GSTIN_Number ,
                            Transfer_Type,Favouring_Name ,Ac_no,Ifsc_Code,Bank ,TELEPHONE_NO,FAX,CC_email,ALIAS1) 
                            
                            SELECT m.Name,
                            CASE
                                WHEN m.Area='' THEN 'Suspense A/c'
                                ELSE 'Area'||CAST(m.Area AS VARCHAR)
                            END
                            ,m.YROPBAL,
                            CASE
                            	WHEN m.YROPTYPE=='C'THEN 'Cr'
                                ELSE 'Dr'
                            END,
                            NULL,NULL,m.ADRS1,m.ADRS2,m.ADRS3,'India',
                            CASE
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '01%' THEN 'JAMMU AND KASHMIR'
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '02%' THEN 'HIMACHAL PRADESH'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '03%' THEN 'PUNJAB'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '04%' THEN 'CHANDIGARH'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '38%' THEN 'LADAKH'
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '06%' THEN 'HARYANA'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '07%' THEN 'DELHI'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '08%' THEN 'RAJASTHAN'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '09%' THEN 'UTTAR PRADESH'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '10%' THEN 'BIHAR'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '11%' THEN 'SIKKIM'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '12%' THEN 'ARUNACHAL PRADESH'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '13%' THEN 'NAGALAND'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '14%' THEN 'MANIPUR'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '15%' THEN 'MIZORAM'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '16%' THEN 'TRIPURA'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '17%' THEN 'MEGHALAYA'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '18%' THEN 'ASSAM'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '19%' THEN 'WEST BENGAL'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '20%' THEN 'JHARKHAND'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO)  LIKE '21%' THEN 'ODISHA'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '22%' THEN 'CHATTISGARH'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '23%' THEN 'MADHYA PRADESH'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '24%' THEN 'GUJARAT'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '26%' THEN 'DADRA AND NAGAR HAVELI'  
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '25%' THEN 'DAMAN AND DIU' 	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '27%' THEN 'MAHARASHTRA'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '28%' THEN 'ANDHRA PRADESH(BEFORE DIVISION)'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '29%' THEN 'KARNATAKA'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '30%' THEN 'GOA'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO)  LIKE '31%' THEN 'LAKSHADWEEP'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '32%' THEN 'KERALA'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '33%' THEN 'TAMIL NADU'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '34%' THEN 'PUDUCHERRY'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '35%' THEN 'ANDAMAN AND NICOBAR ISLANDS'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE '36%' THEN 'TELANGANA'	
                                WHEN IIF(length(m.UPST_NO) = 15,m.UPST_NO,m.CST_NO) LIKE' 37%' THEN 'ANDHRA PRADESH' 	
                                ELSE 'UTTARAKHAND'
                            END ,
                            NULL,NULL,m.PHONE,m.MAIL,NULL,NULL,
                            CASE 
                            	WHEN length(m.CST_NO) = 15 or length(m.UPST_NO)= 15  THEN 'Regular'
                                ELSE 'Unregistered'
                            END,
                            CASE
                            	WHEN length(m.UPST_NO) = 15   THEN m.UPST_NO
                                WHEN length(m.CST_NO) = 15  THEN m.CST_NO
                                ELSE ''
                            END
                            ,NULL,NULL,NULL,NULL,BANK,NULL,NULL,NULL,m.CODE
                            FROM MASTER m WHERE m.UPST_NO NOT LIKE '50%' ;   
                   """,

    'insert_02sales'    :   """
                                INSERT INTO sales02 
                                SELECT pt.BILL_NO,
                                SUBSTR(pt.DATE,5,6) ||'-'||SUBSTR(pt.DATE,3,2) ||'- 20' || SUBSTR(pt.DATE,1,2),
                                'UTTARAKHAND',l.Ledger_Name,l.GSTIN_Number,l.GST_Registration_Type,l.State,'Sales',pt.NARATION,
                                'GST SALES@'||CAST(S.GST_IGST AS VARCHAR)||'%',
                                s.STOCK_ITEM_NAME,s.GST_TAXABILITY,S.GST_IGST,s.GST_HSN,s.GST_HSN_DESCRIPTION,s.GROUP_NAME,
                                s.MRP_RATE,pt.GODOWN,pt.PRO_QTY,
                                pt.PRO_QTY + pt.FREE,pt.PRO_RATE,
                                s.BASE_UNITS,pt.DISC_PER,(s.GST_IGST * pt.PRO_QTY) - pt.DISC_PER
                                ,s.GST_CGST,s.GST_SGST,s.GST_IGST,NULL,NULL,NULL,NULL,NULL,NULL,NULL,l.Ledger_Group,l.Ledger_Add1,l.Ledger_Add2,
                                NULL,s.ITEM_DESCRIPTION,NULL
                               
                               FROM ledger l,stockitem s,prodtal pt,temp
                                WHERE pt.TRN_TYPE == 'P' AND l.ALIAS1 = pt.party_code AND s.b_code == pt.pro_code
                                and
                                (CAST(pt.DATE AS INTEGER)>=temp.sd and CAST(pt.DATE AS INTEGER)<=temp.ed);

                            """,
    
    'insert_02purchase'    :   """
                                INSERT INTO purchase02 
                                SELECT pt.BILL_NO,
                                SUBSTR(pt.DATE,5,6) ||'-'||SUBSTR(pt.DATE,3,2) ||'- 20' || SUBSTR(pt.DATE,1,2),
                                'UTTARAKHAND',l.Ledger_Name,l.GSTIN_Number,l.GST_Registration_Type,l.State,'Sales',pt.NARATION,
                                'GST SALES@'||CAST(S.GST_IGST AS VARCHAR)||'%',
                                s.STOCK_ITEM_NAME,s.GST_TAXABILITY,S.GST_IGST,s.GST_HSN,s.GST_HSN_DESCRIPTION,s.GROUP_NAME,
                                s.MRP_RATE,pt.GODOWN,pt.PRO_QTY,
                                pt.PRO_QTY + pt.FREE,pt.PRO_RATE,
                                s.BASE_UNITS,pt.DISC_PER,(s.GST_IGST * pt.PRO_QTY) - pt.DISC_PER
                                ,s.GST_CGST,s.GST_SGST,s.GST_IGST,NULL,NULL,NULL,NULL,NULL,NULL,NULL,l.Ledger_Group,l.Ledger_Add1,l.Ledger_Add2,
                                NULL,s.ITEM_DESCRIPTION,NULL
                                FROM ledger l,stockitem s,prodtal pt,temp
                                WHERE pt.TRN_TYPE == 'P' AND l.ALIAS1 = pt.party_code AND s.b_code == pt.pro_code
                                and
                                (CAST(pt.DATE AS INTEGER)>=temp.sd and CAST(pt.DATE AS INTEGER)<=temp.ed);
                            """,

    'insert_stockitem' : """    INSERT INTO stockitem
                                SELECT p.B_CODE,p.B_DESC,NULL,NULL,p.[GROUP],NULL,u.base_unit,u.base_formal,0,u.alt_unit,u.alt_formal,
                                0,1,p.CASE_QTY,p.SEL_PRICE,t.d,p.PUR_PRICE,t.d,
                                p.MRP,t.d,
                                CASE 
                                    WHEN p.TAX>0 THEN 'Taxable'
                                ELSE 'Nil Rated'
                                END,
                                NULL,p.SH_NAME, p.TAX * 2,p.TAX,p.TAX,NULL,NULL,NULL,t.d,NULL,NULL,NULL,p.OP_QTY,p.PUR_PRICE,
                                                            OP_QTY * PUR_PRICE,NULL,NULL,NULL,NULL
                                FROM product p,temp t,units u WHERE u.Stock_name = p.B_DESC;
                        """,
        
    'insert_ldgr':  """ INSERT INTO ldgr SELECT
                            TRN_TYPE,TYPE_NAR,CENT,TRNDATE,CODE,'',TRNAMT,AMTTYPE,
                            CASE
                                WHEN AMTTYPE=='D' THEN TRNAMT
                                ELSE 0
                            END,
                            CASE
                                WHEN AMTTYPE=='C' THEN TRNAMT
                                ELSE 0
                            END,
                            DISC,BILL_NO,NARATION,VR_NO,VR_TYPE,CAS_CRE,TAX_PER,SALE_TYPE,PRO_CODE,FRGHT,FRGH_CODE,LP_NO,POST_YN,OBILL_NO,POSTED
                            ,BALAMT,BALTYPE,COMP_NO,POST_DATE,VEH_NO
                            FROM TEMP;
                        """,
    'insert_Sale03Acct' :   """ INSERT INTO Sale03Acct
                                SELECT BILL_NO,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2),
                                c_state,ledger.Ledger_Name,GSTIN_Number,GST_Registration_Type,State,VR_TYPE,NARRATION,
                                IIF(ledger.Ledger_Name like '%28!%%' ESCAPE '!',TRNAMT,0),
                                IIF(ledger.Ledger_Name like '%18!%%' ESCAPE '!',TRNAMT,0),
                                IIF(ledger.Ledger_Name like '%12!%%' ESCAPE '!',TRNAMT,0),
                                IIF(ledger.Ledger_Name like '%5!%%' ESCAPE '!',TRNAMT,0),
                                IIF(ledger.Ledger_Name like '%0!%%' ESCAPE '!',TRNAMT,0),
                                IIF(ledger.Ledger_Name like '%!%%' ESCAPE '!',0,TRNAMT),
                                IIF(ledger.Ledger_Name like '%28!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.14,2),0),
                                IIF(ledger.Ledger_Name like '%28!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.14,2),0),
                                IIF(ledger.Ledger_Name like '%28!%%' ESCAPE '!' AND LOWER(c_state) <> LOWER(State),round(TRNAMT * 0.28,2),0),

                                IIF(ledger.Ledger_Name like '%18!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.09,2),0),
                                IIF(ledger.Ledger_Name like '%18!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.09,2),0),
                                IIF(ledger.Ledger_Name like '%18!%%' ESCAPE '!' AND LOWER(c_state) <> LOWER(State),round(TRNAMT * 0.18,2),0),
                                
                                
                                IIF(ledger.Ledger_Name like '%12!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.06,2),0),
                                IIF(ledger.Ledger_Name like '%12!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.06,2),0),
                                IIF(ledger.Ledger_Name like '%12!%%' ESCAPE '!' AND LOWER(c_state) <> LOWER(State),round(TRNAMT * 0.12,2),0),
                                
                                
                                IIF(ledger.Ledger_Name like '%5!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.025,2),0),
                                IIF(ledger.Ledger_Name like '%5!%%' ESCAPE '!' AND c_state = State,round(TRNAMT * 0.025,2),0),
                                IIF(ledger.Ledger_Name like '%5!%%' ESCAPE '!' AND LOWER(c_state) <> LOWER(State),round(TRNAMT * 0.05,2),0),
                                
                                Ledger_Add1,Ledger_Add2,Ledger_Add3,
                                '','','','',
                                '','','',''
                                from ldgr,ledger,companystate,temp 
                                where ldgr.code = ledger.alias1  and
                                (TRN_TYPE = 'B' or TRN_TYPE = 'S' or TRN_TYPE = 'M' ) and BILL_NO NOT IN (SELECT INVOICE_NUMBER FROM sales02 )
                                and 
                                (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed) ;
                            """,

    'insert_Pur03Acct' :   """  INSERT INTO Pur03Acct
                                SELECT BILL_NO,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2),
                                c_state,ledger.Ledger_Name,GSTIN_Number,GST_Registration_Type,State,VR_TYPE,NARRATION,
                                IIF(ledger.Ledger_Name like '%28!%%' ESCAPE '!',TRNAMT,0),
                                IIF(ledger.Ledger_Name like '%18!%%' ESCAPE '!',TRNAMT,0),
                                IIF(ledger.Ledger_Name like '%12!%%' ESCAPE '!',TRNAMT,0),
                                IIF(ledger.Ledger_Name like '%5!%%' ESCAPE '!',TRNAMT,0),
                                IIF(ledger.Ledger_Name like '%0!%%' ESCAPE '!',TRNAMT,0),
                                IIF(ledger.Ledger_Name like '%!%%' ESCAPE '!',0,TRNAMT),
                                IIF(ledger.Ledger_Name like '%28!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.14,2),0),
                                IIF(ledger.Ledger_Name like '%28!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.14,2),0),
                                IIF(ledger.Ledger_Name like '%28!%%' ESCAPE '!' AND LOWER(c_state) <> LOWER(State),round(TRNAMT * 0.28,2),0),

                                IIF(ledger.Ledger_Name like '%18!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.09,2),0),
                                IIF(ledger.Ledger_Name like '%18!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.09,2),0),
                                IIF(ledger.Ledger_Name like '%18!%%' ESCAPE '!' AND LOWER(c_state) <> LOWER(State),round(TRNAMT * 0.18,2),0),
                                
                                
                                IIF(ledger.Ledger_Name like '%12!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.06,2),0),
                                IIF(ledger.Ledger_Name like '%12!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.06,2),0),
                                IIF(ledger.Ledger_Name like '%12!%%' ESCAPE '!' AND LOWER(c_state) <> LOWER(State),round(TRNAMT * 0.12,2),0),
                                
                                
                                IIF(ledger.Ledger_Name like '%5!%%' ESCAPE '!' AND LOWER(c_state) = LOWER(State),round(TRNAMT * 0.025,2),0),
                                IIF(ledger.Ledger_Name like '%5!%%' ESCAPE '!' AND c_state = State,round(TRNAMT * 0.025,2),0),
                                IIF(ledger.Ledger_Name like '%5!%%' ESCAPE '!' AND LOWER(c_state) <> LOWER(State),round(TRNAMT * 0.05,2),0),
                                
                                Ledger_Add1,Ledger_Add2,Ledger_Add3,
                                '','','','',
                                '','','','',''
                                from ldgr,ledger,companystate,temp 
                                where ldgr.code = ledger.alias1  and
                                (TRN_TYPE = 'I' or TRN_TYPE = 'P'  ) and BILL_NO NOT IN (SELECT INVOICE_NUMBER FROM purchase02 )
                                and 
                                (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed) ;
                            """,

    'insert_sales_AccMultipleDaybookStyle' : """  INSERT INTO AccMultipleDaybookStyle
                                        SELECT BILL_NO,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2)
                                        ,'Sales',
                                        'Sales',NARRATION,ledger.Ledger_Name,
                                        CASE
                                            WHEN AMTTYPE=='D' THEN TRNAMT
                                            ELSE 0
                                        END,
                                        CASE
                                            WHEN AMTTYPE=='C' THEN TRNAMT
                                            ELSE 0
                                        END,''                                        
                                        from ldgr,ledger,temp where ldgr.code = ledger.alias1  and 
                                        (TRN_TYPE = 'B' or TRN_TYPE = 'S' or TRN_TYPE = 'M' )and 
                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                        and
                                        BILL_NO NOT IN (SELECT INVOICE_NUMBER FROM sales02 ) ;

                            """,

    'insert_pur_AccMultipleDaybookStyle' : """  INSERT INTO AccMultipleDaybookStyle
                                        SELECT BILL_NO,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2)
                                        ,'Purchase',
                                        'Purchase',NARRATION,ledger.Ledger_Name,
                                        CASE
                                            WHEN AMTTYPE=='D' THEN TRNAMT
                                            ELSE 0
                                        END,
                                        CASE
                                            WHEN AMTTYPE=='C' THEN TRNAMT
                                            ELSE 0
                                        END,''                                        
                                        from ldgr,ledger,temp where ldgr.code = ledger.alias1  and 
                                        (TRN_TYPE = 'I' or TRN_TYPE = 'P' ) 
                                        and
                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                        and
                                        BILL_NO NOT IN (SELECT INVOICE_NUMBER FROM purchase02 );
                            """,
    'insert_cashdeposit_AccMultipleDaybookStyle' : """  INSERT INTO AccMultipleDaybookStyle
                                                        SELECT 
                                                        CASE 
                                                        WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        ELSE BILL_NO
                                                    END  
                                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2)
                                                        ,'Check Deposit',
                                                        'Check Deposit',NARRATION,ledger.Ledger_Name,
                                                        CASE
                                                            WHEN AMTTYPE=='D' THEN TRNAMT
                                                            ELSE 0
                                                        END,
                                                        CASE
                                                            WHEN AMTTYPE=='C' THEN TRNAMT
                                                            ELSE 0
                                                        END,''                                        
                                                        from ldgr,ledger,temp where ldgr.code = ledger.alias1  and 
                                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                                        and
                                                        (TRN_TYPE = 'H' AND TYPE_NAR = 'V') ;
                                                    """,
    
    'insert_receipt_AccMultipleDaybookStyle' : """  INSERT INTO AccMultipleDaybookStyle
                                                        SELECT 
                                                        CASE 
                                                        WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        ELSE BILL_NO
                                                    END  
                                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2)
                                                        ,'Receipt',
                                                        'Receipt',NARRATION,ledger.Ledger_Name,
                                                        CASE
                                                            WHEN AMTTYPE=='D' THEN TRNAMT
                                                            ELSE 0
                                                        END,
                                                        CASE
                                                            WHEN AMTTYPE=='C' THEN TRNAMT
                                                            ELSE 0
                                                        END,''                                        
                                                        from ldgr,ledger,temp
                                                        where ldgr.code = ledger.alias1  and
                                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                                        and 
                                                        ((TRN_TYPE = 'G' AND TYPE_NAR = 'V') or (TRN_TYPE = '' AND TYPE_NAR = '' )) ;
                                                    """,

    
    'insert_creceipt_AccMultipleDaybookStyle' : """  INSERT INTO AccMultipleDaybookStyle
                                                        SELECT 
                                                        CASE 
                                                        WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        ELSE BILL_NO
                                                    END  
                                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2)
                                                        ,CASE
                                                            WHEN (TRN_TYPE = 'R' AND TYPE_NAR = 'R') THEN 'Cash Receipt'
                                                            WHEN (TRN_TYPE = 'D' AND TYPE_NAR = 'R') THEN 'Discount'
                                                        END,
                                                        CASE
                                                            WHEN (TRN_TYPE = 'R' AND TYPE_NAR = 'R') THEN 'Cash Receipt'
                                                            WHEN (TRN_TYPE = 'D' AND TYPE_NAR = 'R') THEN 'Discount'
                                                        END,
                                                        NARRATION,ledger.Ledger_Name,
                                                        CASE
                                                            WHEN AMTTYPE=='D' THEN TRNAMT
                                                            ELSE 0
                                                        END,
                                                        CASE
                                                            WHEN AMTTYPE=='C' THEN TRNAMT
                                                            ELSE 0
                                                        END,''                                        
                                                        from ldgr,ledger,temp
                                                        where ldgr.code = ledger.alias1  and
                                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                                        and 
                                                        ((TRN_TYPE = 'R' AND TYPE_NAR = 'R')
                                                        or
                                                        (TRN_TYPE = 'D' AND TYPE_NAR = 'R')) ;
                                                    """,

    
    'insert_contra_AccMultipleDaybookStyle' : """  INSERT INTO AccMultipleDaybookStyle
                                                        SELECT 
                                                        CASE 
                                                        WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        ELSE BILL_NO
                                                    END  
                                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2)
                                                        ,'Contra',
                                                        'Contra',NARRATION,ledger.Ledger_Name,
                                                        CASE
                                                            WHEN AMTTYPE=='D' THEN TRNAMT
                                                            ELSE 0
                                                        END,
                                                        CASE
                                                            WHEN AMTTYPE=='C' THEN TRNAMT
                                                            ELSE 0
                                                        END,''                                        
                                                        from ldgr,ledger,temp
                                                        where ldgr.code = ledger.alias1  and 
                                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                                        and
                                                        (TRN_TYPE = 'H' AND TYPE_NAR = 'D') ;
                                                    """,


    'insert_payment_AccMultipleDaybookStyle' : """  INSERT INTO AccMultipleDaybookStyle
                                                        SELECT 
                                                        CASE 
                                                        WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                                        ELSE BILL_NO
                                                    END  
                                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2)
                                                        ,'Payment',
                                                        'Payment',NARRATION,ledger.Ledger_Name,
                                                        CASE
                                                            WHEN AMTTYPE=='D' THEN TRNAMT
                                                            ELSE 0
                                                        END,
                                                        CASE
                                                            WHEN AMTTYPE=='C' THEN TRNAMT
                                                            ELSE 0
                                                        END,''                                        
                                                        from ldgr,ledger,temp 
                                                        where ldgr.code = ledger.alias1  and 
                                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                                        and
                                                        (TRN_TYPE = 'G' AND TYPE_NAR = 'I') ;
                                                    """,
    

    'insert_receipt_AccountingSingleVch' : """  INSERT INTO AccountingSingleVch
                                        SELECT 
                                        CASE 
                                            WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            ELSE BILL_NO
                                        END    
                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2),
                                        'Receipt','Receipt',NARRATION,
                                        CASE
                                            WHEN AMTTYPE=='D' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,
                                        CASE
                                            WHEN AMTTYPE=='C' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,'',''                                        
                                        from ldgr,ledger,temp
                                        where ldgr.code = ledger.alias1  and
                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                        and
                                        (TRN_TYPE = 'G' AND TYPE_NAR = 'V' ) or (TRN_TYPE = '' AND TYPE_NAR = '' ) 

                            """ ,

                            

    'insert_contra_AccountingSingleVch' : """  INSERT INTO AccountingSingleVch
                                        SELECT 
                                        CASE 
                                            WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            ELSE BILL_NO
                                        END    
                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2),
                                        'Contra','Contra',NARRATION,
                                        CASE
                                            WHEN AMTTYPE=='D' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,
                                        CASE
                                            WHEN AMTTYPE=='C' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,'',''                                        
                                        from ldgr,ledger,temp
                                        where ldgr.code = ledger.alias1  and
                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                        and
                                        (TRN_TYPE = 'H' AND TYPE_NAR = 'D' );

                            """,
    
    'insert_payment_AccountingSingleVch' : """  INSERT INTO AccountingSingleVch
                                        SELECT 
                                        CASE 
                                            WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            ELSE BILL_NO
                                        END    
                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2),
                                        'Payment','Payment',NARRATION,
                                        CASE
                                            WHEN AMTTYPE=='D' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,
                                        CASE
                                            WHEN AMTTYPE=='C' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,'',''                                        
                                        from ldgr,ledger,temp 
                                        where ldgr.code = ledger.alias1  and
                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                        and
                                        (TRN_TYPE = 'G' AND TYPE_NAR = 'I' );
                            """,

    'insert_cashdeposit_AccountingSingleVch' : """  INSERT INTO AccountingSingleVch
                                        SELECT 
                                        CASE 
                                            WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            ELSE BILL_NO
                                        END    
                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2),
                                        'Cash Deposit','Cash Deposit',NARRATION,
                                        CASE
                                            WHEN AMTTYPE=='D' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,
                                        CASE
                                            WHEN AMTTYPE=='C' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,'',''                                        
                                        from ldgr,ledger,temp 
                                        where ldgr.code = ledger.alias1  and 
                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                        and
                                        (TRN_TYPE = 'H' AND TYPE_NAR = 'V' )
                            """,


    'insert_sales_AccountingSingleVch' : """  INSERT INTO AccountingSingleVch
                                        SELECT 
                                        CASE 
                                            WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            ELSE BILL_NO
                                        END    
                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2),
                                        'Sales','Sales',NARRATION,
                                        CASE
                                            WHEN AMTTYPE=='D' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,
                                        CASE
                                            WHEN AMTTYPE=='C' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,'',''                                        
                                        from ldgr,ledger,temp 
                                        where ldgr.code = ledger.alias1  and
                                        (TRN_TYPE = 'B' or TRN_TYPE = 'S' or TRN_TYPE = 'M' )and
                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                        and
                                         BILL_NO NOT IN (SELECT INVOICE_NUMBER FROM sales02 );
                            """,

    'insert_pur_AccountingSingleVch' : """  INSERT INTO AccountingSingleVch
                                        SELECT 
                                        CASE 
                                            WHEN BILL_NO='' THEN 'BLANK'|| ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT' THEN 'NEFT'||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='UPI' THEN 'UPI' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='RTGS' THEN 'RTGS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IBS' THEN 'IBS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='NEFT01' THEN 'NEFT01' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            WHEN trim(BILL_NO)='IMPS' THEN 'IMPS' ||  ROW_NUMBER () OVER ( ORDER BY BILL_NO  ) 
                                            ELSE BILL_NO
                                        END    
                                        ,SUBSTR(TRNDATE,5,6) ||'-'||SUBSTR(TRNDATE,3,2) ||'- 20' || SUBSTR(TRNDATE,1,2),
                                        'Purchase','Purchase',NARRATION,
                                        CASE
                                            WHEN AMTTYPE=='D' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,
                                        CASE
                                            WHEN AMTTYPE=='C' THEN ledger.Ledger_Name
                                            ELSE ''
                                        END,TRNAMT,'',''                                        
                                        from ldgr,ledger,temp 
                                        where ldgr.code = ledger.alias1  and
                                        (TRN_TYPE = 'I' or TRN_TYPE = 'P' )
                                        and
                                        (CAST(TRNDATE AS INTEGER)>=temp.sd and CAST(TRNDATE AS INTEGER)<=temp.ed)
                                        and
                                        BILL_NO NOT IN (SELECT INVOICE_NUMBER FROM purchase02 );
                            """    
    
}                                 
















                      