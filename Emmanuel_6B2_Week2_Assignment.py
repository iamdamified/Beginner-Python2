# # ASSIGNMENT 1
# # Create a function called employee_profile, it should accept two arguments (name and salary).  Your function should return the employee’s name and salary.
## NOTE: Set up the function in a way that it uses NGN 150,000 as the default salary if no value is passed as salary into the function.

# def employee_profile(name, salary ="NGN 150,000"):

#     '''This function prints out a an employee profile'''

#     return f"Welcome {name}, your salary is {salary}"

# # Hardcoding the values

# print(employee_profile("Emmanuel"))
# print(employee_profile("Emmanuel", "NGN 100,000"))

# # INTERACTIVE IMPLEMENTATION: By accepting data from user

# name = input("Enter your name: \n")
# salary = input("Enter your salary: \n")
# # print(employee_profile(name))
# print(employee_profile(name, salary))




# ASSIGNMENT 2
## Create a function called vowel_counter. It should accept a string as an argument and return the number of vowel letters in it.

# def vowel_counter(word):

#     '''This function counts and prints out the number vowel letters in a string'''

#     set1 = set()
#     for i in word:
#         set1.add(i)
#         set1.intersection_update({"a", "e", "i", "o", "u"})
#         count = len(set1)
#     return set1, count # This output shows the vowel letters extracted from the word accepted and the total number.

# # Hardcoding the values
# print(vowel_counter("hello"))


# # INTERACTIVE IMPLEMENTATION: By accepting data from user
# word = (input("Enter any English word: \n"))
# print(vowel_counter(word))

# correction

# def vowel_counter(a):
#     count = 0
#     for i in a:
#         if i in "aeiou":
#             count += 1
#     return count

# b = input("enter a word: ")
# print(vowel_counter(b))
    



# ASSIGNMENT 3

## Create a function called list_maker, it should accept multiple values as arguments and return those values as a list.


# def list_maker(*values):

#     '''This function accepts multiple values, stores them in a list and display them'''

#     return list(values) # This would have produced a tuple if not converted to a List.

## Hardcoding the values
# print(list_maker("Emmanuel", "Damilare", "Adekoya", "35", "Software Engineer"))


# # INTERACTIVE IMPLEMENTATION: By accepting data from user
# values = (input("Enter data for storage: \n"))
# print(list_maker(values))


# Correction:
# def list_make():
#     list = []
#     value = int(input("Enter a number:"))
#     for i in range(value):
#         vals = int(input("enter a value: \n"))
#         list.append(vals)
#     return f"These are your list values: {list}"

# print(list_make())

# def listmake():
#     a = list(map(int, input("enter value(s) with space in btw: \n").strip().split()))
#     return a

# print(listmake())

# mynumber = range(8)
# print(list(mynumber))

