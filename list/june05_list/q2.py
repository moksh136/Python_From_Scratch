"""
=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92"""
n = int(input("Enter number of students: "))

students = []

for i in range(n):
    roll_no, name, course, marks = input().split()
    students.append([int(roll_no), name, course, int(marks)])

# Display all students
print("\nAll Student Details:")
for s in students:
    print(s[0], s[1], s[2], s[3])

# Find topper
topper = students[0]

for s in students:
    if s[3] > topper[3]:
        topper = s

print("\nTopper:")
print(topper[0], topper[1], topper[2], topper[3])

# Count students above 80
count = 0

for s in students:
    if s[3] > 80:
        count += 1

print("\nStudents Above 80:")
print(count)

# Average marks
total = 0

for s in students:
    total += s[3]

average = total / n

print("\nAverage Marks:")
print(average)

# Course-wise students
course_name = input("\nEnter course: ")

print(f"\nStudents in {course_name} Course:")

for s in students:
    if s[2].lower() == course_name.lower():
        print(s[0], s[1], s[2], s[3])