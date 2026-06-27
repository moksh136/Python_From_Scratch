"""
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5"""
s = input("Enter complaint:")
"""s1= s.split()
print("Total words:", len(s1))"""
count= 1
for ch in s:
    if ch == " ":
        count+=1
print("Total words:", count)

