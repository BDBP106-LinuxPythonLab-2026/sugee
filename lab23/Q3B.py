# with open("stringmatrix.dat","r")as f:
#     grid= [line.split() for line in f if line.strip()]
#     print(grid)
#     rows = len(grid)
#     cols = len(grid[0])
#
#     columns=[]
# for j in range(cols):
#     column= []
#     for i in range(rows):
#         column.append(grid[i][j])
#     columns.append(column)
# print(columns)
#
# diagonals=[]
# for d in range(rows + cols -1):
#     diagonal= []
#     for i in range(rows):
#         j= d-i
#         if 0 <= j < cols:
#             diagonal.append(grid[i][j])
#     diagonals.append(diagonal)
# print(diagonals)