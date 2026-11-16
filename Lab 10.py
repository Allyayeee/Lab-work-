# Allison Xiong
# 11/4/2026
# lab 10


# the program i am making is to make the user enter a fuirt by pounds of each types.



# user greeting

print('This program will let you create a list of fruits and how many pounds there are of each and then display them back to you.')
print('When you are done please press return without entering a fruit.')


# program loop

run = True
while run == True:


    
 # creating empty lists

    fruitList = []
    weightList = []
    

#creating the user input loop

    run = True
    while run:
        

        # creating variable to control user input loop

        print()
        fruit = input('Please enter a type of fruit: ').title()


        #creating if/else statments

        if fruit == '':
            run = False

        else:

            weight = input('Please enter the weight of the fruit in pounds: ')

            fruitList.append(fruit)
            weightList.append(weight)
            print()

        # creating a FOR loop that displays each listing

        for index in range(len(fruitList)):
                
            print(format(fruitList[index], '<10'), format(weightList[index], '>5'))
    # rerun program

    choice = input('Would you like to rerun the program? y/n: ').lower()


    #error check

    while choice not in ('y', 'n'):
        choice = input('ERROR type in y/n: ').lower()

        #exit program

        if choice == 'n':
            run = False

# exit message

print()

print('Have a nice day!!!')
    

        
        
    




              
