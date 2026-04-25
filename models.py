from datetime import datetime

class Patient:
    def __init__(self, pid, name, age, gender):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.admissions = []

    def add_admission(self, admission):
        self.admissions.append(admission)

    def display(self):
        return f"{self.pid:<5} {self.name:<15} {self.age:<5} {self.gender:<10}"


class Ward:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []

    def has_space(self):
        return len(self.patients) < self.capacity

    def add_patient(self, patient):
        if self.has_space():
            self.patients.append(patient)
            return True
        return False

    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)


class Admission:
    def __init__(self, pid, ward, admit_date):
        self.pid = pid
        self.ward = ward
        self.admit_date = admit_date
        self.discharge_date = None

    def discharge(self):
        self.discharge_date = datetime.now()

    def stay_length(self):
        if self.discharge_date:
            return max(1, (self.discharge_date - self.admit_date).days)
        return 0


class Billing:
    def __init__(self, pid, ward, days, rate):
        self.pid = pid
        self.ward = ward
        self.days = days
        self.rate = rate

    def total(self):
        return self.days * self.rate
