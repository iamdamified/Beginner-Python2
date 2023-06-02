# # 1. Write a program that accepts a username as a string and returns "Welcome[Username]"

# def accept_username(username):
#     return f"Welcome [{username}]"
# print(accept_username("Emmanuelforreal"))

# # 2. Rewrite your pay computation with time-and-a-half for over-time and create a function called computepay which takes two parameters
# # (hours and rate).

# def computepay(rate, hours):
#     pay = rate * hours
#     print(pay)
#     overTime = hours + hours / 2 
#     hours = overTime # if there was overtime work.
#     pay = rate * hours
#     return pay

# print(computepay(1000, 45))
# # Enter Hours: 45
# # Enter Rate: 1000
# # Pay: 45000.0
# # Overtime Pay: 67500.0


# def counter(letters):
#     count1 = 0
#     count2 = 0
#     for i in letters:
#         if i.islower():
#             count1 = count1 + 1
#         else:
#             count2 = count2 + 1
#     return (count1, count2)

# print(counter("Emmanuel"))


# UPLOAD TO GITZHUB: MAPPING ELEMENTS OF 2 LISTS TOGETHER IN A NEW LIST.
# Peronal Practice ############ THOUGH BUT FIGURED OUT
def counter(word):
    countsmall = 0
    countcap = 0
    count_leters = []
    for i in word:
        if i.islower():
            countsmall += 1
        else:
            countcap += 1
    # getting the letter with the highest appearance in the word
    new_list = set(word) # change it to a set
    # for i in new_list:  # use for loop to iterate the elements of the set one by one
    #     word.count(i)   # Then  count the number of times each element of the set appears in the word.
    count_leters = [word.count(i) for i in new_list] # append the count for each element in a new empty list created
        # use mapping to indicate which letter in the set has what count. "zip" is for mapping and would not be printed until it is made a List.
    mapping = list(zip(new_list, count_leters))
        
    return f"{countsmall}, {countcap} == {mapping}"

print(counter("EMManuel"))


# to optimize the above

# def counter(word):
#     a = []
#     countsmalllist = [i for i in word if i.islower()]
#     countcaplist = [i for i in word if i.isupper()]
#     countsmall = len(countsmalllist)
#     countcap = len(countcaplist)
    

        
#     return f"{countsmalllist} = {countsmall}, {countcaplist} = {countcap}"



# print(counter("EMManuel"))



# CLASS WORKS........

# Question: FInd the most common letter in a given string.

# 1. Get all the unique letters by converting to a set in a new variable.
# 2. Get the count of each letter in your string by using the unique letters in the new set variable through a FOR LOOP, .count, and .append
# 3. A second time FOR LOOP, with IF condition to check, recount and identify the highest appearance letter 
# through a recount and compare with the max/highest number appended in "word_count" in the first Loop Operation.

# UPLOAD TO GITZHUB: MOST COMMON LETTER IN A GIVEN STRING.
def most_common(word):
    new = set(word) # display only single rep of each letter in the word.
    word_count = [] 
    for i in new: # This helps you to check through the values of the set "new" which now has a single rep of each letter
        word.count(i)  # This then count the number of times each value found while iterating new is present in the original string "word"
        word_count.append(word.count(i)) # Then append the count result of each letter to your empty List "word_count"
    #Repeat the use of set "new" again but this time to check a condition of which letters in new whose count is equal to highest number in "word_count"
    for i in new:                       
        if word.count(i) == max(word_count):
            return i
            

print(most_common("elephant"))


# UPLOAD TO GITZHUB: ADDITION OF A GIVEN LIST OF NUMBERS.
# def adder(*numbers):
#     a = 0
#     for i in numbers:
#         a += i
#     return a

# print(adder(1, 3, 4, 5))

## HOW TO COLLECT DATA AND SORTING IT BASED ON YOUR PEFERRED OPERATIONS.


# # This accepts and calculates the square of any amount of numbers then store them in a List.
# numbers = list(map(int, input("Enter a few numbers:").strip().split()))
# def sqr(numbers):
#     new = []
#     for i in numbers:
#         i *= i
#         new.append(i)
#     return numbers, new
# print(sqr(numbers))

# # SHORT CUT:

# def sqr(numbers):
#     new = [i * i for i in numbers]
#     return numbers, new

# numbers = list(map(int, input("Enter a few numbers:").strip().split()))
# print(sqr(numbers))

# def square(numList):
#     new = [i*i for i in numList]
        
#     return new

# # map is us
# numList = list(map(int, input("Enter a number:").strip().split()))
# print(square(numList))


# def checker(num1, num2):
#     if num1 % num2 == 0:
#         return "perfect"
#     else:
#         return num1/num2
# print(checker(3, 3))
# print(checker(5, 3))


# def vowelremover(name):
#     vowels = "aeiou"
#     new = ""
#     for i in name:
#         if i not in vowels:
#             new += i
#     return new

# print(vowelremover("emmanuel"))

# def vowelremover(name):
#     vowels = ["a", "e", "i", "o", "u"]
#     new = [i for i in name if i not in vowels]
#     return new

# print(vowelremover("emmanuel"))



# def evennumbers(num1, num2):
#     even = []
#     for i in range(num1, num2):
#         if i % 2 == 0:
#             even.append(i)
#     while len(even) < 10:
#             even.append("value")
#     return even

# num1 = int(input())
# num2 = int(input())
# print(evennumbers(num1, num2))



# def evennumbers(num1, num2):
#     even = [i for i in range(num1, num2) if i % 2 == 0]
#     while len(even) < 10:
#             even.append("value")
#     return even

# print(evennumbers(1, 5))


# EXAMPLE OF ARGS ARGUMENTS: WHEN EVER YOU USE ARGS *variablename as Argument, you must hardcode all the variables you need to run.
# def adder(*num):
#     total = 0

#     for i in num:
#         total += i
#     return total

# print(adder(2, 4, 5, 6, 7))# you can hard code as many integer values as possible.


# # EXAMPLE OF KWARGS ARGUMENTS
# def intro(**data):
#     print("\n Data type of argument:" ,type(data)) # This prints out the data type of your entries.

#     for key, value in data.items():
#         # print("{} is {}".format(key, value))
#         print(f"{key} is {value}")


# ## When calling a function which has KWARGS arguments **Variablename, you must use the functioname, with the key= value in bracket to hardcode every single variable.
# intro(Firstname = "Sita", Lastname = "Sharma", Age = 22, Phone = 1234567890)
# intro(Firstname = "John", Lastname = "Wood", Email = "johnwood@nomail.com", Country = "Wakanda", Age = 25, Phone = 9876543210)


# def kwargs_function(**data):
#     print("\n the Datatype of this argument is:", type(data))
#     for key, value in data.items():
#         print(f"{key} is {value}")                                   

# kwargs_function(name = "Emmanuel", age = 34, work = "software engineer", course = "backend") # NOTE: WHen you apply return in few cases it didnt work properly, try print.