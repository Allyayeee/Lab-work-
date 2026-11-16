# Allison xiong
# 9/21/26
# Lab 8

# this program will Develop and test a program that lets a user
# do calculations with two numbers. The calculations should include:
# addition, subtraction, multiplication, division, truncating
# division, and exponentiation.

# user greeting / instructions for calculations

print('This program will let you addition, subtraction, multiplication, division, truncating,division turncating division, and exponentation for any two numbers.')
print()
print('Choose an "a" for addition, "s" for subtraction, "m" for multiplication, "d" for division, "t" for truncating division, or a "e" for exponentation.')
print()

# creating the program loop

run = True
while run == True:


    # getting user input
    choice = input('Please choose the type of calculation you want to do: ').lower()


    # error check if a, s, m, d, t, or e isnt typed in

    while choice not in ('a', 's', 'm', 'd', 't', 'e',):
        choice = input('ERROR, please choose an a, s, m, d, t, or e: ').lower()


    # get the user input for the two numbers

    print()
    firstNum = float(input('Please enter the first number: '))
    secondNum = float(input('Please enter the second number: '))

    
    # creating the if/elis/else statement
    print()

    if choice == 'a':
        ans = firstNum + secondNum
        message = 'plus'

    elif choice == 's':
        ans = firstNum - secondNum
        message = 'subtracted'

    elif choice == 'm':
        ans = firstNum * secondNum
        message = 'multipled'

    elif choice == 'd':
        ans = firstNum / secondNum
        message = 'divided'

    elif choice == 't':
        ans = firstNum // secondNum
        message = 'truncated'

    else:
        ans = firstNum ** secondNum
        message = 'raised by the power of'


    # making the printline to display answer


    print(firstNum, message, secondNum, 'equals', format(ans, ','))



    # ask if the user wants to rerun the program

    print()
    
    rerun = input('would you like to run the program again? (y or n): ').lower()
    print()

    
    #error check if y or n isnt enter in

    while rerun not in ('y', 'n'):
        rerun = (input('ERROR, please choose a "y" for yes or "n" for no: '))

    if rerun == 'n':
        run = False
    
            
# exit message

print()
print('Have a nice day!')
        

        




    
