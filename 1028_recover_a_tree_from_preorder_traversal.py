# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        stack = []
        count = 0 
        arr = []
        temp_s = ""
        x = []
        for i in s:
            if i == "-":
                if temp_s :
                    arr.append([temp_s,count])
                    count = 0
                    temp_s = ""
                count+=1
            
            else:
                temp_s += i

        if temp_s:
            arr.append([temp_s,count])
        for i in arr:
            
            while stack and stack[-1][1]>=i[1]:
                stack.pop()
            if stack:
                if stack[-1][0].left:
                    stack[-1][0].right = TreeNode(i[0])
                    stack.append([stack[-1][0].right,i[1]])
                else:
                    stack[-1][0].left = TreeNode(i[0])
                    stack.append([stack[-1][0].left,i[1]])
                    
            else:
                stack.append([TreeNode(i[0]),i[1]])


        return stack[0][0]


sol = Solution()

print(sol.recoverFromPreorder("1-2--3--4-5--6--7"))