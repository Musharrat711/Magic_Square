
def Magic_Not_div4(N):

    matrix = []

    matrix = [[[0 for item in range(N//2)] for item in range(N//2)] for item in range(4)]

    M = N//2

    num = 1
    for element in range(4):
        mat = matrix[element]
        col = M//2
        row = 0
        mat[row][col] = num
        num += 1
        for item in range(((M)**2)-1):
            row = row - 1
            col = col + 1

            if row < 0 and col == M:
                row = 1
                col = M - 1

            elif row < 0:
                row = M - 1

            elif col == M:
                col = 0

            elif mat[row][col] != 0:
                row = row + 2
                col = col - 1

            mat[row][col] = num
            num += 1
        matrix[element] = mat

    arrangement = matrix.pop(1)
    matrix.append(arrangement)

    half_magic = [[]]*N

    i = 0
    j = 0
    for item in range(N):
        if item >= N//2:
            half_magic[item] = matrix[2][j] + matrix[3][j]
            j += 1
        else:
            half_magic[item] = matrix[0][i] + matrix[1][i]
            i += 1

    swaps = (M) - 2

    for item in range(swaps):
        for elements in range(M):
            if item >= ((swaps//2)+1):
                half_magic[elements][item+M], half_magic[elements+M][item+M] = half_magic[elements+M][item+M], half_magic[elements][item+M]
            else:
                half_magic[elements][item], half_magic[elements+M][item] = half_magic[elements+M][item], half_magic[elements][item]

    for item in half_magic:
        print(item)
