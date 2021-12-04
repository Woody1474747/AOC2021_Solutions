import time


print("The last Print is the Solution!")

time.sleep(3)

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
finished = []
solution = 0
def end(bingo, number):
    if not bingo in finished:
        finished.append(bingo)
        bingo = bingos[bingo]
        sol = 0
        for row in bingo:
            for rownumber in row:
                if rownumber != "X":
                    sol = sol + int(rownumber)

        solution = sol * int(number)
        print(solution)




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


                end(bingo, number)


        for row in range(0, len(bingos[bingo])):
            Xs = 0
            for bingonumber in range(0, len(bingos[0][0])):
                if bingos[bingo][bingonumber][row] == 'X':

                    Xs = Xs + 1
                if Xs == 5:


                    end(bingo, number)
