matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            ele_row_index = i + 1
            ele_col_index = j + 1
            break

moves = abs(3 - ele_row_index) + abs(3 - ele_col_index)

print(moves)

for row in matrix:
    print(row)