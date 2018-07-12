

## Longest Continuous Increasing Subsequence

### Description

Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right.

Indices of the integers in the subsequence should be continuous.

Example

For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.

### Solution

- Suppose f(i) is the longest continuous increasing subsequnce ended in str(i)
- f(i) = f(i-1) + 1 if str(i) > str(i-1) else 1
- run the algorithm from left to right, then from right to left, report the final max


## Max Square

### Description
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

### Example
```
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
```

### Solution

- Suppose f(i,j) is the length of edge for square whose right bottom is matrx[i,j]
- f(i,j) = min(f(i-1,j), f(i,j-1), f(i-1,j-1)) + 1 if matrix[i,j] = 1 else 0
- use a global tracker to track the longest edge, report area in the end

## Longest Palindrome Substring

### Description
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

### Example
Given the string = "abcdzdcab", return "cdzdc".
Challenge
O(n2) time is acceptable. Can you do it in O(n) time.

### Solution

We define P(i,j) as following:

- P(i,j)=true if the substring Si…Sj is a palindrome, otherwise false
- P(i,j)=(P(i+1,j−1) and Si == Sj
- The base cases are:
  - P(i,i) = true
  - P(i,i+1) = true if Si == Si+1


