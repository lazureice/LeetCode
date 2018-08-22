class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans=[]
        
        for word in words:
        	d=dict() #
        	for i in range(len(word)):
        		if word[i] not in d:
        			d[word[i]]=pattern[i]
        		else:
        			if d[word[i]]!=pattern[i]:
        				break
        	else:
        		d=dict() #
	        	for i in range(len(word)):
	        		if pattern[i] not in d:
	        			d[pattern[i]]=word[i]
	        		else:
	        			if d[pattern[i]]!=word[i]:
	        				break
	        	else:
	        		ans.append(word)
        return ans




words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"


s=Solution()
print(s.findAndReplacePattern(words,pattern))