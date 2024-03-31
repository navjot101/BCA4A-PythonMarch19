my_list = ['q', 'w', 'e', 'r', 't', 'y']

# Loop through each element and its index
for i, element in enumerate(my_list):
  # Calculate positive and negative indexes
  positive_index = i
  negative_index = -(len(my_list) - i)

  # Print the element with both indexes on a separate line
  print(f"Element: {element}, Positive Index: {positive_index}, Negative Index: {negative_index}")
