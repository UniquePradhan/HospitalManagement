from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root 
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="Red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # data frame making
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400,)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Prescriptions")
        DataFrameRight.place(x=990,y=5,width=500,height=350)

        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=520,width=1530,height=70)

        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=595,width=1530,height=180)

        #Data Frame Left Info
        

        lblName=Label(DataFrameLeft,text="Patient Name:",font=("times new roman",14,"bold"),padx=3,pady=8)
        lblName.grid(row=0,column=0)
        nametext=Entry(DataFrameLeft,font=("arial",11),width=40)
        nametext.grid(row=0,column=1)

        lblAddress=Label(DataFrameLeft,text="Patient Address:",font=("times new roman",14,"bold"),padx=3,pady=8)
        lblAddress.grid(row=1,column=0)
        addresstext=Entry(DataFrameLeft,font=("arial",11),width=40)
        addresstext.grid(row=1,column=1)

        lbldob=Label(DataFrameLeft,text="Date of birth:",font=("times new roman",14,"bold"),padx=3,pady=12)
        lbldob.grid(row=2,column=0)
        dobtext=Entry(DataFrameLeft,font=("arial",11),width=40)
        dobtext.grid(row=2,column=1)

        lblpatientid=Label(DataFrameLeft,text="Patient ID:",font=("times new roman",14,"bold"),padx=3,pady=12)
        lblpatientid.grid(row=3,column=0)
        patientidtext=Entry(DataFrameLeft,font=("arial",11),width=40)
        patientidtext.grid(row=3,column=1)

        lblAdmissionDate=Label(DataFrameLeft,text="Admission Date:",font=("times new roman",14,"bold"),padx=3,pady=12)
        lblAdmissionDate.grid(row=4,column=0)
        admissiondate_text=Entry(DataFrameLeft,font=("arial",11),width=40)
        admissiondate_text.grid(row=4,column=1)

        Symptoms_seen=Label(DataFrameLeft,text="Symptoms seen:",font=("times new roman",14,"bold"),padx=3,pady=12)
        Symptoms_seen.grid(row=5,column=0)
        Symptoms_seen_text=Entry(DataFrameLeft,font=("arial",11),width=40)
        Symptoms_seen_text.grid(row=5,column=1)

        Department=Label(DataFrameLeft,text="Department:",font=("times new roman",14,"bold"),padx=6,pady=12)
        Department.grid(row=0,column=2)
        combo_department=ttk.Combobox(DataFrameLeft,state="readonly",font=("times new roman",13,"bold"),width=30)
        combo_department['value']=("ENT","Internal Medicine","Gynaecology","Opthalmic","Orthopaedic","Pediatrics","Anesthesiology","ICU")
        combo_department.grid(row=0,column=3)

        Doctor=Label(DataFrameLeft,text="Doctor in charge:",font=("times new roman",14,"bold"),padx=6,pady=12)
        Doctor.grid(row=1,column=2)
        combo_doctor=ttk.Combobox(DataFrameLeft,state="readonly",font=("times new roman",13,"bold"),width=30)
        combo_doctor['value']=("Dr.Subodh","Dr.Sunil","Dr.Rachana","Dr.Bikesh","Dr.Surya","Dr.Ratna","Dr.Neeshma","Dr.Pranil")
        combo_doctor.grid(row=1,column=3)

        Medical_History=Label(DataFrameLeft,text="Medical History:",font=("times new roman",14,"bold"),padx=3,pady=12)
        Medical_History.grid(row=2,column=2)
        Medical_History_text=Entry(DataFrameLeft,font=("arial",11),width=36)
        Medical_History_text.grid(row=2,column=3)

        Diagnosis=Label(DataFrameLeft,text="Initial Diagnois:",font=("times new roman",14,"bold"),padx=3,pady=12)
        Diagnosis.grid(row=3,column=2)
        Diagnosis_text=Entry(DataFrameLeft,font=("arial",11),width=36)
        Diagnosis_text.grid(row=3,column=3)

        Allergic=Label(DataFrameLeft,text="Allergens to Patient:",font=("times new roman",14,"bold"),padx=3,pady=12)
        Allergic.grid(row=4,column=2)
        Allergic_text=Entry(DataFrameLeft,font=("arial",11),width=36)
        Allergic_text.grid(row=4,column=3)

        Followup=Label(DataFrameLeft,text="Followup Date:",font=("times new roman",14,"bold"),padx=3,pady=12)
        Followup.grid(row=5,column=2)
        Followup_text=Entry(DataFrameLeft,font=("arial",11),width=36)
        Followup_text.grid(row=5,column=3)

        







       

root=Tk()
ob=Hospital(root)
root.mainloop()


