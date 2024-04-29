class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"{" : "}", 
                "[" : "]", 
                "(" : ")"}
        openList =[]
        for c in s:
            if (c == "{" or c == "(" or c == "["):
                openList.append(c)
            else:
                if(len(openList) == 0):
                    return False
                if(dict[openList.pop()] == c):
                    continue
                else:
                    return False
        if(len(openList) == 0):
            return True
        else:
            return False



sol = Solution()

print(sol.isValid("([)]"))