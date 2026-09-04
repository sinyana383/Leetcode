from typing import List
from pprint import pprint

class Solution:
    def mark_island(self, x:int, y:int, grid: List[List[str]], mark:str, x_len:int, y_len:int):
        if x + 1 < x_len and grid[y][x + 1] == "1": #right
            grid[y][x + 1] = mark
            self.mark_island(x+1,y, grid, mark,x_len,y_len)
        if y + 1 < y_len and grid[y+1][x] == "1":  # down
            grid[y+1][x] = mark
            self.mark_island(x, y+1, grid, mark, x_len, y_len)
        if x - 1 >= 0 and grid[y][x-1] == "1":  # left
            grid[y][x-1] = mark
            self.mark_island(x-1, y, grid, mark, x_len, y_len)
        if y - 1 >= 0 and grid[y - 1][x] == "1":  # down
            grid[y - 1][x] = mark
            self.mark_island(x, y - 1, grid, mark, x_len, y_len)

    def numIslands(self, grid: List[List[str]]) -> int:
        y_len = len(grid)
        x_len = len(grid[0])
        res_c = 1

        for i in range(0, y_len):
            for j in range(0,x_len):
                if grid[i][j] == "1":
                    res_c += 1
                    grid[i][j] = str(res_c)
                    self.mark_island(j,i,grid,str(res_c), x_len, y_len)

        return res_c - 1


sol = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))
pprint(grid)