# Allison xiong
# 11/3/2026
# lab 9

# creating a program that converts ounces to grams, inches to centimeters, and kilometers to miles

# creating the user greeting

print('This program will convert Inches to Centimenters, Centimeters to Inches,')
print('Grams to Ounces, Kilometers to Miles, or miles to Kilometers.')


# the I, C,O,G,M,K

print()
print('Enter I convert from Inches to Centimeters.')
print('Enter C to convert from Centimeters to Inches.')
print('Enter O to convert from Ounces to Grams.')
print('Enter G to convert from Grams to Onces.')
print('Enter M to convert from Miles to Kilometers.')
print('Enter K to concert from Kilometers to Miles.')

# creating the variable / program loop 


run = True
while run == True:


    # getting user input for the conversion they want to do and assign it to a  variable

    print()
    choice = input('Enter the type of conversion you would like to do: ').lower()


    # error check if input isnt any of the letters
    while choice not in ('i', 'c', 'o', 'g', 'm', 'k',):
        choice = input('ERROR, please choose I, C, O, G, M, or K: ').lower()


    # user imput for actual number for measurement/ weight

    measure = float(input('Enter the measure/weight to convert: '))
    print()

        
    # creating each statement for EACH calculation


    if measure == 'i':
        ans = measure * 2.54
        firstMes = 'Inches'
        secMes = 'Centimeters'

    elif measure == 'c':
        ans = measure / 2.54
        firstMes = 'Centimeters'
        secMes = 'Inches'

    elif measure == 'o':
        ans = measure * 28.3495231
        firstMes = 'Ounces'
        secMes = 'Grams'

    elif measure == 'g':
        ans = measure / 28.3495231
        firstMes = 'Grams'
        secMes = 'Ounces'

    elif measure == 'm':
        ans = measure * 1.609344
        firstNum = 'Miles'
        secNum = 'Kilometers'

    else:
        ans = measure / 1.609344
        firstNum = 'Kilometers'
        secNum = 'Miles'


    # making the print line to display answer

    print(measure, firstNum, 'equals', format(ans, '.2f'), secNum, '.')


    # asking user if they want to rerun program again

    print()
    rerun = input('Would you like to make another conversion? (y/n): ').lower()


    # error check

    while rerun not in ('y', 'n'):
        rerun = input('ERROR: enter y or n: ').lower()

    if rerun == 'n':
        run = False

# exit message

print()
print('Have a good day!!!')


