"""QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
"""
n = int(input("Enter number of books: "))

books = []

for i in range(n):
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    price = int(input("Enter Price: "))

    books.append([book_id, title, author, price])

# Display all books
print("\nAll Book Details:")
for book in books:
    print(book[0], book[1], book[2], book[3])

# Most Expensive Book
expensive = books[0]

for book in books:
    if book[3] > expensive[3]:
        expensive = book

print("\nMost Expensive Book:")
print(expensive[0], expensive[1], expensive[2], expensive[3])

# Average Price
total = 0

for book in books:
    total += book[3]

average = total / n

print("\nAverage Book Price:")
print(average)

# Search by Author
author_name = input("\nEnter Author Name: ")

print(f"\nBooks Written By {author_name}:")

for book in books:
    if book[2].lower() == author_name.lower():
        print(book[0], book[1], book[2], book[3])