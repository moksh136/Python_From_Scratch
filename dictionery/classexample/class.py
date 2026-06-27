"""d = {1:"deepika", 2:"ram", 3: "virat"}
print(d)
d1 = dict(a="qbd", b = "ghb", c = "nkd")
print(d1)"""
#accessing key values
"""student = {
    "name":"salluu",
    "age": 33,d
    "city":"hyderabad"
}
print(student)
print(student["name"])
print(student.get("name"))
print(student.get("sal", "not found"))"""
#-----------------------------------------------
"""d = {}
n = int(input("enter no of student:"))
i = 1
while i<=n:
    name = input("enter name:")
    marks = input("enter % of studet:")
    d[name]= marks
    i+=1
print("name of student","\t","% of student ")
for x in d:
    print(x, "\t\t", d[x])"""
#----------------------------------------------
#adding and updating dict item
"""d = {1:"dipi", 2:"riou"}
print(d)
d[3]="virat"
print(d)
d[1] = "ram"
print(d)"""
#removing elememt
#pop(): 
"""stu = {"name":"dipita", "age":30, "city":"chennai"}
print(stu)
print(stu.pop("city")) #it shows removed value
print(stu.pop("add"))#it give an error
print(stu)"""
#popitem():
"""stu = {"name":"dipita", "age":30, "city":"chennai"}
print(stu.popitem()) #it return key value pair in form of tuple
print(stu)
#___________________________________________________________
while stu:
    print(stu.popitem())# it runs untill dict is being empty"""
#del :
"""stu = {"name":"dipita", "age":30, "city":"chennai"}
del stu["age"] # it remove key value pair from dict
del stu["add"] # it gives error
# safe way to delete any key in dict
if "add" in stu:
    del stu["add"]
del stu #it delete entire dicctioner
print(stu)"""
#clear():
"""stu = {"name":"dipita", "age":30, "city":"chennai"}
stu.clear()
print(stu) #it clear all the value from the dict"""

#method in dict
#keys()
"""stu = {"name":"dipita", "age":30, "city":"chennai"}
print(stu.keys()) #it give all the key of dict
print(list(stu.keys()))
print(set(stu.keys()))"""


#values
"""stu = {"name":"dipita", "age":30, "city":"chennai"}
print(stu.values()) #it give all the values"""

#items():
"""stu = {"name":"dipita", "age":30, "city":"chennai"}
print(stu.items()) # it gives key and value in tuple form
for key,value in stu.items():
    print(key, value)"""

#update()
"""stu = {"name":"dipita", "age":30, "city":"chennai"}
stu.update({"sal":30000})  # it adds the key and value in dict
stu.update({"city":"indore"}) # if key already exist than value will be updated
print(stu) """

#copy()
"""stu = {"name":"dipita", "age":30, "city":"chennai"}
s1 = stu.copy()
print(s1)"""

"""stu = {"name":"dipita", "age":30, "city":"chennai", "mark":[22,33]}
s1 = stu.copy()
s1["mark"][0] = 44
print(stu)
print(s1)"""
#import copy
#stu = {"name":"dipita", "age":30, "city":"chennai"}
#s1 = stu
#s1 = stu.copy()
#s1 = copy.deepcopy(stu)

#------------------------------------------------
#list comprehension 
#================================================
"""sq = {}
for i in range(1,6):
    sq[i] = i*i
print(sq)"""
"""sq = {i:i*i for i in range (1,6)}
print(sq)
# nested dictonary 

d = {
    101:{"name":"deepu","age":30},
    102:{"name":"deepesh","age":35},
    103:{"name":"vedant","age":20}

}


print(d[101])
print(d[102])
print(d[103])


print(d[101]["name"])
print(d[101]["name"][2])

# modification in nested dictonary

d[101]["name"]="hitesh"
print(d)




d = {
    101:{"name":"deepu","age":30},
    102:{"name":"deepesh","age":35},
    103:{"name":"vedant","age":20}
}
# add new member
d[104]={"name":"moksh","age":20}

print(d)



#  NESTED DICT LOOP

d = {
    101:{"name":"deepu","age":30},
    102:{"name":"deepesh","age":35},
    103:{"name":"vedant","age":20}
}

for k,v in d.items():
    print("ID:",k)
    for k1,v1 in v.items():
        print(k1, "=" ,v1)



company = {
    "emp1":{"name":"deepika","skill":["python","fullstack","java","react"]},
    "emp2":{"name":"deepesh","skill":["javafull stack","video editing"]}
}


print(company["emp1"])
print(company["emp1"]["skill"])
print(company["emp1"]["skill"][1])



response = {
"user":{
"id":101,
"profile":{"name":"deepu","email":"d@gmail.com"}
}
}


print(response["user"]["profile"]["email"])



# USE OF EVAL
d = eval(input("Enter Dictoanry: "))
print(d)
print(type(d))

d1 = input("Enter: ")
print(d1)
print(type(d1))




# WAP TO TACK DICT FROM THE KEY BORD AND PRINT SUM OF VALUES


d = eval(input("Enter Dictoanry: "))
print(d)

s = sum(d.values())
print(s)



# WAP TO TACK DICT FROM THE KEY BORD AND PRINT SUM OF VALUES

n = int(input("Enter Number of items: "))

d = {}

for i in range(n):
    key = input("Enter Key: ")
    value = int(input("Enter Value: "))
    d[key] = value


print(d)
print(sum(d.values()))



# WAP TO TACK DICT FROM THE KEY BORD AND PRINT SUM OF VALUES

n = int(input("Enter Number of items: "))

d = {}

for i in range(n):
    key = input("Enter Key: ")
    value = int(input("Enter Value: "))
    d[key] = value


print(d)
print(sum(d.values()))"""

#WAP to find no. of occurence of each letter present in the given string
"""word = input()
d = {}
for x in word:
    d[x] = d.get(x,0)+1
print(d)
for k, v in d.items():
    print(k, "occured", v , "times")"""


#WAP to find no of occurence of each vowel present in given string
"""word = input()
vowels = {'a', 'e', 'i', 'o', 'u'}
d = {}
for x in word:
    if x in vowels:
        d[x] = d.get(x,0)+1
print(d)
for k, v in d.items():
    print(k, "occured", v , "times")

#if you want result in sorted form than
for k, v in sorted(d.items()):
    print(k, "occured", v , "times")
"""
#WAP to how many time each user login the list
"""login = ["ram", "sid", "kid", "ram"]
d = {}
for user in login:
    d[user] = d.get(user, 0)+1
print(d)"""

#WAP to group words by length
"""word = ["deep", "sidu", "raman",  "suman"]
g = {}
for w in word:
    l = len(w)
    if l not in g:
        g[l]=[]
    g[l].append(w)
print(g)"""

#WAP to merge two dict and sum their values
d1 = {'goa':5, 'nepal':3, 'delhi':6}
d2 = {'goa':1, 'nepal':124, 'delhi':3000}
merge = d1.copy()
for k,v in d2.items():
    merge[k] = merge.get(k, 0)+v
print(merge)