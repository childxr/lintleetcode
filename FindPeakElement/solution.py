class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        left, right = 1, len(A) - 2
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] < A[mid + 1]:
                left = mid
            else:
                right = mid
        if A[left] < A[right]:
            return right
        else:
            return left
