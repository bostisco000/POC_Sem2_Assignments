number1 = int(input('Enter an number'))

number2 = int(input('Enter another number'))

try:
    value = number1/number2
    print('The inverse is', value)
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possisble, sorry')