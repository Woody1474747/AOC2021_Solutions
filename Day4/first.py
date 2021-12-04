with open('test.txt') as file:
    bingos = []
    bingoNumbers = []
    lineNumber = 0
    cache = []
    cache2 = []
    for line in file:

        if lineNumber == 0:
            bingoNumbers = line.split(",")
            bingoNumbers[len(bingoNumbers) - 1] = bingoNumbers[len(bingoNumbers) - 1].split("\n")[0]
        elif line == "\n" and lineNumber:
            bingos.append(cache2)

            cache2 = []
        else:

            cache = line.split(" ")
            for l in cache:
                if l == '':
                    cache.remove(l)
            cache[len(cache) - 1] = cache[len(cache) - 1].split("\n")[0]
            cache2.append(cache)
            cache = []

        lineNumber = lineNumber + 1
bingos.remove([])

def end(bingo, number):
    bingo = bingos[bingo]
    sol = 0
    for row in bingo:
        for rownumber in row:
            if rownumber != "X":

                sol = sol + int(rownumber)
    print(number)
    number = sol * int(number)

    print(number)


for number in bingoNumbers:
    for bingo in range(0, len(bingos)):
        for colum in range(0, len(bingos[0])):
            for bingonumber in range(0, len(bingos[0][0])):
                if bingos[bingo][colum][bingonumber] == number:
                    bingos[bingo][colum][bingonumber] = 'X'
    # Check Horizontal
    for bingo in range(0, len(bingos)):
        for colum in range(0, len(bingos[0])):
            Xs = 0
            for bingonumber in range(0, len(bingos[0][0])):

                if bingos[bingo][colum][bingonumber] == 'X':
                    Xs = Xs + 1
            if Xs == 5:

                print("BINGO")
                end(bingo, number)

                exit()
        for row in range(0, len(bingos[bingo])):
            Xs = 0
            for bingonumber in range(0, len(bingos[0][0])):
                if bingos[bingo][bingonumber][row] == 'X':

                    Xs = Xs + 1
                if Xs == 5:
                    print("BINGO2")
                    end(bingo, number)
                    exit()


