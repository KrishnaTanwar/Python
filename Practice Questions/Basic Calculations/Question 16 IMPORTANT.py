''' Question 16: Program to input the number of overs in a Cricket match and output the maximum runs a
player can score in the match. Assume that there are no extra runs or NO balls in the match
played. For example, in a 50 over match, the maximum runs scored are 1653.'''

# Input Section

a = int(input("Enter no. of overs:"))

# Logic Section

mx = a*33 + 3

# Output Section

print("Maximum  runs a player can score:",mx)
