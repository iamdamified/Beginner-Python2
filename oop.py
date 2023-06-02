# A CLASS IS 
# AN OBJECT IS THE SAME AS AN INSTANCE OF A CLASS
# A METHOD IS A FUNCTION WITHIN A CLASS AFTER INITIALIZATION.


# # AN EMPTY CLASS
# class vehicle:
#     pass


# class Student:
#     def __init__(self, name, age): # Inititalizing the rules guiding the input expected in the class
#         self.name = name
#         self.age = age


#     # Creating a Method
#     def summary(self):
#         return f"Your name is {self.name}, you are {self.age} old"



# student_1 = Student("Emmanuel", 34)


# print(student_1) # returns a message informing user this is an "object" at the a system ID number for Class "Student"
# print(student_1.name)
# print(student_1.age)


# # Calling a Method (a function ) in OOP
# print(student_1.summary())


# ##### SELF EXPLANATION
# #superclass
# class World:
#     def __init__(self, Africa, Asia, Europe, America, Carribean):
#         self.Africa = Africa
#         self.Asia = Asia
#         self.Europe = Europe
#         self.America = America
#         self.Carribean = Carribean

#     def Countries(self):
#         print(f"You are from {self.Africa}")


# #subclass
# class Governments(World):
#     # It would supply all needed information from superclass immediately you type "def __init__"
#     def __init__(self, Africa, Asia, Europe, America, Carribean, NorthAmerica):
#         super().__init__(Africa, Asia, Europe, America, Carribean)
#         self.NorthAmerica = NorthAmerica # NOTE that "NorthAmerica" is a subclass level variable which can either be added to Init for collection or 
#         #not required but present by hardcoding its value
#         #self.NorthAmerica = "Brazil"








# class Employee:
#     def __init__(self, name, phone, job, salary): # Inititalizing the rules guiding the input expected in the class
#         self.name = name
#         self.phone = phone
#         self.job = job
#         self.salary = salary


#         # Creating a Method
#     def annual_salary(self):
#         salary2 = self.salary * 12
#         return f"Your name is {self.name}, your annual pay is {salary2} naira"
#         # return f"{self.salary} , {self.name}, {self.job}, {self.phone}"
    

# staff = Employee("Emmanuel", "08168139718", "secretary", 50000)
# print(staff.annual_salary())
# print(staff.salary)


# class Employee:
#     '''
#     This area before the methods is used to declare general parent data useable in the methods or variable use or change in operations.
#     '''
#     company_name = "Univelcity" # Global variables(Class Level Variables)data or feature shared or to be shared by all members/Instances within the Class
#     raise_percentage = 1.30


#     def __init__(self, name, job, phone, salary):
#         self.name = name
#         self.job = job
#         self.phone = phone
#         self.salary = salary
#         self.email = f"{self.name}@univelcity.com" # (Instance Level Variable)data perculiar to each object/instance but not initialized as a necessary input can be added here.
        

# # Method
#     def append(self):
#         return f"Hi {self.name}, you are the {self.job}"
    
#     def raise_salary(self):
#         self.salary = int(self.salary * self.raise_percentage)
#         # self.salary = int(self.salary * 1.30)
#         return self.salary

# employee1 = Employee("prosper", "Backend Instructor", "08168139718", 10000000)
# employee2 = Employee("emmanuel", "Data Science Instructor", "07081900116", 10000000)



# print(employee1.email)
# print(employee1.append())
# print(employee1.company_name)
# # print(employee1.append(self)# you can not use this syntax to print
# print(employee1.__dict__) # Displays all known information(All within the parent function __init__) which instance(employee1) shares, EXCLUDING Global variables.
# print(Employee.__dict__)# Displays summary of all information within the class: (The Global variables, __init__, All Methods, and All objects/instances.)

# employee1.company_name = "Unilag" # You can change the value/operation/feature of an instance by reassigning the operation to another value.
# print(employee1.company_name)

# employee1.job = "Labourer"
# print(employee1.job)


#raise_salary operations with hard coded figure commented out below the declared operation

# print(employee1.salary)
# print(employee1.raise_salary())
# print(employee1.salary)


# 
# print(employee1.raise_percentage) # normal value
# employee1.raise_percentage = 1.40 # specific change for this instance
# print(employee1.raise_percentage) # New value

# # Applying the new value
# print(employee1.raise_salary())
# print(employee2.salary)
# print(employee2.raise_salary())





#CONTINUE READING
#QUIZ

# class Bird:
#     sound = "chirp"
#     def __init__(self, color, size):
#         self.color = color
#         self.size = size

# parrot = Bird("pink", 25)
# chicken = Bird("white", 20)
# print(parrot.sound)
# chicken.sound = "quark"
# print(chicken.sound)


# class wages:

#     def __init__(self, rate, hours):
#         self.rate = rate
#         self.hours = hours

#     def salary(self):
#         # self.salary = int(self.hours * self.rate)
#         self = int(self.hours * self.rate)
#         # return self.salary
#         return self

# emp1 = wages(1000, 2)

# print(emp1)         #THis show you its an object of Wages at a particular location ID.
# print(type(emp1))       #THis show you the type of object it is(Main class wages because it is an instance of wages).
# print(emp1.salary())



class laptop:
    battery = 5000
    model = "HP"
    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size
        self.keyboard = "360 Keyboard"

# name = laptop("TY", "white", 10)


Lap_1 = laptop("Dell", "blue", 12)
print(Lap_1.model)
print(Lap_1.keyboard)











