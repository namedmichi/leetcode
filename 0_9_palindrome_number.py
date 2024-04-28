class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x <= 0):
            return False
        s = str(x)
        if(len(s) % 2 == 0):
            fHalve = s[0:(int((len(s) / 2)))]
            sHalve = s[(int((len(s) / 2))):len(s)]
        else:
            fHalve = s[0:(int((len(s) / 2)))]
            sHalve = s[(int((len(s) / 2)) + 1):len(s)]
        sHalveReverse = sHalve[::-1]
        if(fHalve == sHalveReverse):
            return True
        else:
            return False


sol = Solution()

sol.isPalindrome(4224)