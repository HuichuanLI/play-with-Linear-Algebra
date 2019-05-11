from playLA.Matrix import Matrix

if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    matrix1 = Matrix([[1, 2], [3, 4]])

    print("matrix={}".format(matrix + matrix1))

    print("matrix={}".format(matrix - matrix1))


    print("matrix={}".format(matrix *2))

    print(len(matrix))

    print(matrix[0, 1])

    print(matrix.col_vector(1))

    print(Matrix.zero(2,3))