file = open("AOC_2021/AOC_Day10/Python/AOC_Day10_Input.txt","r")

input = []
for line in file:
    temp = []
    for char in line:
        temp.append(char)
    input.append(temp)
file.close()

# Part 1 - Answer: 364389
count = 0
opens = {'(', '{', '[', '<'}
vals = {')':3, '}':1197, ']':57, '>':25137}

for line in input:
    stack = []
    for char in line:
        if char in opens:
            stack.append(char)
        for i in range(len(stack)):
            if char == ')':
                if stack.pop() != '(':
                    count += vals[char]
            elif char == '}':
                if stack.pop() != '{':
                    count += vals[char]
            elif char == ']':
                if stack.pop() != '[':
                    count += vals[char]
            elif char == '>':
                if stack.pop() != '<':
                    count += vals[char]
            break

print("Part 1: ", count)