def compound_interest(principal, rate, time):
    # A = P(1 + r/n)^(nt)
    n = 12  # Compounded monthly
    amount = principal * (1 + rate/n)**(n*time)
    compound_interest = amount - principal
    return compound_interest

# Example usage
principal = 1000
rate = 0.05
time = 2
interest = compound_interest(principal, rate, time)
print("Compound Interest:", interest)