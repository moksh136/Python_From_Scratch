"""2.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------

Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101  Ajay
105  Neha
112  Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System"""
students = {}
while True:
    print("      STUDENT MANAGEMENT SYSTEM")
    print("1. Add New Student")
    print("2. Search Student")
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Total Students")
    print("7. Display Students By Course")
    print("8. Display Students By City")
    print("9. Find Student Paying Highest Fees")
    print("10. Find Student Paying Lowest Fees")
    print("11. Exit")
    choice = int(input("Enter Your Choice : "))
    match choice:
        case 1:
            sid = int(input("Enter Student ID : "))
            if sid in students:
                print("Student ID Already Exists")
            else:
                name = input("Enter Name : ")
                course = input("Enter Course : ")
                mobile = input("Enter Mobile Number : ")
                fees = int(input("Enter Fees : "))
                city = input("Enter City : ")
                students[sid] = {
                    "name": name,
                    "course": course,
                    "mobile": mobile,
                    "fees": fees,
                    "city": city
                }
                print("Student Added Successfully")
        case 2:
            sid = int(input("Enter Student ID : "))
            if sid in students:
                print("Student ID :", sid)
                print("Name       :", students[sid]["name"])
                print("Course     :", students[sid]["course"])
                print("Mobile     :", students[sid]["mobile"])
                print("Fees       :", students[sid]["fees"])
                print("City       :", students[sid]["city"])
            else:
                print("Student Not Found")
        case 3:
            sid = int(input("Enter Student ID : "))
            if sid in students:
                new_course = input("Enter New Course : ")
                students[sid]["course"] = new_course
                print("Course Updated Successfully")
            else:
                print("Student Not Found")
        case 4:
            sid = int(input("Enter Student ID : "))
            if sid in students:
                del students[sid]
                print("Student Deleted Successfully")
            else:
                print("Student Not Found")
        case 5:
            if len(students) == 0:
                print("No Student Records")
            else:
                for sid in students:
                    print("----------------------------------")
                    print("Student ID :", sid)
                    print("Name       :", students[sid]["name"])
                    print("Course     :", students[sid]["course"])
                    print("Mobile     :", students[sid]["mobile"])
                    print("Fees       :", students[sid]["fees"])
                    print("City       :", students[sid]["city"])
                    print("----------------------------------")
        case 6:
            print("Total Students :", len(students))
        case 7:
            course = input("Enter Course : ")
            found = False
            for sid in students:
                if students[sid]["course"].lower() == course.lower():
                    print(sid, students[sid]["name"])
                    found = True
            if found == False:
                print("No Students Found")
        case 8:
            city = input("Enter City : ")
            found = False
            for sid in students:
                if students[sid]["city"].lower() == city.lower():
                    print(sid, students[sid]["name"])
                    found = True
            if found == False:
                print("No Students Found")
        case 9:

            if len(students) == 0:
                print("No Student Records")
            else:
                max_fee = -1
                highest = 0
                for sid in students:
                    if students[sid]["fees"] > max_fee:
                        max_fee = students[sid]["fees"]
                        highest = sid
                print("\nHighest Fee Paying Student")
                print("Student ID :", highest)
                print("Name       :", students[highest]["name"])
                print("Course     :", students[highest]["course"])
                print("Mobile     :", students[highest]["mobile"])
                print("Fees       :", students[highest]["fees"])
                print("City       :", students[highest]["city"])
        case 10:
            if len(students) == 0:
                print("No Student Records")
            else:
                min_fee = 999999999
                lowest = 0
                for sid in students:
                    if students[sid]["fees"] < min_fee:
                        min_fee = students[sid]["fees"]
                        lowest = sid
                print("\nLowest Fee Paying Student")
                print("Student ID :", lowest)
                print("Name       :", students[lowest]["name"])
                print("Course     :", students[lowest]["course"])
                print("Mobile     :", students[lowest]["mobile"])
                print("Fees       :", students[lowest]["fees"])
                print("City       :", students[lowest]["city"])
        case 11:
            print("Thank You For Using Student Management System")
            break
        case _:
            print("Invalid Choice")