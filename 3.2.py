def check_number_sign(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

number = int(input("Enter a number: "))
print(check_number_sign(number))