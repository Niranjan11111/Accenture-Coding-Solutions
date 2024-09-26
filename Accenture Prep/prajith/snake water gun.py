# Snake Water Gun
# You are given a string S, which contains the moves played by two players sequentially in a game called Snake Water Gun. The rules of the games are as follows:
# Snake beats Water, Water beats Gurn and Gun beats Snake
# The move played by player A and the move played by player B in the first round will be stored in the string as "snakewater"
# Similarly, in the second round, the moves will be stored in the string as "snakewatergunsnake".
# There are total N rounds that are played in the game and your task is to find and return an integer value representing how many rounds Player A will win.Note: The given string is in lowercase
# Input Specification:

# input1: An integer value N representing the number of roundsinput2: A string value S, representing the moves played by the two players.

# Output Specification:

# Return an integer value representing how many rounds Player A wins in the game
def swg(s):
    s = s.replace("snake","s").replace("gun","g").replace("water","w")
    win = 0
    for i in range(0, len(s), 2):
        a = s[i]
        b = s[i + 1]
        if a == 's' and b == 'w':
            win += 1
        elif a == 'w' and b == 'g':
            win += 1
        elif a == 'g' and b == 's':
            win += 1
    return win
print(swg("watergunwaterwatergunwater"))
print(swg("snakesnakegungun"))
