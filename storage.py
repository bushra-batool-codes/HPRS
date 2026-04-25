import csv, os

PATIENT_FILE = "patients.csv"
BILL_FILE = "billing.csv"
ADMISSION_FILE = "admissions.csv"


def save_patients(patients):
    with open(PATIENT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Age", "Gender"])
        for p in patients:
            writer.writerow([p.pid, p.name, p.age, p.gender])


def save_admission(adm):
    file_exists = os.path.exists(ADMISSION_FILE)
    with open(ADMISSION_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["PID", "Ward", "Admit", "Discharge"])
        writer.writerow([adm.pid, adm.ward, adm.admit_date, adm.discharge_date])


def save_bill(bill):
    file_exists = os.path.exists(BILL_FILE)
    with open(BILL_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["PID", "Ward", "Amount"])
        writer.writerow([bill.pid, bill.ward, bill.total()])
