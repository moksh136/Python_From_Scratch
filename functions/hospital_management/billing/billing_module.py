def generate_bill():
    print("\n========== Generate Bill ==========\n")

    patient_id = input("Enter Patient ID: ")

    consultation_charges = float(input("Enter Consultation Charges: "))
    medicine_cost = float(input("Enter Medicine Cost: "))
    test_charges = float(input("Enter Test Charges: "))

    total_bill = consultation_charges + medicine_cost + test_charges

    print("\n========== Hospital Bill ==========")
    print(f"Patient ID            : {patient_id}")
    print(f"Consultation Charges  : ₹{consultation_charges}")
    print(f"Medicine Cost         : ₹{medicine_cost}")
    print(f"Test Charges          : ₹{test_charges}")
    print("-" * 35)
    print(f"Total Bill            : ₹{total_bill}")
    print("=" * 35)