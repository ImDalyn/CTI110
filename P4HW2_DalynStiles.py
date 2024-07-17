#Dalyn Stiles
#July 6th 2024
#P4HW2
employee_num = 0
total_reghour_pay = 0
total_overtimepay = 0
total_grosspay = 0


employee = input(f"Enter the employee's name or type 'Done' to terminate : ")

while employee != 'Done':

    hours_worked = float(input(f'Enter the number of hours worked : ')) #displays hours worked as input and float

    hourly_pay = float(input(f"Enter the employee's pay rate: ")) #displays pay rate enterd by input and float




    
    if hours_worked > 40:
        overtime = hours_worked - 40
        overtimepay = hourly_pay * 2 * overtime
        reghour_pay = hourly_pay * hours_worked
    else:
        overtime = 0
        overtimepay = 0
        reghour_pay = hourly_pay * hours_worked
    
    gross_pay = reghour_pay
    total_reghour_pay += reghour_pay
    total_overtimepay += overtimepay
    total_grosspay += gross_pay
    employee_num += 1



    print(f'\n{"Employee Name:":<15}{employee:<15}')
    print()
    print(f'Hours Worked      Pay Rate      Overtime     Overtime Pay     RegHour Pay   Gross Pay')
    print('--------------------------------------------------------------------------------------')
    print(f'{hours_worked:.2f}              ${hourly_pay:<10.2f}       {overtime:<5.1f}        ${overtimepay:.2f}         ${reghour_pay:.2f}        ${gross_pay:.2f}')

    employee = input("\nEnter the employee's name or type 'Done' to terminate: ")
    print()

print(f'Total number of employees entered: {employee_num}')
print(f'Total regular pay: ${total_reghour_pay:.2f}')
print(f'Total overtime pay: ${total_overtimepay:.2f}')
print(f'Total gross pay: ${total_grosspay:.2f}')
print('----------------------------------------------------')