# Allison Xiong
# 11/15/26
# Lab 11

# Creating a program that lets the user type in a state name and displays
# that states state abbreviation or conversely enter the state abbreviation
# and display the state name


# list of state names


state_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California",
               "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
               "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
               "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
               "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
               "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
               "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
               "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
               "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
               "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]


# list of state abbreviations


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI",
          "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI",
          "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC",
          "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
          "VT", "VA", "WA", "WV", "WI", "WY"]


# user greeting


print('This program will let you type in a state name and display that states')
print('two letter abbriviation or type in a state abbreviation and display that states name.')


# creating the variable for the main program loop


run = True
while run == True:



    # get input which way the program should run

    print()
    choice = input('Please type "s" to enter a state name or "a" to enter a state abbriviation: ').lower()


    # error check

    while choice not in('s', 'a'):
        choice = input('INPUT ERROR: Enter an "s" or "a": ').lower()



        # creating the if/else asking for user inputs


    if choice == 's':
             stateInput = input('Please enter the state name: ').title


             # error check

             while stateInput not in state_names:
                 stateInput = input('ERROR: Please enter a valid state name: ').title

                 for index in range(len(state_names)):
                     print()
                     print('The state abbreviation is', states[index], '.')


    else:
        # get abbriviation part

        abbriviation = input('please enter the state abbreviation: ').lower()


        # error check abbriviation

        while abbriviation not in states:

            abbriviation = input('ERROR: Please enter a valid abbriviation: ').lower()

            for index in range(len(states)):
                    print()
                    print('The state name is', state_names[index].upper(), '.')




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


                    


            

















    
    
