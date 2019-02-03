from math import sqrt, floor

input = [
        [0, 0, 7, 1, 0, 0, 0, 0, 3],
        [0, 4, 0, 0, 9, 0, 0, 6, 8],
        [3, 0, 0, 0, 0, 4, 7, 0, 0],
        [6, 0, 0, 0, 0, 9, 5, 0, 0],
        [0, 2, 0, 0, 6, 0, 0, 7, 0],
        [0, 0, 8, 2, 0, 0, 0, 0, 6],
        [0, 0, 1, 4, 0, 0, 0, 0, 2],
        [0, 5, 0, 0, 1, 0, 0, 8, 0],
        [8, 0, 0, 0, 0, 7, 6, 0, 0],
]
n = 9
t = [0 for i in range(n)]
cpy = []
for i in range(n):
    cpy.append(t)


def find_empty_location(l):
    global input
    global n
    for i in range(n):
        for j in range(n):
            if input[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def sudoku():
    global n
    global input
    loc = [0, 0]
    if not find_empty_location(loc):
        return True
    row = loc[0]
    col = loc[1]
    for k in range(1, n + 1):
        if promise(row, col, k):
            input[row][col] = k
            if (sudoku()):
                return True
            input[row][col] = 0

    return False


def promise(i, j, k):
    global n
    global input
    s = floor(sqrt(n))
    flag = True
    for r in range(n):
        if input[i][r] == k or input[r][j] == k:
            flag = False
    block_i = i-i % s
    block_j = j-j % s
    for r in range(s):
        for c in range(s):
            if input[block_i+r][block_j+c] == k:
                flag = False
    return flag


def main():
    if sudoku():
        for i in input:
            print(i)
    else:
        print("Answer Not Found")


if __name__ == '__main__':
    main()
