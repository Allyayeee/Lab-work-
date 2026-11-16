# Allison xiong
# 10/7.2026
# lab 6

# this program will calculate the gasoline cost for a trip.  

# user greeting

print('This program will calculate the cost of gasoline for a trip.')
print('You will need to know your car MPG,what you paid for gallon of gas, and the distance in miles you traveled.')
print()

# creating the program loop

run = True 
while run == True:

    # get user input and the variables

    print()
    distance = float(input('Please enter the distance traveled in miles: '))
    mpg = float(input('Enter the Miles Per Gallon for this trip: '))
    costPerGallon = float(input('Enter the cost per gallon paid: '))


    # doing the calculation

    gallon_used = distance / mpg
    trip_cost = gallon_used * costPerGallon


    # displaying the results
    
    print()
    print("The cost for this trip is/was: $", format(trip_cost, '.2f'))


    # asking the user if they want to run the program again

    choice = input('would you like to run the program again? (y or n): ').lower()


    #error check if y or n isnt enter in

    while choice not in ('y', 'n'):
        choice = input(' INPUT ERROR!!! :Please enter a "y" for yes or an "n" for no: ').lower()

    # change the programming loop to another variable so it can exit the program.

    if choice == 'n':
        run = False


# exit message for the user

print()
print('Have a nice day!!!')
