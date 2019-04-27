def rotate(mat):
    n = len(mat)
    for i in range(int(n/2)):
        first = i
        last = n - 1 - i
        for i2 in range(first, last):
            tmp = mat[i][i2]
            mat[i][i2] = mat[n-1-i2][i]
            mat[n-1-i2][i] = mat[n-1-i][n-1-i2]
            mat[n-1-i][n-1-i2] = mat[i2][n-1-i]
            mat[i2][n-1-i] = tmp


def test_1_7():
    mat = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    print(mat)
    rotate(mat)
    print(mat)
    rotate(mat)
    print(mat)
