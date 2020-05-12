bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# first element in the list
print(bicycles[0].title())

# get element at index 1 and index 3
print(bicycles[1])
print(bicycles[3])

# return last element in the list
print(bicycles[-1])

# compose message from first value
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
