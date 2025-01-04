# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
    
        curr = head
        values = []
    
        # Extract values from the linked list
        while curr:
            values.append(curr.val)
            curr = curr.next
    
        # Sort the extracted values
        values.sort()
    
        # Reconstruct the linked list with sorted values
        new_head = ListNode(values[0])
        curr = new_head
        for i in range(1, len(values)):
            curr.next = ListNode(values[i])
            curr = curr.next
    
        return new_head
