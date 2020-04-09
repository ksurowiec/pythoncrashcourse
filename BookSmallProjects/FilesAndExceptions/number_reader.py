import json


filename = 'numbers.json'
with open(filename, mode='r') as file_reader:
    numbers = json.load(file_reader)

print(numbers)
