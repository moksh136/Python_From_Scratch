"""
2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP"""
s = input()
words = s.split()
res = ""
for i in range((len(words)-1), -1 , -1):
    word = words[i]
    rev = ""
    for i in range ((len(word)-1), -1 , -1):
        rev+=word[i]
    res= res + rev + " "
print(res)