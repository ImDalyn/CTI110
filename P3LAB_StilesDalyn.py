#Dalyn Stiles  
#06/26/2024
#P3LAB
#Creating a change calculator

total_cents=float(input(f'Enter the amount of money as a float: '))  #input total amount as a float

total_cents = int(total_cents * 100)  #convert the float into an integer 100 cents = $1.00

numdollars = total_cents //100    #Create variables for number of dollars so cents //100 then do a modulo for cents left after the floor division
centsleft = total_cents % 100

numquarters = centsleft // 25   #create the variable for quarters just like you did for the dollars
centsleft = centsleft %25

numdimes = centsleft // 10     #repeat for dimes
centsleft = centsleft % 10      
 
numnickels = centsleft // 5    #repeat for nickels
centsleft = centsleft % 5      

numpennnies = centsleft // 1    #repeat for pennies
centsleft = centsleft % 1

if total_cents == 0:              #if your change has a value of 0 you will have no change.
    print('fNo change.')

if (numdollars == 1):
    print(f'{numdollars} Dollar')     #if your number of dollars is equal to 1 it will be singular printed dollar. IF plural print dollars.
elif (numdollars>0):
    print(f'{numdollars} Dollars')

if (numquarters == 1):
    print(f'{numquarters} Quarter')   #if your number of quarters is equal to 1 it will be singular printed quarter. IF plural print quarters.
elif (numquarters>0):
    print(f'{numquarters} Quarters')

if (numdimes == 1):
    print(f'{numdimes} Dime')          #if your number of dimes is equal to 1 it will be singular printed dime. IF plural print dimes.
elif (numdimes>0):
    print(f'{numdimes} Dimes')

if (numnickels == 1):
    print(f'{numnickels} Nickel')     #if your number of nickels is equal to 1 it will be singular printed nickel. IF plural print nickels.
elif (numnickels>0):
    print(f'{numnickels} Nickels')

if (numpennnies == 1):
    print(f'{numpennnies} Penny')  #if your number of pennies is equal to 1 it will be singular printed penny. IF plural print pennies.
elif (numpennnies>0):
    print(f'{numpennnies} Pennies')




