# Read in input text file
file = open("AOC_2021/AOC_Day6/Python/AOC_Day6_Input.txt","r")

input = []
input2 = []
for line in file.read().split(','):
    input.append(int(line))
    input2.append(int(line))
file.close()

# Part 1 - Answer: 345793
for i in range(80):
    for ind in range(len(input)):
        if input[ind] == 0:
            input[ind] += 6
            input.append(int(8))
        else:
            input[ind] -= 1

print("Part 1: ", len(input))

# Part 2 - Answer: 1572643095893
dictionary = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for num in input2:
    dictionary[num] += 1

for j in range(256):
    newFish = dictionary[0]
    dictionary[7] += dictionary[0]
    for k in range (1,9):
        dictionary[k-1] = dictionary[k]
    dictionary[8] = newFish

print("Part 2: ", sum(dictionary.values()))
