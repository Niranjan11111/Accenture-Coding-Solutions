def can_survive(N, E, D):
    total_sweets_needed = E * D

    if N >= total_sweets_needed:
        return "Yes, you can survive."
    else:
        return "No, you cannot survive."

N = 100  
E = 5    
D = 15   

print(can_survive(N, E, D))
