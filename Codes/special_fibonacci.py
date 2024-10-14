# speacial fibonacci - Accenture (14 Oct 2024 Coding test)

def special_fibonacci(n):
    # Initialize the first Fibonacci value F(1)
    if n == 1:
        return 1 % 47
    
    # Initialize the first two values F(1) and F(2)
    F1 = 1
    F2 = 2*2 + 1*1  # This is F(2) = 4 + 1 = 5
    
    # If n == 2, return F(2) % 47
    if n == 2:
        return F2 % 47
    
    # For n > 2, calculate F(n) iteratively
    for i in range(3, n + 1):
        Fn = i * i + (i - 1) * (i - 1)  # F(n) = n*n + (n-1)*(n-1)
        F1, F2 = F2, Fn  # Shift F1 to F2, F2 to Fn
    
    # Return F(n) % 47
    return F2 % 47

# Input: a real number N
n = int(input("Enter the value of n: "))  # Convert input to integer

# Output: The special Fibonacci number for the given n mod 47
print(special_fibonacci(n))
