#Dalyn Stiles
#06/28/24
# employee salaries and manipulating output for visual clarity

employee = input(f"Enter the employee's name: ")

hours_worked = float(input(f'Enter the number of hours worked : ')) #displays hours worked as input and float

hourly_pay = float(input(f"Enter the employee's pay rate: ")) #displays pay rate enterd by input and float

print('------------------------------------')

print(f'{"Employee Name : ":<15}{employee:<15}')  #displays employees name with formatting 

print()   #adds spaace between lines of code      

print(f'Hours Worked      Pay Rate      Overtime     Overtime Pay     RegHour Pay   Gross Pay')


print('--------------------------------------------------------------------------------------')

#calculate pay's
overtimepay = hourly_pay * 2 
overtime = hours_worked - 40
overtimepay = hourly_pay * 2 * overtime
gross_pay = hourly_pay * hours_worked + overtimepay

if hours_worked>40:
    overtime = hours_worked - 40
    overtimepay = hourly_pay * 2 * overtime
    reghour_pay = hourly_pay * hours_worked
else:
    overtime = 0
    overtimepay = 0
    reghour_pay = hourly_pay * hours_worked
    gross_pay = reghour_pay

print(f'{hours_worked:.2f}              ${hourly_pay:<10.2f}       {overtime:<5.1f}        ${overtimepay:.2f}         ${reghour_pay:.2f}        ${gross_pay:.2f}')