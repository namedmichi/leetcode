class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for j in jewels:
            for c in stones:
                if c == j:
                    count += 1

        return count