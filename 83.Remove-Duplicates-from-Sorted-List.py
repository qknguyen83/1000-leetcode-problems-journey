class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None:
            currentNode = head
            nextNode = head.next

            while nextNode:
                if currentNode.val != nextNode.val:
                    currentNode.next = nextNode
                    currentNode = currentNode.next

                nextNode = nextNode.next

            currentNode.next = None

        return head
