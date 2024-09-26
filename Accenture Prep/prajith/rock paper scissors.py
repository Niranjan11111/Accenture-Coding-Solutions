# Rock, Paper, Scissors

# Two players A and B, are playing the game of Rock, Paper, Scissors. Player A chooses a move represented by a string value M: and the move can be one of the following: ‘rock’, ‘paper’, or 'scissors' where,
# •	rock beats scissors
# •	scissors beats paper
# •	paper beats rock
# Your task is to find and return a string value representing the winning move for Player B.

# Note: 
# The output is case sensitive

# Input Specification:

# input1: A string value M representing the move chosen by Player A
# Output Specification:

# Return a string representing the winning move for Player B.

def rps(str):
  if str == "rock":
    return "scissors"
  elif str == "scissors":
    return "paper"
  elif str =="paper":
    return "rock"
  else:
    return "Invalid move"
  
