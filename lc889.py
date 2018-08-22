# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        
        if not pre:
            return None
        root=TreeNode(pre[0])

        if len(pre)>1:
            i=post.index(pre[1])
            root.left=self.constructFromPrePost(pre[1:(i+2)],post[:(i+1)])
            root.right=self.constructFromPrePost(pre[(i+2):],post[(i+1):-1])

        return root




s=Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]

print(s.constructFromPrePost(pre,post))