# Allison xiong
# 9/23/2026
# Lab 4

# allows the user to enter any two integers and displays the value of each possible calculation that could be done to them.

# user greeting


print('This program will allow you to enter two integer values then show you all the possible answers.') 
print('Please enter whole numbers.')

print()

# input for the first and second input 


firstNum = int(input('Please enter the first number: '))
secondNum = int(input('Please enter the second number: '))


#  user will get the first and second variables and
# assign the data to both variables


add = firstNum + secondNum
subtract = firstNum - secondNum
multiple = firstNum * secondNum
division = firstNum / secondNum
truncating_divison = firstNum // secondNum
modulus = firstNum % secondNum
exponentiaion = firstNum ** secondNum


# displaying the results for every variable

print()

print(firstNum, '+', secondNum, '=', format(add, ','))
print(firstNum, '-', secondNum, '=', format(subtract, ','))
print(firstNum, '*', secondNum, '=', format(multiple, ','))
print(firstNum, '/', secondNum, '=', format(division, ','))
print(firstNum, '//', secondNum, '=', format(truncating_divison, ','))
print(firstNum, '%', secondNum, '=', format(modulus, ','))
print(firstNum, '**', secondNum, '=', format(exponentiaion, ','))



# exit message

print()

print('Have a great day!')
