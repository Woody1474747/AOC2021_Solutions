with open("test.txt") as file:

    remaining = []
    lines = file.readlines()
    remaining = lines
    for i in range(0, len(lines[0]) -1):
        one = 0
        zero = 0
        cache = remaining
        for line in cache:
            if int(line[i]) == 0:
                zero = zero + 1
            else:
                one = one + 1

        remaining = []

        if one > zero:
            for line in cache:
                if line[i] == "1":
                    remaining.append(line)

        elif one == zero:
            for line in cache:
                if line[i] == "1":
                    remaining.append(line)
        else:
            for line in cache:
                if line[i] == "0":
                    remaining.append(line)
    oxygen = remaining[0]
    remaining = lines
    for i in range(0, len(lines[0]) - 1):
        one = 0
        zero = 0
        cache = remaining
        for line in cache:
            if int(line[i]) == 0:
                zero = zero + 1
            else:
                one = one + 1

        remaining = []

        if one > zero:
            for line in cache:
                if line[i] == "0":
                    remaining.append(line)
        elif one == zero:
            for line in cache:
                if line[i] == "0":
                    remaining.append(line)
        else:
            for line in cache:
                if line[i] == "1":
                    remaining.append(line)

        if int(len(remaining)) == 1:
            co = remaining[0]
            print("end")
            break
        print(len(remaining))



print(int(oxygen, 2) * int(co, 2))




