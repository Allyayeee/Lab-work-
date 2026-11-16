# Allison xiong
# 10/14/2026
# Lab 7

# creating a program that lets the user enter either 'a, b, or c'.

# creating program loop

run = True 
while run == True:


    # creating the user greeting

    print('Please enter an A, B, or C to get a particular fruit.')


    # get the user input and assign it to a  variable
    
    print()
    choice = input('Please enter an A, B, or C: ').upper()


    # error check if a,b or c isnt type in

    while choice not in ('A', 'B', 'C',):
        choice = input('INPUT ERROR: Please enter an A, B, or C: ').upper()

        
    # Remark and create an if/elif/else statement
    print()
    
    if choice == 'A':
        print('You got a Apple!!!')

    elif choice == 'B':
        print('You got a Banana!!!')
        
    else:
        print('You got a Coconut!!!')


    # error check if a,b or c isnt type in

    while choice not in ('A', 'B', 'C',):
        choice = input('INPUT ERROR: Please enter an A, B, or C: ').upper()

    # asking the user if they rerun it again

    choice = input('would you like to run the program again? (y or n): ').lower()


    #error check if y or n isnt enter in
    while choice not in ('y', 'n'):
        choice = input('INPUT ERROR: Please enter a "y" for yes and "n" for no: ').lower()

    # exit the program

    if choice == 'n':
        run = False
    print()

# exit message


print('Have a good day!')
    
        
