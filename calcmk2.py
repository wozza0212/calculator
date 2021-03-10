# Calculator

def add(n1, n2):
    print(f'\n\nThe total is {n1 + n2}')
    return n1 + n2


def divide(n1, n2):
    print(f'\n\nThe total is {n1 / n2}')
    return n1/n2


def multiply(n1, n2):
    print(f'\n\nThe total is {n1 * n2}')
    return n1 * n2


def subtraction(n1, n2):
    print(f'\n\nThe total is {n1 - n2}')
    return n1 - n2


def start():
    print('Welcome to the calculator app')
    while True:
        try:
            n1 = int(input('Please enter your first number here:>>>'))
        except ValueError:
            print('That did look like a number ot me!')
            continue
        else:
            print(f'Your first number is {n1}')
            break
    return n1

def select_operator():

    print('Now please enter what you would like to do with that number')
    print('Please select one of the following operators')
    print('Enter \'*\' for multiplication, enter \'/\' for division, enter \'+\' for addition or \'-\' for subtraction')
    while True:
        operator = input('Enter you operator here:>>>')
        if operator == '+':
            return operator
        elif operator == '/':
            return operator
        elif operator == '*':
            return operator
        elif operator == '-':
            return operator
        else:
            print('That wasn\'t a valid operator for this calculator')


def enter_number():
    print('Now it\'s time to give us your next number')
    while True:
        try:
            n2 = int(input('Please enter your next number here:>>>'))
        except ValueError:
            print('That did look like a number ot me!')
            continue
        else:
            print(f'Your next number is {n2}')
            break
    return n2


n1 = start()
while True:
    operator = select_operator()
    n2 = enter_number()
    if operator == '+':
        total = add(n1, n2)
    elif operator == '/':
        total = divide(n1, n2)
    elif operator == '*':
        total = multiply(n1, n2)
    elif operator == '-':
        total = subtraction(n1, n2)
    while True:
        print('Would you like to continue with this number or start again!')
        carry_on = input('Enter \'t\' to carry on with the total or enter \'r\' to restart the calculator:>>>')
        if carry_on == 't':
            n1 = total
            break
        elif carry_on == 'r':
            n1 = start()
            break
        else:
            print('That wasn\'t a valid option!')



