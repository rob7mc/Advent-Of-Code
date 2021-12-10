file = open("AOC_2021/AOC_Day8/Python/AOC_Day8_Input.txt","r")

inputBefore = []
inputAfter = []
for line in file:
    inputBefore.append(line.split(' | ')[0])
    inputAfter.append(line.split(' | ')[1])

# Part 1 - Answer: 470
count = 0
for line in inputAfter:
    temp = line.split()
    for word in temp:
        if len(word) in [2,4,3,7]: #[1,4,7,8]
            count += 1
print(count)