#Dalyn Stiles
#P4LAB2
#JULY 03 2024
run_again ='yes'
while run_again !="no":
    user_input = int(input("Enter a non negative integer: "))
    if user_input >=  0:
        for item in range(1, 13):
            print(f'{user_input} * {item} = {user_input * item}')        
    else:
        print(f'"This program can not aaccept negative values.')


    run_again = input(f'"Would you like to run the program again? (yes/no): ')
print(f'Exiting Program . . ')