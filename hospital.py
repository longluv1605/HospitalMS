from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
import time
import datetime
import config


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1530x800+0+0")

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.Patientname = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        lbltitle = Label(
            self.root,
            bd=20,
            relief=RIDGE,
            text="HOSPITAL MANAGEMENT SYSTEM",
            fg="red",
            bg="white",
            font=("times new roman", 50, "bold"),
        )
        lbltitle.pack(side=TOP, fill=X)

        # ==========================================Dataframe================================================================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE, bg="red")
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(
            Dataframe,
            bd=10,
            relief=RIDGE,
            padx=10,
            font=("times new roman", 12, "bold"),
            text="Patient Information",
        )

        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(
            Dataframe,
            bd=10,
            relief=RIDGE,
            padx=10,
            font=("times new roman", 12, "bold"),
            text="Prescription",
        )

        DataframeRight.place(x=990, y=5, width=460, height=350)

        # ===========================================Buttons frame===============================================================

        Buttonframe = Frame(self.root, bd=13, relief=RIDGE, padx=23, bg="red")
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ============================================ Details frame =====================================================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # =============================================DataframeLeft=======================================================

        lblNameTablet = Label(
            DataframeLeft,
            text="Names Of tablets",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNametablet = ttk.Combobox(
            DataframeLeft,
            textvariable=self.Nameoftablets,
            state="readonly",
            font=("arial", 12, "bold"),
            width=33,
        )
        comNametablet["value"] = (
            "Nice",
            "Corona Vacacine",
            "Acetaminophen",
            "Adderall",
            "Amlodipine",
            "Ativan",
        )
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref = Label(
            DataframeLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2
        )
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(
            DataframeLeft, font=("arial", 13, "bold"), textvariable=self.ref, width=35
        )
        txtref.grid(row=1, column=1)

        lblDose = Label(
            DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4
        )
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(
            DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Dose, width=35
        )
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="No Of Tablets:",
            padx=2,
            pady=6,
        )
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(
            DataframeLeft,
            font=("arial", 13, "bold"),
            textvariable=self.NumberofTablets,
            width=35,
        )
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(
            DataframeLeft, font=("arial", 12, "bold"), text="lot:", padx=2, pady=6
        )
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(
            DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Lot, width=35
        )
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Issue Date:",
            padx=2,
            pady=6,
        )
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(
            DataframeLeft,
            font=("arial", 13, "bold"),
            textvariable=self.Issuedate,
            width=35,
        )
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(
            DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6
        )
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(
            DataframeLeft,
            font=("arial", 13, "bold"),
            textvariable=self.ExpDate,
            width=35,
        )
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Daily Dose:",
            padx=2,
            pady=4,
        )
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(
            DataframeLeft,
            font=("arial", 13, "bold"),
            textvariable=self.DailyDose,
            width=35,
        )
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Side Effect:",
            padx=2,
            pady=6,
        )
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(
            DataframeLeft,
            font=("arial", 13, "bold"),
            textvariable=self.sideEffect,
            width=35,
        )
        txtSideEffect.grid(row=8, column=1)

        lblFutherinfo = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Futher information:",
            padx=2,
        )
        lblFutherinfo.grid(row=0, column=2, sticky=W)
        txtFutherinfo = Entry(
            DataframeLeft,
            font=("arial", 12, "bold"),
            textvariable=self.FurtherInformation,
            width=35,
        )
        txtFutherinfo.grid(row=0, column=3)

        lblDrivingMachine = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Blood Pressure:",
            padx=2,
            pady=6,
        )
        lblDrivingMachine.grid(row=1, column=2, sticky=W)
        txtDrivingMachine = Entry(
            DataframeLeft,
            font=("arial", 12, "bold"),
            textvariable=self.DrivingUsingMachine,
            width=35,
        )
        txtDrivingMachine.grid(row=1, column=3)

        lblStorage = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Storage Advice:",
            padx=2,
            pady=6,
        )
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(
            DataframeLeft,
            font=("arial", 12, "bold"),
            textvariable=self.StorageAdvice,
            width=35,
        )
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Medication:",
            padx=2,
            pady=6,
        )
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(
            DataframeLeft,
            font=("arial", 12, "bold"),
            textvariable=self.HowToUseMedication,
            width=35,
        )
        txtMedicine.grid(row=3, column=3, sticky=W)

        lblPatientId = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Patient Id:",
            padx=2,
            pady=6,
        )
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(
            DataframeLeft,
            font=("arial", 12, "bold"),
            textvariable=self.PatientId,
            width=35,
        )
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="NHS Number:",
            padx=2,
            pady=6,
        )
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(
            DataframeLeft,
            font=("arial", 12, "bold"),
            textvariable=self.nhsNumber,
            width=35,
        )
        txtNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Patient name:",
            padx=2,
            pady=6,
        )
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname = Entry(
            DataframeLeft,
            font=("arial", 12, "bold"),
            textvariable=self.Patientname,
            width=35,
        )
        txtPatientname.grid(row=6, column=3)

        lblDateOfBirth = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Date Of Birth:",
            padx=2,
            pady=6,
        )
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(
            DataframeLeft,
            font=("arial", 12, "bold"),
            textvariable=self.DateOfBirth,
            width=35,
        )
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(
            DataframeLeft,
            font=("arial", 12, "bold"),
            text="Patient Address:",
            padx=2,
            pady=6,
        )
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(
            DataframeLeft,
            font=("arial", 12, "bold"),
            textvariable=self.PatientAddress,
            width=35,
        )
        txtPatientAddress.grid(row=8, column=3)

        # ===================================================DataframeRight=============================
        self.txtPrescription = Text(
            DataframeRight,
            font=("arial", 12, "bold"),
            width=45,
            height=16,
            padx=2,
            pady=6,
        )
        self.txtPrescription.grid(row=0, column=0)

        # ==================================================Buttons==========================================
        btnPrescription = Button(
            Buttonframe,
            command=self.iPrectioption,
            text="Presciption",
            bg="red",
            fg="white",
            font=("arial", 12, "bold"),
            width=23,
            padx=2,
            pady=6,
        )
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(
            Buttonframe,
            command=self.iPrescriptionData,
            text="Presciption Data",
            bg="red",
            fg="white",
            font=("arial", 12, "bold"),
            width=23,
            padx=2,
            pady=6,
        )
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(
            Buttonframe,
            command=self.update_data,
            text="Update",
            bg="red",
            fg="white",
            font=("arial", 12, "bold"),
            width=23,
            padx=2,
            pady=6,
        )
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(
            Buttonframe,
            command=self.idelete,
            text="Delete",
            bg="red",
            fg="white",
            font=("arial", 12, "bold"),
            width=23,
            padx=2,
            pady=6,
        )
        btnDelete.grid(row=0, column=3)

        btnClear = Button(
            Buttonframe,
            command=self.clear,
            text="Clear",
            bg="red",
            fg="white",
            font=("arial", 12, "bold"),
            width=23,
            padx=2,
            pady=6,
        )
        btnClear.grid(row=0, column=4)

        btnExit = Button(
            Buttonframe,
            command=self.iExit,
            text="Exit",
            bg="red",
            fg="white",
            font=("arial", 12, "bold"),
            width=23,
            padx=2,
            pady=6,
        )
        btnExit.grid(row=0, column=5)

        # ==============================================Table=================================================
        # ===============================================Scrollbar============================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(
            Detailsframe,
            column=(
                "nameoftable",
                "ref",
                "dose",
                "nooftablets",
                "lot",
                "issuedate",
                "expdate",
                "dailydose",
                "storage",
                "nhsnumber",
                "pname",
                "dob",
                "address",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable", text="Name Of Table")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fatch_data()

        # =================================Functinality Declration=====================================================

    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(
                host=config.host,
                username=config.username,
                password=config.password,
                database=config.database,
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.Patientname.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get(),
                ),
            )
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def update_data(self):
        conn = mysql.connector.connect(
            host=config.host,
            username=config.username,
            password=config.password,
            database=config.database,
        )
        my_cursor = conn.cursor()
        my_cursor.execute(
            "update hospital set Nameoftablets=%s, dose=%s, Numbersoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s where Reference_No=%s",
            (
                self.Nameoftablets.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.Patientname.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.ref.get(),
            ),
        )
        conn.commit()
        self.fatch_data()
        messagebox.showinfo("Success", "Record has been updated")

    def fatch_data(self):
        conn = mysql.connector.connect(
            host=config.host,
            username=config.username,
            password=config.password,
            database=config.database,
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital limit 50")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.Patientname.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrectioption(self):
        self.txtPrescription.insert(
            END, "Name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n"
        )
        self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(
            END, "Number Of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n"
        )
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(
            END, "Issue Date:\t\t\t" + self.Issuedate.get() + "\n"
        )
        self.txtPrescription.insert(END, "Exp date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(
            END, "daily Dose:\t\t\t" + self.DailyDose.get() + "\n"
        )
        self.txtPrescription.insert(
            END, "Side Effect:\t\t\t" + self.sideEffect.get() + "\n"
        )
        self.txtPrescription.insert(
            END, "Further Information:\t\t\t" + self.FurtherInformation.get() + "\n"
        )
        self.txtPrescription.insert(
            END, "StorageAdvice:\t\t\t" + self.StorageAdvice.get() + "\n"
        )
        self.txtPrescription.insert(
            END, "DrivingUsingMachine:\t\t\t" + self.DrivingUsingMachine.get() + "\n"
        )
        self.txtPrescription.insert(
            END, "PatientId:\t\t\t" + self.PatientId.get() + "\n"
        )
        self.txtPrescription.insert(
            END, "NHSNumber:\t\t\t" + self.nhsNumber.get() + "\n"
        )
        self.txtPrescription.insert(
            END, "PatientName:\t\t\t" + self.Patientname.get() + "\n"
        )
        self.txtPrescription.insert(
            END, "DateOfBirth:\t\t\t" + self.DateOfBirth.get() + "\n"
        )
        self.txtPrescription.insert(
            END, "PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n"
        )

    def idelete(self):
        conn = mysql.connector.connect(
            host=config.host,
            username=config.username,
            password=config.password,
            database=config.database,
        )
        my_cursor = conn.cursor()
        query = "delete from hospital where Reference_No=%s"
        value = (self.ref.get(),)
        my_cursor.execute(query, value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete", "Patient has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.Patientname.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.set("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno(
            "Hospital managemnt system", "Confirm you want to exit"
        )
        if iExit > 0:
            root.destroy()
            return


root = Tk()
test = Hospital(root)
root.resizable(0, 0)
root.mainloop()
