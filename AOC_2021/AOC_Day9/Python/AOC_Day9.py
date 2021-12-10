file = open("AOC_2021/AOC_Day9/Python/AOC_Day9_Input.txt","r")

heightmap = [[int(c) for c in l.strip()] for l in file.readlines()]
file.close()

# Part 1 - Answer: 607
risklevel = 0
height = len(heightmap)
width = len(heightmap[0])

for y in range(height):
    for x in range(width):
        current = heightmap[y][x]
        # Greater than or equal to the point above it
        if y > 0 and heightmap[y-1][x] <= current:
            continue
        # Greater than or equal to the point left of it
        elif x > 0 and heightmap[y][x-1] <= current:
            continue
        # Greater than or equal to the point below it
        elif y + 1 < len(heightmap) and heightmap[y+1][x] <= current:
            continue
        # Greater than or equal to the point right of it
        elif x + 1 < len(heightmap[y]) and heightmap[y][x+1] <= current:
            continue
        else:
            count = 0
            risklevel += (current + 1)

print("Part 1: ", risklevel)