from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()

        ret = []

        prev = None

        for num in nums:
            if prev == None:
                prev = num
            else:
                ret.append(num)
                ret.append(prev)
                prev = None

        return ret