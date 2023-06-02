# def multiplication(n):
#     for i in range(1, 13):
#         a = i * n
#         print(f"{n} * {i} = {a}")

        
# multiplication(2)

def add_squares(number):
    a = str(number)
    b = []
    add_a = 0
    for i in a:
        i = int(i)
        i = i * i
        b.append(i)
    for i in b:
        add_a += i
    return add_a
print(add_squares(345))

# def add_squares(number):

#     squared_list = []
#     new = list(str(number))
#     for i in new:
#         squared_list.append(int(i) ** 2)
   
#     return sum(squared_list)
# print(add_squares(345))


