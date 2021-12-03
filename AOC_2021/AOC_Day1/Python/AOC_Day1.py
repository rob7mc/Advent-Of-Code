# Read in input text file
file = open("AOC_2021/AOC_Day1/Python/AOC_Day1_Input.txt","r")
# Create an array and populate it with the numbers from the text file
input = []
for num in file.readlines():
    input.append(int(num))
# Close the input text file
file.close()

# Create a count and iterate through the array incrementing the count 
# when the current number is larger than the previous one
count = 0
# Part 1 - Answer: 1624
""" for i in range(1, len(input)):
    if input[i] > input[i-1]:
        count += 1 """

#Part 2 - Answer: 1653
for i in range(3, len(input)):
    if (input[i]+input[i-1]+input[i-2]) > (input[i-1]+input[i-2]+input[i-3]):
        count += 1

# Print the count
print(count)