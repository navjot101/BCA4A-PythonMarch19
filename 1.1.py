def calculate_rectangle_area_perimeter(length, width):

  area = length * width
  perimeter = 2 * (length + width)
  return area, perimeter

# Get the length and width of the rectangle from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area and perimeter
area, perimeter = calculate_rectangle_area_perimeter(length, width)

# Print the area and perimeter
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
