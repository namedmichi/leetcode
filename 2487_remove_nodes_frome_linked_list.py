# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head):
        cur = head
        stack = []
        while cur:
            while stack and stack[-1].val < cur.val:
                a = stack.pop()
            stack.append(cur)
            cur = cur.next
        
        nxt = None
        while stack:
            cur = stack.pop()
            cur.next = nxt
            nxt = cur
        
        return cur
    

sol = Solution()


# Create a ListNode from the array [5,2,13,3,8]
head = ListNode(5)
current = head
for val in [2, 13, 3, 8]:
    current.next = ListNode(val)
    current = current.next

# Call the removeNodes method and print the result
result = sol.removeNodes(head)
print(result)
