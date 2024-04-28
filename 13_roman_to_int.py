class Solution:
    def romanToInt(self, s: str) -> int:
        rS = s[::-1]
        value_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i in range(len(s)):
            c = rS[i]
            value = value_dic[c]
            if(i==0):
                sum += value
                continue
            if (value_dic[rS[i-1]] <= value):
                sum += value
            else:
                sum -= value
        return sum


sol = Solution()

print(sol.romanToInt("LVIII"))