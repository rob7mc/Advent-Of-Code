# Read in input text file
file = open("AOC_2021/AOC_Day2/Python/AOC_Day2_Input.txt","r")
# Create an array and populate it with the commands and numbers as a pair 
# from each line from the text file
input = []
for line in file.readlines():
    input.append(line.split())
file.close()

# Part 1 - Answer: 1693300
# Create a horizontal count and a depth count, iterate through the array 
# incrementing the horizontal count by the current number when the current command 
# is forward, decrementing the depth count by the current number when the current 
# command is up and incrementing the depth count by the current number when the
# current command is down

""" horizontal = 0
depth = 0

for i in range(0, len(input)):
    if input[i][0] == "forward":
        horizontal += int(input[i][1])
    elif input[i][0] == "up":
        depth -= int(input[i][1])
    else:
        depth += int(input[i][1]) """

# Part 2 - Answer: 1857958050
# Create a horizontal count, a depth count and an aim count, iterate through the array 
# incrementing the horizontal count by the current number and the depth count by the 
# current number multiplied by the current aim count when the current command 
# is forward, decrementing the aim count by the current number when the current 
# command is up and incrementing the aim count by the current number when the
# current command is down

horizontal = 0
depth = 0
aim = 0

for i in range(0, len(input)):
    if input[i][0] == "forward":
        horizontal += int(input[i][1])
        depth += (int(input[i][1]) * aim)
    elif input[i][0] == "up":
        aim -= int(input[i][1])
    else:
        aim += int(input[i][1])

# Print the answer
print(horizontal * depth)
