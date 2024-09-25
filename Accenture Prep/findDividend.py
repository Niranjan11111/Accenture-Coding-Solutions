def calculate_dividend(divisor, quotient, remainder):
    dividend = divisor * quotient + remainder
    return dividend

array = [10, 20, 30, 40, 50]
divisor = 6
quotient = 3
remainder = 2

dividend = calculate_dividend(divisor, quotient, remainder)
print(f"The calculated dividend is: {dividend}")
