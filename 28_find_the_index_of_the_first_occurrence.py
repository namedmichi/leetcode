class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        tempW = ""
        for i in range (len(haystack)):
            for y in range(i,len(haystack)):
                tempW += haystack[y]
                if tempW == needle:
                    return i
            tempW = ""
        return -1

sol =Solution()

print(sol.strStr("hello", "ll"))