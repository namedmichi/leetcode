# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        while head:
            stack.append(head)
            head = head.next

        for i in range(len(stack)-1 , 0, -1):
