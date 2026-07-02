# List to store all patients
patients = []


def add_patient():
    patient = {}

    patient["id"] = input("Enter Patient ID: ")
    patient["name"] = input("Enter Patient Name: ")
    patient["age"] = int(input("Enter Age: "))
    patient["gender"] = input("Enter Gender: ")
    patient["disease"] = input("Enter Disease: ")
    patient["mobile"] = input("Enter Mobile Number: ")

    patients.append(patient)

    print("\nPatient Added Successfully.\n")


def display_patients():
    if len(patients) == 0:
        print("\nNo Patient Records Found.\n")
        return

    print("\n========== Patient List ==========")

    for patient in patients:
        print(f"Patient ID      : {patient['id']}")
        print(f"Name            : {patient['name']}")
        print(f"Age             : {patient['age']}")
        print(f"Gender          : {patient['gender']}")
        print(f"Disease         : {patient['disease']}")
        print(f"Mobile Number   : {patient['mobile']}")
        print("-" * 35)


def search_patient():
    pid = input("Enter Patient ID to Search: ")

    for patient in patients:
        if patient["id"] == pid:
            print("\nPatient Found\n")
            print(f"Patient ID      : {patient['id']}")
            print(f"Name            : {patient['name']}")
            print(f"Age             : {patient['age']}")
            print(f"Gender          : {patient['gender']}")
            print(f"Disease         : {patient['disease']}")
            print(f"Mobile Number   : {patient['mobile']}")
            return

    print("\nPatient Not Found.\n")