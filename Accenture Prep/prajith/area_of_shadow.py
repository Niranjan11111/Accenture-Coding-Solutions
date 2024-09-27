# Canopy Area
# You are developing a feature for an environmental awareness app that helps users to know how much area their tree’s shadow covers. You have the distance D from a tree’s trunk to the edge of the shadow. Your task is to calculate and return an integer value representing the shadow area of the canopy.
# note: Round off the result to nearest integer
# Input Specification:

# Input 1 : An integer value D. representing the distance from the tree trunk to the edge of shadow

# Output Specification:

# Return an integer value representing the shadow area of the canopy

def canopy(d):
    return round(3.14*d*d)
n = int(input())
canopy(n)




