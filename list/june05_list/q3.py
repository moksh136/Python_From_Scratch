"""====================================================================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2"""
n = int(input("Enter number of patients: "))

patients = []

for i in range(n):
    patient_id, patient_name, age, disease = input().split()
    patients.append([patient_id, patient_name, int(age), disease])

# Display all patients
print("\nAll Patient Details:")
for p in patients:
    print(p[0], p[1], p[2], p[3])

# Search Patient by ID
search_id = input("\nEnter Patient ID: ")

found = False

for p in patients:
    if p[0] == search_id:
        print("\nPatient Found:")
        print(p[0], p[1], p[2], p[3])
        found = True
        break

if not found:
    print("\nPatient Not Found")

# Patients Above 60
print("\nPatients Above 60:")

for p in patients:
    if p[2] > 60:
        print(p[0], p[1], p[2], p[3])

# Count patients with a disease
disease_name = input("\nEnter Disease: ")

count = 0

for p in patients:
    if p[3].lower() == disease_name.lower():
        count += 1

print(f"\nPatients with {disease_name}:")
print(count)