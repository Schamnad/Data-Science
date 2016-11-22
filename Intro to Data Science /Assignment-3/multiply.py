import MapReduce
import sys

"""
Matrix multiply.
Assume two matrices A and B in a sparse matrix format, where each record is of the form i, j, value. Compute the matrix multiplication A x B
Each list will be in th eform: [matrix, i, j, value] where matrix is a
string ("a" from matrix A, "b" from B),  and i,j, value are integers.
Since we are told the matrix is sparse), we can assume we know the dimensions.
"""

DIM_MAT = 5

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(matrix_record):
    # key: result cell no, value: Aij once for each B col or Bjk once for each A row
    # value: count
    matrix = matrix_record[0]
    row = matrix_record[1]
    col = matrix_record[2]
    value = matrix_record

    # Set an entry for a dot product over every column in B
    if matrix == "a":
        for j in range(DIM_MAT):
            key = (row, j)
            mr.emit_intermediate(key,value)
    # Set an entry for a dot product over every row in A
    elif matrix == "b":
        for i in range(DIM_MAT):
            key = (i, col)
            mr.emit_intermediate(key, value)

def reducer(key, list_of_matrix_values):
    matrix_value = 0
    # key: result matrix cell
    # value: component cells to dot prod
    for cell in list_of_matrix_values:
        #assuming a always before b
        if cell[0] == "a":
            for c in list_of_matrix_values:
                if c[0] == "b" and cell[2] == c[1]:
                    matrix_value += cell[3]*c[3]

    mr.emit((key[0], key[1], matrix_value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
