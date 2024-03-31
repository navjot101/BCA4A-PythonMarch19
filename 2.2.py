# Prompt the user for a string
user_input = input("Enter a string: ")

# Print the length of the string
print("Length of the string:", len(user_input))

# Print the string in uppercase
print("String in uppercase:", user_input.upper())

# Print the string in lowercase
print("String in lowercase:", user_input.lower())

# Print the string in title case
print("String in title case:", user_input.title())

# Print the string in reverse
print("String in reverse:", user_input[::-1])

# Print the first index of a substring
print("Index of the first occurrence of 'world':", user_input.find('world'))

# Print the string with spaces removed
print("String with spaces removed:", user_input.replace(' ', ''))

# Print the string with all occurrences of a substring replaced
print("String with 'world' replaced by 'universe':", user_input.replace('world', 'universe'))