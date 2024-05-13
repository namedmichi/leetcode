from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []

        temp = []

        for i in range(len(grid) - 2):
            for y in range(len(grid) - 2):
                tempList = []
                tempList.append(grid[i+0][y+0])
                tempList.append(grid[i+0][y+1])
                tempList.append(grid[i+0][y+2])
                tempList.append(grid[i+1][y+0])
                tempList.append(grid[i+1][y+1])
                tempList.append(grid[i+1][y+2])
                tempList.append(grid[i+2][y+0])
                tempList.append(grid[i+2][y+1])
                tempList.append(grid[i+2][y+2])
                tempList.sort()
                max = tempList.pop()
                temp.append(max)
            result.append(temp)
            temp = []

        return result