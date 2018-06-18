class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if k <= 0 or not A or k > len(A):
            return -1
        return self.innerKthLargestElement(len(A) - k, A, 0, len(A) - 1)
    
    def innerKthLargestElement(self, k, A, lo, hi):
        index = self.partition(A, lo, hi)
        assert index >= 0
        if index == k:
            return A[k]
        if index < k:
            return self.innerKthLargestElement(k, A, index + 1, hi)
        else:
            return self.innerKthLargestElement(k, A, lo, index - 1)
    
    def partition(self, A, lo, hi):
        if lo > hi:
            return lo
        i, j = lo, hi + 1
        while True:
            i += 1
            j -= 1
            while i < hi and A[lo] > A[i]:
                i += 1
            while j > lo and A[lo] < A[j]:
                j -= 1

            if i >= j:
                break
            self.swap(A, i, j)
        
        self.swap(A, lo, j)
        return j
    def swap(self, A, a, b):
        A[a], A[b] = A[b], A[a]