# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fastPointer = head
        slowPointer = head
        
        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            
        previousNode = None
        while slowPointer:
            temp = slowPointer.next
            slowPointer.next = previousNode
            previousNode = slowPointer
            slowPointer = temp
        
        leftPointer = head
        rightPointer = previousNode
        while rightPointer:
            if leftPointer.val != rightPointer.val:
                return False
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next
        return True