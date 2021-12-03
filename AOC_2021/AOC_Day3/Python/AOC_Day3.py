# Read in input text file
file = open("AOC_2021/AOC_Day3/Python/AOC_Day3_Input.txt","r")

# Create an array and populate it with the binary numbers from each 
# line from the text file
input = []
for line in file.readlines():
    input.append(line)
file.close()

# Part 1 - Answer: 3901196
def gamma(arr):
    gamma = ""

    for column in range(0, 12):
        count0 = 0
        count1 = 0
        for row in range(0, len(arr)):
            if arr[row][column] == '1':
                count1 += 1
            else:
                count0 += 1
        if count1 == count0 or count1 > count0:
            gamma += "1"
        else:
            gamma += "0"

    return gamma

def epsilon(arr):
    epsilon = ""

    for column in range(0, 12):
        count0 = 0
        count1 = 0
        for row in range(0, len(arr)):
            if arr[row][column] == '1':
                count1 += 1
            else:
                count0 += 1
        if count1 == count0 or count1 > count0:
            epsilon += "0"
        else:
            epsilon += "1"
            
    return epsilon

gammaDec = int(gamma(input), 2)
epsilonDec = int(epsilon(input), 2)
print("Part 1: ", gammaDec * epsilonDec)

# Part 2 - Answer: 4412188
ogr = input
c02sr = input

for column in range(0, 12):
    mC = []
    g = gamma(ogr)
    for row in range(len(ogr)):
        if g[column] == '1' and ogr[row][column] == '1':
            mC.append(ogr[row])
        elif g[column] == '0' and ogr[row][column] == '0':
            mC.append(ogr[row])
        else:
            continue
    ogr = mC
    if len(ogr) <= 2:
        if ogr[0][column] == '1':
            ogr = ogr[0]
            break
        else:
            ogr = ogr[1]
            break


for column in range(0, 12):
    lC = []
    e = epsilon(c02sr)
    for row in range(len(c02sr)):
        if e[column] == '1' and c02sr[row][column] == '1':
            lC.append(c02sr[row])
        elif e[column] == '0' and c02sr[row][column] == '0':
            lC.append(c02sr[row])
        else:
            continue
    c02sr = lC
    if len(c02sr) <= 2:
        if c02sr[0][column] == '0':
            c02sr = c02sr[0]
            break
        else:
            c02sr = c02sr[1]
            break

ogrDec = int(ogr, 2)
c02srDec = int(c02sr, 2)
print("Part 2: ", ogrDec * c02srDec)