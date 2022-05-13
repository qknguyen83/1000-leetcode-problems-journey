class Solution:
    def helper(self, nodes):
        for i in range(0, len(nodes) - 1):
            nodes[i].next = nodes[i+1]
        nodes[len(nodes) - 1].next = None
        
    def connect(self, root: 'Node') -> 'Node':
        nodes = [root]
        
        while len(nodes) > 0 and root != None:
            self.helper(nodes)
            
            nextNodes = []
            for node in nodes:
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
                    
            nodes = nextNodes
        
        return root
