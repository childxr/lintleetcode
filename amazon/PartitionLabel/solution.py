class Solution:
    """
    @param S: a string
    @return: a list of integers representing the size of these parts
    """
    def partitionLabels(self, S):
        # Write your code here
        
        m = {s: i for i, s in enumerate(S)}
        start = 0
        end = 0
        i = 0
        ans = []
        
        while i < len(S):
            end = max(end, m[S[i]])
            if end == i:
                ans.append(end-start+1)
                start = end + 1
            i += 1
        
        return ans
            
            
