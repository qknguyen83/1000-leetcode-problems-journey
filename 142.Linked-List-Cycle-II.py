class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        record = set()
        currentNode = head
        while currentNode:
            if currentNode in record:
                break
            record.add(currentNode)
            currentNode = currentNode.next
        
        return currentNode
