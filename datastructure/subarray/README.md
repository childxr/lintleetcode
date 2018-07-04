# Subarray Related

## 1. Maximum Subarray

### Description

Given an array of integers, find a contiguous subarray which has the largest sum.

The subarray should contain at least one number.

### Example

Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

#### Challenge
Can you do it in time complexity O(n)?

### Solution

- define a dp function  f(i), where f(i) is the value of max subarray sum ending in index i
- f(i) = max(f(i-1), 0) + a[i]
- objective: max(f(i)) for i in [0, ..., n-1]
- f(0) = a[0]


### TAG

- Dynamic Programming


## 2. Subarray Sum


### Description

Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

There is at least one subarray that it's sum equals to zero.

### Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

### Solution

- Use a runing pointer to compute a running sum
- Save running sum into a hash table where key is the sum, value is the end index of subarray
- At each position, compute the running sum, if running sum = 0, then output [0, cur]. Otherwise check if (running sum - 0) exists in hash table or not. If so, get the index out, output [index+1, cur]

### TAG

- Hash
- Running Sum(in Hash)

## 3. Minimum Size Subarray Sum

### Description

Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.

### Example
Given the array [2,3,1,2,4,3] and s = 7, the subarray [4,3] has the minimal length under the problem constraint.

### Challenge

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

### Solution

- Use two pointers, left and right(-1, 0 initially)
- Keep running right pointer until we gets a running sum that is >= target
- While loop to compute minimum size when shrinking left pointer to find minimum size, the compute equation is (right-left)

```
import sys
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        
        if not nums or sum(nums) < s:
            return -1
        
        running, left, right = 0, -1, 0
        ans = sys.maxint
        while right < len(nums):
            running += nums[right]
            while running >= s:
                ans = min(ans, right-left)
                left += 1
                running -= nums[left]
            right += 1
        
        while running >= s:
            ans = min(ans, right-left-1)
            left += 1
            running -= nums[left]
        
        return ans
```

### TAG

- Two Pointer

## 4. Maximum Average Subarray II

### Description

Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.

It's guaranteed that the size of the array is greater or equal to k.

### Example

Given nums = `[1, 12, -5, -6, 50, 3]`, k = 3

Return 15.667 // (-6 + 50 + 3) / 3 = 15.667

### Solution

```
public class Solution {
    /*
     * @param nums: an array with positive and negative numbers
     * @param k: an integer
     * @return: the maximum average
     */
    public double maxAverage(int[] nums, int k) {
        // write your code here
        if(nums == null || nums.length == 0) return 0.0;
        int n = nums.length;
        double left = nums[0], right = nums[0];
        
        for(int i = 0; i < n; i++) {
            left = Math.min(left, nums[i]);
            right = Math.max(right, nums[i]);
        }
        while (left <= right) {
            double mid = left + (right - left)/2.0;
            if(hasAverageAbove(nums, k, mid)) {
                left = mid + 1e-5;
            } else {
                right = mid - 1e-5;
            }
        }
        return right;
    }
    
    private boolean hasAverageAbove(int[] nums, int k, double target) {
        double sum = 0, extraSum = 0;
        for(int i = 0; i < k; i++) {
            sum += nums[i] - target;
        }
        int i = k;
        while(i < nums.length) {
            if(sum >= 0) return true;
            sum += nums[i] - target;
            extraSum += nums[i-k] - target;
            if(extraSum < 0) {
                sum -= extraSum;
                extraSum = 0;
            }
            i++;
        }
        return sum >= 0;
    }
}
```

### TAG

- Binary Search


## 5. Maximum Product Subarray

### Description

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

### Example

For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.

### Solution

- Define two variable: a running_min and running_max
- At each element, keep updating running min and running max by
	- running_min = **min**(running_min*a[i], a[i])
	- running_max = **max**(running_max*a[i], a[i])
	- running_ans = **max**(running_max, running_ans)


### TAG

- Dynamic Programming


## 6. Continuous Subarray Sum

### Description

Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number. (If their are duplicate answer, return anyone)

### Example

Give [-3, 1, 3, -3, 4], return [1,4].

### Solution

```
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        # write your code here
        ans = -0x7fffffff
        sm = 0
        start, end = 0, 0
        result = [-1, -1]
        
        for i, val in enumerate(A):
            if sm < 0:
                sm = val
                start = end = i
            else:
                sm += val
                end = i
            if sm > ans:
                ans = sm
                result = [start, end]

        return result
```

### TAG

- Dynamic Programming


## 7. Continue Subarray Sum II

### Description
Given an circular integer array (the next element of the last element is the first element), find a continuous subarray in it, where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number.

If duplicate answers exist, return any of them.

### Example
Give [3, 1, -100, -3, 4], return [4,1].


### Solution

- The tricky part of this problem is how to compute the sum for subarray where start in larger index but end in smaller index. 
- The idea is to compute a candidate result based on the approach **Continuous Subarray Sum**. While computing this candidate result, get the sum of the whole array.
- Then we could do another round of array scan, the target of this round is to find a minimum running sum. By subjecting this minimum sum, we could get a maximum subarray which cross over the end of array and start of array.
- [code](https://github.com/childxr/lintleetcode/blob/master/ContinuousSubarraySumII/solution.py)


### TAG

- Running sum
- Reverse problem transformation
- DP

## 8. Subarray Sum Closest

### Description

Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

### Example

Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4]

#### Challenge

O(nlogn) time

### Solution

- Compute the running sum, saved in an array, called sums, where sums[i] is the running sum of subarray ended in index i
- Sort this array while preserving the index of i
- Find minimum value between two elements in sorted running sum, recover the index to output
- [code](https://github.com/childxr/lintleetcode/blob/master/SubarraySumClosest/solution.py)

### TAG
- sorting
- running sum

## 9. Subarray Sum II

### Description

Given an integer array, find a subarray where the sum of numbers is in a given interval. Your code should return the number of possible answers. (The element in the array should be positive)

### Example

Given [1,2,3,4] and interval = [1,3], return 4. The possible answers are:

`[0, 0]`

`[0, 1]`

`[1, 1]`

`[2, 2]`

### Solution

```
public class Solution {
    /**
     * @param A an integer array
     * @param start an integer
     * @param end an integer
     * @return the number of possible answer
     */
    int find(int[] A, int len, int value) {
        if (A[len-1] < value )
            return len;
        
        int l = 0, r = len-1, ans = 0;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (value <= A[mid]) {
                ans = mid;
                r = mid - 1;
            }  else
                l = mid + 1;
        }
        return ans;
    }

    public int subarraySumII(int[] A, int start, int end) {
        // Write your code here
        int len = A.length;
        for (int i = 1; i <len; ++i)
            A[i] += A[i-1];

        int cnt = 0;
        for (int i = 0; i <len; ++i) {
            if (A[i] >= start && A[i] <= end)
                cnt ++;
            int l = A[i] - end;
            int r = A[i] - start;
            cnt += find(A, len, r+1) - find(A, len, l); 
        }
        return cnt;
    }
}
```


### TAG

- Binary Search
- Running Sum

