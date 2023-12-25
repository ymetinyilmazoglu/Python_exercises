###############################################
# Python Exercises
###############################################

###############################################
# TASK 1: Examine the types of data structures.
###############################################


x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

# Changeable, Sequential
l = [1, 2, 3, 4, "String", 3.2, False]
type(l)

# Changeable, Unordered
d = {"Name": "Jake",
     "Age": [27, 56],
     "Adress": "Downtown"}
type(d)

# Immutable, Sequential
t = ("Machine Learning", "Data Science")
type(t)

# Interchangeable, Unordered + Unique
s = {"Python", "Machine Learning", "Data Science", "Python"}
type(s)

###############################################
# TASK 2: Convert all letters of the given string expression to uppercase. Put space instead of commas and periods, separate them word by word.
###############################################


text = "The goal is to turn data into information, and information into insight."
newtext = text.upper().replace(","," ").replace("."," ").split()
print(newtext)



###############################################
# TASK 3: Perform the following tasks for the given list.
###############################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step 1: Look at the number of elements of the given list.
len(lst)

# Step 2: Call the elements at the zeroth and tenth index.
lst[0]
lst[10]

# Step 3: Create list ["D","A","T","A"] from the given list.
lst2 = lst[0:4]
lst2

# Step 4: Delete the element at the eighth index.
lst.pop(8)
lst

# Step 5: Add a new element.
lst.append("M")

# Step 6: Add element "N" again to the eighth index.
lst.insert(8, "N")

###############################################
# TASK 4: Apply the following steps to the given dictionary structure.
###############################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Step 1: Access the key values.

dict.keys()

# Step 2: Access the values.

dict.values()

# Step 3: Update the value 12 of Daisy key to 13.

dict.update({"Daisy": ["England",13]})
dict

dict["Daisy"][1] = 14
dict

# Step 4: Add a new value with the key value Ahmet value [Turkey,24].

dict.update({"Ahmet":["Turkey",24]})
dict

# Step 5: Delete Antonio from the dictionary.

dict.pop("Antonio")
dict

###############################################
# TASK 5: Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists, and returns these lists.
###############################################

l = [2, 13, 18, 93, 22]


def func(l):
    ciftlist = []
    teklist = []

    for a in l:
        if a % 2 == 0:
            ciftlist.append(a)
        else:
            teklist.append(a)

    return ciftlist, teklist


çift,tek = func(l)

###############################################
# TASK 6: The list given below contains the names of the students who achieved success in engineering and medical faculties.
# While the first three students represent the success order of the faculty of engineering, the last three students belong to the student rank of the faculty of medicine.
# Print student degrees specifically for the faculty using Enumarate.
###############################################

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci: ",x)
    else:
        i -= 2
        print("Tıp Fakültesi",i,". öğrenci: ",x)



###############################################
# TASK 7: Below are 3 lists. The lists contain the code, credit and quota information of a course, respectively. Print the course information using Zip.
###############################################

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

list(zip(ders_kodu, kredi, kontenjan))

###############################################
# TASK 8: Below are 2 sets.
# You are expected to define the function that will print the common elements of the 1st set if it covers the 2nd set, and the difference of the 2nd set from the 1st set if it does not.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def farkbulma():
    print(kume2.difference(kume1))


farkbulma()

kume2.intersection(kume1)
kume2.issuperset(kume1)


