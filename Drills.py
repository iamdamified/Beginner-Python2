# # INHERITANCE DRILLS


# class Vehicle:

#     def __init__(self, type, price, milleage):
#         self.type = type
#         self.price = price
#         self.milleage = milleage

#     def Is_new(self):
#         if self.milleage > 6000:
#             return "old car"
#         return "new car"
#     def checker(self):
#         if isinstance(self, Vehicle):
#             return True
#         return False
#     def duplicatemilleage(self):
#         self.milleage = self.milleage * 2
#         return self.milleage
    
# class Car(Vehicle):
#     def __init__(self, type, price, milleage, brand):
#         Vehicle.__init__(self, type, price, milleage,)
#         self.tyre = 4
#         self.brand = brand


#     def increment(self):
#         self.price = self.price + 200
#         return self.price

#     def profile(self):
#         return f"{self.brand}, {self.price}, {self.milleage}"
    
   



# Car_1 = Car("luxury", 1200, 2300, "Honda" )
# print(Car_1.duplicatemilleage())


# print(type(Car_1))

# print(Car_1.price)

# print(Car_1.Is_new())


# class Phone:
#     def __init__(self, price, color, model):
#         self.price = price
#         self.color = color
#         self.model = model

    
# class Apple(Phone):
#     def __init__(self, price, color, model):
#         super().__init__(price, color, model)
#         self.brand = "iphone"

#     def increment(self):
#         self.price = self.price * 2
#         return self.price


# Apple_1 = Apple(1000, "Blue", "Pro Max")
# print(type(Apple_1))

# print(Apple_1.increment())



# class Vehicle:
#     def __init__(self, name, unit_price, distance):
#         self.name = name
#         self.unit_price = unit_price
#         self.distance = distance

#     def bill(self):
#         self.unit_price = self.unit_price * self.distance
#         return self.unit_price
    

# user = Vehicle("EMmanuel", 100, 5)
# print(user.bill())


# def swap_cases(sentence):
#     sentence_change = ""
#     for i in sentence:
#         if i.islower():
#             sentence_change += i.upper()
#         else:
#             sentence_change += i.lower()
#     return sentence_change
    

# print(swap_cases("HELO i am prosper"))


# def adder():
#     add = 0
#     count = 0
#     while count < 100:
#         add += count
#         count += 1
        
#     return add
            
        
# print(adder())


# times = [92.5, 93.8, 91.0, 95.0]

# def atheletes(times):
#     count = 1
#     times2 = []
#     while count < 4:
#         times2.append((min(times)))
#         times2.append(count)
#         times.remove(min(times))
#         count += 1
#     return times2

# print(atheletes(times))



# def checker(sentence):
#     count1 = 0
#     count2 = 0
#     count3 = 0
#     sentence_change = ""
#     for i in sentence:
#         if i.isupper():
#             count1 += 1
#         elif i.islower():
#             count2 += 1
#         elif i.isdigit():
        
#             count3 += 1
#     return (count1, count2, count3)
    

print(checker("I am 25 years old"))
        
    


        



        

