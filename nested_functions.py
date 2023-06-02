# FUNCTIONS INSIDE A FUNCTION 

# name = input("Enter your name:")
# gender = input("Enter your gender ")

# def greet(name):
#     def display_name(gender):
#         print(f"Hello {name}, your gender is {gender}") # FOR NESTED FUNCTIONS, DO NOT USE RETURN, USE PRINT FOR DISPLAYING VARIABLES INSIDE THE NESTED FUNCTION, UNLESS IT IS AN OPERATION.
#     display_name(gender)
# greet(name)


#NOTE: WHen PRINT has been used within a function, the function should only be called to display result without the keyword PRINT
# and when RETURN is used within a function, you may use PRINT keyword to display the result
# HOWEVER. FOR NESTED FUNCTIONS, you must call the CHILD FUNCTION-NAME alone and PARENT FUNCTION-NAME alone if PRINT was used within
# if RETURN was used within call with RETURN and PRINT for PARENT FUNCTION-NAME.

name = input("enter your name")
def sentence(name):
    def greet():
        return (f"you are {name}")
    return greet()
print(sentence(name))




# name = input("Enter your name:")
# gender = input("Enter your gender ")

# def greet(name):
#     def display_name(gender):
#         return f"Hello {name}, your gender is {gender}"
#     return display_name(gender)
# print(greet(name))




# Below is a NESTED ARGS adder function.

# def collect_numbers(*numbers):
#     def add_numbers():
#         a = 0
#         for i in numbers:
#             a += i
#         return a
#     return add_numbers()  ### NOTE THIS IS AN OPERATION WITHIN THE NESTED FUNCTION, NOT STRING DISPLAY THEREFORE NO NEED FOR PRINT, ONLY RETURNS, AND PRINT CAN APPEAR WHEN CALLING THE FUNCTION
# print(collect_numbers(1, 2, 3, 4))





