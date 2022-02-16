class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        while currentNode:
            nextNode = currentNode.next

            if nextNode:
                temp = currentNode.val
                currentNode.val = nextNode.val
                nextNode.val = temp

                currentNode = nextNode.next
            else:
                break

        return head
