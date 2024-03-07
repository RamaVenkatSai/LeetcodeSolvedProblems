# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        temp=head
        i=0
        while temp!=None:
            i+=1
            temp=temp.next
        mid=i//2+1
        
        j=1
        temp=head
        while j<mid:
            temp=temp.next
            j+=1
        return temp