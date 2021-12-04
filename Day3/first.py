with open("test.txt") as file:

    gamma = ""
    epsilon = ""
    lines = file.readlines()
    for i in range(0, len(lines[0]) -1):
        one = 0
        zero = 0
        for line in lines:
            if int(line[i]) == 0:

                zero = zero + 1
            else:
                one = one + 1
        if one > zero:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"



print()
print(int(epsilon, 2) * int(gamma, 2))



