#Dalyn Stiles
#06/19/2024
#P2HW1
# formatting adjustments

print("This program calculates and displays travel expenses")
#Get total budget, int 
#Change int to floats

budget=float(input("Enter budget:"))

#Enter locaation (str)

location=(input("\nEnter your travel destination:"))

#Add gas, accommodation, and food expenses. now a float
#change input from int to floats
gas=float(input("\nHow much do you think you will spend on gas?"))

hotel=float(input("\nApproximately, how much will you need for accomodation/hotel?"))

food=float(input("\nLast, how much do you need for food?"))

#string formatting for viewers pleasure

print("------------Travel Expenses------------")
print(f"{'Location:' : <20}", f"{ location : <20}")
print(f"{'Initial budget:' : <20}", f"{ '$'+str(float(budget)) : <20}")
print(f"{'Fuel:' : <20}", f"{'$'+str(float(gas)) : <20}")
print(f"{'Accommodation:' : <20}", f" {'$'+str(float(hotel)) : <20}")
print(f"{'Food:' : <20}", f"{'$'+str(float(food)) : <20}")

#create new variable that displays remaining balance with $ sign and 2 places after the decimal
remaining_balance=budget - gas - hotel-food
print(f'Remaining Balance:  $ {remaining_balance:.2f}')