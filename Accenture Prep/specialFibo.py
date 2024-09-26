def special_fibonacci(n, a=0, b=1):
    fib_series = [a, b]
    
    for i in range(2, n):
        next_value = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_value)
    
    return fib_series

# Example usage
n = 10  # Number of terms in the series
a = 2   # Custom first term
b = 3   # Custom second term

result = special_fibonacci(n, a, b)
print(result)