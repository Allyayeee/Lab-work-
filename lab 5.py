# Allison Xiong
# 9/30/2026
# Lab 5

# this program will create  a temperature in Celsius and have it converted to Fahrenheit.


# user greeting

print('This program will convert degrees Celsius to degrees Fahrenheit.')


# creating program loop

run = True 
while run == True:
    

    # getting user input

    print('Please enter the temperature in degrees Celsius; you may use decimals.')


    # user second imput

    print()
    num = float(input('Enter a temperature in degrees Celsius: '))


    # calculation to get answer

    ans = num * 9/5 + 32


    # showing the results

    print()
    print(num, 'degrees Celsius is equal to', format(ans, '.1f'), 'degrees Fahrenheit.')
    print()


    # Ask the user if they want to rerun the program 

    choice = input('would you like to run the program again? (y or n): ').lower()

    
    # error check if y or n isnt typed in
    
    while choice not in ('y', 'n'):
    
         choice = input('INPUT ERROR: Please enter a "y" for yes or an "n" for no: ').lower()


    # changes the variable that controls the program loop. So the program exits.
    if choice == 'n':

        run = False

        
# exit message

print()
print('Have a great day!')




