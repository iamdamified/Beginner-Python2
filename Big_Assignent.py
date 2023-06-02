
# guestlist = {"Raisa": ["pizza", "cookies", 3], "Susan": ["salad", 2], "Jia": ["ice cream", 0], "Val": ["cake", 2], "Brian": ["pasta", "cheese", "crackers", 2], "Chandra": ["burgers", "buns", 3]}

# Write a program that uses this structure above

# First, print out a line for each guest that reads "<name> is bringing <food items>", 
# where <name> and <food items> are replaced by the name of the guest and the food items that guest is bringing. 
# For example, the first line would be "Raisa is bringing pizza and cookies.", 
# the second line would read "Susan is bringing salad." etc. 
# 
# Each sentence should be on a separate line, one line
# per guest and it should end with a period. 
# 
# The word "and" should be used between food items appropriately. 
# 
# Your code should work for any number of guests and any number of food items per guest. Note that you may assume that everyone is bringing at least
# one food item and that there is always a number of additional guests listed, even if this number is 0.

def guestlist(**guests):
    

    for key, value in guests.items():
        value[0:-1] += " and "

        print(f"{key} is bringing {value[0:-1]}.")

guestlist(Raisa = ["pizza", "cookies", 3], Susan = ["salad", 2], Jia = ["ice cream", 0], Val = ["cake", 2], Brian = ["pasta", "cheese", "crackers", 2], Chandra = ["burgers", "buns", 3])