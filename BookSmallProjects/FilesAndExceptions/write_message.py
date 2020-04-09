filename = 'programming.txt'

with open(filename, 'w') as file_writer:
    line = ''

    while True:
        line = input('Type text to save in text file:')

        if line == 'end':
            break

        file_writer.write(f'{line}\n')
