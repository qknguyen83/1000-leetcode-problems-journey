class Solution:
    def helper(self, root, arr):
        if root != None:
            self.helper(root.left, arr)
            arr.append(root.val)
            self.helper(root.right, arr)
        
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.helper(root, arr)
        
        return arr
