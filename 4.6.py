def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter the value of n: "))
result = fibonacci(n)
print("Fibonacci sequence up to", n, ":", result)