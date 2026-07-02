# List to store doctor records
doctors = []


def add_doctor():
    doctor = {}

    doctor["id"] = input("Enter Doctor ID: ")
    doctor["name"] = input("Enter Doctor Name: ")
    doctor["specialization"] = input("Enter Specialization: ")
    doctor["experience"] = int(input("Enter Experience (Years): "))
    doctor["fees"] = float(input("Enter Consultation Fees: "))

    doctors.append(doctor)

    print("\nDoctor Added Successfully.\n")


def display_doctors():
    if len(doctors) == 0:
        print("\nNo Doctor Records Found.\n")
        return

    print("\n========== Doctor List ==========")

    for doctor in doctors:
        print(f"Doctor ID          : {doctor['id']}")
        print(f"Doctor Name        : {doctor['name']}")
        print(f"Specialization     : {doctor['specialization']}")
        print(f"Experience         : {doctor['experience']} Years")
        print(f"Consultation Fees  : ₹{doctor['fees']}")
        print("-" * 40)