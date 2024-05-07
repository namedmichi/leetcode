class Solution(object):
    def compareVersion(self, version1, version2):

        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        if version1 == version2:
            return 0
        split1 = version1.split(".")
        split2 = version2.split(".")

        splitDif = len(split1) - len(split2)

        if(splitDif < 0):
            for i in range(-splitDif):
                split1.append("0")
        elif(splitDif > 0):
            for i in range(splitDif):
                split2.append("0")

        for i in range(len(split1)):
            if len(split1[i]) > 1:
                for c in split1[i]:
                    if int(c) > 0:
                        break
                    else:
                        split1[i] = split1[i].replace("0", "", 1)
                    if len(split1[i]) == 1:
                        break
            if len(split2[i]) > 1:
                for c in split2[i]:
                    if int(c) > 0:
                        break
                    else:
                        split2[i] = split2[i].replace("0", "", 1)
                    if len(split2[i]) == 1:
                        break

            if len(split1[i]) > len(split2[i]):
                return 1
            elif len(split1[i]) < len(split2[i]):
                return -1
            if split1[i] > split2[i]:
                return 1
            elif split1[i] < split2[i]:
                return -1
            else:
                continue
        return 0
    

sol = Solution()

print(sol.compareVersion("19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.00.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000", "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000"))