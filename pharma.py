import tkinter as tk
from tkinter import Frame
from tkinter import ttk
from tkinter import messagebox
import pymysql

class PharmacyManSys:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # Variable Decl..
        # Add Med..
        self.add_med = tk.StringVar()
        self.ref_med = tk.StringVar()

        ##Main Medicine Variable
        self.med_refNo = tk.StringVar()
        self.med_cmpName = tk.StringVar()
        self.med_medType = tk.StringVar()
        self.med_medName = tk.StringVar()

        self.med_lotNo = tk.StringVar()
        self.med_isDate = tk.StringVar()
        self.med_exDate = tk.StringVar()
        self.med_uses = tk.StringVar()

        self.med_sideEff = tk.StringVar()
        self.med_dosage = tk.StringVar()
        self.med_prec = tk.StringVar()
        self.med_price = tk.StringVar()
        self.med_quan = tk.StringVar()

        lbTitle = tk.Label(self.root, text="Pharmacy Management System", bd=15, relief=tk.RIDGE, bg='white',
                           fg='blue', font=("times new roman", 50, "bold"), padx=2, pady=4)
        lbTitle.pack(side=tk.TOP, fill=tk.X)

        def fetchRef():
            con = pymysql.connect(host="localhost", user="root", password="Root@1234")
            myCursor = con.cursor()
            query = 'use pharmaDB'
            myCursor.execute(query)
            query = 'select ref from pharma'
            myCursor.execute(query)
            ref = myCursor.fetchall()
            return ref

        def deleteInfo():
            try:
                con = pymysql.connect(host="localhost", user="root", password="Root@1234", database="pharmaDB")
                myCursor = con.cursor()
                query = 'DELETE FROM pharma WHERE ref=%s'
                myCursor.execute(query, (self.ref_med.get(),))
                con.commit()
                fetchInfo()
                messagebox.showinfo('Success', 'Data Deleted Successfully')
            except:
                messagebox.showinfo('Error', 'Error in Deleting Data')

        def updateInfo():
            try:
                con = pymysql.connect(host="localhost", user="root", password="Root@1234", database="pharmaDB")
                myCursor = con.cursor()
                query = 'UPDATE pharma SET medName=%s WHERE ref=%s;'
                myCursor.execute(query, (self.add_med.get(), self.ref_med.get()))
                con.commit()
                fetchInfo()
                messagebox.showinfo('Success', 'Data Updated Successfully')
            except:
                messagebox.showinfo('Error', 'Error in Updating Data')

        def fetchMed():
            con = pymysql.connect(host="localhost", user="root", password="Root@1234")
            myCursor = con.cursor()
            query = 'use pharmaDB'
            myCursor.execute(query)
            query = 'select medName from pharma'
            myCursor.execute(query)
            med = myCursor.fetchall()
            return med

        def fetchInfo():
            con = pymysql.connect(host="localhost", user="root", password="Root@1234")
            myCursor = con.cursor()
            query = 'use pharmaDB'
            myCursor.execute(query)
            query = 'select * from pharma'
            myCursor.execute(query)
            fetched_data = myCursor.fetchall()
            self.medicine_table.delete(*self.medicine_table.get_children())
            for data in fetched_data:
                dataList = list(data)
                self.medicine_table.insert('', tk.END, values=dataList)

        def clearInfo():
            self.medicine_table.delete(*self.medicine_table.get_children())

        def addInfo():
            try:
                con = pymysql.connect(host="localhost", user="root", password="Root@1234")
                myCursor = con.cursor()
                query = 'use pharmaDB'
                myCursor.execute(query)
                query = 'insert into pharma values(%s,%s)'
                myCursor.execute(query, (self.ref_med.get(), self.add_med.get()))
                con.commit()
                messagebox.showinfo('Success', 'Data Added Successfully')
            except:
                messagebox.showinfo('Error', 'Error in Adding Data')
            fetchInfo()

        # --------------------Main Table Func.....----------------------------------

        def fetchMedicInfo():
            con = pymysql.connect(host="localhost", user="root", password="Root@1234")
            myCursor = con.cursor()
            query = 'use pharmaDB'
            myCursor.execute(query)
            query = 'select * from medicineInfo'
            myCursor.execute(query)
            fetched_data = myCursor.fetchall()
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for data in fetched_data:
                dataList = list(data)
                self.pharmacy_table.insert('', tk.END, values=dataList)

        def addMedicInfo():
            try:
                con = pymysql.connect(host="localhost", user="root", password="Root@1234")
                myCursor = con.cursor()
                query = 'use pharmaDB'
                myCursor.execute(query)
                query = 'insert into medicineInfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                myCursor.execute(query, (self.med_refNo.get(), self.med_cmpName.get(), self.med_medType.get(),
                                         self.med_medName.get(), self.med_lotNo.get(), self.med_isDate.get(),
                                         self.med_exDate.get(), self.med_uses.get(), self.med_sideEff.get(),
                                         self.med_dosage.get(), self.med_prec.get(), self.med_price.get(),
                                         self.med_quan.get()))
                con.commit()
                messagebox.showinfo('Success', 'Medicine Information Added Successfully')
            except:
                messagebox.showinfo('Error', 'Error in Adding Data')
            fetchMedicInfo()

        def showAllMedicInfo():
            fetchMedicInfo()


        def deleMedicInfo():
            try:
                con = pymysql.connect(host="localhost", user="root", password="Root@1234", database="pharmaDB")
                myCursor = con.cursor()
                query = 'DELETE FROM medicineInfo WHERE refNo=%s'
                myCursor.execute(query, (self.med_refNo.get(),))
                con.commit()
                fetchMedicInfo()
                messagebox.showinfo('Success', 'Medicine Info. Deleted Successfully')
            except:
                messagebox.showinfo('Error', 'Error in Deleting Data')


        def updateMedicInfo():
            try:
                con = pymysql.connect(host="localhost", user="root", password="Root@1234", database="pharmaDB")
                myCursor = con.cursor()
                query = 'UPDATE medicineInfo SET cmpName=%s,medType=%s,medName=%s,lotNo=%s,isDate=%s,exDate=%s,uses=%s,sideEff=%s,dosage=%s,prec=%s,price=%s,quan=%s WHERE refNo=%s;'
                myCursor.execute(query, (self.med_cmpName.get(), self.med_medType.get(),
                                         self.med_medName.get(), self.med_lotNo.get(), self.med_isDate.get(),
                                         self.med_exDate.get(), self.med_uses.get(), self.med_sideEff.get(),
                                         self.med_dosage.get(), self.med_prec.get(), self.med_price.get(),
                                         self.med_quan.get(),self.med_refNo.get()))
                con.commit()
                fetchMedicInfo()
                messagebox.showinfo('Success', 'Medicine Info. Updated Successfully')
            except:
                messagebox.showinfo('Error', 'Error in Updating Data')
        
        def resetTable():
            selected_item = self.pharmacy_table.focus()
            values = self.pharmacy_table.item(selected_item, 'values')
            if values:
                self.med_cmpName.set("")
                self.med_lotNo.set("")
                self.med_isDate.set("")
                self.med_exDate.set("")
                self.med_uses.set("")
                self.med_sideEff.set("")
                self.med_dosage.set("")
                self.med_prec.set("")
                self.med_price.set("")
                self.med_quan.set("")

        def searchMedInfoTable():
            search_value = self.search_txt.get()
            search_criteria = self.search_var.get()
            print(search_value, search_criteria)
            if search_value and search_criteria:
                try:
                    con = pymysql.connect(host="localhost", user="root", password="Root@1234", database="pharmaDB")
                    myCursor = con.cursor()
                    
                    if search_criteria == "Ref":
                        query = 'SELECT * FROM medicineInfo WHERE refNo=%s'
                    elif search_criteria == "Medname":
                        query = 'SELECT * FROM medicineInfo WHERE medName=%s'
                    elif search_criteria == "Lot":
                        query = 'SELECT * FROM medicineInfo WHERE lotNo=%s'
                    elif search_criteria == "Use":
                        query = "SELECT * FROM medicineInfo WHERE uses LIKE %s"
                        search_value = '%' + search_value + '%'                        
                    myCursor.execute(query, (search_value))
                    fetched_data = myCursor.fetchall()
                    
                    self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                    for data in fetched_data:
                        dataList = list(data)
                        self.pharmacy_table.insert('', tk.END, values=dataList)
                except:
                    messagebox.showinfo('Error', 'Error in Searching Data')




        def onPharmacyTableSelect(event):
            selected_item = self.pharmacy_table.focus()
            values = self.pharmacy_table.item(selected_item, 'values')
            if values:
                self.med_refNo.set(values[0])
                self.med_cmpName.set(values[1])
                self.med_medType.set(values[2])
                self.med_medName.set(values[3])
                self.med_lotNo.set(values[4])
                self.med_isDate.set(values[5])
                self.med_exDate.set(values[6])
                self.med_uses.set(values[7])
                self.med_sideEff.set(values[8])
                self.med_dosage.set(values[9])
                self.med_prec.set(values[10])
                self.med_price.set(values[11])
                self.med_quan.set(values[12])
        
        
        #----------------------------------------------------------------
        # Data Frame
        DataFrame = Frame(self.root, bd=15, relief=tk.RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1435, height=400)

        DataFrameLeft = tk.LabelFrame(DataFrame, bd=10, relief=tk.RIDGE, padx=20, text="Medicine Information",
                                      fg="darkgreen", font=("times new roman", 20, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        DataFrameRight = tk.LabelFrame(DataFrame, bd=10, relief=tk.RIDGE, padx=20, text="Medicine Add Department",
                                       fg="darkgreen", font=("times new roman", 20, "bold"))
        DataFrameRight.place(x=910, y=5, width=460, height=350)

        # BUTTON FRAME
        ButtonFrame = Frame(self.root, bd=15, relief=tk.RIDGE, padx=20)
        ButtonFrame.place(x=0, y=520, width=1435, height=60)

        # Main Button
        btnAddData = tk.Button(ButtonFrame, text="Medicine Add", command=addMedicInfo, font=("arial", 12, "bold"),
                               bg="darkgreen")
        btnAddData.grid(row=0, column=0)

        btnUpdMed = tk.Button(ButtonFrame, text="Update", command=updateMedicInfo, font=("arial", 12, "bold"),
                              bg="darkgreen")
        btnUpdMed.grid(row=0, column=1)

        btnDelMed = tk.Button(ButtonFrame, text="Delete", command=deleMedicInfo, font=("arial", 12, "bold"),
                              bg="darkgreen")
        btnDelMed.grid(row=0, column=2)

        btnRestMed = tk.Button(ButtonFrame, text="Reset",command=resetTable, font=("arial", 12, "bold"), bg="darkgreen")
        btnRestMed.grid(row=0, column=3)

        btnExitMed = tk.Button(ButtonFrame, text="Exit", font=("arial", 12, "bold"), bg="darkgreen")
        btnExitMed.grid(row=0, column=4)

        LblSearch = tk.Label(ButtonFrame, font=("arial", 17, "bold"), text="Search By", padx=2, bg="red",
                             fg="white")
        LblSearch.grid(row=0, column=5, sticky="w")

        #ComboBox Variable Decl.
        self.search_var = tk.StringVar()

        serch_combo = ttk.Combobox(ButtonFrame,textvariable=self.search_var, width=12, font=("arial", 17, "bold"), state="readonly")
        serch_combo["values"] = ("Ref", "Medname", "Lot", "Use")
        serch_combo.grid(row=0, column=6)
        serch_combo.current(0)

        self.search_txt = tk.StringVar()
        txtSerch = tk.Entry(ButtonFrame,textvariable=self.search_txt, bd=3, relief=tk.RIDGE, width=50, font=("arial", 14, "bold"))
        txtSerch.grid(row=0, column=7)

        srchButton = tk.Button(ButtonFrame,command=searchMedInfoTable, text="Search", font=("arial", 12, "bold"), bg="darkgreen")
        srchButton.grid(row=0, column=8)

        showABtn = tk.Button(ButtonFrame, text="Show All",command=showAllMedicInfo, font=("arial", 12, "bold"), bg="darkgreen")
        showABtn.grid(row=0, column=9)

        # Ref Frame

        LblRefno = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Reference No", padx=2)
        LblRefno.grid(row=0, column=0, sticky="w")

        ref = fetchRef()
        ref_combo = ttk.Combobox(DataFrameLeft, textvariable=self.med_refNo, width=25, font=("arial", 17, "bold"),
                                 state="readonly")
        ref_combo["values"] = ref
        ref_combo.grid(row=0, column=1)
        ref_combo.current(0)

        # Comp Name
        LblCompanyName = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Company Name", padx=2)
        LblCompanyName.grid(row=1, column=0, sticky="w")
        cmpSerch = tk.Entry(DataFrameLeft, textvariable=self.med_cmpName, bd=3, relief=tk.RIDGE, width=32,
                            font=("arial", 14, "bold"))
        cmpSerch.grid(row=1, column=1)

        # Med Type
        LblMedTyp = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Med. Type", padx=2)
        LblMedTyp.grid(row=2, column=0, sticky="w")

        medType_combo = ttk.Combobox(DataFrameLeft, textvariable=self.med_medType, width=25,
                                     font=("arial", 17, "bold"), state="readonly")
        medType_combo["values"] = ("Tablet", "Liquid", "Capsules", "Drops", "Inhalers", "Injections")
        medType_combo.grid(row=2, column=1)
        medType_combo.current(0)

        # Med Name
        LblMedName = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Med. Name", padx=2)
        LblMedName.grid(row=3, column=0, sticky="w")

        med = fetchMed()
        medName_combo = ttk.Combobox(DataFrameLeft, textvariable=self.med_medName, width=25,
                                     font=("arial", 17, "bold"), state="readonly")
        medName_combo["values"] = med
        medName_combo.grid(row=3, column=1)
        medName_combo.current(0)

        # Lot No.
        LblLotNo = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Lot No: ", padx=2)
        LblLotNo.grid(row=4, column=0, sticky="w")
        txtLotNo = tk.Entry(DataFrameLeft, textvariable=self.med_lotNo, bd=3, relief=tk.RIDGE, width=32,
                            font=("arial", 14, "bold"))
        txtLotNo.grid(row=4, column=1)

        # Issue Date.
        LblIssueDt = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Issue Date: ", padx=2)
        LblIssueDt.grid(row=5, column=0, sticky="w")
        txtIssuDt = tk.Entry(DataFrameLeft, textvariable=self.med_isDate, bd=3, relief=tk.RIDGE, width=32,
                             font=("arial", 14, "bold"))
        txtIssuDt.grid(row=5, column=1)

        # Exp Date.
        LblExpDt = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Expiry Date: ", padx=2)
        LblExpDt.grid(row=6, column=0, sticky="w")
        txtExpDt = tk.Entry(DataFrameLeft, textvariable=self.med_exDate, bd=3, relief=tk.RIDGE, width=32,
                            font=("arial", 14, "bold"))
        txtExpDt.grid(row=6, column=1)

        # Uses.
        LblUses = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Uses: ", padx=2)
        LblUses.grid(row=7, column=0, sticky="w")
        txtUses = tk.Entry(DataFrameLeft, textvariable=self.med_uses, bd=3, relief=tk.RIDGE, width=32,
                           font=("arial", 14, "bold"))
        txtUses.grid(row=7, column=1)

        # Side Effect.
        LblSideEf = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Side Effect: ", padx=2)
        LblSideEf.grid(row=8, column=0, sticky="w")
        txtSideEf = tk.Entry(DataFrameLeft, textvariable=self.med_sideEff, bd=3, relief=tk.RIDGE, width=32,
                             font=("arial", 14, "bold"))
        txtSideEf.grid(row=8, column=1)

        # Dosage.
        LblDosage = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Dosage: ", padx=2)
        LblDosage.grid(row=0, column=2, sticky="w")
        txtDosage = tk.Entry(DataFrameLeft, textvariable=self.med_dosage, bd=3, relief=tk.RIDGE, width=32,
                             font=("arial", 14, "bold"))
        txtDosage.grid(row=0, column=3)

        # Prec.
        LblPrec = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Prescription: ", padx=2)
        LblPrec.grid(row=1, column=2, sticky="w")
        txtPrec = tk.Entry(DataFrameLeft, textvariable=self.med_prec, bd=3, relief=tk.RIDGE, width=32,
                           font=("arial", 14, "bold"))
        txtPrec.grid(row=1, column=3)

        # Price.
        LblPrice = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Price: ", padx=2)
        LblPrice.grid(row=2, column=2, sticky="w")
        txtPrice = tk.Entry(DataFrameLeft, textvariable=self.med_price, bd=3, relief=tk.RIDGE, width=32,
                            font=("arial", 14, "bold"))
        txtPrice.grid(row=2, column=3)

        # Quant.
        LblQuant = tk.Label(DataFrameLeft, font=("arial", 15, "bold"), text="Product Quant: ", padx=2)
        LblQuant.grid(row=3, column=2, sticky="w")
        txtQuant = tk.Entry(DataFrameLeft, textvariable=self.med_quan, bd=3, relief=tk.RIDGE, width=32,
                            font=("arial", 14, "bold"))
        txtQuant.grid(row=3, column=3)


        ##Right Side Data Frame

        # refNo
        LblrefNo = tk.Label(DataFrameRight, font=("arial", 15, "bold"), text="Refrence Number: ", padx=2)
        LblrefNo.grid(row=0, column=0, sticky="w")
        txtrefNo = tk.Entry(DataFrameRight, textvariable=self.ref_med, bd=3, relief=tk.RIDGE, width=32,
                            font=("arial", 14, "bold"))
        txtrefNo.grid(row=0, column=1)

        # MedName
        LblMedName = tk.Label(DataFrameRight, font=("arial", 15, "bold"), text="Medicine Name: ", padx=2)
        LblMedName.grid(row=1, column=0, sticky="w")
        txtMedName = tk.Entry(DataFrameRight, textvariable=self.add_med, bd=3, relief=tk.RIDGE, width=32,
                              font=("arial", 14, "bold"))
        txtMedName.grid(row=1, column=1)

        ##----------Side Frame----------------------
        SideFrame = Frame(DataFrameRight, bd=4, relief=tk.RIDGE, bg="white")
        SideFrame.place(x=0, y=150, width=400, height=160)

        sc_x = ttk.Scrollbar(SideFrame, orient=tk.HORIZONTAL)
        sc_x.pack(side=tk.BOTTOM, fill="x")

        sc_y = ttk.Scrollbar(SideFrame, orient=tk.VERTICAL)
        sc_y.pack(side=tk.RIGHT, fill="y")

        self.medicine_table = ttk.Treeview(SideFrame, column=("ref", "medname"), xscrollcommand=sc_x.set,
                                           yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill="both", expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        # ##-----------------Med Add. Frame----------------------

        down_frame = Frame(DataFrameRight, bd=4, relief=tk.RIDGE, bg="black")
        down_frame.place(x=10, y=70, width=390, height=60)

        btnAdd = tk.Button(down_frame, text="Add", command=addInfo, font=("arial", 12, "bold"), bg="darkgreen")
        btnAdd.grid(row=0, column=0, padx=15, pady=10)

        btnUp = tk.Button(down_frame, text="Update", command=updateInfo, font=("arial", 12, "bold"), bg="darkgreen")
        btnUp.grid(row=0, column=1, padx=10)

        btnDel = tk.Button(down_frame, text="Delete", command=deleteInfo, font=("arial", 12, "bold"), bg="darkgreen")
        btnDel.grid(row=0, column=2, padx=10)

        btnClr = tk.Button(down_frame, text="Clear", command=clearInfo, font=("arial", 12, "bold"), bg="darkgreen")
        btnClr.grid(row=0, column=3, padx=10)

        # Down FRAMe
        DownFrame = Frame(self.root, bd=15, relief=tk.RIDGE)
        DownFrame.place(x=0, y=590, width=1435, height=190)

        # Table FRAMe
        TableFrame = Frame(DownFrame, bd=4, relief=tk.RIDGE)
        TableFrame.place(x=0, y=1, width=1400, height=160)

        # TableFrame=Frame(self.root, bd=15, relief=tk.RIDGE)
        # TableFrame.place(x=0, y=590, width=1435, height=190)

        scroll_x = ttk.Scrollbar(TableFrame, orient=tk.HORIZONTAL)
        scroll_x.pack(side=tk.BOTTOM, fill="x")

        scroll_y = ttk.Scrollbar(TableFrame, orient=tk.VERTICAL)
        scroll_y.pack(side=tk.RIGHT, fill="y")

        self.pharmacy_table = ttk.Treeview(TableFrame,
                                           column=("reg", "companyName", "type", "tabletNm",
                                                   "lotNo", "issueDate", "expDate", "uses", "sideEffect",
                                                   "dosage","precaution", "price", "quan"),
                                           xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("reg", text="Reference No.")
        self.pharmacy_table.heading("companyName", text="Company Name")
        self.pharmacy_table.heading("type", text="Med. Type")
        self.pharmacy_table.heading("tabletNm", text="Med. Name")
        self.pharmacy_table.heading("lotNo", text="Lot No.")
        self.pharmacy_table.heading("issueDate", text="Issue Date")
        self.pharmacy_table.heading("expDate", text="Expiry Date")
        self.pharmacy_table.heading("uses", text="Uses")
        self.pharmacy_table.heading("sideEffect", text="Side Effect")
        self.pharmacy_table.heading("dosage", text="Dosage")
        self.pharmacy_table.heading("precaution", text="Precaution")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("quan", text="Quantity")

        self.pharmacy_table.pack(fill="both", expand=1)

        self.pharmacy_table.column("reg", width=100)
        self.pharmacy_table.column("companyName", width=100)
        self.pharmacy_table.column("type", width=100)
        self.pharmacy_table.column("tabletNm", width=100)
        self.pharmacy_table.column("lotNo", width=100)
        self.pharmacy_table.column("issueDate", width=100)
        self.pharmacy_table.column("expDate", width=100)
        self.pharmacy_table.column("uses", width=100)
        self.pharmacy_table.column("sideEffect", width=100)
        self.pharmacy_table.column("dosage", width=100)
        self.pharmacy_table.column("precaution", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.column("quan", width=100)

        fetchInfo()
        self.pharmacy_table.bind("<<TreeviewSelect>>", onPharmacyTableSelect)







    def exit(self):
        self.root.quit()


root = tk.Tk()
app = PharmacyManSys(root)
root.mainloop()




