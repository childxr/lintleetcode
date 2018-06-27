class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        return self.findKth(matrix, k)
    
    def findKth(self, matrix, k):
        # find the kth number in matrix
        # using binaray search, identify a number that is in K position by
        # - initiate a search range (0, sys.maxint) == (start, end)
        # - give a initial guess of Kth position number's value, which is low+(high-low)/2 == guess
        # - counting elements in all rows in the matrix that is smaller than the guess, cnt
        # - if cnt is >= k, our guess number is too big, we need to guess with a smaller number, we could adjust this by making high = guess
        # - else, make make low = guess
        # if we eventually narrow down to a range [low, high] where low + 1 = high
        # just need to count in the matrix, if guess = low, is it only K elements <= low, if true, low is the guess, else, high is the guess
        
        low, high = 0, sys.maxint
        while low + 1 < high:
            guess = low + (high-low)/2
            cnt = self.countMatrix2D(matrix, guess)
            if cnt < k:
                low = guess
            else:
                high = guess
        
        if self.countMatrix2D(matrix, low) >= k:
            return low
        else:
            return high
            
    
    def countMatrix2D(self, matrix, target):
        res = 0
        for row in matrix:
            res += self.countSmaller(row, target) # get how many elements are smaller or equal to target
        return res

    def countSmaller(self, row, target):
        low, high = 0, len(row) - 1
        while low + 1 < high:
            mid = low + (high-low)/2
            if row[mid] <= target:
                low = mid
            else:
                high = mid
        
        if row[low] > target:
            return low
        elif row[high] > target:
            return high
        return len(row)
