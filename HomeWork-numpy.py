import numpy as np

def arr(N):
    a = np.arange(N-1, -1, -1)
    print(type(a), '\n', a)

def dia(N):
    d = np.arange(N).reshape((3, 3))
    print(type(d), '\n', d, '\n', sum(np.diag(d)))

def sis():
    xyz = [4, 2, 1, 1, 3, 0, 0, 5, 4]
    f = [4, 12, -3]

    matrix = np.array(xyz).reshape((3, 3))
    print('x, y, z', np.linalg.solve(matrix, f))

    result = []
    deter_xyz = np.linalg.det(matrix)
    for j in range(0, 3):
        m = matrix.copy()
        for i in range(0, 3):
            m[i][j] = f[i]
        result.append(np.linalg.det(m)/deter_xyz)
    print('x, y, z', result)


if __name__ == '__main__':
    #arr(10)
    #dia(9)
    sis()