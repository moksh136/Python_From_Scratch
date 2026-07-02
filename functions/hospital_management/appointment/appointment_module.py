# List to store appointments
appointments = []


def book_appointment():
    appointment = {}

    appointment["appointment_id"] = input("Enter Appointment ID: ")
    appointment["patient_id"] = input("Enter Patient ID: ")
    appointment["doctor_id"] = input("Enter Doctor ID: ")
    appointment["date"] = input("Enter Appointment Date (DD/MM/YYYY): ")
    appointment["time"] = input("Enter Appointment Time (HH:MM): ")

    appointments.append(appointment)

    print("\nAppointment Booked Successfully.\n")


def show_appointments():
    if len(appointments) == 0:
        print("\nNo Appointments Found.\n")
        return

    print("\n========== Appointment List ==========")

    for appointment in appointments:
        print(f"Appointment ID : {appointment['appointment_id']}")
        print(f"Patient ID     : {appointment['patient_id']}")
        print(f"Doctor ID      : {appointment['doctor_id']}")
        print(f"Date           : {appointment['date']}")
        print(f"Time           : {appointment['time']}")
        print("-" * 40)