"""
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times"""
a = input("Enter product review ")

count = 0

for ch in a.lower():
    if ch in "o":
        count += 1

print("Character 'o' occurs", count)

