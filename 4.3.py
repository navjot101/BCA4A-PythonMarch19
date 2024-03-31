# Using break statement
for i in range(1, 6):
    if i == 3:
        print("Encountered the break statement, stopping the loop")
        break
    print("Current value is", i)

# Using continue statement
for j in range(1, 6):
    if j == 3:
        print("Encountered the continue statement, skipping this iteration")
        continue
    print("Current value is", j)