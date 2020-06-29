# sorting in place using sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sorting in place using sort - reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# using sorted function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# printing the list in reverse order
print("\n")
print(cars)

cars.reverse()
print(cars)

# printing the length of the list
print("\n")
print(len(cars))