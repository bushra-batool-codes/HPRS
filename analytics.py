import pandas as pd
import numpy as np
import os
from storage import BILL_FILE, ADMISSION_FILE


def average_stay(admissions):
    stays = [a.stay_length() for a in admissions if a.stay_length() > 0]
    return np.mean(stays) if stays else 0


def ward_occupancy(wards):
    return {w.name: (len(w.patients) / w.capacity) * 100 for w in wards}


def monthly_expense():
    if not os.path.exists(BILL_FILE):
        return None
    df = pd.read_csv(BILL_FILE)
    return df.groupby("Ward").sum()


def peak_admissions():
    if not os.path.exists(ADMISSION_FILE):
        return None
    df = pd.read_csv(ADMISSION_FILE)
    df['Admit'] = pd.to_datetime(df['Admit'])
    return df['Admit'].dt.month.value_counts()
