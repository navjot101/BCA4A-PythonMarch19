import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(variance):
    return math.sqrt(variance)

def main():
    numbers = [float(x) for x in input("Enter the list of numbers separated by spaces: ").split()]

    mean = calculate_mean(numbers)
    variance = calculate_variance(numbers, mean)
    std_deviation = calculate_standard_deviation(variance)

    print("Mean:", mean)
    print("Variance:", variance)
    print("Standard Deviation:", std_deviation)

if __name__ == "__main__":
    main()
