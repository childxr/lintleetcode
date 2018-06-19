class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        if not S or len(S) < 3:
            return 0
            
        S.sort(reverse=True)
        cnt = 0
        for index, longest in enumerate(S):
            j = index + 1
            k = index + 2
            while k < len(S) and S[j] + S[k] > longest:
                k += 1
            k -= 1
            while j < k:
                cnt += k - j
                j += 1
                while j < k and S[j] + S[k] <= longest:
                    k -= 1
        return cnt
            
