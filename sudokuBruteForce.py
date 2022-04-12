# sudoku brute force

from datetime import datetime



def printTable(table):
    print("-------------------------")
    for row in range(9):
        print('| ', end='')
        for column in range(3):
            print(str(table[row][column][0]) + ' ', end='')
        print('| ', end='')
        for column in range(3, 6):
            print(str(table[row][column][0]) + ' ', end='')    
        print('| ', end='')
        for column in range(6, 9):
            print(str(table[row][column][0]) + ' ', end='')    
        print('|')
        if row == 2 or row == 5 or row == 8:
            print("-------------------------")


def createTable(table):
    blankTable = [['-' for j in range(9)] for i in range(9)]
    for row in range(9):
        print('row ' + str(row))
        for column in range(9):
            blankTable[row][column] = input('column ' + str(column) + ': ')


def willFit(table, int, row, column):
    result = True       # True, as in, "it is True that this int is a possible solution for this cell"
    # check the row
    # print("trying to put " + str(int) + " into " + str(row) + "/" + str(column))
    # printTable(table)
    for rowCheck in range(9):
        if table[row][rowCheck][0] == int:
            result = False
            # print("                         at " + str(row) + "/" + str(rowCheck) + ": found " + str(int) + " in same row")
    # check the column
    for colCheck in range(9):
        if table[colCheck][column][0] == int:
            result = False
            # print("                         at " + str(colCheck) + "/" + str(column) + ": found " + str(int) + " in same column")
    # check the box
    boxRow = -1
    colRow = -1
    if row < 3:
        boxRow = 0
    elif row < 6 and row > 2:
        boxRow = 1
    elif row > 5:
        boxRow = 2
    if column < 3:
        colRow = 0
    elif column < 6 and column > 2:
        colRow = 1
    elif column > 5:
        colRow = 2

    for rr in range(3):
        for cc in range(3):
            if boxRow == rr:
                if colRow == cc:
                    for rw in range(rr * 3, (rr+1) * 3):
                        for col in range(cc * 3, (cc+1) * 3):
                            if table[rw][col][0] == int:
                                result = False
                                # print("                         at " + str(rw) + "/" + str(col) + ": found " + str(int) + " in same box")
    # if result == True:
    #     print("                         " + str(int) + " will fit at " + str(row) + " / " + str(column))
    return result


def isItSolved(table):
    solved = True
    # check every row
    for row in range(9):
        contentsOfRow = []        
        for col in range(9):
            contentsOfRow.append(table[row][col][0])
        for int in range(9):
            if int+1 not in contentsOfRow:
                solved = False
                # print("                                                     failed row test, at row " + str(row))
    # check every column
    for col in range(9):
        contentsOfCol = []
        for row in range(9):
            contentsOfCol.append(table[row][col][0])
        for int in range(9):
            if int+1 not in contentsOfCol:
                solved = False
                # print("                                                     failed col test, at col " + str(col))
    return solved



def solveBrutely(table):
    global tableSolved
    if tableSolved == False:
        for row in range(9):
            for column in range(9):
                if table[row][column][1] == False and table[row][column][0] == '-':
                    for int in range(9):
                        if willFit(table, int+1, row, column) and tableSolved == False:
                            # copyOfTable = table
                            table[row][column][0] = int+1
                            # print("******************************************************************************")
                            # print("             putting " + str(int+1) + " into " + str(row) + "/" + str(column) + "   counter:" + str(counter))
                            # printTable(table)
                            if row == 8 and column == 8:
                                tableSolved = isItSolved(table)
                                printTable(table)                         
                            solveBrutely(table)
                    table[row][column][0] = '-'
                    return













sudokuTable = [[['-', False] for j in range(9)] for i in range(9)]          # False that it is hardcoded... so it can be changed

sudokuTable[0][0] = [7, True]           # True that it is hardcoded, and cannot be changed
# sudokuTable[0][1] = [1, True]
sudokuTable[0][2] = [2, True]
sudokuTable[0][3] = [9, True]
sudokuTable[0][4] = [1, True]
sudokuTable[0][5] = [4, True]
sudokuTable[0][6] = [8, True]
sudokuTable[0][7] = [5, True]
# sudokuTable[0][8] = [7, True]

sudokuTable[1][0] = [3, True]
# sudokuTable[1][1] = [1, True]
sudokuTable[1][2] = [4, True]
# sudokuTable[1][3] = [1, True]
sudokuTable[1][4] = [7, True]
sudokuTable[1][5] = [8, True]
sudokuTable[1][6] = [2, True]
sudokuTable[1][7] = [6, True]
sudokuTable[1][8] = [9, True]

sudokuTable[2][0] = [5, True]
# sudokuTable[2][1] = [1, True]
sudokuTable[2][2] = [9, True]
# sudokuTable[2][3] = [1, True]
# sudokuTable[2][4] = [8, True]
# sudokuTable[2][5] = [3, True]
# sudokuTable[2][6] = [5, True]
# sudokuTable[2][7] = [6, True]
sudokuTable[2][8] = [1, True]

# sudokuTable[3][0] = [1, True]
# sudokuTable[3][1] = [1, True]
sudokuTable[3][2] = [7, True]
# sudokuTable[3][3] = [1, True]
# sudokuTable[3][4] = [8, True]
# sudokuTable[3][5] = [3, True]
sudokuTable[3][6] = [3, True]
sudokuTable[3][7] = [8, True]
# sudokuTable[3][8] = [1, True]

# sudokuTable[4][0] = [1, True]
# sudokuTable[4][1] = [1, True]
# sudokuTable[4][2] = [1, True]
sudokuTable[4][3] = [8, True]
# sudokuTable[4][4] = [8, True]
sudokuTable[4][5] = [1, True]
sudokuTable[4][6] = [6, True]
# sudokuTable[4][7] = [6, True]
sudokuTable[4][8] = [7, True]

# sudokuTable[5][0] = [1, True]
sudokuTable[5][1] = [9, True]
# sudokuTable[5][2] = [1, True]
# sudokuTable[5][3] = [1, True]
sudokuTable[5][4] = [3, True]
# sudokuTable[5][5] = [3, True]
# sudokuTable[5][6] = [5, True]
# sudokuTable[5][7] = [6, True]
# sudokuTable[5][8] = [1, True]

# sudokuTable[6][0] = [1, True]
sudokuTable[6][1] = [2, True]
sudokuTable[6][2] = [1, True]
# sudokuTable[6][3] = [1, True]
sudokuTable[6][4] = [8, True]
sudokuTable[6][5] = [5, True]
# sudokuTable[6][6] = [5, True]
# sudokuTable[6][7] = [6, True]
# sudokuTable[6][8] = [1, True]

# sudokuTable[7][0] = [1, True]
# sudokuTable[7][1] = [1, True]
sudokuTable[7][2] = [8, True]
# sudokuTable[7][3] = [1, True]
# sudokuTable[7][4] = [8, True]
# sudokuTable[7][5] = [3, True]
# sudokuTable[7][6] = [5, True]
# sudokuTable[7][7] = [6, True]
sudokuTable[7][8] = [6, True]

# sudokuTable[8][0] = [1, True]
sudokuTable[8][1] = [7, True]
# sudokuTable[8][2] = [1, True]
sudokuTable[8][3] = [3, True]
# sudokuTable[8][4] = [8, True]
sudokuTable[8][5] = [9, True]
# sudokuTable[8][6] = [5, True]
sudokuTable[8][7] = [2, True]
# sudokuTable[8][8] = [1, True]




###################################################
# tableSolved = False
# printTable(sudokuTable)
# print("beginning to solve now")
# start = datetime.now()
# solveBrutely(sudokuTable)
# end = datetime.now()
# print("time passed: " + str(end - start))
###################################################


# willFit(sudokuTable, 9, 7, 7)
# inputString = '--581-6---9------2-----3---5------8---867-1-----4-------7--4---2--73---6-----53--'
# inputString = '- - - - 1 - - - 6 2- - 5 - 6 3 - - - 5 - - 4 - - - - - 2 - 7 - 9 - - 4 3 - - - - - - 8 - - - - - 5 - - - - - - - - - 1 - - - - 7 - 6 - 2 - - 9 - - 9 - - - 4 - - '
# inputString = '-5-17---4--6---5------2------891--7------6--9-1---2----6-45---73------8------9---'
# inputString = '-------2---68--3-7-1--9------5----4-9---8-5-2---2---6-6----3-----37--8-5------4--'
# inputString = '8----------36------7--9-2---5---7-------457-----1---3---1----68--85---1--9----4--'   # hardest ever
inputString = '--53-----8------2--7--1-5--4----53---1--7---6--32---8--6-5----9--4----3------97--'
inputString = inputString.replace(" ", "")


newTable = [[['-', False] for j in range(9)] for i in range(9)]



increment = 0
for i in range(9):
    for j in range(9):
        if inputString[increment] != '-':
            newTable[i][j][0] = int(inputString[increment])
            newTable[i][j][1] = True
        else: 
            newTable[i][j][0] = inputString[increment]
        increment += 1



###################################################
print("printing newTable: ")
printTable(newTable)
tableSolved = False
print("beginning to solve now")
start = datetime.now()
solveBrutely(newTable)
end = datetime.now()
print("time passed: " + str(end - start))
###################################################


# fileName = 'evilDifficulty.txt'
# with open(fileName, 'w') as fileObject:
#     fileObject.write(inputString)

# fileContents = open(fileName, 'r')
# fileContents.close()
