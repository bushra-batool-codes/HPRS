from models import Patient, Ward, Admission, Billing
from utils import validate_patient
from storage import save_patients, save_admission, save_bill
from analytics import average_stay, ward_occupancy, peak_admissions
from visualization import plot_bar, plot_pie, plot_line
from datetime import datetime


def main():
    patients = []
    admissions = []
    ids = set()

    wards = [Ward("General", 3), Ward("ICU", 2), Ward("Private", 2)]
    rates = {"General": 500, "ICU": 2000, "Private": 1500}

    while True:
        print("\n1.Add 2.View 3.Search 4.Admit 5.Discharge 6.Analytics 7.Exit")
        ch = input("Choice: ")

        # ADD PATIENT
        if ch == '1':
            pid = input("ID: ")
            name = input("Name: ")

            try:
                age = int(input("Age: "))
            except ValueError:
                print("Invalid age")
                continue

            gender = input("Gender: ")

            v, msg = validate_patient(pid, name, age, gender)
            if not v:
                print(msg)
                continue

            if pid in ids:
                print("Duplicate ID")
                continue

            p = Patient(pid, name, age, gender)
            patients.append(p)
            ids.add(pid)
            print("Patient added successfully")

        # VIEW
        elif ch == '2':
            for p in patients:
                print(p.display())

        # SEARCH (ID + NAME)
        elif ch == '3':
            key = input("Enter ID or Name: ").lower()
            found = False
            for p in patients:
                if p.pid == key or key in p.name.lower():
                    print(p.display())
                    found = True
            if not found:
                print("No patient found")

        # ADMIT
        elif ch == '4':
            pid = input("Enter ID: ")
            p = next((x for x in patients if x.pid == pid), None)

            if not p:
                print("Patient not found")
                continue

            print("Select Ward:")
            for i, w in enumerate(wards):
                print(i + 1, w.name)

            try:
                choice = int(input("Choice: ")) - 1
            except ValueError:
                print("Invalid input")
                continue

            if choice < 0 or choice >= len(wards):
                print("Invalid ward choice")
                continue

            w = wards[choice]

            if w.add_patient(p):
                adm = Admission(pid, w.name, datetime.now())
                p.add_admission(adm)
                admissions.append(adm)
                save_admission(adm)
                print("Admitted to", w.name)
            else:
                print("No beds available")

        # DISCHARGE
        elif ch == '5':
            pid = input("Enter ID: ")
            adm_list = [a for a in admissions if a.pid == pid and not a.discharge_date]

            if not adm_list:
                print("No active admission")
                continue

            adm = adm_list[-1]
            adm.discharge()

            days = adm.stay_length()
            bill = Billing(pid, adm.ward, days, rates[adm.ward])
            save_bill(bill)

            for w in wards:
                if w.name == adm.ward:
                    patient_obj = next(p for p in patients if p.pid == pid)
                    w.remove_patient(patient_obj)

            print("\n🧾 BILL SUMMARY")
            print(f"Patient ID : {pid}")
            print(f"Ward       : {adm.ward}")
            print(f"Days       : {days}")
            print(f"Rate/day   : ₹{rates[adm.ward]}")
            print(f"Total Bill : ₹{bill.total()}\n")

        # ANALYTICS
        elif ch == '6':
            print("Average Stay:", average_stay(admissions))
            print("Total Patients:", len(patients))

            occ = ward_occupancy(wards)
            print("Occupancy:", occ)

            plot_bar(occ)
            plot_pie(occ)

            series = peak_admissions()
            if series is not None:
                plot_line(series)

            print("Charts generated")

        # EXIT
        elif ch == '7':
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == 'y':
                save_patients(patients)
                print("Data saved. Exiting...")
                break

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()

