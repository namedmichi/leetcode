from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0

        liste = []
        for i in nums:
            if i in liste:
                count += 1
            else:
                liste.append(i)
        nums = liste
        print(nums)
        return(len(nums))


sol = Solution()

print(sol.removeDuplicates([1,1,2]))