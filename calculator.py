print('Welcome to Delton, you simple calculator! \n')

#Main loop to keep the calculator running
while True:
    x = float(input('Enter first number: '))
    y = float(input('Enter second number: '))   

#Loop to select an operation 
    while True:
        z = input('What operation would you like to perform? (+,-,*,/)? ')

        if z == '+':
            print(f'Result: {x+y}')
            break
        elif z == '-':
            print(f'Result: {x-y}')
            break
        elif z == '*':
            print(f'Result: {x*y}')
            break
        elif z == '/':
            #This is to handle division by the vlaue 0
            if y == 0:
                print('Error: Division by zero is not allowed.\n')
                continue
            print(f'Result: {x/y}')
            break
        else:
            print('Invalid operation. Please enter one of +, -, *, or /.')

    #This asks the user if they want to perform another calculation
    again = input('Would you like to perform another calculation? (yes/no): ').strip().lower()
    if again != 'yes':
        print('Thank you for using Delton!')
        print('Goodbye!')
        break 