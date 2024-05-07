class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort()

        total_satisfaction = 0
        max_satisfaction = 0
        len_dishes = len(satisfaction)

        for i in range(len_dishes - 1, -1, -1):
            if satisfaction[i] > -total_satisfaction:
                total_satisfaction += satisfaction[i]
                max_satisfaction += total_satisfaction
            else:
                break

        return max_satisfaction
    

sol = Solution()

print(sol.maxSatisfaction([-1,-8,0,5,-7]))