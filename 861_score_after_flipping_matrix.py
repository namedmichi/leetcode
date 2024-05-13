from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                grid[i][0] = 1
                for y in range(1,len(grid[i])):
                    grid[i][y] = grid[i][y] ^ 1
        zero = 0
        for i in range(1,len(grid[0])):
            for y in range(len(grid)):
                if grid[y][i] == 0:
                    zero += 1
            if zero > len(grid)/2:
                for p in range(len(grid)):
                    grid[p][i] = grid[p][i] ^ 1
            zero = 0


        tempString = ""
        sum = 0
        for i in range(len(grid)):
            for y in range(len(grid[i])):
                tempString += str(grid[i][y])
            base10Int = int(tempString, 2)
            sum += base10Int
            tempString = ""
        return sum


sol = Solution()

sol.matrixScore([[0,1,1],[1,1,1],[0,1,0]])