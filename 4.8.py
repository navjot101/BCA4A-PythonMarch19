rows = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(rows):
  # Print asterisks equal to the current row number (i + 1)
  for j in range(i + 1):
    print("*", end="")
  # Move to the next line
  print()
