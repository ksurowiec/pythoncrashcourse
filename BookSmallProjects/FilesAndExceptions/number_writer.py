import json


numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'

with open(filename, mode='w') as file_writer:
    json.dump(numbers, file_writer)
