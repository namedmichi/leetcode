class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            pArray = word.split(ch, 1)
            p = pArray[0][::-1]
            return ch +  p + pArray[1]
        return word