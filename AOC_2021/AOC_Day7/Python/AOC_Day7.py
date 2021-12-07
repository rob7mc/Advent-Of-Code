# Read in input text file
file = open("AOC_2021/AOC_Day7/Python/AOC_Day7_Input.txt","r")

input = []
for line in file.read().split(','):
    input.append(int(line))
file.close()

# Part 1 - Answer: 337488
sum = float('inf')
for i in range(min(input), max(input)+1):
    currentSum = 0
    for num in input:
        currentSum += abs(i-num)
    if currentSum < sum:
        sum = currentSum

print("Part 1: ", sum)

# Part 2 - Answer: 89647695
sum2 = float('inf')
for i in range(min(input), max(input)+1):
    currentSum = 0
    for num in input:
        diff = abs(i-num)
        currentSum += (diff * (diff + 1)) / 2
    if currentSum < sum2:
        sum2 = currentSum

print("Part 2: ", sum2)