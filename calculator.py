#This prints the welcome message
print('Welcome, to Delton, your simple calculator! \n')

#This variable keeps track of whether to continue
repeat='yes'

#This loops the code as long as the repeat value is 'yes'
while repeat== 'yes':
    x=float(input('What is the first number? '))
    y=float(input('What is the second number? '))
    z=input('What operation will you like to perform, +, -, *, /? ')
#This block performs the calculation based on the operator
    if z=='+':
        print(x+y)
    if z=='-':
        print(x-y)
    if z=='*':
        print(x*y)
    if z=='/':
        print(x/y)

#This asks the user if they want to perform another calculation
    repeat=input('Would you like to perform another calculation? (yes/no) ').lower()
#This prints the thank you message if the user inputs anthing other than 'yes'
print('Thank you for using Delton, goodbye!')
