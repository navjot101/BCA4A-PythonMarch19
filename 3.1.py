def check_divisibility(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    elif num1 % num2 == 0:
        return f"{num1} is divisible by {num2}"
    else:
        return f"{num1} is not divisible by {num2}"

print(check_divisibility(10, 2))
print(check_divisibility(10, 3))
print(check_divisibility(10, 0))