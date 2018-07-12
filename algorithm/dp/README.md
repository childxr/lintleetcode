# Dynamic Programing

## Max Square II

### Description

Given a 2D binary matrix filled with 0's and 1's, find the largest square which diagonal is all 1 and others is 0.
Only consider the main diagonal situation.

### Example
For example, given the following matrix:

```
1 0 1 0 0
1 0 0 1 0
1 1 0 0 1
1 0 0 1 0
return 9
```


### Solution

- To be qualified as a square, need to keep track of the number of 1 in diagnose and number of 0 in both up-down and left-right direction
- Consider a matrix point [i,j]
- Suppose u(i,j) is the number of continuous 0s from upper direction to matrix point [i,j] 
- Suppose l(i,j) is the number of continuous 0s from left direction to matrix point [i,j]
- Suppose f(i,j) is the max length of square when matrix point[i,j] is taken
- if matrix point [i,j] is 0
	- u(i,j) = u(i-1,j)+1 if i > 0 else 1
	- l(i,j) = l(i,j-1)+1 if j > 0 else 1
	- f(i,j) = 0
- else
	- f(i,j) = min(f(i-1,j-1), min(u(i-1,j), l(i,j-1)) when i > 0 and j > 0
	- f(i,j) = 1

- Need a global max variable to keep track of max(f(i,j))

### TAG

- DP

## Longest Repeating Subsequence

### Description

Given a string, find length of the longest repeating subsequence such that the two subsequence don’t have same string character at same position, i.e., any ith character in the two subsequences shouldn’t have the same index in the original string.

### Example

str = abc, return 0, There is no repeating subsequence

str = aab, return 1, The two subsequence are a(first) and a(second).
Note that b cannot be considered as part of subsequence as it would be at same index in both.

str = aabb, return 2

### Solution

Given a string str

- Suppose f(i,j) is the longest repeating subsequence for substring of str ended in i and subtring of str ended in j
- if str[i] != str[j], then f(i,j) is decided by either f(i-1, j) or f(i, j-1), whichever max wins. This result excludes either str[i] or str[j] for comparison
- if str[i] == str[j], where i != j, then f(i,j) = f(i-1,j-1) + 1
- f(0,0) = 0


## Longest Continuous Increasing Subsequence

### Description

Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right.

Indices of the integers in the subsequence should be continuous.

### Example

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
