# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def lengthoflist(head):
            temp=head
            length=0
            while temp:
                temp=temp.next
                length+=1
            return length
        if(lengthoflist(head)==1 and n==1):
            return None
        if(n==lengthoflist(head)):
            return head.next
        else:
            temp=head
            counter=lengthoflist(head)-n-1
            while counter:
                temp=temp.next
                counter-=1
            temp.next=temp.next.next
            return head