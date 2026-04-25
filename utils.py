def validate_patient(pid, name, age, gender):
    if not pid:
        return False, "Invalid ID"
    if not name.strip():
        return False, "Name required"
    if age <= 0:
        return False, "Invalid age"
    if gender.lower() not in ['male', 'female', 'other']:
        return False, "Invalid gender"
    return True, "Valid"
