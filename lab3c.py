#!/usr/bin/env python3

'''Lab 3 Inv 2 function operate '''
# Author ID: [seneca_id]

def operate(number1, number2, operator, *extra_args):

    # Place logic in this function
    if number1 is None or number2 is None or operator is None or extra_args:
        print('Error: the function requires  three argument.')
    elif operator == 'add':
        sum = number1 + number2
    elif operator == 'subtract':
        sum = number1 - number2
    elif operator == 'multiply':
        sum = number1 * number2
    else:
        sum = 'Error: function operator can be "add", "subtract", or "multiply"'
    
    return sum


 # Main Program


if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))