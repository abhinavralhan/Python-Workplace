'''
**Calculator** -
 A simple calculator to do basic operators. Make it a scientific calculator for added complexity. 
'''

#!/usr/bin/env python3

def calculator(a, b, op):

    if op not in '+-/*':
        return 'Please only type one of these characters: "+, -, *, /"!'

    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))


def main():  # Wrapper

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))
    op = input('What kind of operation would you like to do? \nChoose between "+, -, *, /" : ')

    print(calculator(a, b, op))

main()