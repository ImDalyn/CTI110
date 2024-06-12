#Dalyn Stiles
#06/12/2024
#P1HW2
# Using input, print, and int, to show a vacation budget. Also using psuedocode to explain what the code is doing.
#PSEUDOCODE ATTEMPT:
#Get total budget, int
#Enter locaation (str)
#Add gas, accommodation, and food expenses. int
#Subtract expenses from budget
print("This program calculates and displays travel expenses")
budget=int(input("Enter budget:"))
location=(input("Enter your travel destination:"))
gas=int(input("How much do you think you will spend on gas?"))
hotel=int(input("Approximately, how much will you need for accomodation/hotel?"))
food=int(input("Last, how much do you need for food?"))
print("------------Traavel Expenses------------")
print("Location:", location)
print("Initial Budget:", budget)

print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food", food)

print("Remaining Balance",budget-gas-hotel-food)
