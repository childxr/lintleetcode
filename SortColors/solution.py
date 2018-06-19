class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        freq = [0 for i in xrange(k)]
        for color in colors:
            freq[color - 1] += 1
        cnt = 0
        for i in xrange(k):
            for j in xrange(freq[i]):
                colors[cnt] = i + 1
                cnt += 1
        

