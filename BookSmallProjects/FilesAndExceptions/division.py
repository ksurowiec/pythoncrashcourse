print('Give me two numbers, and I will divide them.')
print('Enter \'q\' to quit.')

while True:
    first_number = input('First number: ')
    second_number = input('Second numner: ')

    if (first_number or second_number) == 'q':
        break

    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cannot divide by zero !')
    except ValueError:
        print('You should enter only numbers !')
    else:
        print(result)
