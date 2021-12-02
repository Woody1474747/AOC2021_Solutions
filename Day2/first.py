with open("test.txt") as f:
    data = []
    for line in f:
        sline = line.split(" ")
        sline[1] = sline[1].split("\n")[0]
        data.append(sline)

depth = 0
horizontal = 0
aim = 0
for line in data:
    if line[0] == "forward":
        horizontal = horizontal + int(line[1])

    elif line[0] == "up":
        depth = depth - int(line[1])

    elif line[0] == "down":
        depth = depth + int(line[1])

print(horizontal*depth)