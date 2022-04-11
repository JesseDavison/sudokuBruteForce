# sudoku brute force



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
    print("***********************")
    print("trying to put " + str(int) + " into " + str(row) + "/" + str(column))
    for rowCheck in range(9):
        if table[row][rowCheck][0] == int:
            result = False
            print("                         at " + str(row) + "/" + str(rowCheck) + ": found " + str(int) + " in same row")
    # check the column
    for colCheck in range(9):
        if table[colCheck][column][0] == int:
            result = False
            print("                         at " + str(colCheck) + "/" + str(column) + ": found " + str(int) + " in same column")
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
                                print("                         at " + str(rw) + "/" + str(col) + ": found " + str(int) + " in same box")
    if result == True:
        print("                         " + str(int) + " will fit at " + str(row) + " / " + str(column))
    return result








# counter = 0
def solveBrutely(table):
    for row in range(9):
        for column in range(9):
            if table[row][column][1] == False and table[row][column][0] == '-':
                for int in range(9):
                    if willFit(table, int+1, row, column):
                        table[row][column][0] = int+1
                        # global counter
                        # counter += 1
                        printTable(table)
                        print("putting " + str(int+1) + " into " + str(row) + "/" + str(column))

                        solveBrutely(table)
                    if int == 8:
                        return



    print("table solved:")
    printTable(table)

# print("counter: " + str(counter))












sudokuTable = [[['-', False] for j in range(9)] for i in range(9)]          # False that it is hardcoded... so it can be changed

sudokuTable[0][0] = [1, True]           # True that it is hardcoded, and cannot be changed
# sudokuTable[0][1] =
# sudokuTable[0][2] = 
# sudokuTable[0][3] = 
# sudokuTable[0][4] = 
# sudokuTable[0][5] = 
# sudokuTable[0][6] = 
# sudokuTable[0][7] = 
sudokuTable[0][8] = [7, True]

# sudokuTable[1][0] =
# sudokuTable[1][1] = 
# sudokuTable[1][2] = 
# sudokuTable[1][3] = 
sudokuTable[1][4] = [8, True]
sudokuTable[1][5] = [3, True]
sudokuTable[1][6] = [5, True]
sudokuTable[1][7] = [6, True]
# sudokuTable[1][8] = 

sudokuTable[1][5] = [3, True]
sudokuTable[1][6] = [5, True]
sudokuTable[1][7] = [6, True]

sudokuTable[2][2] = [8, True]
sudokuTable[2][3] = [6, True]
sudokuTable[2][5] = [7, True]

sudokuTable[3][0] = [8, True]
sudokuTable[3][3] = [4, True]
sudokuTable[3][6] = [1, True]
sudokuTable[3][7] = [7, True]

sudokuTable[4][0] = [4, True]
sudokuTable[4][2] = [5, True]
sudokuTable[4][6] = [2, True]
sudokuTable[4][8] = [6, True]

sudokuTable[5][2] = [6, True]
sudokuTable[5][4] = [3, True]

sudokuTable[6][1] = [8, True]
sudokuTable[6][2] = [4, True]
sudokuTable[6][3] = [2, True]
sudokuTable[6][5] = [6, True]
sudokuTable[6][6] = [9, True]
sudokuTable[6][7] = [1, True]
sudokuTable[6][8] = [5, True]

sudokuTable[7][1] = [2, True]
sudokuTable[7][2] = [1, True]
sudokuTable[7][4] = [5, True]

sudokuTable[8][1] = [7, True]
sudokuTable[8][2] = [9, True]
sudokuTable[8][3] = [3, True]
sudokuTable[8][4] = [1, True]
sudokuTable[8][5] = [4, True]
sudokuTable[8][6] = [6, True]
sudokuTable[8][8] = [8, True]

# newTable = []
# createTable(newTable)

printTable(sudokuTable)
print("trying solve now: ")
solveBrutely(sudokuTable)



# willFit(sudokuTable, 9, 7, 7)