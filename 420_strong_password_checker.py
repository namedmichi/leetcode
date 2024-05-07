class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        # check missing chars
        leng = len(password)
        missing = 6 - leng
        toMuch = leng - 20
        # check lower, upper and digit
        lower = False
        upper = False
        digit = False

        # check three chars
        lastSame = 1
        lastC = ""
        counterthreerow = 0
        for c in password:
            if ord(c) >= 97 and ord(c) <= 122:
                lower = True
            elif ord(c) >= 65 and ord(c) <= 90:
                upper = True
            elif ord(c) >= 48 and ord(c) <= 57:
                digit = True
            if c == lastC:
                lastSame += 1
            else:
                lastSame = 1
            if lastSame == 3:
                counterthreerow += 1
                lastSame = 1
                lastC = ""
            else:
                lastC = c
            

        toAdd = 0
        # calculate
        if not lower:
            toAdd += 1
        if not upper:
            toAdd += 1
        if not digit:
            toAdd += 1

        toAddTemp = missing - toAdd
        if toAddTemp >= 0:
            toAdd = toAdd + toAddTemp


        temp = counterthreerow - toAdd
        if (toMuch - counterthreerow) > 0:
            if temp >= 0:
                return toMuch + toAdd
            return toAdd + toMuch - counterthreerow
        else:
            if temp >= 0:
                if (toMuch - toAdd > 0):
                    if(toAdd > 0):
                        return counterthreerow + toMuch - toAdd
                    else:
                        return temp
                else:
                    return counterthreerow
            return toAdd

sol = Solution()

print(sol.strongPasswordChecker("FFFFFFFFFFFFFFF11111111111111111111AAA"))