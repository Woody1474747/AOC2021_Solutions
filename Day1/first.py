with open("input.txt") as file:
    increases = -1
    number = 0
    for line in file:
        if(int(line) > number):
            increases += 1
        number = int(line)

print("Number of Increases: " + str(increases))