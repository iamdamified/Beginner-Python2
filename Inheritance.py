# class Employee:
#     raise_percentage = 1.40
#     def __init__(self, first, last, pay): # Inititalizing the rules guiding the input expected in the class
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = f"{self.first}.{self.last}@gmail.com"

#     # def __str__(self): #Needs further explanations and code is not complete here.
#     #     pass


#         # Creating a Method
#     def profile(self):
#         return f"Your name is {self.first}, your annual pay is {self.pay} naira"
    
#     def raisesalary(self):
#         self.pay = int(self.pay * self.raise_percentage)
#         return  self.pay
    

# emp1 = Employee("Emmanuel", "Adekoya", 50000)
# # print(emp1)

# class Student(Employee):
#     def __init__(self, first, last, pay, course):
#         Employee.__init__(self, first, last, pay)
#         super().__init__(first, last, pay) # You may use the style below.
#         self.course = course

#     raise_percentage = 1.20
    
# print(Student.__dict__)

# print(help(Student))  ###### This prints out all the properties of the CHILD CLASS called Student and the MRO- Method Resolution Order(That is the sequence of solution to operations)
# print(help(Employee))  #######  This prints out all the properties of the PARENT CLASS Employee and the Initializations
# print(help(emp1))
# student_1 = Student("Emmanuel", "Adekoya", "NULL", "Backend",)
# print(student_1.email)
# print(student_1.pay)

# print(emp1.raisesalary())
# print(emp1.raise_percentage)
# print(student_1.raise_percentage)

# A METHOD RESOLUTION ORDER(MRO): checking within its own class, parent class, before checking the inbuilt object methods. Just as the above outputs.


class Human:
    has_hair = True # class variable

    def __init__(self, name, age, language, country):
        self.name = name
        self.age = age
        self.language = language
        self.country = country
        self.name = name

    def background(self):
        return f"Hello {self.name}, you are a citizen of {self.country}"
    
    def profile(self):
        return "This is my profile"
    
class African(Human):
    def __init__(self, name, age, language, country):
        super().__init__(name, age, language, country)
        self.complexion = "black" # Note this has no extra or different argument but was declared at the child class instance level.


    def background(self):
        return f"{super().background()}, you are a {self.complexion} man, {super().profile()}"
    

class European(African):    # NOTE that this could have been a direct child of the Parent class HUMAN but the parent or grandparent inheriting from must be indicated in the bracket.
    def __init__(self, name, age, language, country):
        super().__init__(name, age, language, country)
        self.complexion = "white" # Note this has no extra or different argument but was declared at the child class instance level.


# var = African("Yusuf", 30, "Swahili", "Namibia")
# var2 = European("Jane", 35, "English", "USA")
# print(var2.complexion)
# print(var2.background())
# print(var.background())

human_1 = Human("Emmanuel", 34, "Yoruba", "Nigeria")
print(isinstance(human_1, Human))
print(issubclass(European, Human))












        


