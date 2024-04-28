from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if(len(strs[0]) == 0):
            return ""
        for i in range(200):
            try:
                prefix += strs[0][i]
            except:
                return prefix
            for y in range(len(strs)):
                try:
                    if(strs[y][i] == prefix[i]):
                        continue
                except:
                    return prefix[0:len(prefix)-1]
                else:
                    return prefix[0:len(prefix)-1]



sol = Solution()

print(sol.longestCommonPrefix(["flower","flow","flight"]))