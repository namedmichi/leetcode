# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        number_string = ""
        while head:
            number_string += str(head.val)
            head = head.next 
        
        number_string = str(int(number_string) * 2)


        prev = None
        for i in range(len(number_string) -1, -1, -1):
            curr = ListNode(int(number_string[i]))
            curr.next = prev
            prev = curr

        return prev