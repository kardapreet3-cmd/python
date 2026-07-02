from datetime import date
class Hospital:
    hospital_name="Birla hospital"
    hospital_address="Udipur"
    hospital_id=2208
    def __init__(self, patient_id, name, age, disease,gender,mobile_no,doctor_name,emergency):
        self.patient_id = patient_id
        self.patient_name = name
        self.patient_age = age
        self.patient_disease = disease
        self.gender = gender
        self.mobile_no = mobile_no
        self.doctor_name = doctor_name
        self.emergency =  emergency
        self.admission = input("Is the patient admitted? (yes/no): ")

    def admit(self):

        if self.admission.lower() == "yes":
            print("\nAdmission Status : Admitted")
            print("Room Allotted :", self.room_no)
        else:
            print("\nPatient is not admitted.")
    def discharge(self):
        print(f"after {self.days} you will discharged.")
        print(f"------After {self.days} days------")
        print("\nDischarge Status : Discharged")
        print(self.patient_name, "patient has been discharged.")
        print(self.patient_name, "patient health is good now!!")
    def display(self):
        print("\n----- Patient Details -----")
        print("Hospital Name: ", self.hospital_name)
        print("Hospital Address: ", self.hospital_address)
        print("Hospital ID: ", self.hospital_id)
        print("Patient ID: ", self.patient_id)
        print("Patient name: ", self.patient_name)
        print("Patient age: ", self.patient_age)
        print("Patient disease",self.patient_disease)
        print("Patient gender",self.gender)
        print("Patient mobile no: ", self.mobile_no)
        print("Patient doctor name: ", self.doctor_name)
        print("Emergency :", self.emergency)
class In_patient(Hospital):

    def __init__(self, patient_id, name, age, disease, gender,
                 mobile_no, doctor_name,emergency):

        super().__init__(patient_id, name, age, disease,
                         gender, mobile_no, doctor_name,emergency)
        if self.admission.lower() == "yes":
            self.room_type = input("Enter Room Type (AC/Non-AC): ")
            self.room_no = int(input("Enter Room Number: "))
            self.days = int(input("Enter Number of Days: "))
            if self.room_type.upper() == "AC":
                self.room_charge = 3000
            else:
                self.room_charge = 1500
            self.room_bill = self.room_charge * self.days
            self.medicine_bill = float(input("Enter Medicine Bill: "))
            self.total_bill = self.room_bill + self.medicine_bill
            if self.patient_age >= 60:
                self.discount = self.total_bill * 0.10
            else:
                self.discount = 0

            self.final_bill = self.total_bill - self.discount
            self.payment = input("Payment Done? (Yes/No): ")
            self.admission_date = date.today()
        else:
            self.room_type = "Not Allotted"
            self.room_no = "-"
            self.days = 0
            self.room_charge = 0
            self.bill
    def display(self):
        super().display()
        print("\n----- Patient Details -----")
        print("Patient Name :", self.patient_name)
        print("Disease :", self.patient_disease)
        print("Admission Status :", self.admission)
        print("=======================================")
        if self.admission.lower() == "yes":
            print("\n========== IN-PATIENT REPORT ==========")
            print("Admission Status :", self.admission)
            print("Admission Date   :", self.admission_date)
            print("Room Type        :", self.room_type)
            print("Room Number      :", self.room_no)
            print("Days Stayed      :", self.days)
            print("Room Bill        : ₹", self.room_bill)
            print("Medicine Bill    : ₹", self.medicine_bill)
            print("Discount         : ₹", self.discount)
            print("Final Bill       : ₹", self.final_bill)
            print("Payment Status   :", self.payment)
            print("=======================================")
        else:
            print("Patient is not admitted.")
            print("No room allotted.")
patient_id = int(input("Enter Patient ID: "))
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
disease = input("Enter Disease: ")
gender = input("Enter Gender(female/male/other): ")
mobile_no = input("Enter Mobile Number: ")
doctor_name = input("Enter Patient Doctor Name: ")
emergency=input("Is it an Emergency? (Yes/No): ")
p1 = In_patient(patient_id, name, age, disease, gender, mobile_no, doctor_name,emergency)
p1.admit()
p1.display()
if p1.admission.lower() == "yes":
    p1.discharge()
else:
    print("\nPatient is not admitted, so discharge is not possible.")