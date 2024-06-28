#Dalyn Stiles
#06/27/2024
#P3HW1


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))     #Fixed some indenting issues and typos also converted into floats
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]       #added commas and fixed unneeded capitalization
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)                             #max is used to find the highest number
total_sum = sum (grades)
avg = (mod_1 +  mod_2 +  mod_3 + mod_4 + mod_5 + mod_6) /6       #defined how to find the average of the grades

# TO DO: finish this

print("------------Results------------")
print(f'{"Lowest Grade:"}{min(grades)}')  #lowest
print(f'{"Highest Grade:"}{max(grades)}') #highest
print(f'{"Sum of Grades:"}{sum(grades)}') #combined
print(f'{"Average Grade:"}{avg:.2f}') #average
print(f'------------------------')
if avg >= 90:
    print(f'Your grade is: A')
elif avg>=80:
    print(f'Your grade is: B')
elif avg<=70:
    print(f'Your grade is C')
else:
    print('Your grade is: F') 




