from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {1: "Gold", 2: "Silver", 3: "Bronze"}
        sorted =  score.copy()
        sorted.sort(reverse = True)
        liste = []
        for sc in score:
            index = sorted.index(sc)+1
            if index <= 3:
                liste.append(dic[index] + " Medal")
            else:
                liste.append(str(index))

        return liste
