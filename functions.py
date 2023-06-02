# Time() function ( Always ensure you put your import time at the top of your codes if it will be used earlier or later on in the program.)
# Random() function ( Always ensure you put your import random at the top of your codes if it will be used earlier or later on in the program.)
# import time
import random
# print("Welcome to Univelcity")

# # time.sleep(2)

# print("We are happy to have you here")

# zip() function - used for mapping elements of 2 different Lists and works on Lists only

first_iterble = (2, 4, 6, 8)
second_iterble = ("a", "b", "c", "d", "e")

first_output = zip(first_iterble, second_iterble)
print(first_output)
print(list(first_output)) # Since this process would not be printed out because it is internal process. We convert output to List
# second_output = list(first_output) # The solution in this case was changed it to List and reassigned. BEST PRACTICE

# print(second_output)


# enumerate() function
# artists = ["Ed Sheeran", "Usher", "Oxlade", "Usher"]

# output = enumerate(artists)
# print(output) # Since this process would not be printed out because it is internal process, We make the output a list.
# print(list(output))

# range() function
# for i in range(1, 8, 2):
#     print(i)

# b = range(1, 8, 2) # Note that this code will not produce the answer but will only return the code values
# print(b)

# a = list(range(1,8, 2))
# print(a)


# # random() function
# print(random.choice([1,2,3])) #1


# s = [1,2,3,4,5,6,7,8,9,10]
# random.shuffle(s) #2
# print(s)

# new_s = random.sample(s, 6)
# print(new_s)

# print(random.randrange(0,10,2))

# print(a = random.seed(s[5])) ############# NOT CLEAR

# print
# #USER DEFINED FUNCTIONS

# def greet():
#     '''This function prints out a greeting'''
#     return "Good morning"
# print(greet())

# # or 

# def Hello():
#     # this is a function
#     print("Adekoya")

# Hello()


# def greet(n):
#     '''This is a function that prints out a greeting'''
#     print("Good morning " + n) #or print(f"Good morning {n}")

# greet("mercy")

# def calculator(number1, number2):
#     '''function to add 2 variables'''
#     ans = number1 + number2
#     return ans
# # applying the above function on two values.
# print(calculator(3, 4))

# This function calculates a worker salary, after accepting his work rate and hours worked.
# def salary(rate, hours):
#     product = rate * hours
#     return (f"Your salary is {product}")

# hours = int(input("Enter your working hours:\n"))
# rate = int(input("Enter your work rate:\n"))
# print(salary(rate, hours))

# def raisetopower(first, higher):
#     ans = first ** higher
#     return ans

# print(raisetopower(2, 3))



# def square(number):
#     sqr = number * number
#     return sqr

# print(square(10)) # Hardcoding a number 10

# # using the square() function above in the process of iterating each member of the lists
# a = []
# lists = [2, 4, 6, 8]
# for i in lists:         # iterating the lists content to apply the square() function
#     square(i)
#     a.append(square(i))
    
# print(a)




# def reverse(letters):
#     n = (letters[::-1]) # This is the slicing formular to rewrite a string from back to front. like in Arabic writing(right to left)
#     return n

# letters = "prosper"
# print(reverse(letters))


# def maximum(num1, num2, num3):
#     return max(num1, num2, num3)
    
# print(maximum(2, 3, 4))

# CONTINUE READING
#Arbitrary Argument


# def greet(*names):
#     return f"Good day {names[0]}."

# print(greet("Damilare", "Emmanuel", "Adekoya"))


# def greet():
#     names = []
#     for i in range(3):
#         a = input("Please enter your names:")
#         names.append(a)
#     return f"Good day {names[0]}."


# print(greet())

# def greet():
#     names = list(map(str, input("Please enter your names: ").strip().split()))
#     return f"Welcome {names[0]}, your full name is {names[0]} {names[1]} {names[2]}"

# print(greet())


# def country(country="Nigeria"):
#     return f"You are from {country}"


# print(country("England"))

#################################################### NOT CLEAR I NEED EXPLANATION
# def func_three(**country):
#     print(country["east"] + " " + "is a country in Africa")

# func_three(south = "")

# new = []
# numbers = [2, 6, 15, 14, 12, 13, 84, 17]

# def even_numbers(numbers):
#     for i in numbers:
#         if i % 2 == 0:
#             new.append(i)
#     return new
        
# print(even_numbers(numbers))

# num1 = int(input("enter a number: "))
# num2 = int(input("enter second number: "))
# operator = (input("enter an operator: "))

# def calculator(num1, num2, operator):
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-" :
#         return num1 - num2
#     elif operator == "/" :
#         return num1 / num2
#     elif operator == "*" :
#         return num1 * num2
#     else:
#         return f"this is not accurate"

        
# print(calculator(num1, num2, operator))

     


# name = input("enter a word with small and capital letters: ")

# def checker(name):
#     countcap = 0
#     countsmall = 0
#     for i in name:
#         if i.islower():
#             countsmall += 1
#         else:
#             countcap += 1
            
#     return[countsmall, countcap]
# print(checker(name))



## ASSIGNMENT

# def employee_profile(name, salary ="NGN 150,000"):
#     return f"Welcome {name}, your salary is {salary}"

# print(employee_profile("Emmanuel", "NGN 100,000"))

# print(employee_profile("Emmanuel"))


# classwork


# def multiplication(*listnumbers):
#     a = 1
#     for i in listnumbers:
#         a *= i
#     return a 
    
# print(multiplication(1, 2, 3))


# def dilist(set1):
#     a = set1.difference({1, 3, 5, 7})
#     return a

# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(dilist(set1))

# def compare(list1):
#    new_list = [ i for i in list1 if i not in [1, 3, 5, 7]]
#    return new_list

# set1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(compare(set1))

# #palindrome: words that produces same word when spelt backwards

# def checker(sentence):
#     if sentence == sentence[::-1]:
#         return True
#     return False

# print(checker("mem"))


#MORE CODES FROM WEEK 3 AS EXTRA PRACTICES

# input_string = input("enter elements of a list separated by space")
# userlist = input_string.split()
# print(userlist)


# for i in range(0, 5):
#     print("prosper")




# Allows you to accept multiple data ONE AFTER THE OTHER and store them in a List( USING FOR LOOP)
# number_list = []
# n = int(input("ENter the list size "))

# for i in range(0, n):
#     i = int(input())
#     number_list.append(i)


# print("User list is ", number_list)


#putting the above in a function we have below: ####### I was unable to make this a function

# def collectListOfNumbers():
#        number_list = []
#        n = int(input("ENter the list size "))
#        for i in range(0, n):
#               list_item = int(input("Enter list items each at a time: "))
#               number_list.append(list_item)

#        return ("User list is ", number_list)
# print(collectListOfNumbers())


# def collectListOfNumbers(n):
#        number_list = []
#        for i in range(0, n):
#               list_item = int(input("Enter list items each at a time: ")) # list item can be replaced with i
#               number_list.append(list_item)

#        return ("User list is ", number_list)

# list_size = int(input("ENter the list size "))
# print(collectListOfNumbers(list_size))

#Uju Solution

# number_list = []
# def user(n):
#     for i in range(0, n):
#         item = int(input("Enter a number"))
#         number_list.append(item)
#     return f"user list is {number_list}"

# n = int(input("Enter list size: "))
# print(user(n))

# Another Mate Solution
# def user():
#     number_list = []
#     for i in range(0, n):
#        item = int(input("Enter a list"))
#        number_list.append(item)
#     return (f'user list is', number_list)

# n = int(input("Enter list size: "))
# print(user())


# # # Allows you to accept multiple data at ONCE and store them in a List(USING LIST-MAP-INT-INPUT-STRIP-SPLIT(list(MSS)) LMIISS
# numList = list(map(int, input("ENter the list numbers separated by space ").strip().split()))
# print("User List: ", numList)



# Make the ablove a function
# def multipleNumbers():
#        number_list = list(map(int, input("ENter a few numbers with space: ").strip().split()))
#        return f"User list is {number_list}"


# print(multipleNumbers())

# def many(*a):    # As long as you have the asteric, it would accept all the entries, but without the asteric it will return error and accept only one entry.
#     return [a]
# print(many(1, 2, 3, 4, 5))





# def accept_seq(num):

    
#         if i in range(0, 10):
#         return f"True"


# num = (1, 2, 3, 4)
# print(accept_seq(num))




# def checkname(name):
#         for i in name:
#             if i.isupper():
#                   return True
#         return False
#        #  return f"False"

# a = input("enter a word: ")
# print(checkname(a))



# def checkeven():
#        a = [i for i in range(0, 10) if i % 2 == 0]
#        return a


# print(checkeven())


# def calculation(num1, num2): 
#        sum = num1 + num2
#        sub = num1 - num2
#        return (sum, sub)

# print(calculation(50, 10))


# def prime_checker(figure):
#        if figure == 1:
#               return True
#        elif figure == 2:
#               return False
#        else:
#               for i in range(2, figure):
#                      if(figure % i == 0):
#                             return False
#        return True
    
# a = int(input("enter a figure:"))
# print(prime_checker(a))
# print(prime_checker(10))
                            
