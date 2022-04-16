class Solution:
    def merger(self, head1, head2):
        theHead = None
        if head1.val <= head2.val:
            theHead = head1
            head1 = head1.next
        else:
            theHead = head2
            head2 = head2.next
        
        currentNode = theHead
        while head1 and head2:
            if head1.val <= head2.val:
                currentNode.next = head1
                currentNode = currentNode.next
                head1 = head1.next
            else:
                currentNode.next = head2
                currentNode = currentNode.next
                head2 = head2.next
        
        if head1:
            currentNode.next = head1
        if head2:
            currentNode.next = head2
        
        return theHead

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        ans = None
        for i in range(0, len(lists)):
            if lists[i] == None:
                continue
            
            if ans == None:
                ans = lists[i]
                continue
            
            ans = self.merger(ans, lists[i])
        
        return ans
