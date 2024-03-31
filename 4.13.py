def sum_of_n_naturals(n):


  
  sum = 0

  
  for i in range(1, n + 1):
    sum += i

  return sum


n = int(input("Enter the number of natural numbers: "))


sum_of_first_n = sum_of_n_naturals(n)
print("Sum of the first", n, "natural numbers:", sum_of_first_n)
