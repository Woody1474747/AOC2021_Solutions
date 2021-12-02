def NumberOfIncreases(data):
    increases = 0
    for i in range(1,len(data)):
        if data[i] > data[i - 1]:
            increases +=1
    return increases

with open("input.txt") as f:
    one = []
    for line in f:
        one.append(int(line))

three = []
for i in range(2, len(one)):
    three.append(one[i] + one[i-1] + one[i-2])

print("solution: " + str(NumberOfIncreases(three)))