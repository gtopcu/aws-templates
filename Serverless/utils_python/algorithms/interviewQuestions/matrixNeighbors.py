
# Input format orthogonal matrix i.e. "000_010"
# If adjacent live cells are less than 2 or more than 3, they die
# If adjacent live cells are 2 or 3, they live
# If a cell is dead and has 3 live neighbors, it comes to life
# def game_of_life(input: str) -> str:
    
#     # mylist = [item for sublist in list for item in sublist]
#     output = []
#     rows = input.split("_")
#     row_count = len(rows)
#     for i, row in enumerate(rows):
#         if len(row) == 0: 
#              continue
#         current_row = []
#         for j, cell in enumerate(row):
#             val_current = int(cell)
#             current_row.append(val_current)
#         output.append(current_row)
  
#     for i, row in enumerate(output):
#         for j, cell in enumerate(row):
#             current_state = cell
#             live_neighbors = 0
#             dead_neighbors = 0

#             if output[i+1][j+1] == 1:
#                 live_neighbors += 1


            
# def game_of_life(input: str) -> str:


# from pprint import pprint

# def get_neighbors(matrix):
    
#     rows, cols = len(matrix), len(matrix[0])
#     alive_matrix = {}

#     for x in range(rows):
#         for y in range(cols): 

#             alive = alive_matrix.setdefault((x, y), 0)

#             if y-1 >= 0:
#                 if matrix[x][y-1] == 1:
#                     alive += 1
#             if y+1 < cols:
#                 if matrix[x][y+1] == 1:
#                     alive += 1
#             if x-1 >= 0:
#                 if matrix[x-1][y] == 1:
#                     alive += 1
#                 if y-1 >= 0:
#                     if matrix[x-1][y-1] == 1:
#                         alive += 1
#                 if y+1 < cols:
#                     if matrix[x-1][y+1] == 1:
#                         alive += 1
#             if x+1 < rows:
#                 if matrix[x+1][y] == 1:
#                     alive += 1
#                 if y-1 >= 0:
#                     if matrix[x+1][y-1] == 1:
#                         alive += 1
#                 if y+1 < cols:
#                     if matrix[x+1][y+1] == 1:
#                         alive += 1
            
#             alive_matrix[(x, y)] = alive


#     # print("AliveMatrix: ")
#     # pprint(alive_matrix)
#     #result =  { (i, j): i for i in range(rows) j for j in range(cols) }
    

# if __name__ == "__main__":
#     # print(game_of_life("0"))
#     # print(game_of_life("01"))
#     # print(game_of_life("01_"))
#     # print(game_of_life("01_1"))
#     # print(game_of_life("01_11_"))
#     # print(game_of_life("010_101_111")§)

#     matrix = [[0, 1, 0], [1, 0, 1], [1, 1, 1]]
#     #matrix = [[1, 1], [1, 1,]]
#     #pprint(matrix)
#     get_neighbors(matrix)

# # [0, 1, 0]
# # [1, 0, 1]
# # [1, 1, 1]

# # [1, 1]
# # [1, 1]


def print_neighbors(grid, x, y):
    
    rows = len(grid)
    cols = len(grid[0])
    neighbors = [
        (x-1, y),   # Left
        (x+1, y),   # Right
        (x, y-1),   # Up
        (x, y+1)    # Down
    ]
    for neighbor_x, neighbor_y in neighbors:
        if 0 <= neighbor_x < rows and 0 <= neighbor_y < cols:
            print("Neighbor at ({}, {}): {}".format(neighbor_x, neighbor_y, grid[neighbor_x][neighbor_y]))
        else:
            pass #print("Neighbor at ({}, {}): Out of bounds".format(neighbor_x, neighbor_y))

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_neighbors(grid, 0, 0)

