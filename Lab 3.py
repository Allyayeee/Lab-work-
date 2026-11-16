# Allison xiong
# 9/14/2026
# lab 3

# this program will get the user input and assign to variables.

# user greeting

print('This program will let you raise any intger to any integer power.')
print('Remember to use only whole numbers.')

print()

# user input for the first input

base = input('Please enter the base number: ')


# user input in the text displayed and use the comma format for the answer.

print()
power = int(input("What power of " + (base) + ": "))

# remaking the base to add to the power


base = int(base)


# formating the answer


ans = base ** power
print()

#displaying the answer


print(base, "to the power of", power, "is:", format(ans, ',') + '.')

print()
# displaying a exit message

print('Thank you for using the power calulator.')
print('Have a nice day!')
