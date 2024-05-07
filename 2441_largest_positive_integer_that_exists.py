class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for num in nums:
            if -num in nums:
                return -num
        return -1