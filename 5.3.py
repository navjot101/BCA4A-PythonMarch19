# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Add an element to the end
numbers.append(6)
print("List after append:", numbers)

# Insert an element at a specific index
numbers.insert(2, 1.5)
print("List after insert:", numbers)

# Remove the first occurrence of an element
numbers.remove(3)
print("List after remove:", numbers)

# Remove and return the element at a specific index
removed_element = numbers.pop(1)
print("Removed element:", removed_element)
print("List after pop:", numbers)

# Find the index of the first occurrence of an element
index = numbers.index(4)
print("Index of 4:", index)

# Sort the list in ascending order
numbers.sort()
print("List after sort:", numbers)

# Reverse the order of elements
numbers.reverse()
print("List after reverse:", numbers)

# Create a shallow copy of the list
copy_of_numbers = numbers.copy()
print("Copy of the list:", copy_of_numbers)

# Remove all elements from the list
numbers.clear()
print("List after clear:", numbers)
