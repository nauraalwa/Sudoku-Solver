#using backtracking algorithm : 1. find empty pos, 2. check valid or no, 3. if yes continue, 4. if not go back
#checking valid means whether the number is already written in rows and columns and the box
#if board is full, then solution is found

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(bo)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else: 
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i, row in enumerate(bo):
        for j, val in enumerate(row):
            if val == 0:
                return (i,j) #row, col
    
    return None

def valid(bo, num, pos):
    #check rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check columns    
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
            
    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find #using recursion we keep looping until find empty position

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0

    return False

print_board(board)
solve(board)
print("__________________")
print("                  ")
print_board(board)


            



