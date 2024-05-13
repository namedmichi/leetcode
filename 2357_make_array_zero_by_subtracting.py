from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        c = 0

        while True:
            while 0 in nums:
                nums.remove(0)
            if(len(nums) == 0):
                break
            smallest = min(nums)
            for i in range(len(nums)):
                nums[i] = nums[i] - smallest
            c += 1

        return c