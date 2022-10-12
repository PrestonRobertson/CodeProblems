## https://leetcode.com/problems/max-area-of-island/
## 695. Max Area of Island
## You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
## The area of an island is the number of cells with a value 1 in the island.
## Return the maximum area of an island in grid. If there is no island, return 0.

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        unvisited = [(0, 0)]
        visited = []
        maxArea = 0

        def addUnvisited(x, y):
            if (y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])):
                if (x, y) not in visited:
                    unvisited.append((x, y))

        while (len(unvisited) > 0):
            (x, y) = unvisited.pop()

            print((x, y))

            if (grid[y][x] == 1):
                print("found an island!")
            else:
                addUnvisited(x, y + 1)
                addUnvisited(x + 1, y)
                addUnvisited(x, y - 1)
                addUnvisited(x - 1, y)

            visited.append((x, y))

        return maxArea    

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
sol = Solution()
sol.maxAreaOfIsland(grid)

