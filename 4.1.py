# This program prints a given text until it is interrupted by the user.

text = "Hello, World!"
i = 0

while True:
    print(text)
    i += 1
    if i == 10:
        break