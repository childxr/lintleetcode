class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        
        if not s:
            return 0
        if len(s) < k:
            return len(s)
        
        left, right = -1, 0
        cnt = 0
        ans = 0
        mapper = [0 for i in xrange(256)]
        while right < len(s):
            ch = s[right]
            mapper[ord(ch)] += 1
            if mapper[ord(ch)] == 1:
                cnt += 1
            while cnt > k:
                left += 1
                rm = s[left]
                mapper[ord(rm)] -= 1
                if mapper[ord(rm)] == 0:
                    cnt -= 1
            if cnt <= k:
                ans = max(right-left, ans)
            right += 1
        
        return ans
            
