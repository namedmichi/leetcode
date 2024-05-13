from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(arr)):
            for y in range(i+1, len(arr)):
                dic[str(arr[i]) + "/"+ str(arr[y])] = float(arr[i]/arr[y])

        dic = dict(sorted(dic.items(), key=lambda item: item[1]))

        key = list(dic.keys())[k-1]

        split = key.split("/")

        split[0] = int(split[0])
        split[1] = int(split[1])

        return split



sol = Solution()


sol.kthSmallestPrimeFraction([1,2,3,5],3)