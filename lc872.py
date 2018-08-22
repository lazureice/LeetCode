
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
		
class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        L1=[]
        L2=[]
        self.findLeaf(root1,L1)
        
        self.findLeaf(root2,L2)
        # print(L1)
        # print(L2)
		
        return L1 == L2
        
    
    def findLeaf(self,root,L):
        print(root.left,root.right)
        if not(root.left or root.right):
            print('yes')
            L.append(root.val)
            print(L)
            
        if root.left:
            self.findLeaf(root.left,L)
        if root.right:
            self.findLeaf(root.right,L)
        
		
		
		
root1=TreeNode(1)
root2=TreeNode(2)

sol=Solution()

print(sol.leafSimilar(root1,root2))
	   


	   