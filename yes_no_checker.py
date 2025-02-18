def yes_no(question):
    while True:
    
        response= input(question).lower()
        if response == 'yes' or response == 'y':
            return 'Yes'
        elif response == 'no' or response == 'n':
            return 'No'
        else:
            print('Please enter yes (y) or no (n).\n')

while True:
    want_instructions = yes_no('Do you want to read the instructions? ')
    print(f"You chose {want_instructions}\n")