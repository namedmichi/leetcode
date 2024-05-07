class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        ascii_list = []

        total = 0

        for c in s:
            ascii_list.append(ord(c))

        for i in range(len(ascii_list)-1):
            total += abs(ascii_list[i] - ascii_list[i+1])
        
        return total
    

sol = Solution()

print(sol.scoreOfString("hello"))