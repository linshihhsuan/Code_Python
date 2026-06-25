x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = ['a', 'b', 'c', 'd', 'e']
z = [x, y]

# Print all elements in list x
print(f"list elements: {x}")
# Get elements from index 2 to the end
print(f"x[2:] = {x[2:]}")
# Get elements from the beginning to index 2, excluding index 2
print(f"x[:2] = {x[:2]}")
# Get elements from index 0 to index 3, excluding index 3
print(f"x[0:3] = {x[0:3]}")
# Get elements from index 1 to index 4, excluding index 4
print(f"x[1:4] = {x[1:4]}")
# Get elements from index 0 to index 9, excluding index 9, with a step of 2
print(f"x[0:9:2] = {x[0:9:2]}")
# Get every second element from the entire list
print(f"x[::2] = {x[::2]}")
# Get elements from index 2 to the end with a step of 3
print(f"x[2::3] = {x[2::3]}")
# Create a copy of the entire list
print(f"x[:] = {x[:]}")
# Reverse the list
print(f"x[::-1] = {x[::-1]}")
# Get elements from index -3 to index -7, excluding index -7, moving backward
print(f"x[-3:-7:-1] = {x[-3:-7:-1]}")
# Get the last element of the list
print(f"x[-1] = {x[-1]}")

# Get the length of the list
print(f"length of x = {len(x)}")

# Change the content of the list
print(f"list elements: y{y}")
y[3] = 'z'
print(f"list elements: y{y}")

# Addition of list
sum = x + y
print(f"list elements: sum{sum}")



