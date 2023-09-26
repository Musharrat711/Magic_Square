def Odd_Magic_Square(N):

    List = [[0 for element in range(N)] for item in range(N)]

    num = 1
    row = 0
    col = N//2
    while True:
        if num == N * N + 1:
            break
        if num == 1:
            List[row][col] = num
        else:
            row = row - 1
            col = col + 1

            if (row < 0) and (col > N - 1):
                row = row + 2
                col = N-1

            elif row < 0:
                row = N - 1

            elif col > N - 1:
                col = 0

            if List[row][col] != 0:
                row = row + 2
                col = col - 1

            List[row][col] = num

        num += 1


    for item in List:
        print(*item)
