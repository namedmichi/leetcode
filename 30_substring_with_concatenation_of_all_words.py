from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        permutations = []
        index_list = []
        for i in range(len(words)):
            temp = words[i]
            for y in range(len(words)):
                if i == y:
                    continue
                temp += words[y]
            permutations.append(temp)
        print(permutations)

        for i in range(len(s)):
            temp = s[i]
            for y in range(i+1, len(s)):
                temp += s[y]
                if temp in permutations:
                    index_list.append(i)
                    

        return index_list


        
sol =Solution()

print(sol.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))