def yes_no(question): #defines the yes_no question
    while True: #loops my code when asking for an answer
    
        response= input(question).lower() #converts the question to lowercase
        if response == 'yes' or response == 'y': #If the user returns either yes or letter y
            return 'Yes'
            break
        elif response == 'no' or response == 'n': #If the user returns either no or letter n
            return 'No'
            break
        else:
            print('Please enter yes (y) or no (n).\n') #Goes back to the start if yes or no is not entered

while True: #loops the question
    want_instructions = yes_no('Do you want to read the instructions? ')
    print(f"You chose {want_instructions}\n") 
    