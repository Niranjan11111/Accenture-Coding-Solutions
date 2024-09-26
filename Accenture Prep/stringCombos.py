def generate_combinations(char_array, length_of_string):
    def backtrack(current_comb):
        # Base case: if the current combination is of the desired length, add to results
        if len(current_comb) == length_of_string:
            combinations.append(current_comb)
            return
        
        # Recursive case: for each character, append it to the current combination and recurse
        for char in char_array:
            backtrack(current_comb + char)
    
    combinations = []
    backtrack('')  # Start recursion with an empty combination
    return combinations

# Example usage:
IP_1 = ['e', 'i', 'o']  # Array of characters
IP_2 = 3  # Length of the string

result = generate_combinations(IP_1, IP_2)

# Print all the combinations
for comb in result:
    print(comb)
