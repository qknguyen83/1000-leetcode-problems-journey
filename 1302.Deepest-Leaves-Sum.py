class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = [root]
        result = 0
        while len(level) > 0:
            nextLevel = []
            tempResult = 0
            for node in level:
                tempResult = tempResult + node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            result = tempResult
            level = nextLevel
        return result
