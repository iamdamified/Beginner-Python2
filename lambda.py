## Lambda functions are quick use and not saved in the memory and you may not use it. 

# How to write a Lambda Function:
# Choose a variable name of your choice.( This variable name will become your function name)
# Assign your Arguments to the variable: starting with lambda, followed by your argument(s), then ended with a colon :
# Then follow the colon with the action you want the Lambda Function to perform.

## Defining lambda function for 1 arguments
# greet_user = lambda name : print('Hey there,', name)

## Calling a lambda function
# greet_user('Delilah')

## Defining lambda function for two or more arguments
# greet_user = lambda name, age : print('Hey there,', name, age)
   
## Calling a lambda function
# greet_user('Delilah', '20')


# Another Lambda Application
# profile = lambda name, email : print('successfully logged in as', email)

# profile('Dami','iamdamified@gmail.com')

# Personal LAMBDA PRACTICES

Country = lambda nigeria : print(f"I am from {nigeria} Nigeria")

Country("Ogun state")


Myname = lambda name, email, phone : print(f"my name is {name}, and my contacts are {email}, {phone}.")

Myname("Emmanuel", "iamdamified@gmail.com", "08168139718")

























