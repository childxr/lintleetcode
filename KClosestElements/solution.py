class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A:
            return []
        
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left)/2
            if A[mid] < target:
                left = mid
            else:
                right = mid
        
        ans = []
        cnt = 0
        
        while cnt < k:
            if left < 0 and right == len(A):
                break
            cnt += 1
            if left >= 0 and right < len(A):
                if abs(A[left] - target) <= abs(A[right] - target):
                    ans.append(A[left])
                    left -= 1
                else:
                    ans.append(A[right])
                    right += 1
            elif left < 0:
                ans.append(A[right])
                right += 1
            else:
                ans.append(A[left])
                left -= 1
        
        return ans