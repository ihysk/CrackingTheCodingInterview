def set_zero(mat):
    rowvec = [False] * len(mat)
    colvec = [False] * len(mat[0])
    for i1, l in enumerate(mat):
        for i2, num in enumerate(l):
            if num == 0:
                rowvec[i1] = True
                colvec[i2] = True

    for i in range(len(mat)):
        if rowvec[i]:
            nullify_row(mat, i)

    for i in range(len(mat[0])):
        if colvec[i]:
            nullify_col(mat, i)


def nullify_col(mat, i):
    for n in range(len(mat)):
        mat[n][i] = 0


def nullify_row(mat, i):
    for n in range(len(mat[i])):
        mat[i][n] = 0


def test_1_8():
    mat = [[1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1]]
    print(mat)
    set_zero(mat)
    print(mat)
