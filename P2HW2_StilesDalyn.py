#Dalyn Stiles
#06/19/2024
#P2HW2

#submits the grades
Module1=float(input("\nEnter grade for Module 1:"))
Module2 = float(input("Enter grade for Module 2: "))
Module3 = float(input("Enter grade for Module 3: "))
Module4 = float(input("Enter grade for Module 4: "))
Module5 = float(input("Enter grade for Module 5: "))
Module6 = float(input("Enter grade for Module 6: "))

print()

mod_grades = [Module1, Module2, Module3, Module4, Module5, Module6]

#Grades are shown
print("------------Results------------")
print(f'{"Lowest Grade:":<30}{min(mod_grades):<15}')  #lowest
print(f'{"Highest Grade:":<30}{max(mod_grades):<15}') #highest
print(f'{"Sum of Grades:":<30}{sum(mod_grades):<15}') #combined

average_grade= (Module1 + Module2 + Module3 + Module4 + Module5 +Module6) /6    #this calculates the average of all the grades. Add up all scores then divide by the number of scores you added.

print(f'{"Average:":<30}{average_grade:<15.2f}')
